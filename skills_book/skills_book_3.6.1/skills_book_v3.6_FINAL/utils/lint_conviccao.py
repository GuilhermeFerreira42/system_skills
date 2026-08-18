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

    # -- Vetor 2: storytelling heroico (genérico na v3.6) ----------------------
    cenas_sem_personagem = [nome for nome, c in cenas if not cena_tem_nome_proprio(c, nomes)]
    nota2 = 10 if not cenas_sem_personagem else max(0, 10 - 3 * len(cenas_sem_personagem))
    for nome in cenas_sem_personagem:
        problemas.append(f"[V2] cena sem nome próprio detectado: {nome} — adicione um personagem/"
                         f"autoridade concreta com data, lugar ou obstáculo (ou passe --nomes)")
    v["storytelling_heroico"] = {"nota": nota2, "cenas_sem_personagem": cenas_sem_personagem,
                                 "detecao": "genérica (título+nome ou sobrenome duplo)"}

    # -- Vetor 3: metáfora âncora persistente ---------------------------------
    alvo = metafora
    if not alvo:
        candidatos = ("aquário", "aquario", "casa", "carro", "motor", "caixa", "jardim", "forno")
        alvo = max(candidatos, key=lambda c: sem_acento(texto).lower().count(sem_acento(c)))
    alvo_n = sem_acento(alvo).lower()
    na_primeira = alvo_n in sem_acento(cenas[0][1]).lower()
    na_ultima = alvo_n in sem_acento(cenas[-1][1]).lower()
    caps_com_eco = [nome for nome, c in capitulos if alvo_n in sem_acento(c).lower()]
    total_eco = sem_acento(texto).lower().count(alvo_n)
    nota3 = 10 if (na_primeira and na_ultima and len(caps_com_eco) == len(capitulos)) else \
            6 if (na_primeira and na_ultima) else 3 if total_eco >= 2 else 0
    if not na_primeira:
        problemas.append(f"[V3] metáfora-mestra ('{alvo}') ausente da cena de abertura.")
    if not na_ultima:
        problemas.append(f"[V3] metáfora-mestra ('{alvo}') não retomada no fechamento — METAFORA_DESCARTAVEL.")
    v["metafora_ancora"] = {"nota": nota3, "imagem": alvo, "ocorrencias": total_eco,
                            "abertura": na_primeira, "fechamento": na_ultima,
                            "capitulos_com_eco": f"{len(caps_com_eco)}/{len(capitulos)}"}

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

    # -- Vetor 6: fechamento de 30 segundos ------------------------------------
    blocos = [b.strip() for b in cenas[-1][1].strip().split("\n\n")
              if b.strip() and set(b.strip()) != {"-"}]
    ultimo = blocos[-1]
    plano = sem_acento(ultimo).lower()
    tem_verbo = any(sem_acento(x) in plano for x in VERBOS_IMPERATIVOS)
    tem_medida = bool(re.search(r"\b\d+\s*(ml|g|grama|copo|segundo|minuto|hora|litro)", plano))
    tem_criterio = bool(re.search(r"crit[eé]rio|transparente|voc[eê] confere|conferir|deve continuar", plano))
    tem_tarefa = bool(re.search(r"registre|anote|marque|por (7|sete) dias|di[aá]rio", plano))
    nota6 = 10 if (tem_verbo and tem_medida and tem_criterio and not tem_tarefa) else \
            6 if (tem_verbo and (tem_medida or tem_criterio) and not tem_tarefa) else 2
    if tem_tarefa:
        problemas.append("[V6] fechamento usa léxico de dever de casa (GENERO §4).")
    if not tem_criterio:
        problemas.append("[V6] fechamento sem critério de sucesso conferível pelo leitor.")
    v["fechamento_30s"] = {"nota": nota6, "verbo_imperativo": tem_verbo, "medida_exata": tem_medida,
                           "criterio_visivel": tem_criterio, "tarefa_burocratica": tem_tarefa}

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
