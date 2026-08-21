#!/usr/bin/env python3
"""lint_conviccao.py — Auditor dos Vetores de Ouro (Skill v3.6).

Uso:
    python3 utils/lint_conviccao.py obra.md
    python3 utils/lint_conviccao.py obra.md --metafora aquário --json
    python3 utils/lint_conviccao.py obra.md --nomes "Carrel,Batmanghelidj,Agre"

Mudanças da v3.6 (decisões da sessão de calibração 2026-08-18):

- F1 (fonte visível), F2 (disclaimer), F3 (hedge) e F5 (quantificador vago)
  DEIXARAM de ser infrações. A atribuição de fontes e a cautela de conteúdo
  são responsabilidade de camadas externas (script de fontes + revisão humana
  especializada), não do texto. O lint mantém apenas F6 (ação burocrática)
  como bloqueio duro.
- A lista fixa de cientistas (CIENTISTAS_PADRAO) foi REMOVIDA: o Vetor 2 usa
  detecção genérica de nome próprio, com lista opcional por projeto via --nomes.
- O Vetor 1 (notação) foi afrouxado: não exige LaTeX em 100% dos capítulos.
- O Vetor 4 (listas) foi afrouxado: nota máxima por lista bem usada, não por
  volume (e sem capar em 5 — a lista segue fiel à fonte).
- Correção orientada à causa (opção 2 da sessão): as mensagens apontam o
  problema de fundo, não o padrão de regex que disparou.

Saída: nota 0-10 por vetor, média, ocorrências com número de linha e código de
saída 1 quando algum hard gate é violado.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

# --------------------------------------------------------------------------- #
# DNA §10 v3.6 — apenas a família de ação burocrática permanece como bloqueio
# duro. As demais famílias viraram direção preferencial (ver DNA §10 reescrito).
# --------------------------------------------------------------------------- #
LEXICO_PROIBIDO: dict[str, tuple[str, ...]] = {
    "F6_acao_burocratica": (
        r"\bregistre\b", r"\banote\b", r"\bpreencha\b", r"\bmonitore\b",
        r"\bfa[cç]a um di[aá]rio\b", r"por (sete|7|catorze|14|trinta|30) dias",
    ),
}

VERBOS_IMPERATIVOS = (
    "beba", "encha", "levante", "pare", "caminhe", "coloque", "dissolva",
    "meça", "respire", "feche", "abra", "tome",
)

# Detecção genérica de nome próprio (v3.6 — sem lista hardcoded de cientistas):
# 1) título + sobrenome (Dr. Carrel, Prof. Jhon, Sir ...)
# 2) duas ou mais palavras capitalizadas consecutivas (Alexis Carrel, Peter Agre)
PADRAO_NOME_TITULO = re.compile(
    r"\b(?:Dr\.?|Dra\.?|Prof\.?|Prof[ªa]?|Sir|Santo|Santa|São|Rei|Rainha)\s+[A-ZÁ-Ú][a-zá-úçãõéíóúâêôîû]+"
)
PADRAO_NOME_SOBRENOME = re.compile(
    r"\b[A-ZÁ-Ú][a-zá-úçãõéíóúâêôîû]{2,}(?:\s+[A-ZÁ-Ú][a-zá-úçãõéíóúâêôîû]{2,}){1,3}\b"
)


def sem_acento(texto: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")


def dividir_cenas(texto: str) -> list[tuple[str, str]]:
    """Divide por cabeçalhos '## CENA ...' ou '# Cena ...'."""
    padrao = re.compile(r"^#{1,3}\s*CENA\b.*$", re.IGNORECASE | re.MULTILINE)
    marcas = list(padrao.finditer(texto))
    if not marcas:
        return [("obra inteira", texto)]
    cenas = []
    for i, m in enumerate(marcas):
        fim = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
        cenas.append((m.group(0).strip("# ").strip(), texto[m.end():fim]))
    return cenas


def dividir_capitulos(texto: str) -> list[tuple[str, str]]:
    padrao = re.compile(r"^#{1,2}\s*CAP[IÍ]TULO\b.*$", re.IGNORECASE | re.MULTILINE)
    marcas = list(padrao.finditer(texto))
    if not marcas:
        return [("obra inteira", texto)]
    caps = []
    for i, m in enumerate(marcas):
        fim = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
        caps.append((m.group(0).strip("# ").strip(), texto[m.end():fim]))
    return caps


def corpo_da_obra(texto: str) -> str:
    """Remove o Aparato de Fontes: ressalva no aparato é legítima (GENERO §12.3)."""
    corte = re.search(r"^#{1,3}\s*AP[EÊ]NDICE|^#{1,3}\s*APARATO", texto, re.IGNORECASE | re.MULTILINE)
    return texto[:corte.start()] if corte else texto


def ocorrencias(texto: str, padroes: tuple[str, ...]) -> list[tuple[int, str]]:
    achados = []
    linhas = texto.split("\n")
    for n, linha in enumerate(linhas, 1):
        plano = sem_acento(linha).lower()
        for p in padroes:
            for m in re.finditer(sem_acento(p).lower(), plano):
                trecho = linha[max(0, m.start() - 40): m.end() + 40].strip()
                achados.append((n, f"{m.group(0)!r} … “{trecho}”"))
    return achados


def cena_tem_nome_proprio(cena: str, nomes: list[str] | None) -> bool:
    """Vetor 2 genérico: nome próprio detectado por padrão, ou lista --nomes."""
    if nomes:
        return any(n.lower() in cena.lower() for n in nomes if n.strip())
    return bool(PADRAO_NOME_TITULO.search(cena) or PADRAO_NOME_SOBRENOME.search(cena))


def auditar(texto_bruto: str, metafora: str | None, nomes: list[str] | None) -> dict:
    texto = corpo_da_obra(texto_bruto)
    cenas = dividir_cenas(texto)
    capitulos = dividir_capitulos(texto)
    problemas: list[str] = []
    v: dict[str, dict] = {}

    # -- Vetor 1: notação técnica (afrouxado na v3.6) -------------------------
    latex = re.findall(r"\$\\text\{[^}]*\}", texto)
    percentuais = re.findall(r"\b\d+(?:[.,]\d+)?\s*%", texto)
    nota1 = 10 if (len(latex) >= 2 and len(percentuais) >= 3) else \
            7 if (len(latex) >= 1 or len(percentuais) >= 2) else 3
    v["notacao_tecnica"] = {"nota": nota1, "latex": len(latex), "percentuais": len(percentuais),
                            "obs": "v3.6: sem exigência de notação em 100% dos capítulos"}

    # -- Vetor 2: storytelling (v3.6.2 — opcional, sem penalizar ausência) -----
    # Personagem NUNCA é obrigatório: se a fonte não tem pessoas, a cena segue sem.
    # O lint apenas INFORMA quais cenas têm/podem ter personagem, e reprova apenas
    # o caso de inventar: cena com nome próprio que NÃO veio da lista --nomes do
    # projeto (quando a lista é fornecida). Sem --nomes, é puramente informativo.
    cenas_com_nome = [nome for nome, c in cenas if cena_tem_nome_proprio(c, nomes)]
    cenas_sem_personagem = [nome for nome, _ in cenas if nome not in cenas_com_nome]
    nota2 = 10  # ausência não penaliza (fidelidade à fonte)
    if nomes:
        # Se o projeto declarou personagens, toda cena com nome próprio deve vir da lista
        inventados = []
        for nome, c in cenas:
            achados = set(PADRAO_NOME_TITULO.findall(c)) | set(PADRAO_NOME_SOBRENOME.findall(c))
            if achados:
                na_lista = any(n.lower() in c.lower() for n in nomes if n.strip())
                if not na_lista:
                    inventados.append(nome)
        if inventados:
            nota2 = max(0, 10 - 3 * len(inventados))
            problemas.append(f"[V2] personagem(s) fora da lista --nomes em: "
                             f"{', '.join(inventados[:5])} — verifique se não foi inventado.")
    v["storytelling_heroico"] = {"nota": nota2,
                                 "cenas_com_personagem": len(cenas_com_nome),
                                 "cenas_sem_personagem": cenas_sem_personagem,
                                 "obs": "v3.6.2: personagem opcional; nunca inventar; fidelidade à fonte"}

    # -- Vetor 3: metáfora (v3.6.2 — opcional, consistente no escopo) ----------
    # Metáfora NÃO é obrigatória: livro sem imagem passa 10. Quando --metafora é
    # fornecido, verifica-se apenas a consistência da imagem declarada (presente
    # em ≥2 pontos da obra, idealmente capítulos diferentes) — não a presença em
    # toda cena, nem a retomada obrigatória no fechamento.
    alvo = metafora
    if not alvo:
        nota3 = 10  # sem metáfora declarada → não exigível
        v["metafora_ancora"] = {"nota": nota3, "imagem": None, "ocorrencias": 0,
                                "obs": "v3.6.2: sem --metafora, imagem não é exigida"}
    else:
        alvo_n = sem_acento(alvo).lower()
        caps_com_eco = [nome for nome, c in capitulos if alvo_n in sem_acento(c).lower()]
        total_eco = sem_acento(texto).lower().count(alvo_n)
        na_primeira = alvo_n in sem_acento(cenas[0][1]).lower()
        # obra com 1 capítulo: consistência = presença em ≥2 pontos do corpo;
        # obra com 2+ capítulos: presença em ≥2 capítulos + ≥3 ocorrências.
        um_capitulo = len(capitulos) <= 1
        consistente = (total_eco >= 3) if not um_capitulo else (total_eco >= 2)
        caps_ok = True if um_capitulo else (len(caps_com_eco) >= 2)
        nota3 = 10 if (consistente and caps_ok) else \
                7 if total_eco >= 2 else 5 if total_eco >= 1 else 0
        if total_eco < 2:
            problemas.append(f"[V3] metáfora declarada ('{alvo}') quase ausente ({total_eco} ocorrência(s)) — "
                             f"ou a use com consistência ou não declare.")
        v["metafora_ancora"] = {"nota": nota3, "imagem": alvo, "ocorrencias": total_eco,
                                "abertura": na_primeira,
                                "capitulos_com_eco": f"{len(caps_com_eco)}/{len(capitulos)}",
                                "obs": "v3.6.2: metáfora opcional; consistência no escopo, não obrigatoriedade"}

    # -- Vetor 4: listas de memória (afrouxado na v3.6) ------------------------
    numeradas = len(re.findall(r"^\s*\d\.\s+\*?\*?\w", texto, re.MULTILINE))
    ordinais = len(re.findall(r"\b(Primeir[oa]|Segund[oa]|Terceir[oa]|Quart[oa]|Quint[oa])\s+(mito|propriedade|erro|fase|passo|regra)", texto, re.IGNORECASE))
    total_listas = numeradas + ordinais
    nota4 = 10 if total_listas >= 2 else 7 if total_listas >= 1 else 3
    v["listas_memoria"] = {"nota": nota4, "itens_numerados": numeradas, "ordinais_ancorados": ordinais,
                           "obs": "v3.6: lista fiel à fonte, sem teto de 5 itens e sem exigir volume"}

    # -- Vetor 5: convicção ativa (v3.6 = só F6) ------------------------------
    detalhes: dict[str, list] = {}
    infracoes_duras = 0
    for familia, padroes in LEXICO_PROIBIDO.items():
        achados = ocorrencias(texto, padroes)
        if achados:
            detalhes[familia] = [f"linha {n}: {t}" for n, t in achados]
            infracoes_duras += len(achados)
    nota5 = 10 if infracoes_duras == 0 else max(0, 10 - 2 * infracoes_duras)
    if infracoes_duras:
        problemas.append(
            "[V5] F6 — a ação virou tarefa burocrática ('registre', 'anote', "
            "'por 7 dias'). O problema de fundo: o fechamento não é um gesto físico "
            "imediato. Reescreva como ação executável agora, com medida exata."
        )
    v["conviccao_ativa"] = {"nota": nota5, "infracoes": infracoes_duras, "detalhes": detalhes,
                            "obs": "v3.6: F1/F2/F3/F5 não são mais infrações (fontes e cautela são camadas externas)"}

    # -- Vetor 6: fechamento (toda cena) + chamado tátil de 30s (última) -------
    # v3.6: TODA cena deve terminar com um fechamento próprio (GENERO §4).
    # Cenas do meio: parágrafo de cristalização (curto, conclusivo).
    # Última cena: verbo + medida + critério (chamado tátil).

    def _blocos(cena: str) -> list[str]:
        """Blocos de prosa da cena, ignorando cabeçalhos (#) e linhas de corte.

        Um cabeçalho pode aparecer colado no fim de um bloco (ex.: capítulo que
        começa sem linha em branco após o fechamento da cena) — nesse caso o
        bloco é cortado na linha do cabeçalho."""
        blocos = []
        for b in cena.strip().split("\n\n"):
            b = b.strip()
            if not b or set(b) == {"-"}:
                continue
            # corta no primeiro cabeçalho interno (## / ### / ####)
            linhas = b.split("\n")
            parte = []
            for linha in linhas:
                if linha.lstrip().startswith("#"):
                    break
                parte.append(linha)
            b = "\n".join(parte).strip()
            if b:
                blocos.append(b)
        return blocos

    def _limpar_markdown(b: str) -> str:
        """Remove marcação leve de markdown para inspecionar o texto puro."""
        b = re.sub(r"[*_`#]", "", b)
        b = b.replace("$\text{", "").replace("}", "").replace("$", "")
        return b

    def _e_fechamento(bloco: str, e_ultima_cena: bool = False) -> bool:
        """Fechamento = último bloco de prosa que conclui a cena.
        - Remove markdown (negrito no fim quebrava a detecção).
        - Termina em pontuação de fechamento (. ! ? …).
        - Não é pergunta retórica aberta.
        - Não é bloco de 'nota' vazado no corpo.
        - Cenas do meio: bloco contido (até 120 palavras).
        - Última cena: o chamado tátil vale como fechamento mesmo se longo."""
        limpo = _limpar_markdown(bloco)
        plano = sem_acento(limpo).rstrip()
        palavras = len(plano.split())
        if re.search(r"\b(nota|obs|observa[cç][aã]o|epist[eê]mica|seguran[cç]a)\b", plano.lower()):
            return False
        if plano.endswith("?") and plano.count(".") == 0:
            return False
        if not re.search(r"[.!?…]\s*$", plano):
            return False
        if not e_ultima_cena and palavras > 120:
            return False
        return True

    cenas_sem_fechamento = []
    for i, (nome, conteudo) in enumerate(cenas):
        e_ultima = (i == len(cenas) - 1)
        blocos = _blocos(conteudo)
        if not blocos or not _e_fechamento(blocos[-1], e_ultima):
            cenas_sem_fechamento.append(nome)

    # Chamado tátil — verificação na última cena
    blocos_ultima = _blocos(cenas[-1][1])
    ultimo = blocos_ultima[-1] if blocos_ultima else ""
    plano = sem_acento(ultimo).lower()
    tem_verbo = any(sem_acento(x) in plano for x in VERBOS_IMPERATIVOS)
    tem_medida = bool(re.search(r"\b\d+\s*(ml|g|grama|copo|segundo|minuto|hora|litro)", plano))
    tem_criterio = bool(re.search(r"crit[eé]rio|transparente|voc[eê] confere|conferir|deve continuar", plano))
    tem_tarefa = bool(re.search(r"registre|anote|marque|por (7|sete) dias|di[aá]rio", plano))

    nota6 = 10
    if cenas_sem_fechamento:
        nota6 -= 3 * len(cenas_sem_fechamento)
        problemas.append(f"[V6] {len(cenas_sem_fechamento)} cena(s) sem fechamento próprio: "
                         f"{', '.join(cenas_sem_fechamento[:5])} — TODA cena deve concluir com "
                         f"cristalização (GENERO §4).")
    if not (tem_verbo and tem_medida and tem_criterio and not tem_tarefa):
        nota6 -= 2
        problemas.append("[V6] última cena sem chamado tátil completo (verbo + medida + critério, "
                         "sem tarefa burocrática — GENERO §4).")
    nota6 = max(0, min(10, nota6))

    v["fechamento_30s"] = {"nota": nota6,
                           "cenas_sem_fechamento": cenas_sem_fechamento,
                           "verbo_imperativo": tem_verbo, "medida_exata": tem_medida,
                           "criterio_visivel": tem_criterio, "tarefa_burocratica": tem_tarefa,
                           "obs": "v3.6: fechamento exigido em TODAS as cenas; chamado tátil na última"}

    notas = [x["nota"] for x in v.values()]
    media = round(sum(notas) / len(notas), 2)
    reprovado = media < 9.0 or any(n < 8 for n in notas) or v["conviccao_ativa"]["infracoes"] > 0
    return {"cenas": len(cenas), "capitulos": len(capitulos),
            "palavras": len(texto.split()), "vetores": v, "media": media,
            "status_geral": "REPROVADO" if reprovado else "APROVADO", "problemas": problemas}


def main() -> int:
    ap = argparse.ArgumentParser(description="Auditor dos Vetores de Ouro (Skill v3.6)")
    ap.add_argument("obra", type=Path)
    ap.add_argument("--metafora", default=None, help="imagem-mãe registrada na Bible")
    ap.add_argument("--nomes", default=None,
                    help="lista opcional de nomes/personagens do projeto, separados por vírgula "
                         "(substitui a detecção genérica do Vetor 2)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    nomes = [n.strip() for n in args.nomes.split(",")] if args.nomes else None
    rel = auditar(args.obra.read_text(encoding="utf-8"), args.metafora, nomes)
    if args.json:
        print(json.dumps(rel, ensure_ascii=False, indent=2))
    else:
        print(f"\n=== {args.obra.name} — {rel['palavras']} palavras | "
              f"{rel['capitulos']} capítulo(s) | {rel['cenas']} cena(s) ===\n")
        rotulos = {"notacao_tecnica": "1. Notação Técnica",
                   "storytelling_heroico": "2. Storytelling (nome próprio por cena)",
                   "metafora_ancora": "3. Metáfora Âncora Persistente",
                   "listas_memoria": "4. Listas de Memória",
                   "conviccao_ativa": "5. Convicção (sem ação burocrática)",
                   "fechamento_30s": "6. Fechamento de 30 Segundos"}
        for chave, dados in rel["vetores"].items():
            nota = dados["nota"]
            barra = "█" * nota + "░" * (10 - nota)
            print(f"  {rotulos[chave]:<42} {barra} {nota}/10")
        print(f"\n  MÉDIA: {rel['media']}/10   →   {rel['status_geral']}\n")
        for p in rel["problemas"]:
            print("   " + p)
        if rel["vetores"]["conviccao_ativa"]["detalhes"]:
            print("\n   F6 — ocorrências de ação burocrática (DNA §10):")
            for familia, itens in rel["vetores"]["conviccao_ativa"]["detalhes"].items():
                for i in itens[:6]:
                    print(f"        {i}")
                if len(itens) > 6:
                    print(f"        (+{len(itens) - 6} outras)")
        print()
    return 0 if rel["status_geral"] == "APROVADO" else 1


if __name__ == "__main__":
    raise SystemExit(main())
