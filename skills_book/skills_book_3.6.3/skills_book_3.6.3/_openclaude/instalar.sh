#!/usr/bin/env bash
# Instala os adaptadores na raiz do sistema, ao lado de cerebros/.
# Os arquivos originais das skills NÃO são tocados.
#
# IMPORTANTE: chame com `bash instalar.sh`.
# O bit de execução não sobrevive ao ciclo compactar -> .txt -> restaurar,
# entao `./instalar.sh` pode falhar com "Permission denied".
# No Windows (sem Git Bash/WSL), use: python instalar.py
set -euo pipefail
AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RAIZ="$(cd "$AQUI/.." && pwd)"
mkdir -p "$RAIZ/.openclaude/agents"
cp "$AQUI/.openclaude/agents/"*.md "$RAIZ/.openclaude/agents/"
echo "Instalado em $RAIZ/.openclaude/agents/"
echo "Verifique com: python3 "$AQUI/instalar.py" --verificar"
echo "Rode a ferramenta com o diretorio de trabalho em: $RAIZ"
