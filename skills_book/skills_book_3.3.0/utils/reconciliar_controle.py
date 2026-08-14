#!/usr/bin/env python3
"""Reconcilia Controle da Obra com o filesystem sem corrigir conteúdo."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from atomic import atomic_write_json  # noqa: E402
from checksum import checksum_file  # noqa: E402


def locate_control(project: Path) -> Path:
    candidates = (
        project / "execucao" / "controle" / "controle_da_obra.json",
        project / "controle" / "controle_da_obra.json",
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError("controle_da_obra.json não encontrado")


def reconcile(project: Path) -> dict:
    control_path = locate_control(project)
    control = json.loads(control_path.read_text(encoding="utf-8"))
    differences: list[dict] = []
    scenes = control.get("cenas", [])
    if not isinstance(scenes, list):
        raise ValueError("campo 'cenas' do Controle deve ser uma lista")

    for scene in scenes:
        scene_id = scene.get("id", "sem_id")
        relative = scene.get("worktree")
        if not relative:
            differences.append({"id": scene_id, "tipo": "worktree_ausente"})
            continue
        worktree = project / "execucao" / relative
        final = worktree / "_saida_final.md"
        expected = scene.get("checksum_final")
        if not final.is_file():
            differences.append({"id": scene_id, "tipo": "arquivo_final_ausente", "caminho": str(final)})
            continue
        actual = checksum_file(final)
        if expected and expected != actual:
            differences.append({
                "id": scene_id,
                "tipo": "MODIFICADO_MANUALMENTE",
                "esperado": expected,
                "atual": actual,
            })
        if scene.get("status") == "CONCLUIDO" and not (worktree / "_manifesto_integridade.json").is_file():
            differences.append({"id": scene_id, "tipo": "manifesto_ausente"})

    report = {
        "projeto": str(project),
        "controle": str(control_path),
        "reconciliado_em": datetime.now(timezone.utc).isoformat(),
        "status": "OK" if not differences else "REVALIDACAO_NECESSARIA",
        "diferencas": differences,
    }
    report_path = control_path.with_name("reconciliacao_ultima.json")
    atomic_write_json(report_path, report)
    return report


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print("Uso: python3 utils/reconciliar_controle.py RAIZ_DO_PROJETO", file=sys.stderr)
        return 2
    try:
        report = reconcile(Path(args[0]).resolve())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "OK" else 1


if __name__ == "__main__":
    raise SystemExit(main())