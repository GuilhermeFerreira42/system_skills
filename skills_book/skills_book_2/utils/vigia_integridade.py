#!/usr/bin/env python3
"""Vigia da Fabrica — CAMADA A (deterministica, ZERO tokens).

Verifica INTEGRIDADE e LINHAGEM de uma cena.

INTEGRIDADE:
  - presenca e ordem dos artefatos (escritor -> atomizador -> march ->
    continuidade -> editor -> final -> revisor cego)
  - _saida_final.md == _saida_editor.md (ou _saida_escritor.md se sem editor)

LINHAGEM (a peca que faltava — pega o Gargalo 4):
  - cada validador deve registrar no JSON de saida o campo "input_checksum":
    o checksum etiquetado (v1.0:xxxx) do _saida_escritor.md que ELE leu.
  - o vigia recalcula o checksum ATUAL do _saida_escritor.md e compara.
  - se nao bater, o validador leu uma versao antiga -> FALHA.

Uso:
  python3 utils/vigia_integridade.py <caminho_da_cena>

Exit: 0 = OK | 1 = FALHA (alguma checagem reprovou) | 2 = uso incorreto
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Permite importar o checksum.py irmao (utils/checksum.py)
sys.path.insert(0, str(Path(__file__).resolve().parent))

from checksum import calcular_checksum_etiquetado  # noqa: E402

SAIDA_ESCRITOR = "_saida_escritor.md"
AFIRMACOES = "_afirmacoes_para_validar.json"
RESULTADO_MARCH = "_resultado_march.json"
RESULTADO_CONT = "_resultado_continuidade.json"
SAIDA_EDITOR = "_saida_editor.md"
METADADOS_EDITOR = "_metadados_editor.json"
SAIDA_FINAL = "_saida_final.md"
RESULTADO_REVISOR = "_resultado_revisor_cego.json"

CHECKS: list[tuple[str, str]] = []


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
    if registrado == texto_atual_checksum:
        registrar("OK", f"{json_path.name}: linhagem OK ({registrado})")
    else:
        registrar("FALHA",
                  f"{json_path.name}: LINHAGEM QUEBRADA — validou {registrado}, "
                  f"mas o texto atual e {texto_atual_checksum} (validador leu versao antiga)")


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
        atual = calcular_checksum_etiquetado(str(escritor))
    else:
        registrar("FALHA", f"{SAIDA_ESCRITOR} ausente (escritor nao executou)")
        atual = "(sem escritor)"

    afirmacoes = cena / AFIRMACOES
    registrar("OK" if afirmacoes.exists() else "FALHA",
              f"{AFIRMACOES} presente" if afirmacoes.exists() else f"{AFIRMACOES} ausente")

    checar_linhagem(cena / RESULTADO_MARCH, atual)
    checar_linhagem(cena / RESULTADO_CONT, atual)

    editor = cena / SAIDA_EDITOR
    final = cena / SAIDA_FINAL
    if editor.exists():
        registrar("OK", f"{SAIDA_EDITOR} presente (editor usado)")
        checar_linhagem(cena / METADADOS_EDITOR, atual)
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

    revisor = cena / RESULTADO_REVISOR
    if revisor.exists():
        checar_linhagem(revisor, atual)
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
    for status, msg in CHECKS:
        print(f"[{status}] {msg}")
    print(f"---\nVIGIA: {n_ok} OK | {n_falha} FALHA | {n_aviso} aviso(s)")
    return 1 if n_falha else 0


if __name__ == "__main__":
    raise SystemExit(main())
