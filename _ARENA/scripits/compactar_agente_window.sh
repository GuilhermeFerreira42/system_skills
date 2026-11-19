#!/usr/bin/env bash
# compactar_agente_window.sh
#
# Compacta o projeto agente_window/ SEM as pastas de Node
# (node_modules, .runtime, .cache) e gera o base64 em arquivo.txt
# — o mesmo fluxo que você fazia na mão:
#     tar -vzcf agente_window.tar.gz agente_window/
#     base64 -w 76 agente_window.tar.gz > arquivo.txt
#
# Uso:
#   ./compactar_agente_window.sh
#   ./compactar_agente_window.sh /outro/caminho/agente_window
#
# Saída (na pasta pai do projeto, ex.: /home/user/):
#   agente_window.tar.gz
#   arquivo.txt

set -euo pipefail

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Aceita caminho como argumento; senão detecta se o script está
# dentro do projeto ou ao lado dele (ex.: na home).
if [ -n "${1:-}" ]; then
  PROJETO="$1"
elif [ -d "$AQUI/platform" ] || [ -f "$AQUI/iniciar.sh" ]; then
  PROJETO="$AQUI"
else
  PROJETO="$AQUI/agente_window"
fi

if [ ! -d "$PROJETO" ]; then
  echo "ERRO: pasta do projeto não encontrada: $PROJETO" >&2
  exit 1
fi

PROJETO="$(cd "$PROJETO" && pwd)"
NOME="$(basename "$PROJETO")"
PAI="$(dirname "$PROJETO")"

TAR="${NOME}.tar.gz"
B64="arquivo.txt"

echo "Projeto : $PROJETO"
echo "Saída   : $PAI/$TAR  +  $PAI/$B64"
echo "Excluindo: platform/node_modules, platform/.runtime, platform/.cache"
echo

cd "$PAI"

# Exclusões pedidas: só as coisas de Node (deps, runtime e cache).
# --exclude com o nome da pasta vale para qualquer nível da árvore.
tar -vzcf "$TAR" \
  --exclude="$NOME/platform/node_modules" \
  --exclude="$NOME/platform/.runtime" \
  --exclude="$NOME/platform/.cache" \
  --exclude='node_modules' \
  --exclude='.runtime' \
  --exclude='.cache' \
  "$NOME/"

echo
echo "Gerando base64 (quebra de 76 colunas)..."
base64 -w 76 "$TAR" > "$B64"

echo
echo "Pronto:"
ls -lh "$TAR" "$B64"
echo
echo "Conferência rápida (não deve aparecer node_modules/.runtime):"
tar -tzf "$TAR" | grep -E 'node_modules|/\.runtime|/\.cache' | head -5 || true
echo "(vazio acima = OK)"
