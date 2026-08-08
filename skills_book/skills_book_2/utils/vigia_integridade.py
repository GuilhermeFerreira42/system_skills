#!/usr/bin/env python3
"""Vigia da Fabrica — CAMADA A (deterministica, ZERO tokens).

Verifica INTEGRIDADE e LINHAGEM de uma cena.

INTEGRIDADE:
  - presenca e ordem dos artefatos (escritor -> atomizador -> march ->
    continuidade -> editor -> final -> revisor cego)
  - _saida_final.md == _saida_editor.md (ou _saida_escritor.md se sem editor)

LINHAGEM (a peca que faltava — pega o Gargalo 4):
  - cada validador deve registrar no JSON de saida o campo "input_checksum":
    o checksum etiquetado (v1.0:xxxxxxxx, 8 hex) do texto que ELE leu.
  - BASELINE por agente (corrigido em 2026-08-08):
      MARCH, Continuidade, Editor  -> leem _saida_escritor.md
      Revisor Cego                 -> le _saida_final.md (apos o Editor)
    (antes o revisor era comparado ao _saida_escritor.md; se o Editor
     mudasse qualquer caractere, a linhagem do revisor NUNCA fechava.)
  - o vigia recalcula os checksums ATUAIS e compara.
  - se nao bater, o agente leu uma versao antiga -> FALHA.
  - formato obrigatorio: "v1.0:" + 8 hex, produzido SOMENTE por
    utils/checksum.py (nunca hash manual/inventado).

LOG: a cada execucao o vigia grava o relatorio em <cena>/_log_vigia.md
(overwrite). Nao depende de redirecionamento de shell.

Uso:
  python3 [skills_book_2/]utils/vigia_integridade.py <caminho_da_cena>

Exit: 0 = OK | 1 = FALHA (alguma checagem reprovou) | 2 = uso incorreto
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Permite importar o checksum.py irmao (utils/checksum.py)
sys.path.insert(0, str(Path(__file__).resolve().parent))

from checksum import calcular_checksum_etiquetado  # noqa: E402
from medir_ritmo import medir_texto  # noqa: E402

SAIDA_ESCRITOR = "_saida_escritor.md"
AFIRMACOES = "_afirmacoes_para_validar.json"
RESULTADO_MARCH = "_resultado_march.json"
RESULTADO_CONT = "_resultado_continuidade.json"
SAIDA_EDITOR = "_saida_editor.md"
METADADOS_EDITOR = "_metadados_editor.json"
SAIDA_FINAL = "_saida_final.md"
RESULTADO_REVISOR = "_resultado_revisor_cego.json"
LOG_VIGIA = "_log_vigia.md"

FORMATO_ETIQUETA = re.compile(r"^v1\.0:[0-9a-f]{8}$")

# Chaves que o Revisor Cego precisa colar do medir_ritmo.py (prova de medicao).
METRICAS_OBRIGATORIAS = (
    "media_palavras_por_frase",
    "max_seq_frases_curtas",
    "pct_paragrafos_densos",
    "desvio_paragrafo",
    "veredito_ritmo",
)

CHECKS: list[tuple[str, str]] = []


def _proximo(a, b, tol=0.15) -> bool:
    try:
        return abs(float(a) - float(b)) <= tol
    except (TypeError, ValueError):
        return False


def checar_metricas_ritmo(json_path: Path, texto_final_path: Path) -> None:
    """Anti-carimbo: o Revisor so vale se entregou as medidas do medir_ritmo.py.

    O vigia remede o _saida_final.md e confere: (1) presenca das metricas,
    (2) numeros declarados batem com o texto ATUAL, (3) o status_geral do
    revisor nao contradiz o veredito deterministico do medidor.
    """
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        registrar("FALHA", f"{json_path.name} ilegivel para checagem de ritmo: {exc}")
        return
    metricas = data.get("metricas_ritmo")
    if not isinstance(metricas, dict):
        registrar("FALHA",
                  f"{json_path.name}: SEM 'metricas_ritmo' — aprovacao por nota "
                  f"(carimbo) nao vale. Obrigatorio: executar "
                  f"python3 skills_book_2/utils/medir_ritmo.py <_saida_final.md> --json "
                  f"e colar o resultado, incluindo 'veredito_ritmo'")
        return
    ausentes = [k for k in METRICAS_OBRIGATORIAS if k not in metricas]
    if ausentes:
        registrar("FALHA", f"{json_path.name}: metricas_ritmo incompleto, faltam: {', '.join(ausentes)}")
        return
    re_calc = medir_texto(texto_final_path.read_text(encoding="utf-8"))
    divergentes = [k for k in METRICAS_OBRIGATORIAS[:-1] if not _proximo(metricas.get(k), re_calc.get(k))]
    if divergentes:
        registrar("FALHA",
                  f"{json_path.name}: metricas declaradas NAO batem com o texto atual "
                  f"({', '.join(divergentes)} — remede com utils/medir_ritmo.py)")
        return
    if re_calc.get("veredito_ritmo") == "REPROVADO" and data.get("status_geral") == "APROVADO":
        registrar("FALHA",
                  f"{json_path.name}: status APROVADO contradiz o medidor "
                  f"(medir_ritmo.py reprova o ritmo do texto atual)")
        return
    registrar("OK", f"{json_path.name}: metricas_ritmo verificadas (veredito {re_calc.get('veredito_ritmo')})")


def registrar(status: str, msg: str) -> None:
    CHECKS.append((status, msg))


def checar_linhagem(json_path: Path, texto_atual_checksum: str) -> None:
    """Confere se o JSON de um validador registrou o checksum do texto que leu."""
    if not json_path.exists():
        registrar("FALHA", f"{json_path.name} ausente (validador nao executou)")
        return
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        registrar("FALHA", f"{json_path.name} ilegivel: {exc}")
        return
    registrado = data.get("input_checksum")
    if not registrado:
        registrar("FALHA",
                  f"{json_path.name}: SEM input_checksum (linhagem ausente) — "
                  f"validou uma versao sem registro de qual texto leu")
        return
    if not FORMATO_ETIQUETA.match(str(registrado)):
        registrar("FALHA",
                  f"{json_path.name}: input_checksum '{registrado}' fora do formato "
                  f"canonico v1.0:xxxxxxxx — use SOMENTE utils/checksum.py")
        return
    if registrado == texto_atual_checksum:
        registrar("OK", f"{json_path.name}: linhagem OK ({registrado})")
    else:
        registrar("FALHA",
                  f"{json_path.name}: LINHAGEM QUEBRADA — validou {registrado}, "
                  f"mas o texto atual e {texto_atual_checksum} (validador leu versao antiga; "
                  f"apos qualquer reescrita, TODAS as validacoes devem ser refeitas)")


def main() -> int:
    if len(sys.argv) < 2:
        print("Uso: python3 utils/vigia_integridade.py <caminho_da_cena>")
        return 2
    cena = Path(sys.argv[1]).resolve()
    if not cena.is_dir():
        print(f"FALHA: pasta da cena nao encontrada: {cena}")
        return 1

    escritor = cena / SAIDA_ESCRITOR
    if escritor.exists():
        registrar("OK", f"{SAIDA_ESCRITOR} presente")
        atual_escritor = calcular_checksum_etiquetado(str(escritor))
    else:
        registrar("FALHA", f"{SAIDA_ESCRITOR} ausente (escritor nao executou)")
        atual_escritor = "(sem escritor)"

    afirmacoes = cena / AFIRMACOES
    registrar("OK" if afirmacoes.exists() else "FALHA",
              f"{AFIRMACOES} presente" if afirmacoes.exists() else f"{AFIRMACOES} ausente")

    checar_linhagem(cena / RESULTADO_MARCH, atual_escritor)
    checar_linhagem(cena / RESULTADO_CONT, atual_escritor)

    editor = cena / SAIDA_EDITOR
    final = cena / SAIDA_FINAL
    if editor.exists():
        registrar("OK", f"{SAIDA_EDITOR} presente (editor usado)")
        checar_linhagem(cena / METADADOS_EDITOR, atual_escritor)
        if final.exists():
            if final.read_text(encoding="utf-8") == editor.read_text(encoding="utf-8"):
                registrar("OK", f"{SAIDA_FINAL} == {SAIDA_EDITOR}")
            else:
                registrar("FALHA", f"{SAIDA_FINAL} DIFERE de {SAIDA_EDITOR}")
        else:
            registrar("FALHA", f"{SAIDA_FINAL} ausente")
    else:
        registrar("AVISO", f"{SAIDA_EDITOR} ausente (sem editor nesta cena)")
        if final.exists() and escritor.exists():
            if final.read_text(encoding="utf-8") == escritor.read_text(encoding="utf-8"):
                registrar("OK", f"{SAIDA_FINAL} == {SAIDA_ESCRITOR}")
            else:
                registrar("FALHA", f"{SAIDA_FINAL} DIFERE de {SAIDA_ESCRITOR}")

    # Baseline do Revisor Cego: ele le _saida_final.md (depois do Editor),
    # NAO o _saida_escritor.md. Comparar com o checksum do _saida_final.md.
    revisor = cena / RESULTADO_REVISOR
    if revisor.exists():
        if final.exists():
            atual_final = calcular_checksum_etiquetado(str(final))
            checar_linhagem(revisor, atual_final)
            # Anti-carimbo (v1.1-rc2): revisor so vale com medidas reais do medidor.
            checar_metricas_ritmo(revisor, final)
        else:
            registrar("FALHA", f"{RESULTADO_REVISOR}: impossivel conferir linhagem ({SAIDA_FINAL} ausente)")
        try:
            data = json.loads(revisor.read_text(encoding="utf-8"))
            status = data.get("status_geral", "?")
            if status == "APROVADO":
                registrar("OK", f"{RESULTADO_REVISOR}: status APROVADO")
            else:
                registrar("FALHA", f"{RESULTADO_REVISOR}: status {status} (deveria ser APROVADO)")
        except Exception as exc:  # noqa: BLE001
            registrar("FALHA", f"{RESULTADO_REVISOR} ilegivel: {exc}")
    else:
        registrar("AVISO", f"{RESULTADO_REVISOR} ausente (revisor nao rodou nesta cena)")

    n_ok = sum(1 for s, _ in CHECKS if s == "OK")
    n_falha = sum(1 for s, _ in CHECKS if s == "FALHA")
    n_aviso = sum(1 for s, _ in CHECKS if s == "AVISO")
    linhas = [f"[{status}] {msg}" for status, msg in CHECKS]
    resumo = f"---\nVIGIA: {n_ok} OK | {n_falha} FALHA | {n_aviso} aviso(s)"
    saida = "# LOG DO VIGIA DA FABRICA\n\n" + "\n".join(linhas) + "\n" + resumo + "\n"
    print("\n".join(linhas))
    print(resumo)
    # Sempre grava o relatorio na pasta da cena (overwrite) — a prova do
    # vigia nao pode depender de redirecionamento de shell.
    try:
        (cena / LOG_VIGIA).write_text(saida, encoding="utf-8")
    except OSError as exc:
        print(f"[AVISO] nao foi possivel gravar {LOG_VIGIA}: {exc}")
    return 1 if n_falha else 0


if __name__ == "__main__":
    raise SystemExit(main())
