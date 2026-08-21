#!/usr/bin/env python3
"""gerar_pontos_de_acao.py — Manifesto externo dos Chamados Táteis (Skill v3.6).

Uso:
    python3 utils/gerar_pontos_de_acao.py LIVRO_FINAL.md
    python3 utils/gerar_pontos_de_acao.py LIVRO_FINAL.md -o PONTOS_DE_ACAO.md

Escaneia a obra e extrai, para cada cena, os blocos de fechamento imperativo
(verbo de ação + medida exata + critério — o padrão do "Chamado Tátil" do
Vetor 6). Gera um checklist externo de prioridade para a revisão humana
especializada: em vez de reler a obra inteira, o revisor vai direto nos pontos
onde o leitor é instruído a fazer algo físico com o próprio corpo.

NÃO altera o livro. Este manifesto é um espelho de apoio à revisão.
"""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path

VERBOS_IMPERATIVOS = (
    "beba", "encha", "levante", "pare", "caminhe", "coloque", "dissolva",
    "meça", "respire", "feche", "abra", "tome",
)

PADRAO_CENA = re.compile(r"^#{1,3}\s*CENA\b.*$", re.IGNORECASE | re.MULTILINE)
PADRAO_CAPITULO = re.compile(r"^#{1,2}\s*CAP[IÍ]TULO\b.*$", re.IGNORECASE | re.MULTILINE)

MEASURE_RE = re.compile(
    r"\b\d+(?:[.,]\d+)?\s*(?:ml|g|grama|copo|colher|litro|minuto|segundo|hora)\b"
    r"|\b(?:ml|mililitro|litro|copo|copos|colher|pitada|gota|gole|grama|minuto|hora|vezes)\b"
    r"|\b(?:duas?|três|quatro|cinco|seis|sete|oito|nove|dez|meia|meio)\s+(?:copos?|colheres?|vezes)\b",
    re.IGNORECASE)


def sem_acento(t: str) -> str:
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")


def bloco_e_imperativo(bloco: str) -> tuple[bool, str | None, str | None]:
    """Chamado Tátil = verbo imperativo + medida numérica (e, idealmente, critério).

    Exige AMBOS para evitar falso-positivos (ex.: "Pare um instante e pense"
    tem verbo mas nenhuma medida numérica — não é um chamado tátil).
    """
    plano = sem_acento(bloco).lower()
    tem_verbo = any(sem_acento(v) in plano for v in VERBOS_IMPERATIVOS)
    if not tem_verbo:
        return False, None, None
    m = MEASURE_RE.search(plano)
    if not m:
        return False, None, None
    medida = m.group(0)
    tem_criterio = bool(re.search(r"crit[eé]rio|voc[eê] confere|conferir|deve continuar|urina|24 horas", plano))
    return True, (medida + (" · critério" if tem_criterio else "")), bloco


def capitulo_da_cena(capitulos: list[tuple[int, str]], posicao: int) -> str:
    nome = "—"
    for inicio, cap in capitulos:
        if inicio <= posicao:
            nome = cap
        else:
            break
    return nome


def main() -> int:
    ap = argparse.ArgumentParser(description="Manifesto externo dos Chamados Táteis (v3.6)")
    ap.add_argument("obra", type=Path)
    ap.add_argument("-o", "--saida", type=Path, default=Path("PONTOS_DE_ACAO.md"))
    args = ap.parse_args()

    texto = args.obra.read_text(encoding="utf-8")
    corpo = re.split(r"^#{1,3}\s*(?:AP[EÊ]NDICE|APARATO)\b", texto, flags=re.IGNORECASE | re.MULTILINE)[0]

    cenas = list(PADRAO_CENA.finditer(corpo))
    caps = [(m.start(), m.group(0).strip("# ").strip()) for m in PADRAO_CAPITULO.finditer(corpo)]

    pontos: list[dict] = []
    for i, m in enumerate(cenas):
        fim = cenas[i + 1].start() if i + 1 < len(cenas) else len(corpo)
        conteudo = corpo[m.end():fim]
        blocos = [b.strip() for b in conteudo.split("\n\n") if b.strip() and set(b.strip()) != {"-"}]
        for b in blocos:
            imperativo, medida, trecho = bloco_e_imperativo(b)
            if imperativo:
                pontos.append({
                    "cena": m.group(0).strip("# ").strip(),
                    "capitulo": capitulo_da_cena(caps, m.start()),
                    "medida": medida or "sem medida numérica explícita",
                    "trecho": " ".join(trecho.split())[:300],
                })

    if not pontos:
        print("Nenhum Chamado Tátil (fechamento imperativo) encontrado no corpo da obra.")
        return 1

    agora = datetime.now().astimezone().strftime("%d/%m/%Y %H:%M:%S %z")
    linhas = [
        "# PONTOS DE AÇÃO — Checklist de Prioridade para Revisão Humana Especializada",
        "",
        f"> Gerado por `utils/gerar_pontos_de_acao.py` em {agora} a partir de `{args.obra.name}`.",
        "> Este manifesto NÃO faz parte do livro. Ele lista os trechos onde o leitor",
        "> é instruído a fazer algo físico com o próprio corpo (verbo imperativo + medida).",
        "> A revisão especializada deve priorizar estes pontos.",
        "",
        f"Total de Chamados Táteis encontrados: **{len(pontos)}**",
        "",
    ]
    for i, p in enumerate(pontos, 1):
        linhas += [
            f"## {i}. {p['cena']}",
            f"- **Capítulo:** {p['capitulo']}",
            f"- **Medida citada:** {p['medida']}",
            f"- **Trecho:** “{p['trecho']}…”",
            "",
        ]

    args.saida.parent.mkdir(parents=True, exist_ok=True)
    args.saida.write_text("\n".join(linhas), encoding="utf-8", newline="\n")
    print(f"Manifesto gerado: {args.saida.resolve()}")
    print(f"Chamados Táteis: {len(pontos)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
