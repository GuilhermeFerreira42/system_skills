#!/usr/bin/env python3
"""Vigia físico da Skill 3.

Este script verifica presença, linhagem, igualdade de bytes e status dos
artefatos. Ele não calcula ou julga ritmo, estilo, clareza ou qualidade.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from atomic import atomic_write_text  # noqa: E402
from checksum import checksum_file  # noqa: E402

REQUIRED = (
    "_saida_candidato.md",
    "_saida_final.md",
    "_afirmacoes_para_validar.json",
    "_resultado_march.json",
    "_resultado_continuidade.json",
    "_resultado_revisor_cego.json",
    "_manifesto_integridade.json",
)


def _load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path.name} não contém um objeto JSON")
    return value


def _check_status(data: dict, filename: str, errors: list[str]) -> None:
    if data.get("status_geral") != "APROVADO":
        errors.append(f"{filename}: status_geral não é APROVADO")


def verify_scene(scene: Path) -> tuple[int, str]:
    checks: list[str] = []
    errors: list[str] = []
    missing = [name for name in REQUIRED if not (scene / name).is_file()]
    if missing:
        errors.extend(f"arquivo ausente: {name}" for name in missing)
        return 1, _render(checks, errors)
    checks.extend(f"presente: {name}" for name in REQUIRED)

    try:
        affirmations = _load(scene / "_afirmacoes_para_validar.json")
        march = _load(scene / "_resultado_march.json")
        continuity = _load(scene / "_resultado_continuidade.json")
        reviewer = _load(scene / "_resultado_revisor_cego.json")
        manifest = _load(scene / "_manifesto_integridade.json")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors.append(f"JSON ilegível: {exc}")
        return 1, _render(checks, errors)

    candidate = scene / "_saida_candidato.md"
    final = scene / "_saida_final.md"
    candidate_checksum = checksum_file(candidate)
    final_checksum = checksum_file(final)

    if candidate.read_bytes() != final.read_bytes():
        errors.append("_saida_final.md difere de _saida_candidato.md")
    else:
        checks.append("candidato e final têm os mesmos bytes")

    if manifest.get("candidate_checksum") != candidate_checksum:
        errors.append("manifesto: candidate_checksum não corresponde ao disco")
    else:
        checks.append(f"checksum do candidato OK ({candidate_checksum})")
    if manifest.get("final_checksum") != final_checksum:
        errors.append("manifesto: final_checksum não corresponde ao disco")
    else:
        checks.append(f"checksum final OK ({final_checksum})")

    for data, filename in (
        (affirmations, "_afirmacoes_para_validar.json"),
        (march, "_resultado_march.json"),
        (continuity, "_resultado_continuidade.json"),
        (reviewer, "_resultado_revisor_cego.json"),
    ):
        registered = data.get("input_checksum")
        if registered != candidate_checksum:
            errors.append(f"{filename}: input_checksum não corresponde ao candidato")
        else:
            checks.append(f"linhagem OK: {filename}")

    _check_status(march, "_resultado_march.json", errors)
    _check_status(continuity, "_resultado_continuidade.json", errors)
    _check_status(reviewer, "_resultado_revisor_cego.json", errors)

    for filename in ("_log_prompt_checker.md", "_log_prompt_continuidade.md"):
        path = scene / filename
        if path.exists():
            log = path.read_text(encoding="utf-8")
            if candidate.read_text(encoding="utf-8") in log:
                errors.append(f"{filename}: cegueira violada; candidato vazou no prompt")
            else:
                checks.append(f"cegueira preservada: {filename}")

    physical_status = manifest.get("status_fisico")
    if physical_status not in {"FECHAMENTO_EM_VERIFICACAO", "APROVADO"}:
        errors.append(
            "manifesto: status_fisico deve ser FECHAMENTO_EM_VERIFICACAO ou APROVADO"
        )
    else:
        checks.append(f"status físico aceito: {physical_status}")

    return (1 if errors else 0), _render(checks, errors)


def _render(checks: list[str], errors: list[str]) -> str:
    lines = ["# Log do Vigia da Fábrica — Skill 3", ""]
    lines.extend(f"[OK] {item}" for item in checks)
    lines.extend(f"[FALHA] {item}" for item in errors)
    lines.append("")
    lines.append(f"VIGIA: {len(checks)} OK | {len(errors)} FALHA")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print("Uso: python3 utils/vigia_integridade.py CAMINHO_DA_CENA", file=sys.stderr)
        return 2
    scene = Path(args[0]).resolve()
    if not scene.is_dir():
        print(f"Pasta de cena inexistente: {scene}", file=sys.stderr)
        return 2
    code, report = verify_scene(scene)
    print(report, end="")
    try:
        atomic_write_text(scene / "_log_vigia.md", report)
    except OSError as exc:
        print(f"[FALHA] não foi possível salvar _log_vigia.md: {exc}", file=sys.stderr)
        return 1
    return code


if __name__ == "__main__":
    raise SystemExit(main())
