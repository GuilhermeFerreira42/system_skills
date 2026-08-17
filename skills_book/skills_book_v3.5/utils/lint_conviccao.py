#!/usr/bin/env python3
"""lint_conviccao.py — Auditor executável dos 6 Vetores de Ouro (Skill v3.5).

Uso:
    python3 utils/lint_conviccao.py obra.md
    python3 utils/lint_conviccao.py obra.md --metafora aquário --json

Implementa mecanicamente a RUBRICA_QUALITATIVA_V3 §6.3 (auditoria literal) e os
pisos do GENERO §1/§4 e do DNA §10. Não substitui o Revisor Cego: entrega a ele
a contagem que o julgamento sozinho deixou passar no ciclo v3.4.

Saída: nota 0-10 por vetor, média, ocorrências com número de linha e código de
saída 1 quando algum hard gate (§6.1) é violado.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

# --------------------------------------------------------------------------- #
# DNA §10 — as sete famílias de perda de convicção (busca literal, sem acento)
# --------------------------------------------------------------------------- #
LEXICO_PROIBIDO: dict[str, tuple[str, ...]] = {
    "F1_fonte_visivel": (
        r"\bno corpus\b", r"\bdo corpus\b", r"\bo corpus (sugere|afirma|adverte|indica|mostra)",
        r"\bo material (aponta|sugere|afirma)", r"\bsegundo os dados\b",
        r"\bconforme o estudo\b", r"\ba literatura (aponta|indica|sugere)",
        r"\ba palestra (menciona|afirma|diz)",
    ),
    "F2_disclaimer": (
        r"(este livro|esta obra|este texto|o conte[uú]do)[^.]{0,40}n[aã]o substitui",
        r"n[aã]o substitui (o |a |um |uma )?(atendimento|acompanhamento|avalia|consulta|tratamento|diagn[oó]stico|m[eé]dico|profissional|evid[eê]ncia)",
        r"n[aã]o constitui recomenda", r"procure orienta",
        r"consulte (um|seu) (profissional|m[eé]dico)", r"n[aã]o fa[cç]a (isso )?por conta pr[oó]pria",
        r"os resultados podem variar",
    ),
    "F3_hedge_empilhado": (
        r"\bpode ser que\b", r"\btalvez\b", r"\bem alguns casos\b", r"\bnem sempre\b",
        r"\bn[aã]o necessariamente\b", r"\bde modo geral\b",
    ),
    "F5_numero_desidratado": (
        r"\bboa parte\b", r"\buma parcela relevante\b", r"\bcerca de dois ter[cç]os\b",
        r"\balguns fatores\b",
    ),
    "F6_acao_burocratica": (
        r"\bregistre\b", r"\banote\b", r"\bpreencha\b", r"\bmonitore\b",
        r"\bfa[cç]a um di[aá]rio\b", r"por (sete|7|catorze|14|trinta|30) dias",
    ),
}
# F3 tem tolerância: 1-2 por cena é nuance (ver DNA §10).
TOLERANCIA_F3_POR_CENA = 2

CIENTISTAS_PADRAO = (
    "Carrel", "Batmanghelidj", "Agre", "Brownstein", "Coandă", "Coanda",
    "Jhon", "Frassetto", "Feldman", "Pollack", "Szent", "Kurzweil", "Hayflick",
)

VERBOS_IMPERATIVOS = (
    "beba", "encha", "levante", "pare", "caminhe", "coloque", "dissolva",
    "meça", "respire", "feche", "abra", "tome",
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
    return texto[: corte.start()] if corte else texto


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


def auditar(texto_bruto: str, metafora: str | None) -> dict:
    texto = corpo_da_obra(texto_bruto)
    cenas = dividir_cenas(texto)
    capitulos = dividir_capitulos(texto)
    problemas: list[str] = []
    v: dict[str, dict] = {}

    # -- Vetor 1: notação técnica destemida ---------------------------------
    latex = re.findall(r"\$\\text\{[^}]+\}[^$]*\$|\$\\text\{[^}]+\}\$", texto)
    percentuais = re.findall(r"\b\d+(?:[.,]\d+)?\s*%", texto)
    caps_com_latex = sum(1 for _, c in capitulos if re.search(r"\$\\text\{", c))
    nota1 = 10 if (caps_com_latex == len(capitulos) and len(percentuais) >= 5) else \
            7 if latex else 2
    if caps_com_latex < len(capitulos):
        problemas.append(f"[V1] {len(capitulos) - caps_com_latex} capítulo(s) sem notação explícita.")
    v["notacao_tecnica"] = {"nota": nota1, "latex": len(latex), "percentuais": len(percentuais),
                            "capitulos_com_notacao": f"{caps_com_latex}/{len(capitulos)}"}

    # -- Vetor 2: storytelling heroico --------------------------------------
    cenas_sem_personagem = [nome for nome, c in cenas
                            if not any(x in c for x in CIENTISTAS_PADRAO)]
    total_nomes = sum(len(re.findall("|".join(CIENTISTAS_PADRAO), c)) for _, c in cenas)
    nota2 = 10 if not cenas_sem_personagem else max(0, 10 - 3 * len(cenas_sem_personagem))
    for nome in cenas_sem_personagem:
        problemas.append(f"[V2] cena sem personagem científico nomeado: {nome}")
    v["storytelling_heroico"] = {"nota": nota2, "mencoes": total_nomes,
                                 "cenas_sem_personagem": cenas_sem_personagem}

    # -- Vetor 3: metáfora âncora persistente -------------------------------
    alvo = metafora
    if not alvo:  # heurística: substantivo doméstico mais repetido entre candidatos
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

    # -- Vetor 4: listas numeradas de memória -------------------------------
    numeradas = len(re.findall(r"^\s*\d\.\s+\*?\*?\w", texto, re.MULTILINE))
    ordinais = len(re.findall(r"\b(Primeir[oa]|Segund[oa]|Terceir[oa]|Quart[oa]|Quint[oa])\s+(mito|propriedade|erro|fase|passo|regra)", texto, re.IGNORECASE))
    nota4 = 10 if (numeradas + ordinais) >= 6 else 7 if (numeradas + ordinais) >= 3 else 3
    v["listas_memoria"] = {"nota": nota4, "itens_numerados": numeradas, "ordinais_ancorados": ordinais}

    # -- Vetor 5: convicção ativa (eliminatório) ----------------------------
    detalhes: dict[str, list] = {}
    infracoes_duras = 0
    for familia, padroes in LEXICO_PROIBIDO.items():
        achados = ocorrencias(texto, padroes)
        if familia == "F3_hedge_empilhado":
            limite = TOLERANCIA_F3_POR_CENA * max(1, len(cenas))
            excedente = max(0, len(achados) - limite)
            detalhes[familia] = [f"{len(achados)} ocorrência(s); limite tolerado {limite}"]
            infracoes_duras += excedente
        elif achados:
            detalhes[familia] = [f"linha {n}: {t}" for n, t in achados]
            infracoes_duras += len(achados)
    nota5 = 10 if infracoes_duras == 0 else max(0, 10 - 2 * infracoes_duras)
    if infracoes_duras:
        problemas.append(f"[V5] ELIMINATÓRIO: {infracoes_duras} ocorrência(s) do léxico proibido (DNA §10).")
    v["conviccao_ativa"] = {"nota": nota5, "infracoes": infracoes_duras, "detalhes": detalhes}

    # -- Vetor 6: fechamento de 30 segundos ---------------------------------
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
    ap = argparse.ArgumentParser(description="Auditor dos 6 Vetores de Ouro (Skill v3.5)")
    ap.add_argument("obra", type=Path)
    ap.add_argument("--metafora", default=None, help="imagem-mãe registrada na Bible")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rel = auditar(args.obra.read_text(encoding="utf-8"), args.metafora)
    if args.json:
        print(json.dumps(rel, ensure_ascii=False, indent=2))
    else:
        print(f"\n=== {args.obra.name} — {rel['palavras']} palavras | "
              f"{rel['capitulos']} capítulo(s) | {rel['cenas']} cena(s) ===\n")
        rotulos = {"notacao_tecnica": "1. Notação Técnica Destemida",
                   "storytelling_heroico": "2. Storytelling Heroico",
                   "metafora_ancora": "3. Metáfora Âncora Persistente",
                   "listas_memoria": "4. Listas Numeradas de Memória",
                   "conviccao_ativa": "5. Convicção Ativa de Descobridor",
                   "fechamento_30s": "6. Fechamento de 30 Segundos"}
        for chave, dados in rel["vetores"].items():
            nota = dados["nota"]
            barra = "█" * nota + "░" * (10 - nota)
            print(f"  {rotulos[chave]:<38} {barra} {nota}/10")
        print(f"\n  MÉDIA: {rel['media']}/10   →   {rel['status_geral']}\n")
        for p in rel["problemas"]:
            print("   " + p)
        if rel["vetores"]["conviccao_ativa"]["detalhes"]:
            print("\n   Léxico proibido encontrado (DNA §10):")
            for familia, itens in rel["vetores"]["conviccao_ativa"]["detalhes"].items():
                print(f"    - {familia}:")
                for i in itens[:6]:
                    print(f"        {i}")
                if len(itens) > 6:
                    print(f"        (+{len(itens) - 6} outras)")
        print()
    return 0 if rel["status_geral"] == "APROVADO" else 1


if __name__ == "__main__":
    raise SystemExit(main())
