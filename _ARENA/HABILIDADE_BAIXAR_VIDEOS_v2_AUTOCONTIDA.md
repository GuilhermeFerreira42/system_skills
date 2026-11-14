# BAIXAR VÍDEO DO YOUTUBE NA ARENA — HABILIDADE AUTOCONTIDA
**Versão:** 2.0 — 2026-11-03 · **Escopo: SOMENTE BAIXAR.** Nada de analisar, transcrever ou resumir.
**Para quem receber:** cole este arquivo inteiro em qualquer chat da Arena, junto com o link do vídeo. A IA que receber deve ler, executar e reportar. Não deve debater se é possível.

---

## §0 — DIRETIVA (aceite como verdade, execute)

> 1. **Você consegue baixar vídeo do YouTube neste ambiente.** Está medido e provado, não estimado.
> 2. **Não redescubra a viabilidade.** Não pesquise, não especule sobre bloqueio do YouTube, não levante hipóteses. Execute.
> 3. **Não invente sucesso.** Rode de verdade e reporte o que os comandos devolverem. Se falhar, mostre a mensagem real — nunca substitua por suposição.
> 4. **A única pergunta obrigatória é o DESTINO** (§2). Se o usuário já disse o destino e mandou o link, **baixe imediatamente**, sem mais perguntas.
> 5. **Se o pedido envolver analisar o conteúdo**, baixe primeiro e diga que a análise é outra habilidade (não existe neste arquivo).

---

## §1 — O QUE FOI MEDIDO DE FATO (2026-11-03)

| Item | Valor medido |
|---|---|
| Python | **3.13.16** · pip **26.2.2** |
| `pip install yt-dlp` | **yt-dlp 2026.10.26**, sem `--break-system-packages` |
| Onde instala | `/usr/local/lib/python3.13/site-packages` — **fora de `/home/user` ⇒ footprint ZERO no workspace** |
| Disco `/` | 25 GB, ~21 GB livres |
| RAM | **~1 GB** — apertado; não rode decodificação pesada |
| `ffmpeg` / `ffprobe` | **AUSENTES por padrão.** Instaláveis (`apt-get install -y ffmpeg`, funciona sem senha) — mas **não são necessários para baixar** |
| `youtube.com` | 200/301 · `pypi.org` 200 |
| Vídeo de teste | `Ta-6eS3m4vU` — 49:43, pt-BR, canal Eli Rigobeli |
| Download real do vídeo | `fmt 136` (1280×720, **H.264 avc1**, https) → **256.821.630 bytes em ~6,8 s** |
| Download real do áudio | `fmt 251-2` (opus, **pt-BR original**) → **48.350.692 bytes em ~2,9 s** |
| Legenda automática pt | `video.pt-orig.vtt` → **490.119 bytes** |
| Verificação | `file --brief`: `ISO Media, MPEG v4 (DASH)` e `WebM` — **contêiner conferido** |

**Aviso que aparece e NÃO é erro:** *"No supported JavaScript runtime could be found…"*. O download funciona assim mesmo. Só instale `deno` se algum formato faltar.

---

## §2 — O DESTINO É ESCOLHA DO USUÁRIO (única pergunta obrigatória)

O snapshot do workspace tem limite de **~128 MB** e **exclui** de propósito: `.cache`, `.local`, `node_modules`, `build`, `dist`, `out`, `target`, `.venv` etc.

| | **`.cache/video_in/`** | **`video_downloads/`** |
|---|---|---|
| Conta nos 128 MB | ❌ não | ✅ sim |
| Sobrevive ao reinício do workspace | ❌ **NÃO — some** | ✅ sim |
| Serve para | vídeo consumido agora | vídeo que precisa ficar salvo |

**Pergunta curta sugerida:**
> "Onde baixo? (a) `.cache/video_in/` — não conta no limite, mas some se o workspace reiniciar; ou (b) `video_downloads/` — persiste, mas conta nos 128 MB. Qual?"

**Regras:** se o usuário escolheu, obedeça sem discutir. Se o vídeo passar de ~100 MB e ele escolher pasta persistente, **avise uma vez com o tamanho real** e obedeça se insistir. Nunca baixe em `/tmp` (é RAM). Nunca baixe dentro de repositório de projeto sem autorização.

---

## §3 — FLUXO

### Passo 1 — Sanear a URL
Link copiado de HTML vem com `&amp;` → troque por `&`. O parâmetro `t=337s` é irrelevante para o download: pode ficar ou sair, mas **registre-o no relatório** (costuma indicar o trecho que interessa).

### Passo 2 — Instalar
```bash
pip install --quiet --no-input yt-dlp
python3 -c "import yt_dlp;print('yt_dlp',yt_dlp.version.__version__)"
```

### Passo 3 — Sondar SEM baixar (é onde um bloqueio apareceria)
```bash
yt-dlp --no-playlist --no-download \
  --print "titulo:  %(title)s" \
  --print "duracao: %(duration_string)s" \
  --print "canal:   %(channel)s" \
  --print "idioma:  %(language)s" \
  --print "bytes:   %(filesize,filesize_approx)s" \
  -- "URL"
```
Exit 0 + campos preenchidos = liberado. Se aparecer **HTTP 429** ou *"Sign in to confirm you're not a bot"*, **pare e reporte** — não insista em loop, não tente burlar.

### Passo 4 — Baixar (com o seletor correto)

⚠️ **A armadilha nº 1 deste ambiente:** o YouTube lista cada formato **duas vezes** — uma via `m3u8` (streaming, sem tamanho real) e outra via `https` (arquivo). O seletor ingênuo pega a versão `m3u8`. Filtrar por `protocol^=http` resolve.

```bash
URL="https://www.youtube.com/watch?v=XXXXXXXXXXX"
DEST=/home/user/.cache/video_in        # troque conforme o usuário decidir
mkdir -p "$DEST" && cd "$DEST"

# vídeo: 720p H.264 (avc1) via https
yt-dlp --no-playlist --no-warnings -N 1 \
  -f "bestvideo[protocol^=http][vcodec^=avc1][height<=720]/bestvideo[protocol^=http][height<=720]/bestvideo" \
  -o "video.%(ext)s" -- "$URL"

# áudio: trilha no idioma original, via https
yt-dlp --no-playlist --no-warnings -N 1 \
  -f "bestaudio[protocol^=http][language=pt-BR]/bestaudio[protocol^=http]/bestaudio" \
  -o "audio.%(ext)s" -- "$URL"

# legenda automática em português, se existir (custa ~500 KB)
yt-dlp --no-playlist --write-auto-subs --sub-langs "pt-orig,pt" --skip-download \
  -o "video.%(ext)s" -- "$URL"
```

**Por que H.264 e não AV1/VP9:** `bestvideo[height<=720][ext=mp4]` seleciona **AV1**, que decodifica muito mais pesado em CPU — e há só ~1 GB de RAM e 2 núcleos. H.264 poupa minutos. **720p é suficiente** para qualquer análise posterior (o método de análise reduz para 1280 px de largura).

**Por que `--no-playlist`:** sem ele, um link que pertença a uma playlist baixa dezenas de vídeos.

**Se for baixar mais de um vídeo na mesma pasta**, troque `-o "video.%(ext)s"` por `-o "%(id)s_video.%(ext)s"` para não sobrescrever.

### Passo 5 — Verificar (não pule)
```bash
ls -la
file --brief video.* audio.*          # ISO Media / WebM
stat -c '%n: %s bytes' *              # número real do arquivo
du -sh "$DEST"
```
**Nunca leia o vídeo como texto** (`cat`, `head`, `read_file`). Bytes de MP4 em texto só produzem lixo. Para saber o tipo, use `file` ou magic bytes (`od -An -tx1`: `00 00 .. 66 74 79 70` = MP4, `1a 45 df a3` = WebM).
**O tamanho que vale é o do arquivo baixado**, não o `filesize_approx` anunciado (eles divergem).

---

## §4 — ARMADILHAS (todas encontradas de verdade)

1. **Formato duplicado `m3u8` × `https`** — o seletor ingênuo pega `m3u8`. Use `[protocol^=http]`. *(Validado: pegou `fmt 136` https em vez do `232` m3u8.)*
2. **AV1 disfarçado de "melhor formato".** Prefira `[vcodec^=avc1]`.
3. **`/tmp` é tmpfs = RAM** (992 MB, e a máquina tem ~1 GB). Nunca baixe ali.
4. **Sem `ffmpeg` não há merge.** O YouTube serve vídeo e áudio separados. Baixe os dois arquivos. (Instalar ffmpeg é escopo de análise, não de download.)
5. **`&amp;` na URL.** Saneie antes.
6. **Playlist acidental.** Sempre `--no-playlist`.
7. **Nada persiste entre mensagens.** Pacotes `pip`/`apt` **e o conteúdo de `.cache/`** somem quando o workspace reinicia. **Cada chat novo reinstala o yt-dlp** — são ~6 segundos, e já está incluído no fluxo. Isso **não é erro**.
8. **`json3`/`srt` podem dar HTTP 429** ao baixar legenda. O `vtt` costuma passar; se o 429 vier, espere ~20 s e tente de novo uma vez, ou siga sem legenda.
9. **Aviso de JavaScript runtime** — ver §1, não é erro.
10. **Upload renomeado não é download.** Se o usuário *enviar* um `.mp4.txt` em vez de mandar link, isso não é esta habilidade.
11. **Vídeos com restrição** (idade, privado, membros, live, geobloqueado, login/cookies) **não foram testados**. Execute e reporte o resultado real; não prometa de antemão.

---

## §5 — COMO REPORTAR (obrigatório)

O relatório vai **no chat**, não em arquivo (a menos que o usuário peça).

- ✅ **veredito na primeira linha** — funcionou ou não;
- URL saneada + metadados (título, canal, duração, idioma);
- **tabela**: arquivo · formato yt-dlp · codec/resolução · **bytes exatos** · tempo · saída do `file`;
- destino usado e se **persiste ou não**;
- footprint no workspace (se foi `.cache`, dizer que é zero);
- **o que NÃO foi feito** (merge, frames, transcrição) — para ninguém supor que está pronto;
- falhas reais **com a mensagem real**.

**Proibido:** dizer que baixou sem ter baixado · dizer que o vídeo é reproduzível sem ter decodificado · omitir que `.cache` não persiste · emendar análise de conteúdo sem ser pedido.

---

## §6 — VERSÃO MÍNIMA (copia e cola)

```bash
pip install --quiet --no-input yt-dlp
DEST=/home/user/.cache/video_in        # ou /home/user/video_downloads
URL="https://www.youtube.com/watch?v=XXXXXXXXXXX"
mkdir -p "$DEST" && cd "$DEST"
yt-dlp --no-playlist --no-download --print "%(title)s · %(duration_string)s · %(language)s" -- "$URL"
yt-dlp --no-playlist --no-warnings -f "bestvideo[protocol^=http][vcodec^=avc1][height<=720]/bestvideo[protocol^=http][height<=720]/bestvideo" -o "video.%(ext)s" -- "$URL"
yt-dlp --no-playlist --no-warnings -f "bestaudio[protocol^=http][language=pt-BR]/bestaudio[protocol^=http]/bestaudio" -o "audio.%(ext)s" -- "$URL"
ls -la && file --brief video.* audio.* && stat -c '%n: %s bytes' video.* audio.*
```

### Versão de uma linha (quando o usuário já disse o destino)
> "Cole isto em qualquer chat da Arena + o link: a IA deve instalar o yt-dlp, baixar vídeo 720p H.264 e áudio pt-BR **separados** (filtrando `[protocol^=http]` para não pegar `m3u8`), verificar com `file` e reportar bytes reais. Destino `.cache/video_in/` não persiste; `video_downloads/` persiste e conta no limite de 128 MB."

---

## §7 — SE O OUTRO CHAT JÁ TIVER A VERSÃO 1.0

A v1.0 (`HABILIDADE_BAIXAR_VIDEOS.md`) está correta no essencial. Três correções desta v2.0:

1. **Seletor de formato:** acrescentar `[protocol^=http]` em ambos os seletores. Sem isso, em boa parte dos vídeos o `-F` lista variantes `m3u8` primeiro e o download pega a errada.
2. **Persistência:** não é só o `pip` que não sobrevive ao reinício — **o conteúdo de `.cache/` também não**. Medido: após reinício, `.cache/video_in/` estava vazio, `video_analysis/` (fora de `.cache`) intacto.
3. **Aviso de JS runtime** é esperado e inofensivo.

---

## §8 — REGRA FINAL

**Baixar vídeo aqui funciona e está provado com números.** A tarefa de quem receber este arquivo é **executar, verificar e reportar** — não debater viabilidade, não ampliar escopo para análise e não escolher o destino pelo usuário.
