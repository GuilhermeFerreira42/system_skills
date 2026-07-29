# execucao/ — Pasta de Trabalho por Projeto

**Versão:** 3.0
**Aplicação:** esta é a pasta que você copia (junto com o pacote inteiro) para a IA produtora. É aqui que o livro vai ser efetivamente produzido.

---

## O que tem aqui (template vazio)

Esta pasta começa vazia quando você acabou de copiar o pacote. Antes de passar para a IA, você precisa preencher três coisas:

1. `CONFIG.md` — copie da raiz do pacote e preencha
2. `GENERO.md` — copie do gênero escolhido em `generos_completos/[perfil]/`
3. `corpus/` — coloque aqui as fontes (transcrições, documentos, etc.)

As pastas `bible/`, `estado/` e `capitulos/` começam vazias. A IA produtora vai criar e preencher esses diretórios durante a execução.

---

## Estrutura final esperada (depois da execução)

```
execucao/
├── README.md                       ← este arquivo
├── CONFIG.md                       ← VOCÊ preenche antes
├── GENERO.md                       ← VOCÊ copia do gênero escolhido
│
├── corpus/                         ← VOCÊ coloca as fontes aqui
│   ├── fonte_01.md
│   ├── fonte_02.md
│   └── ...
│
├── bible/                          ← IA cria durante a execução
│   └── BIBLE_DA_OBRA.md            ← Fonte da verdade da obra
│
├── estado/                         ← IA cria durante a execução
│   └── ESTADO_DA_OBRA.md           ← Checkpoint operacional
│
└── capitulos/                      ← IA cria durante a execução
    └── capitulo_NN/
        └── cena_MM/
            ├── _saida_escritor.md
            ├── _afirmacoes_para_validar.json
            ├── _perguntas_continuidade.json
            ├── _resultado_march.json
            ├── _resultado_continuidade.json
            ├── _saida_editor.md
            ├── _saida_final.md
            └── _log_prompt_checker.md
```

---

## Como preparar a pasta antes de passar para a IA

### Passo 1 — Copie o CONFIG.md

```bash
cp ../CONFIG.md ./CONFIG.md
```

Abra e preencha:
- Título do livro
- Gênero escolhido (aponte para `generos_completos/[perfil]/GENERO.md`)
- Caminho do corpus (aponte para `execucao/corpus/`)
- Foco do usuário (instrução NotebookLM-style)

### Passo 2 — Copie o GENERO.md

```bash
cp ../generos_completos/[perfil_escolhido]/GENERO.md ./GENERO.md
```

Onde `[perfil_escolhido]` é `podbook_mentor`, `ficcao_literaria`, `tecnico_manual`, ou qualquer outro gênero customizado que você tenha criado.

### Passo 3 — Coloque o corpus

Copie as transcrições ou fontes para `execucao/corpus/`. Se o corpus vier misturado com material de marketing, separe antes — use só o conteúdo didático.

### Passo 4 — Verifique

Confirme que tem:
- `execucao/CONFIG.md` preenchido
- `execucao/GENERO.md` copiado
- `execucao/corpus/` com arquivos

### Passo 5 — Passe para a IA

Diga para a IA:

> "Leia primeiro o `execucao/CONFIG.md`, depois o `execucao/GENERO.md`, depois o `LEIA-ME-PRIMEIRO.md` e o `REGRAS_GREENFORGE_PIPELINE.md` e o `FLUXO_COMPLETO_PIPELINE.md`, depois a SKILL do seu papel. Comece pelo Passo 1 do BOOT do Orquestrador."

A IA vai seguir o pipeline cena por cena até o livro estar pronto.

---

## O que a IA vai criar durante a execução

A IA **NÃO** mexe em `CONFIG.md` nem em `GENERO.md` (são seus). A IA pode criar e modificar:

- `execucao/bible/BIBLE_DA_OBRA.md` — fonte da verdade, atualizada atomicamente
- `execucao/estado/ESTADO_DA_OBRA.md` — checkpoint operacional, atualizado atomicamente
- `execucao/capitulos/capitulo_NN/cena_MM/*` — todas as 8 saídas por cena

Esses arquivos são a entrega. No final da execução, o livro pronto é a concatenação de todos os `_saida_final.md` (após o Consolidador montar o front matter).
