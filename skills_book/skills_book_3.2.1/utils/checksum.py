#!/usr/bin/env python3
"""Checksum etiquetado para prova física de artefatos da Skill 3.

O checksum identifica bytes; ele não decide se um texto é bom. A etiqueta de
versão evita confundir mudança de algoritmo com drift do arquivo.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ALGORITHM = "sha256"
ALGORITHM_VERSION = "1.0"
DIGEST_SIZE = 8
LABEL_RE = re.compile(r"^v(?P<version>[0-9]+\.[0-9]+):(?P<digest>[0-9a-f]{8})$")


def checksum_bytes(data: bytes, size: int = DIGEST_SIZE) -> str:
    digest = hashlib.new(ALGORITHM, data).hexdigest()[:size]
    return f"v{ALGORITHM_VERSION}:{digest}"


def checksum_file(path: str | Path, size: int = DIGEST_SIZE) -> str:
    return checksum_bytes(Path(path).read_bytes(), size=size)


def parse_checksum(value: str) -> tuple[str, str]:
    match = LABEL_RE.fullmatch(value.strip())
    if not match:
        raise ValueError(f"checksum fora do formato vX.Y:xxxxxxxx: {value!r}")
    return match.group("version"), match.group("digest")


def verify_checksum(path: str | Path, expected: str) -> bool:
    version, digest = parse_checksum(expected)
    if version != ALGORITHM_VERSION:
        return False
    actual_version, actual_digest = parse_checksum(checksum_file(path))
    return actual_version == version and actual_digest == digest


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in {"-h", "--help"}:
        print("Uso:")
        print("  python3 utils/checksum.py calcular ARQUIVO")
        print("  python3 utils/checksum.py verificar ARQUIVO CHECKSUM")
        return 0

    command = args.pop(0)
    if command == "calcular" and len(args) == 1:
        path = Path(args[0])
        print(f"{path}: {checksum_file(path)}")
        return 0
    if command == "verificar" and len(args) == 2:
        ok = verify_checksum(args[0], args[1])
        print("OK" if ok else "DRIFT")
        return 0 if ok else 1

    print("Uso inválido. Consulte --help.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
