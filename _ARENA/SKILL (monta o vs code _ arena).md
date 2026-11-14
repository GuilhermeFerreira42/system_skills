---
name: code-server-arena
description: Sobe e mantém um VS Code (code-server) no navegador dentro de um sandbox Linux da Arena — preview na porta 8080, tema escuro, terminal integrado funcionando. Idempotente entre sessões, com verificação real e protocolo de keep-alive. Use quando o usuário pedir "monta o VS Code", "quero um editor", "VS Code no navegador", ou quando for preciso manter o editor vivo ao fim de cada turno.
---

# VS Code no sandbox (code-server)

## Como usar esta skill em outra Arena

Anexe **este arquivo** (`SKILL.md`) na conversa e escreva uma linha:

> Siga a skill em anexo: monte o VS Code e mantenha ele no ar até o fim da interação.

O arquivo é autossuficiente: contém o script completo, o verificador, as regras e o
troubleshooting. O agente só precisa de shell e rede. Ele deve (1) escrever o script,
(2) subir pelo `start_process`, (3) verificar com o teste de terminal, e (4) deixar um
`AGENTS.md` com a regra de keep-alive — o modelo desse arquivo está em "Protocolo de
keep-alive".

## O que esta skill entrega

Um VS Code completo no preview da porta **8080**, aberto em `/home/user`, tema escuro,
terminal integrado rodando bash de verdade, Git, busca, markdown com preview. Depois de
qualquer reinício de sessão, **um comando** reconstroi tudo em ~6 s.

O que ela resolve — e que não é óbvio:

1. O sandbox **apaga os pacotes instalados** entre sessões. Só arquivos em `/home/user`
   sobrevivem (e `.cache`, `.local`, `node_modules` NÃO entram no snapshot). Então runtime
   se reinstala, configuração se persiste.
2. O build mais recente do code-server **tem o terminal quebrado** (detalhe abaixo). A
   versão escolhida aqui é a que funciona.
3. O settings do usuário tem um caminho que **parece** certo e é ignorado — o tema escuro
   depende de acertar esse caminho.

## Regras duras (violação = falha silenciosa)

1. **Use `VERSION=4.104.0`.** No build `4.135.0` (Code 1.135.0) o terminal integrado
   **nunca conecta**: o `ptyHost` sobe e morre, o log repete
   `No ptyHost heartbeat after 6 seconds` e o painel do terminal fica mudo, sem shell.
   Não é o sandbox — o `node-pty` do próprio pacote funciona quando chamado direto.
   Já testado: trocar para 4.104.0 resolve de primeira.
2. **Runtime sempre em `~/.cache/code-server-runtime`.** ~450 MB. Em `.cache` ele fica fora
   do snapshot de 128 MB. Nunca instale o code-server dentro da pasta do projeto.
3. **Settings do usuário = `<user-data-dir>/User/settings.json`.** Com
   `--user-data-dir ~/.vscode-data`, o arquivo é `~/.vscode-data/User/settings.json`.
   O caminho `~/.vscode-data/data/User/settings.json` é de outro layout e é **ignorado em
   silêncio** — você edita, o tema não muda, e não há erro.
4. **Bind em `0.0.0.0`**, sempre. `127.0.0.1` não aparece no preview.
5. **Para o preview existir, suba com o `start_process`** (nome: `VS Code`) usando o modo
   `run`. O modo `ensure` (destacado) serve para keep-alive e para quando não houver
   `start_process` — ele deixa o servidor no ar, mas quem registra o preview é o
   `start_process`.
6. **Não declare pronto só porque o processo subiu.** Verifique `healthz` **e** o terminal
   com um efeito colateral em disco (o teste está abaixo). O modo de falha desta stack é
   "abre, parece ok, e não funciona".
7. **`--auth none`**: quem tiver a URL do preview entra. Não coloque segredo no workspace;
   se o usuário pedir, troque para `--auth password`.
8. **Keep-alive ao fim de cada turno** (protocolo abaixo). O usuário pediu explicitamente
   que o VS Code esteja sempre no ar.

## Quickstart

```bash
# 0. se o snapshot restaurou os arquivos sem bit de execução, conserte:
chmod +x ~/bin/*.sh ~/skills/*/scripts/* 2>/dev/null || true

# 1. escreva o script (conteúdo completo na seção "O script")
mkdir -p ~/skills/code-server-arena/scripts
$EDITOR ~/skills/code-server-arena/scripts/start-code-server.sh
chmod +x ~/skills/code-server-arena/scripts/start-code-server.sh

# 2. suba COM start_process (é isso que registra o preview), modo run, porta 8080
#    start_process(command="bash ~/skills/code-server-arena/scripts/start-code-server.sh run", name="VS Code")

# 3. verifique
bash ~/skills/code-server-arena/scripts/start-code-server.sh status
```

Pronto: o preview da porta 8080 abre o VS Code em `/home/user`.

## O script

Um único arquivo, sem dependências além de `curl` e `tar`. Modos: `run` (primeiro plano),
`ensure` (idempotente, background), `status`, `stop`.

```bash
#!/usr/bin/env bash
# =============================================================================
#  start-code-server.sh — VS Code (code-server) idempotente num sandbox Linux
# =============================================================================
#  Modos:
#    run      (padrão)  sobe em primeiro plano  → use com start_process
#    ensure             sobe em background se preciso; sai 0 se já estiver no ar
#    status             imprime estado e versão
#    stop               derruba o servidor
#
#  Env: VERSION (4.104.0) · PORT (8080) · FOLDER ($HOME)
#       RUNTIME (~/.cache/code-server-runtime) · DATA (~/.vscode-data)
#       EXTS (~/.cache/code-server-ext)
#
#  Regra de ouro: o runtime (~450 MB) vive em .cache porque esse diretório NÃO
#  entra no snapshot do sandbox. Se ele sumiu, este script baixa de novo (~10 s).
# =============================================================================
set -euo pipefail

VERSION="${VERSION:-4.104.0}"
PORT="${PORT:-8080}"
FOLDER="${FOLDER:-$HOME}"
RUNTIME="${RUNTIME:-$HOME/.cache/code-server-runtime}"
DATA="${DATA:-$HOME/.vscode-data}"
EXTS="${EXTS:-$HOME/.cache/code-server-ext}"
MODE="${1:-run}"
RELEASE="code-server-${VERSION}-linux-amd64"
TARBALL_URL="https://github.com/coder/code-server/releases/download/v${VERSION}/${RELEASE}.tar.gz"

log() { printf '==> %s\n' "$*"; }

health() { curl -fsS -m 3 -o /dev/null "http://127.0.0.1:${PORT}/healthz" 2>/dev/null; }

# ---------------------------------------------------------------- runtime ----
install_runtime() {
  if [[ -f "$RUNTIME/out/node/entry.js" && -x "$RUNTIME/lib/node" ]]; then
    return 0
  fi
  log "runtime ausente — baixando code-server ${VERSION} (~225 MB)"
  mkdir -p "$RUNTIME" "$(dirname "$EXTS")"
  local dl="$RUNTIME/.download-${VERSION}.tar.gz"
  curl -fsSL -o "$dl" "$TARBALL_URL"
  tar -xzf "$dl" -C "$RUNTIME" --strip-components=1
  rm -f "$dl"
  chmod +x "$RUNTIME/lib/node" "$RUNTIME/bin/code-server" 2>/dev/null || true
}

# ------------------------------------------------------------- settings ------
# ATENÇÃO: com --user-data-dir X, o settings do usuário é X/User/settings.json
# (NÃO X/data/User/settings.json — esse caminho é de outro layout e é ignorado).
seed_settings() {
  mkdir -p "$DATA/User" "$EXTS" "$HOME/.vscode"
  if [[ ! -f "$DATA/User/settings.json" ]]; then
    cat > "$DATA/User/settings.json" <<'JSON'
{
  "workbench.colorTheme": "Default Dark Modern",
  "window.autoDetectColorScheme": false,
  "telemetry.telemetryLevel": "off",
  "update.mode": "none",
  "extensions.autoUpdate": false,
  "terminal.integrated.gpuAcceleration": "off",
  "editor.accessibilitySupport": "off"
}
JSON
    log "settings de usuário criados (tema escuro) em $DATA/User/settings.json"
  fi
  if [[ ! -f "$HOME/.vscode/settings.json" ]]; then
    cat > "$HOME/.vscode/settings.json" <<'JSON'
{
  "terminal.integrated.env.linux": { "PATH": "/home/user/bin:${env:PATH}" },
  "terminal.integrated.defaultProfile.linux": "bash",
  "terminal.integrated.cwd": "/home/user",
  "editor.minimap.enabled": false,
  "files.watcherExclude": { "**/.cache/**": true, "**/node_modules/**": true },
  "files.exclude": { "**/.cache": true, "**/.local": true, "**/.vscode-data": true, "**/__pycache__": true }
}
JSON
    log "workspace settings criados em $HOME/.vscode/settings.json"
  fi
}

start_foreground() {
  install_runtime; seed_settings
  log "$("$RUNTIME/lib/node" "$RUNTIME/out/node/entry.js" --version 2>/dev/null | head -1)"
  log "http://0.0.0.0:${PORT}  •  pasta: $FOLDER"
  cd "$RUNTIME"
  # shellcheck disable=SC2086
  exec $RUNTIME/lib/node out/node/entry.js \
    --bind-addr "0.0.0.0:${PORT}" --auth none \
    --disable-telemetry --disable-update-check --disable-workspace-trust \
    --user-data-dir "$DATA" --extensions-dir "$EXTS" "$FOLDER"
}

start_detached() {
  cd "$RUNTIME"
  setsid nohup ./lib/node out/node/entry.js \
    --bind-addr "0.0.0.0:${PORT}" --auth none \
    --disable-telemetry --disable-update-check --disable-workspace-trust \
    --user-data-dir "$DATA" --extensions-dir "$EXTS" "$FOLDER" \
    > "$HOME/.vscode-data/server.log" 2>&1 < /dev/null &
  disown || true
}

wait_healthy() {
  local i
  for i in $(seq 1 60); do
    health && return 0
    sleep 1
  done
  return 1
}

case "$MODE" in
  run|start)
    start_foreground
    ;;
  ensure)
    if health; then
      echo "code-server já está no ar em :${PORT}"
      exit 0
    fi
    log "code-server fora do ar — subindo"
    install_runtime; seed_settings
    mkdir -p "$DATA"
    start_detached
    if wait_healthy; then
      echo "code-server no ar em :${PORT} ($("$RUNTIME/lib/node" "$RUNTIME/out/node/entry.js" --version 2>/dev/null | head -1))"
    else
      echo "FALHOU: sem healthz em ${PORT} — veja ~/.vscode-data/server.log" >&2
      tail -20 "$HOME/.vscode-data/server.log" >&2 || true
      exit 1
    fi
    ;;
  status)
    if health; then
      echo "no ar em :${PORT}"
      "$RUNTIME/lib/node" "$RUNTIME/out/node/entry.js" --version 2>/dev/null | head -1
    else
      echo "fora do ar (healthz falhou em :${PORT})"
      [[ -d "$RUNTIME" ]] && echo "runtime presente em $RUNTIME" || echo "runtime ausente em $RUNTIME"
      exit 1
    fi
    ;;
  stop)
    pkill -f "out/node/entry.js --bind-addr 0.0.0.0:${PORT}" && echo "parado" || echo "nada rodando em :${PORT}"
    ;;
  *)
    sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'
    ;;
esac

```

## Verificação (faça, não presuma)

**Nível 1 — servidor:**

```bash
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8080/healthz    # 200
curl -s -o /dev/null -w '%{http_code}\n' 'http://127.0.0.1:8080/?folder=/home/user'  # 200
curl -sD - -o /dev/null http://127.0.0.1:8080/ | grep -i x-frame          # vazio = ok no iframe
```

**Nível 2 — terminal (o teste que importa).** O terminal é onde esta stack quebra. Prove com
efeito colateral: rode um comando *dentro do terminal do editor* que escreva um arquivo, e
confira o arquivo por fora. Não confie em screenshot: o xterm desenha em canvas e às vezes
aparece vazio mesmo funcionando.

```python
# pip install playwright && python -m playwright install chromium
from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1400, "height": 880})
    pg.goto("http://127.0.0.1:8080/?folder=/home/user", wait_until="domcontentloaded", timeout=60000)
    pg.wait_for_selector(".monaco-workbench", timeout=90000)   # workbench montou
    time.sleep(7)
    print("tema:", [c for c in pg.eval_on_selector(".monaco-workbench", "e => e.className").split() if "vs-" in c])
    pg.keyboard.press("Control+Backquote"); time.sleep(9)       # abre o terminal
    pg.mouse.click(700, 700); time.sleep(1)                     # foca o xterm
    pg.keyboard.type("echo OK > /tmp/TERM_OK", delay=20)
    pg.keyboard.press("Enter"); time.sleep(6)
    b.close()
```

Depois: `cat /tmp/TERM_OK` → se imprimir `OK`, o terminal funciona de verdade. Se o arquivo
não existir, o `ptyHost` está morto: confira a versão (regra 1) e o log do servidor.

Ou rode o verificador que acompanha a skill (faz os três níveis e sai != 0 se falhar):

```bash
python3 ~/skills/code-server-arena/scripts/verify-vscode.py      # --json para parsear
```

Resultado esperado (tema escuro, explorer, terminal com shell real):
`references/expected-result.png`.

**Nível 3 — aparência:** o `className` do `.monaco-workbench` tem que conter `vs-dark`
(regra 3). Se vier `vs` sem `vs-dark`, o settings foi escrito no caminho errado.

## Protocolo de keep-alive (a cada turno)

Este é o pedido explícito do usuário: **o VS Code tem que estar no ar quando a interação
termina.** No fim de todo turno:

1. Rode `bash ~/bin/ensure-vscode.sh` (atalho idempotente: silencioso se já está no ar,
   reconstrói se a sessão reiniciou) ou `.../start-code-server.sh status` para olhar sem agir.
2. `healthz` respondeu 200 → nada a fazer, siga.
3. Não respondeu → **a sessão reiniciou**. Rode
   `bash ~/skills/code-server-arena/scripts/start-code-server.sh ensure` (baixa o runtime se
   precisar, ~6 s) e, se você tiver `start_process`, suba por ele no modo `run` para o
   preview voltar a ser registrado.
4. Confirme com `status` e diga ao usuário em uma linha que o editor está no ar (e que ele
   pode recarregar o preview).

**Sintoma de sessão reiniciada** (é assim que você descobre sem perguntar):
`~/.cache/code-server-runtime` não existe, o processo `entry.js` sumiu, e
`curl :8080/healthz` retorna `000`.

Se o usuário disser "sumiu o VS Code" / "o preview caiu": é isso. Não investigue, reconstrua.

## Troubleshooting

| Sintoma | Causa | Correção |
|---|---|---|
| Editor abre, terminal mudo, sem shell | build 4.135 quebrado (`No ptyHost heartbeat after 6 seconds`) | `VERSION=4.104.0` (o padrão do script) |
| Tema claro apesar do settings | settings no caminho errado (`data/User`) | mover para `<user-data-dir>/User/settings.json` |
| `healthz` 000 e Runtime ausente | sessão reiniciou e `.cache` foi limpo | `ensure` (baixa de novo) |
| Preview em branco / conexão recusada | bind em `127.0.0.1` ou processo subiu sem `start_process` | rebind `0.0.0.0` + subir por `start_process` |
| `Executable doesn't exist ... ms-playwright` ao verificar | browsers do Playwright vivem em `.cache` e somem com a sessão | `python3 -m playwright install chromium` (~12 s) |
| `Error: write EPIPE` ao abrir | cliente antigo tentando reconectar | recarregar o preview |
| 404 de `vsda_bg.wasm` / `vsda.js` no console | assinatura web do Copilot, não vem na release | ignorar, é inofensivo |
| `skill ausente` / `Permission denied` ao rodar script | o snapshot da Arena restaura arquivos como 644, **sem** bit de execução | `chmod +x ~/bin/*.sh ~/skills/*/scripts/*` e invoque com `bash script.sh` |
| Extensão desapareceu depois da sessão | `--extensions-dir` em `.cache` (efêmero de propósito) | reinstalar, ou mover para `~/.vscode-data/extensions` se for fixa |

## Persistência

| Sobrevive à sessão | Não sobrevive |
|---|---|
| arquivos do projeto, `~/.vscode-data` (settings/atalhos da UI), `~/.vscode/settings.json` | runtime (~450 MB em `.cache`), extensões, processos |

## Fluxo alternativo: usuário manda um tarball do code-server

Se a pessoa anexar um `restore-code-server.sh` (do tipo que espera um
`code-server-workspace.txt` = tarball gzip renomeado contendo o fonte + `node_modules`),
**confira se o tarball existe de fato** em `/home/user/uploads/`:

- **Existe:** `mv` para `.tar.gz`, extraia, rode o script do usuário, e siga esta skill para
  verificação, tema e keep-alive.
- **Não existe (caso comum):** não tente adivinhar nem compile do fonte. Use esta skill — a
  release oficial pré-compilada entrega o mesmo resultado (`lib/node`, `lib/vscode`,
  `out/node/entry.js`) em 6 s em vez de ~10 min.

## Segurança

`--auth none` em porta exposta pelo proxy do sandbox. A URL é aleatória e morre com a
sessão; ainda assim, trate o workspace como público. Para senha:
`--auth password --password <...>` no lugar de `--auth none`.
