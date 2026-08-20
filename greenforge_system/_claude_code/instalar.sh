#!/usr/bin/env bash
# Instala os adaptadores na raiz do sistema, ao lado de cerebros/.
# Os arquivos originais das skills NÃO são tocados.
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$RAIZ/.claude/agents"
cp "$(dirname "${BASH_SOURCE[0]}")/.claude/agents/"*.md "$RAIZ/.claude/agents/"
echo "Instalado em $RAIZ/.claude/agents/"
echo "Rode a ferramenta com o diretório de trabalho em: $RAIZ"
