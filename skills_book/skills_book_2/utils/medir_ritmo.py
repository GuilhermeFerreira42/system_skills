#!/usr/bin/env python3
"""Medidor de Ritmo (CAMADA A — deterministica, ZERO tokens).

Mede os indicadores do contrato de ritmo ("prosa de rio") em um arquivo de
prosa e devolve o veredito. Os limites canonicos moram em
utils/constantes.py (bloco RITMO_*) — este script NAO tem numeros hardcoded.

Por que este script existe (incidente de 2026-08-08):
  - o Revisor Cego aprovava "por nota", sem medir nada;
  - os checks de ritmo em texto foram aplicados INVERTIDOS em uma rodada;
  - com script deterministico, a medicao e sempre a mesma, quem quer que rode.

Uso:
  python3 skills_book_2/utils/medir_ritmo.py <arquivo_de_prosa.md>
  python3 skills_book_2/utils/medir_ritmo.py <arquivo_de_prosa.md> --json

Saida --json: bloco pronto para o Revisor Cego colar no campo
"metricas_ritmo" do _resultado_revisor_cego.json (veredito incluso).

Exit: 0 = ritmo em conformidade | 1 = reprovado em algum criterio | 2 = uso incorreto
"""
from __future__ import annotations

import json
import re
import statistics
import sys
from pathlib import Path

# Importa os limites canonicos do irmao (utils/constantes.py)
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from constantes import (
        RITMO_MEDIA_FRASE_MIN,
        RITMO_MEDIA_FRASE_MAX,
        RITMO_FRASE_CURTA_PALAVRAS,
        RITMO_MAX_SEQ_FRASES_CURTAS,
        RITMO_PARAGRAFO_DENSO_PALAVRAS,
        RITMO_PCT_PARAGRAFOS_DENSOS_MIN,
        RITMO_DESVIO_PARAGRAFO_MIN,
    )
except Exception:  # noqa: BLE001 - fallback de sobrevivencia (nao deveria ocorrer)
    RITMO_MEDIA_FRASE_MIN, RITMO_MEDIA_FRASE_MAX = 12, 22
    RITMO_FRASE_CURTA_PALAVRAS = 8
    RITMO_MAX_SEQ_FRASES_CURTAS = 2
    RITMO_PARAGRAFO_DENSO_PALAVRAS = 40
    RITMO_PCT_PARAGRAFOS_DENSOS_MIN = 65
    RITMO_DESVIO_PARAGRAFO_MIN = 36


def _limpar_prosa(texto: str) -> str:
    """Remove metadados do rodape e titulos de cabecalho antes de medir."""
    texto = re.split(r"\n---\n\n## Metadados", texto)[0]
    texto = re.sub(r"^#.*$", "", texto, flags=re.M)
    return texto


def medir_texto(texto: str) -> dict:
    """Mede o texto e retorna o dicionario canonico de metricas_ritmo."""
    texto = _limpar_prosa(texto)
    paragrafos = [p.strip().replace("\n", " ") for p in re.split(r"\n\s*\n", texto) if len(p.strip()) > 20]
    frases = [f.strip() for f in re.split(r"(?<=[.!?…])\s+", " ".join(paragrafos)) if f.strip()]

    if not frases or not paragrafos:
        return {
            "erro": "texto vazio ou sem prosa mensuravel",
            "veredito_ritmo": "REPROVADO",
        }

    comp_p = [len(p.split()) for p in paragrafos]
    comp_f = [len(f.split()) for f in frases]

    curtas = sum(1 for x in comp_f if x < RITMO_FRASE_CURTA_PALAVRAS)
    seq = mx = 0
    for x in comp_f:
        seq = seq + 1 if x < RITMO_FRASE_CURTA_PALAVRAS else 0
        mx = max(mx, seq)
    densos = sum(1 for x in comp_p if x >= RITMO_PARAGRAFO_DENSO_PALAVRAS)

    media_f = statistics.mean(comp_f)
    pct_curtas = round(100 * curtas / len(comp_f))
    pct_densos = round(100 * densos / len(comp_p))
    desvio_p = statistics.pstdev(comp_p) if len(comp_p) > 1 else 0.0

    ok_seq = mx <= RITMO_MAX_SEQ_FRASES_CURTAS
    ok_densos = pct_densos >= RITMO_PCT_PARAGRAFOS_DENSOS_MIN
    ok_desvio = desvio_p >= RITMO_DESVIO_PARAGRAFO_MIN
    veredito = "APROVADO" if (ok_seq and ok_densos and ok_desvio) else "REPROVADO"

    return {
        "n_palavras": sum(comp_p),
        "n_paragrafos": len(comp_p),
        "n_frases": len(comp_f),
        "media_palavras_por_frase": round(media_f, 1),
        "mediana_palavras_por_frase": statistics.median(comp_f),
        "banda_media_canonica": f"{RITMO_MEDIA_FRASE_MIN}-{RITMO_MEDIA_FRASE_MAX}",
        "media_na_banda": bool(RITMO_MEDIA_FRASE_MIN <= media_f <= RITMO_MEDIA_FRASE_MAX),
        "pct_frases_curtas": pct_curtas,
        "max_seq_frases_curtas": mx,
        "max_seq_permitida": RITMO_MAX_SEQ_FRASES_CURTAS,
        "seq_frases_curtas_ok": ok_seq,
        "pct_paragrafos_densos": pct_densos,
        "pct_densos_minimo": RITMO_PCT_PARAGRAFOS_DENSOS_MIN,
        "paragrafos_densos_ok": ok_densos,
        "desvio_paragrafo": round(desvio_p, 1),
        "desvio_minimo": RITMO_DESVIO_PARAGRAFO_MIN,
        "desvio_ok": ok_desvio,
        "maior_paragrafo_palavras": max(comp_p),
        "veredito_ritmo": veredito,
    }


def main() -> int:
    if len(sys.argv) < 2:
        print("Uso: python3 skills_book_2/utils/medir_ritmo.py <arquivo_de_prosa.md> [--json]")
        return 2
    alvo = Path(sys.argv[1])
    if not alvo.is_file():
        print(f"Erro: arquivo nao encontrado: {alvo}")
        return 2
    r = medir_texto(alvo.read_text(encoding="utf-8"))

    if "--json" in sys.argv:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        if "erro" in r:
            print(f"[FALHA] {r['erro']}")
            return 1
        print(f"palavras={r['n_palavras']}  paragrafos={r['n_paragrafos']}  frases={r['n_frases']}")
        print(f"media pal/frase   = {r['media_palavras_por_frase']} (banda {r['banda_media_canonica']}: {'OK' if r['media_na_banda'] else 'fora — informativo'})")
        print(f"seq frases curtas = {r['max_seq_frases_curtas']} (max permitida {r['max_seq_permitida']}: {'OK' if r['seq_frases_curtas_ok'] else 'FALHA'})")
        print(f"paragrafos densos = {r['pct_paragrafos_densos']}% (minimo {r['pct_densos_minimo']}%: {'OK' if r['paragrafos_densos_ok'] else 'FALHA'})")
        print(f"desvio paragrafo  = {r['desvio_paragrafo']} (minimo {r['desvio_minimo']}: {'OK' if r['desvio_ok'] else 'FALHA'})")
        print(f"---\nRITMO: {r['veredito_ritmo']}")
    if "erro" in r:
        return 1
    return 0 if r["veredito_ritmo"] == "APROVADO" else 1


if __name__ == "__main__":
    raise SystemExit(main())
