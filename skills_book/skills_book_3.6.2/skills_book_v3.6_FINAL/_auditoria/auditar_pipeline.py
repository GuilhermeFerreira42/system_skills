#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""auditar_pipeline.py — Fiscal do pipeline Skill 3 (skills_book v3.6).

NÃO faz crítica literária. Audita CONFORMIDADE DE PROCESSO:
  1. os artefatos obrigatórios de cada cena existem e fecham em linhagem;
  2. a verificação Python (lint / vigia / reconciliação) foi de fato EXECUTADA
     e o veredito bate com o status registrado;
  3. a autoauditoria de fronteira (regras_negocio/AUTO_AUDITORIA_PIPELINE.md)
     passa na obra consolidada.

Princípio de operação: NÃO CONFIAR NA DECLARAÇÃO — REEXECUTAR E COMPARAR.
O orquestrador pode dizer que rodou o lint. Este script roda de novo e confere.

Somente leitura sobre a obra:
  - `lint_conviccao.py` não escreve nada (é puro stdout) → seguro;
  - `vigia_integridade.py` escreve `_log_vigia.md` na cena → por isso ele é
    executado sobre uma CÓPIA TEMPORÁRIA da cena, para não forjar o artefato
    que o orquestrador deveria ter produzido;
  - `reconciliar_controle.py` regrava `reconciliacao_ultima.json` (relatório
    derivado, é a função dele) → executado no projeto real, e isso é declarado
    no relatório.

Uso:
    python3 _auditoria/auditar_pipeline.py .
    python3 _auditoria/auditar_pipeline.py . --livro LIVRO_FINAL.md
    python3 _auditoria/auditar_pipeline.py . --metafora aquário --json
    python3 _auditoria/auditar_pipeline.py . --cena execucao/capitulos/cap_01/cena_02

Código de saída: 0 = conforme | 1 = não conforme | 2 = erro de uso.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

# Artefatos que o vigia já exige (utils/vigia_integridade.py :: REQUIRED)
REQUIRED_VIGIA = (
    "_saida_candidato.md",
    "_saida_final.md",
    "_afirmacoes_para_validar.json",
    "_resultado_march.json",
    "_resultado_continuidade.json",
    "_resultado_revisor_cego.json",
    "_manifesto_integridade.json",
)

# Artefatos que o vigia NÃO exige, mas o pipeline exige.
# Esta é a lacuna que o fiscal fecha: o vigia só confere os logs de cegueira
# `if path.exists()`. Cena sem log passa no vigia com a cegueira NÃO AUDITADA.
REQUIRED_EXTRA = (
    "_saida_escritor.md",
    "_log_prompt_checker.md",
    "_log_prompt_continuidade.md",
    "_perguntas_continuidade.json",
)

STATUS_FISICO_VALIDOS = {"FECHAMENTO_EM_VERIFICACAO", "APROVADO"}

# AUTO_AUDITORIA_PIPELINE.md §1 e §2
PADROES_MARKETING = (
    r"\bR\$\s*\d", r"\bUS\$\s*\d", r"\bcupom\b", r"\bdesconto\b", r"\boferta\b",
    r"\bcompre (?:agora|j[áa])\b", r"\bclique aqui\b", r"\binscreva-se\b",
    r"\blink na (?:bio|descri[çc][ãa]o)\b", r"\bassine\b", r"\bpromo[çc][ãa]o\b",
    r"\bfrete gr[áa]tis\b", r"\bgarant(?:a|ia de) \d+ dias\b",
)
PADROES_METADADOS = (
    r"input_checksum", r"bible_versao", r"objetivo_cena", r"status_geral",
    r"_saida_(?:escritor|editor|candidato|final)", r"_resultado_(?:march|continuidade|revisor_cego)",
    r"_manifesto_integridade", r"worktree", r"\bv1\.0:[0-9a-f]{8}\b",
    r"\bREPROVADO\b", r"\bCONCLUIDO\b", r"\bNAO_ENCONTRADO\b",
    r"\bValidador (?:MARCH|de Continuidade)\b", r"\bRevisor Cego\b", r"\bAtomizador\b",
)


# --------------------------------------------------------------------------- #
# infra
# --------------------------------------------------------------------------- #

class Achado:
    __slots__ = ("severidade", "escopo", "regra", "mensagem")

    def __init__(self, severidade: str, escopo: str, regra: str, mensagem: str):
        self.severidade = severidade  # BLOQUEIO | ALERTA | INFO
        self.escopo = escopo
        self.regra = regra
        self.mensagem = mensagem

    def as_dict(self) -> dict:
        return {"severidade": self.severidade, "escopo": self.escopo,
                "regra": self.regra, "mensagem": self.mensagem}


def rodar(cmd: list[str], cwd: Path) -> tuple[int, str, str]:
    try:
        p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=180)
        return p.returncode, p.stdout, p.stderr
    except FileNotFoundError as e:
        return 127, "", str(e)
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"


def ler_json(p: Path) -> dict | None:
    try:
        v = json.loads(p.read_text(encoding="utf-8"))
        return v if isinstance(v, dict) else None
    except Exception:
        return None


def descobrir_cenas(raiz: Path, incluir_calibracao: bool = False) -> list[Path]:
    """Cenas = pastas com saída do escritor/candidato.

    Por padrão, IGNORA `capitulos_calibracao/`: essas cenas são amostras de
    referência que acompanham a skill, não a obra do usuário. Elas são pacotes
    propositalmente incompletos e poluiriam o relatório. Use
    --incluir-calibracao para auditá-las também.
    """
    marcas = {"_saida_candidato.md", "_saida_escritor.md"}
    cenas = set()
    for m in marcas:
        for f in raiz.rglob(m):
            partes = f.relative_to(raiz).parts
            if any(p in {"_auditoria", "_claude_code", "_openclaude", "cerebros"} for p in partes):
                continue
            if not incluir_calibracao and "capitulos_calibracao" in partes:
                continue
            cenas.add(f.parent)
    return sorted(cenas)


# --------------------------------------------------------------------------- #
# Bloco A — conformidade de artefatos e linhagem
# --------------------------------------------------------------------------- #

def auditar_artefatos(cena: Path, rel: str, ach: list[Achado]) -> dict:
    presentes = {n: (cena / n).is_file() for n in REQUIRED_VIGIA + REQUIRED_EXTRA}
    faltando_vigia = [n for n in REQUIRED_VIGIA if not presentes[n]]
    faltando_extra = [n for n in REQUIRED_EXTRA if not presentes[n]]

    for n in faltando_vigia:
        ach.append(Achado("BLOQUEIO", rel, "A1.artefato_obrigatorio",
                          f"artefato ausente: {n} (exigido por vigia_integridade.py)"))
    for n in faltando_extra:
        sev = "BLOQUEIO" if n.startswith("_log_prompt") else "ALERTA"
        extra = (" — o vigia NÃO reprova essa ausência (só confere o log se ele existir), "
                 "então sem este arquivo a cegueira fica NÃO AUDITÁVEL"
                 if n.startswith("_log_prompt") else "")
        ach.append(Achado(sev, rel, "A2.artefato_nao_coberto_pelo_vigia",
                          f"artefato ausente: {n}{extra}"))

    # linhagem: input_checksum dos derivados == checksum do candidato
    cand = cena / "_saida_candidato.md"
    if cand.is_file():
        import hashlib
        digest = hashlib.sha256(cand.read_bytes()).hexdigest()[:8]
        cks = f"v1.0:{digest}"
        for nome in ("_afirmacoes_para_validar.json", "_resultado_march.json",
                     "_resultado_continuidade.json", "_resultado_revisor_cego.json"):
            d = ler_json(cena / nome)
            if d is None:
                continue
            if d.get("input_checksum") != cks:
                ach.append(Achado("BLOQUEIO", rel, "A3.linhagem",
                                  f"{nome}: input_checksum {d.get('input_checksum')!r} != "
                                  f"checksum do candidato {cks!r} → REVALIDACAO_NECESSARIA"))
        fin = cena / "_saida_final.md"
        if fin.is_file() and fin.read_bytes() != cand.read_bytes():
            ach.append(Achado("BLOQUEIO", rel, "A4.final_difere_do_candidato",
                              "_saida_final.md não é byte a byte igual ao candidato aprovado"))

    man = ler_json(cena / "_manifesto_integridade.json")
    if man is not None:
        sf = man.get("status_fisico")
        if sf not in STATUS_FISICO_VALIDOS:
            ach.append(Achado("BLOQUEIO", rel, "A5.status_fisico",
                              f"manifesto: status_fisico={sf!r} fora de {sorted(STATUS_FISICO_VALIDOS)}"))

    # interação conhecida: revisor com ressalvas reprova no vigia
    rev = ler_json(cena / "_resultado_revisor_cego.json")
    if rev is not None and rev.get("status_geral") == "APROVADO_COM_RESSALVAS":
        ach.append(Achado("ALERTA", rel, "A6.ressalva_vs_vigia",
                          "revisor devolveu APROVADO_COM_RESSALVAS; o vigia exige exatamente "
                          "'APROVADO' e vai reprovar a cena. Decida explicitamente: tratar a "
                          "ressalva ou registrar a exceção."))

    return {"faltando_vigia": faltando_vigia, "faltando_extra": faltando_extra}


# --------------------------------------------------------------------------- #
# Bloco B — a verificação Python foi mesmo executada?
# --------------------------------------------------------------------------- #

def auditar_lint(raiz: Path, cena: Path, rel: str, metafora: str | None,
                 nomes: str | None, ach: list[Achado]) -> dict:
    """Reexecuta lint_conviccao.py sobre o candidato.

    O lint NÃO escreve nada em disco: não existe prova de que ele rodou.
    A única forma de auditar é reexecutar e comparar o veredito com o status
    registrado para a cena.
    """
    alvo = cena / "_saida_candidato.md"
    if not alvo.is_file():
        alvo = cena / "_saida_escritor.md"
    if not alvo.is_file():
        return {"executado": False, "motivo": "sem candidato nem saída do escritor"}

    cmd = [sys.executable, "utils/lint_conviccao.py", str(alvo.relative_to(raiz)), "--json"]
    if metafora:
        cmd += ["--metafora", metafora]
    if nomes:
        cmd += ["--nomes", nomes]
    code, out, err = rodar(cmd, raiz)

    if code == 127:
        ach.append(Achado("BLOQUEIO", rel, "B0.lint_indisponivel",
                          f"não foi possível executar utils/lint_conviccao.py: {err}"))
        return {"executado": False, "erro": err}

    try:
        r = json.loads(out)
    except json.JSONDecodeError:
        ach.append(Achado("BLOQUEIO", rel, "B1.lint_saida_ilegivel",
                          f"lint_conviccao.py não devolveu JSON (exit {code}). stderr: {err[:300]}"))
        return {"executado": True, "exit": code, "erro": "saída ilegível"}

    status = r.get("status_geral")
    media = r.get("media")
    infr = r.get("vetores", {}).get("conviccao_ativa", {}).get("infracoes", 0)

    if status == "REPROVADO":
        ach.append(Achado("BLOQUEIO", rel, "B2.lint_reprova",
                          f"lint_conviccao.py REPROVA o candidato (média {media}, "
                          f"{infr} infração(ões) F6). Problemas: "
                          + " | ".join(r.get("problemas", []) or ["(sem detalhe)"])))
    if infr:
        ach.append(Achado("BLOQUEIO", rel, "B3.f6_acao_burocratica",
                          f"{infr} ocorrência(s) de ação burocrática (hard gate F6 do DNA §10)"))

    # prova de execução: o lint não deixa rastro
    if not (cena / "_log_lint_conviccao.json").is_file():
        ach.append(Achado("ALERTA", rel, "B4.lint_sem_prova_de_execucao",
                          "não há prova em disco de que o Estágio 1 (lint) foi executado pelo "
                          "Orquestrador: lint_conviccao.py só escreve em stdout. Recomendação: "
                          "o Orquestrador deve persistir a saída `--json` em "
                          "`_log_lint_conviccao.json` na cena. Este fiscal reexecutou o lint "
                          "para suprir a lacuna."))
    else:
        antigo = ler_json(cena / "_log_lint_conviccao.json") or {}
        if antigo.get("status_geral") and antigo["status_geral"] != status:
            ach.append(Achado("BLOQUEIO", rel, "B5.lint_divergente",
                              f"o log registrado diz {antigo['status_geral']}, mas a reexecução "
                              f"diz {status}. O candidato mudou depois do lint, ou o log é falso."))

    return {"executado": True, "exit": code, "status_geral": status,
            "media": media, "infracoes_f6": infr, "problemas": r.get("problemas", [])}


def auditar_vigia(raiz: Path, cena: Path, rel: str, ach: list[Achado]) -> dict:
    """Reexecuta o vigia sobre uma CÓPIA da cena (ele escreve _log_vigia.md)."""
    utils = raiz / "utils" / "vigia_integridade.py"
    if not utils.is_file():
        ach.append(Achado("BLOQUEIO", rel, "B6.vigia_indisponivel",
                          "utils/vigia_integridade.py não encontrado"))
        return {"executado": False}

    with tempfile.TemporaryDirectory(prefix="auditoria_vigia_") as tmp:
        espelho = Path(tmp) / cena.name
        shutil.copytree(cena, espelho)
        code, out, err = rodar([sys.executable, str(utils), str(espelho)], raiz)

    falhas = [l for l in out.splitlines() if l.startswith("[FALHA]")]
    if code != 0:
        for f in falhas:
            ach.append(Achado("BLOQUEIO", rel, "B7.vigia_falha", f.replace("[FALHA] ", "")))
        if not falhas:
            ach.append(Achado("BLOQUEIO", rel, "B7.vigia_falha",
                              f"vigia_integridade.py saiu com código {code}. stderr: {err[:300]}"))

    log = cena / "_log_vigia.md"
    if not log.is_file():
        ach.append(Achado("BLOQUEIO", rel, "B8.vigia_nao_executado",
                          "não existe `_log_vigia.md` na cena: o Orquestrador NÃO executou o "
                          "Vigia (ou não o executou nesta versão). O pipeline exige o Vigia "
                          "antes de declarar CONCLUIDO."))
    else:
        registrado = log.read_text(encoding="utf-8")
        reg_falhas = [l for l in registrado.splitlines() if l.startswith("[FALHA]")]
        if bool(reg_falhas) != bool(falhas):
            ach.append(Achado("BLOQUEIO", rel, "B9.vigia_divergente",
                              f"o `_log_vigia.md` registrado tem {len(reg_falhas)} falha(s), mas a "
                              f"reexecução encontrou {len(falhas)}. O pacote mudou depois do Vigia."))

    return {"executado": True, "exit": code, "falhas": falhas,
            "log_presente": log.is_file()}


def auditar_reconciliacao(raiz: Path, ach: list[Achado]) -> dict:
    script = raiz / "utils" / "reconciliar_controle.py"
    if not script.is_file():
        ach.append(Achado("ALERTA", "obra", "B10.reconciliador_indisponivel",
                          "utils/reconciliar_controle.py não encontrado"))
        return {"executado": False}
    code, out, err = rodar([sys.executable, str(script), str(raiz)], raiz)
    if code == 2:
        ach.append(Achado("ALERTA", "obra", "B11.reconciliacao_erro",
                          f"reconciliar_controle.py não pôde rodar: {err.strip()[:300]}"))
        return {"executado": False, "erro": err.strip()}
    try:
        rep = json.loads(out)
    except json.JSONDecodeError:
        return {"executado": True, "exit": code, "erro": "saída ilegível"}
    if rep.get("status") != "OK":
        for d in rep.get("diferencas", []):
            ach.append(Achado("BLOQUEIO", "obra", "B12.controle_divergente",
                              f"cena {d.get('id')}: {d.get('tipo')}"
                              + (f" (esperado {d.get('esperado')}, atual {d.get('atual')})"
                                 if d.get("esperado") else "")))
    return {"executado": True, "exit": code, "status": rep.get("status"),
            "diferencas": rep.get("diferencas", []),
            "nota": "reconciliacao_ultima.json foi regravado (é o relatório derivado do script)"}


# --------------------------------------------------------------------------- #
# Bloco C — autoauditoria da obra (AUTO_AUDITORIA_PIPELINE.md)
# --------------------------------------------------------------------------- #

def auditar_obra(raiz: Path, livro: Path | None, cenas: list[Path],
                 metafora: str | None, nomes: str | None, ach: list[Achado]) -> dict:
    if livro is None or not livro.is_file():
        ach.append(Achado("INFO", "obra", "C0.sem_livro",
                          "obra consolidada não encontrada; testes §1-§5 da autoauditoria pulados"))
        return {"livro": None}

    texto = livro.read_text(encoding="utf-8")
    rel = str(livro.relative_to(raiz)) if livro.is_relative_to(raiz) else str(livro)

    for p in PADROES_MARKETING:
        for m in re.finditer(p, texto, re.IGNORECASE):
            linha = texto[:m.start()].count("\n") + 1
            ach.append(Achado("BLOQUEIO", rel, "C1.marketing",
                              f"linha {linha}: possível conteúdo de conversão — {m.group(0)!r}"))
    for p in PADROES_METADADOS:
        for m in re.finditer(p, texto):
            linha = texto[:m.start()].count("\n") + 1
            ach.append(Achado("BLOQUEIO", rel, "C2.metadado_vazado",
                              f"linha {linha}: metadado operacional na prosa — {m.group(0)!r}"))

    # §3/§4 — ordem, duplicatas e omissões contra o Controle da Obra
    ctrl = None
    for c in (raiz / "execucao" / "controle" / "controle_da_obra.json",
              raiz / "controle" / "controle_da_obra.json"):
        if c.is_file():
            ctrl = ler_json(c)
            break
    ids_livro = [m.group(0).strip("# ").strip()
                 for m in re.finditer(r"^#{1,3}\s*CENA\b.*$", texto, re.IGNORECASE | re.MULTILINE)]
    if ctrl:
        concluidas = [c.get("id") for c in ctrl.get("cenas", []) if c.get("status") == "CONCLUIDO"]
        nao_concluidas = [c.get("id") for c in ctrl.get("cenas", []) if c.get("status") != "CONCLUIDO"]
        for cid in concluidas:
            if cid and not any(str(cid) in t for t in ids_livro):
                ach.append(Achado("BLOQUEIO", rel, "C4.omissao",
                                  f"cena {cid} está CONCLUIDO no Controle mas não aparece no livro"))
        for cid in nao_concluidas:
            if cid and any(str(cid) in t for t in ids_livro):
                ach.append(Achado("BLOQUEIO", rel, "C4.cena_indevida",
                                  f"cena {cid} NÃO está CONCLUIDO mas aparece no livro"))
        vistos: dict[str, int] = {}
        for t in ids_livro:
            vistos[t] = vistos.get(t, 0) + 1
        for t, n in vistos.items():
            if n > 1:
                ach.append(Achado("BLOQUEIO", rel, "C4.duplicata",
                                  f"cabeçalho de cena aparece {n}x no livro: {t!r}"))
    else:
        ach.append(Achado("ALERTA", "obra", "C3.sem_controle",
                          "controle_da_obra.json não encontrado; testes §3/§4 (ordem, duplicatas, "
                          "omissões) não puderam ser executados"))

    # §7 — o lint na obra inteira (fechamento por cena, chamado tátil na última)
    cmd = [sys.executable, "utils/lint_conviccao.py", str(livro), "--json"]
    if metafora:
        cmd += ["--metafora", metafora]
    if nomes:
        cmd += ["--nomes", nomes]
    code, out, err = rodar(cmd, raiz)
    lint_obra = None
    try:
        lint_obra = json.loads(out)
    except json.JSONDecodeError:
        ach.append(Achado("ALERTA", rel, "C5.lint_obra_ilegivel",
                          f"lint na obra não devolveu JSON (exit {code})"))
    if lint_obra and lint_obra.get("status_geral") == "REPROVADO":
        ach.append(Achado("BLOQUEIO", rel, "C6.lint_obra_reprova",
                          f"lint_conviccao.py REPROVA a obra consolidada (média "
                          f"{lint_obra.get('media')}): "
                          + " | ".join(lint_obra.get("problemas", []))))

    return {"livro": rel, "cabecalhos_de_cena": len(ids_livro), "lint_obra": lint_obra}


# --------------------------------------------------------------------------- #
# Relatório
# --------------------------------------------------------------------------- #

def render_md(rep: dict) -> str:
    L = ["# Relatório de Auditoria do Pipeline — Skill 3", "",
         f"- **Projeto:** `{rep['projeto']}`",
         f"- **Executado em:** {rep['executado_em']}",
         f"- **Cenas auditadas:** {rep['cenas_auditadas']}"
         + ("" if rep.get("incluiu_calibracao") else "  _(cenas de `capitulos_calibracao/` ignoradas — use `--incluir-calibracao`)_"),
         f"- **Veredito:** **{rep['veredito']}**", ""]
    c = rep["contagem"]
    L += ["| Severidade | Qtd |", "|---|---:|",
          f"| BLOQUEIO | {c['BLOQUEIO']} |", f"| ALERTA | {c['ALERTA']} |",
          f"| INFO | {c['INFO']} |", ""]
    L += ["## Verificação Python — foi executada?", "",
          "| Script | Deixa prova em disco? | Situação |", "|---|---|---|",
          "| `lint_conviccao.py` | ❌ não (só stdout) | reexecutado por este fiscal em toda cena |",
          "| `vigia_integridade.py` | ✅ `_log_vigia.md` | reexecutado em cópia temporária e comparado |",
          "| `reconciliar_controle.py` | ✅ `reconciliacao_ultima.json` | executado no projeto |", ""]
    if not rep["achados"]:
        L += ["## Achados", "", "Nenhum. Pipeline conforme.", ""]
    else:
        L += ["## Achados", ""]
        for sev in ("BLOQUEIO", "ALERTA", "INFO"):
            itens = [a for a in rep["achados"] if a["severidade"] == sev]
            if not itens:
                continue
            L += [f"### {sev} ({len(itens)})", ""]
            for a in itens:
                L.append(f"- **[{a['regra']}]** `{a['escopo']}` — {a['mensagem']}")
            L.append("")
    L += ["---", "",
          "Este fiscal audita **conformidade de processo**, não qualidade literária.",
          "Fluidez é responsabilidade do Escritor, do Editor e do Revisor Cego",
          "(AUTO_AUDITORIA_PIPELINE.md §7). Toda falha aqui é **falha de pacote**."]
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Fiscal de conformidade do pipeline Skill 3")
    ap.add_argument("projeto", type=Path, help="raiz do skills_book_v3.6_FINAL")
    ap.add_argument("--livro", type=Path, default=None, help="obra consolidada (ex: LIVRO_FINAL.md)")
    ap.add_argument("--cena", type=Path, default=None, help="auditar apenas uma cena")
    ap.add_argument("--metafora", default=None, help="repassado ao lint_conviccao.py")
    ap.add_argument("--nomes", default=None, help="repassado ao lint_conviccao.py")
    ap.add_argument("--incluir-calibracao", action="store_true",
                    help="audita também as cenas de capitulos_calibracao/ (amostras da skill)")
    ap.add_argument("--json", action="store_true", help="imprime JSON em vez do relatório legível")
    ap.add_argument("-o", "--saida", type=Path, default=None,
                    help="pasta do relatório (padrão: <projeto>/_auditoria)")
    args = ap.parse_args()

    raiz = args.projeto.resolve()
    if not raiz.is_dir():
        print(f"Erro: projeto inexistente: {raiz}", file=sys.stderr)
        return 2
    if not (raiz / "utils" / "lint_conviccao.py").is_file():
        print(f"Erro: {raiz} não parece a raiz do skills_book (falta utils/lint_conviccao.py).",
              file=sys.stderr)
        return 2

    cenas = [args.cena.resolve()] if args.cena else descobrir_cenas(raiz, args.incluir_calibracao)
    achados: list[Achado] = []
    detalhe_cenas = []

    for cena in cenas:
        rel = str(cena.relative_to(raiz)) if cena.is_relative_to(raiz) else str(cena)
        d = {"cena": rel}
        d["artefatos"] = auditar_artefatos(cena, rel, achados)
        d["lint"] = auditar_lint(raiz, cena, rel, args.metafora, args.nomes, achados)
        d["vigia"] = auditar_vigia(raiz, cena, rel, achados)
        detalhe_cenas.append(d)

    reconc = auditar_reconciliacao(raiz, achados)

    livro = args.livro.resolve() if args.livro else None
    if livro is None:
        for cand in ("LIVRO_FINAL.md", "execucao/LIVRO_FINAL.md"):
            if (raiz / cand).is_file():
                livro = raiz / cand
                break
    obra = auditar_obra(raiz, livro, cenas, args.metafora, args.nomes, achados)

    contagem = {s: sum(1 for a in achados if a.severidade == s)
                for s in ("BLOQUEIO", "ALERTA", "INFO")}
    veredito = "NAO_CONFORME" if contagem["BLOQUEIO"] else (
        "CONFORME_COM_ALERTAS" if contagem["ALERTA"] else "CONFORME")

    rep = {
        "projeto": str(raiz),
        "executado_em": datetime.now().astimezone().isoformat(),
        "cenas_auditadas": len(cenas),
        "incluiu_calibracao": bool(args.incluir_calibracao),
        "veredito": veredito,
        "contagem": contagem,
        "achados": [a.as_dict() for a in achados],
        "detalhe_cenas": detalhe_cenas,
        "reconciliacao": reconc,
        "obra": obra,
    }

    destino = (args.saida or (raiz / "_auditoria")).resolve()
    destino.mkdir(parents=True, exist_ok=True)
    (destino / "relatorio_auditoria.json").write_text(
        json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
    md = render_md(rep)
    (destino / "relatorio_auditoria.md").write_text(md, encoding="utf-8")

    print(json.dumps(rep, ensure_ascii=False, indent=2) if args.json else md, end="")
    print(f"\nRelatório salvo em: {destino}/relatorio_auditoria.md", file=sys.stderr)
    return 1 if veredito == "NAO_CONFORME" else 0


if __name__ == "__main__":
    raise SystemExit(main())
