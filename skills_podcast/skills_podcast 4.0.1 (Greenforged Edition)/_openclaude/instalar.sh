#!/usr/bin/env bash
# Instala os adaptadores na raiz do sistema, ao lado de cerebros/.
# Os arquivos originais das skills NÃO são tocados.
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$RAIZ/.openclaude/agents"
cp "$(dirname "${BASH_SOURCE[0]}")/.openclaude/agents/"*.md "$RAIZ/.openclaude/agents/"
echo "Instalado em $RAIZ/.openclaude/agents/"
echo "Rode a ferramenta com o diretório de trabalho em: $RAIZ"
