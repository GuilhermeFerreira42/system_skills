#!/usr/bin/env python3
"""Operações de persistência atômica usadas pelos checkpoints da Skill 3."""
from __future__ import annotations

import json
import os
import shutil
import tempfile
from pathlib import Path
from typing import Any


def _replace_bytes(path: str | Path, data: bytes) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(prefix=f".{target.name}.", suffix=".tmp", dir=target.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, target)
    finally:
        temporary.unlink(missing_ok=True)


def atomic_write_text(path: str | Path, text: str) -> None:
    _replace_bytes(path, text.encode("utf-8"))


def atomic_write_json(path: str | Path, value: Any) -> None:
    text = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    atomic_write_text(path, text)


def atomic_copy(source: str | Path, destination: str | Path) -> None:
    source_path = Path(source)
    _replace_bytes(destination, source_path.read_bytes())


def backup(path: str | Path) -> Path | None:
    source = Path(path)
    if not source.exists():
        return None
    target = source.with_name(source.name + ".bak")
    shutil.copy2(source, target)
    return target


==========================================
Conteúdo de checksum.py (caminho: skills_book_3/utils/checksum.py) [enc: utf-8]:

==========================================
Conteúdo de checksum.py (caminho: skills_book_3/utils/checksum.py) [enc: utf-8]: