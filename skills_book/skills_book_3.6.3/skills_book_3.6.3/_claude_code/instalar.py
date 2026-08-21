#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Instalador dos adaptadores Claude Code — multiplataforma.

Copia os adaptadores para `.claude/agents/` na raiz deste sistema, ao lado de
`cerebros/`, e VERIFICA o resultado. Nenhum arquivo original de skill é tocado.

Uso:
    python3 instalar.py              # instala e verifica
    python3 instalar.py --verificar  # só verifica, não copia
    python3 instalar.py --forcar     # sobrescreve sem perguntar

Funciona no Windows, macOS e Linux, e não depende do bit de execução.
Código de saída: 0 = tudo certo | 1 = problema encontrado.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

CFG = ".claude"
FERRAMENTA = "Claude Code"
COMANDO = "claude"

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
ORIGEM = AQUI / CFG / "agents"
DESTINO = RAIZ / CFG / "agents"
CEREBROS = RAIZ / "cerebros"


def frontmatter(texto: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return {}
    campos = {}
    for linha in m.group(1).split("\n"):
        if ":" in linha and not linha.startswith((" ", "\t", "#")):
            k, v = linha.split(":", 1)
            campos[k.strip()] = v.strip().strip('"').strip("'")
    return campos


def verificar(arquivos: list[Path]) -> list[str]:
    problemas = []
    if not arquivos:
        problemas.append(f"nenhum adaptador encontrado em {DESTINO}")
        return problemas
    vistos = {}
    for f in sorted(arquivos):
        texto = f.read_text(encoding="utf-8")
        fm = frontmatter(texto)
        if not fm:
            problemas.append(f"{f.name}: sem frontmatter YAML")
            continue
        if not fm.get("name"):
            problemas.append(f"{f.name}: frontmatter sem 'name'")
        if not fm.get("description"):
            problemas.append(f"{f.name}: frontmatter sem 'description'")
        nome = fm.get("name", "")
        if nome and not re.fullmatch(r"[a-z0-9-]+", nome):
            problemas.append(f"{f.name}: name '{nome}' fora de [a-z0-9-]")
        if nome in vistos:
            problemas.append(f"{f.name}: name '{nome}' duplicado (também em {vistos[nome]})")
        vistos[nome] = f.name
        if CFG == ".claude" and "maxSteps" in fm:
            problemas.append(f"{f.name}: 'maxSteps' não é campo do Claude Code")
        if CFG == ".openclaude" and "model" in fm:
            problemas.append(f"{f.name}: 'model' não vai no frontmatter do OpenClaude "
                             f"(use agentModels/agentRouting em ~/.openclaude/settings.json)")
        ref = re.search(r"```\ncerebros/([a-z0-9\-]+\.md)\n```", texto)
        if not ref:
            problemas.append(f"{f.name}: corpo não referencia nenhum cérebro")
        elif not (CEREBROS / ref.group(1)).is_file():
            problemas.append(f"{f.name}: cérebro ausente -> cerebros/{ref.group(1)}")
    return problemas


def main() -> int:
    ap = argparse.ArgumentParser(description=f"Instalador dos adaptadores {FERRAMENTA}")
    ap.add_argument("--verificar", action="store_true", help="só verifica, não copia")
    ap.add_argument("--forcar", action="store_true", help="sobrescreve sem perguntar")
    args = ap.parse_args()

    print(f"Sistema : {RAIZ}")
    print(f"Destino : {DESTINO}")

    if not CEREBROS.is_dir():
        print(f"\nERRO: nao existe {CEREBROS}. Os adaptadores dependem dos cerebros "
              f"e nao funcionam sem eles.", file=sys.stderr)
        return 1

    if not args.verificar:
        if not ORIGEM.is_dir():
            print(f"\nERRO: nao existe {ORIGEM}.", file=sys.stderr)
            return 1
        origem_arquivos = sorted(ORIGEM.glob("*.md"))
        if not origem_arquivos:
            print(f"\nERRO: nenhum .md em {ORIGEM}.", file=sys.stderr)
            return 1

        DESTINO.mkdir(parents=True, exist_ok=True)
        existentes = {p.name for p in DESTINO.glob("*.md")}
        conflito = [f.name for f in origem_arquivos
                    if f.name in existentes and f.read_bytes() != (DESTINO / f.name).read_bytes()]
        if conflito and not args.forcar:
            print(f"\nAVISO: {len(conflito)} arquivo(s) ja existem com conteudo DIFERENTE:")
            for n in conflito[:10]:
                print(f"  - {n}")
            resp = input("Sobrescrever? [s/N] ").strip().lower()
            if resp not in {"s", "sim", "y", "yes"}:
                print("Abortado. Nada foi alterado.")
                return 1

        copiados = 0
        for f in origem_arquivos:
            shutil.copyfile(f, DESTINO / f.name)
            copiados += 1

        validos = {f.name for f in origem_arquivos}
        orfaos = [p for p in DESTINO.glob("*.md") if p.name not in validos]
        for p in orfaos:
            p.unlink()

        print(f"\nCopiados : {copiados} adaptador(es)")
        if orfaos:
            print(f"Removidos: {len(orfaos)} orfao(s) -> {', '.join(p.name for p in orfaos)}")

    instalados = sorted(DESTINO.glob("*.md")) if DESTINO.is_dir() else []
    problemas = verificar(instalados)

    print(f"\nVerificacao de {len(instalados)} adaptador(es) em {CFG}/agents/:")
    if problemas:
        print(f"  {len(problemas)} PROBLEMA(S):")
        for p in problemas:
            print(f"   - {p}")
        return 1

    print("  OK: frontmatter valido, nomes unicos, todo cerebro resolve.")
    for f in instalados:
        fm = frontmatter(f.read_text(encoding="utf-8"))
        print(f"   - {fm.get('name', f.stem)}")
    print(f"\nPronto. Rode a ferramenta com o diretorio de trabalho na raiz do sistema:")
    print(f'  cd "{RAIZ}"')
    print(f"  {COMANDO}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
