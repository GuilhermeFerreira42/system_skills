# Pipeline Genérico Greenforge v3

**Versão:** 3.0 (Pipeline Parametrizado)
**Aplicação:** framework genérico de produção de livros. Copie, escolha um gênero, configure, e passe para qualquer IA.

---

## O que é isso

Este pacote é um **pipeline de produção de livros** baseado no framework Greenforge. Ele é **genérico** — não tem gênero embutido, não tem voz fixa, não tem extensão por cena rigidamente definida. Tudo isso vem do **arquivo de gênero** que o usuário escolhe ou cria.

A ideia central é separar duas coisas que normalmente ficam misturadas: **a estrutura do pipeline** (como produzir, validar, atualizar atomicamente) e **as decisões de gênero** (que voz, que formato, que extensão). Este pacote entrega a primeira parte. O gênero é um arquivo separado que pode ser trocado, customizado, ou criado do zero.

## Para quem é

- Para quem quer produzir livros (não-ficção, ficção, técnico) com garantia de qualidade consistente
- Para quem quer um pipeline que possa ser passado para qualquer IA (Claude, ChatGPT, Gemini, etc.)
- Para quem quer reutilizar a mesma estrutura para diferentes gêneros sem reescrever as skills
- Para quem valoriza rastreabilidade, validação contra corpus, e auditabilidade

## Para quem NÃO é

- Para quem quer "escrever um livro em 5 minutos" — este pipeline é lento por design (cena por cena, validação dupla)
- Para quem não tem corpus ou fonte de verdade — sem fontes, a validação MARCH fica limitada
- Para quem não aceita a granularidade — se você quer produzir 50 cenas numa só chamada, este pipeline vai te frustrar

---

## Como funciona (visão geral)

O pipeline tem **7 agentes especializados** que trabalham em sequência cena por cena:

1. **Orquestrador** — coordena o loop, mantém Bible e Estado
2. **Escritor** — produz a prosa da cena seguindo o gênero
3. **Atomizador** — extrai afirmações factuais para validação
4. **Validador MARCH** — verifica afirmações contra o corpus (cego, não vê a prosa)
5. **Validador de Continuidade** — verifica coerência com Bible e Estado (cego, não vê a prosa)
6. **Editor** — faz polimento sem mudar substância
7. **Consolidador** — junta todas as cenas finais no livro

Cada cena passa por todos os 7, com salvamento atômico (Lei 3), checksum SHA256 (Lei 4), e isolada em pasta própria (Lei 5).

---

## Início rápido (5 passos)

### 1. Copie o pacote

```bash
cp -r skills_book_v3_PIPELINE_GENERICO/ meu_livro/
cd meu_livro/
```

### 2. Escolha um gênero

Veja os gêneros disponíveis em `generos_completos/`:

- `podbook_mentor/` — para livros baseados em transcrições de aulas (1ª pessoa, voz de mentor)
- `ficcao_literaria/` — para romances, contos, narrativas literárias
- `tecnico_manual/` — para manuais how-to, livros didáticos de programação

### 3. Preencha o CONFIG.md

```bash
cp CONFIG.md execucao/CONFIG.md
```

Abra `execucao/CONFIG.md` e preencha:
- Título do livro
- Gênero escolhido (ex: `generos_completos/podbook_mentor/GENERO.md`)
- Caminho do corpus
- Foco do usuário

### 4. Copie o GENERO.md e o corpus

```bash
cp generos_completos/podbook_mentor/GENERO.md execucao/GENERO.md
cp -r /caminho/do/seu/corpus/* execucao/corpus/
```

### 5. Passe para a IA

Diga:

> "Leia primeiro o `execucao/CONFIG.md`, depois o `execucao/GENERO.md`, depois o `LEIA-ME-PRIMEIRO.md` e o `REGRAS_GREENFORGE_PIPELINE.md` e o `FLUXO_COMPLETO_PIPELINE.md`, depois a SKILL do seu papel. Comece pelo Passo 1 do BOOT do Orquestrador."

A IA vai seguir o pipeline cena por cena até o livro estar pronto.

---

## Estrutura do pacote

```
skills_book_v3_PIPELINE_GENERICO/
├── README.md                                ← ESTE ARQUIVO
├── LEIA-ME-PRIMEIRO.md                      ← Para a IA produtora
├── REGRAS_GREENFORGE_PIPELINE.md            ← As 6 leis duras
├── FLUXO_COMPLETO_PIPELINE.md                ← Passo a passo do loop
├── CONFIG.md                                ← Você preenche antes
│
├── generos_template/
│   └── TEMPLATE_GENERO_VAZIO.md              ← Para criar gênero novo
│
├── generos_completos/                       ← Repositório de gêneros
│   ├── README.md
│   ├── podbook_mentor/
│   ├── ficcao_literaria/
│   └── tecnico_manual/
│
├── escritor/                                 ← 7 agentes (BOOT + SKILL)
├── atomizador/
├── validador_march/
├── validador_continuidade/
├── editor/
├── consolidador/
├── orquestrador/
│
├── bible/                                    ← Templates da fonte da verdade
├── estado/                                   ← Template do checkpoint operacional
├── regras_negocio/                           ← Cenas proibidas + auto-auditoria
├── templates_bible_worktree/                ← 6 templates JSON/MD
│
├── capitulos_exemplo/                        ← Calibração (vazio por padrão)
│
└── execucao/                                 ← Pasta de trabalho por projeto
    ├── README.md
    ├── CONFIG.md                             ← Você preenche (copia da raiz)
    ├── GENERO.md                             ← Você copia do gênero escolhido
    ├── corpus/                               ← Você coloca as fontes
    ├── bible/                                ← IA cria
    ├── estado/                               ← IA cria
    └── capitulos/                            ← IA cria
```

---

## As 6 Leis Duras (resumo)

1. **Cena por cena, sempre.** Nunca produza o livro inteiro em uma chamada. Uma cena = uma unidade de produção.
2. **Validação dupla cega, sempre.** MARCH (corpus) + Continuidade (Bible/Estado). Ambos cegos para a prosa.
3. **Atualização atômica, sempre.** Bible e Estado via `os.replace`, nunca `write` direto.
4. **Checksum e round-trip, sempre.** SHA256 (8 primeiros chars) + verificação contra o disco.
5. **Isolamento por worktree, sempre.** Cada cena em pasta isolada, nada vaza entre cenas.
6. **Zero material de marketing, sempre.** O livro é didático, não página de venda.

Detalhes em `REGRAS_GREENFORGE_PIPELINE.md`.

---

## Adicionando um gênero novo

Se você quer produzir livros em um gênero que não está nos 3 exemplos:

1. Copie `generos_template/TEMPLATE_GENERO_VAZIO.md` para `generos_completos/[nome]/GENERO.md`
2. Preencha todas as 11 seções (nenhuma pode ter "[definir]")
3. Crie uma Bible exemplo em `generos_completos/[nome]/BIBLE_EXEMPLO.md`
4. Produza 1-2 capítulos de calibração usando o pipeline
5. Valide que funciona
6. Adicione uma entrada no `generos_completos/README.md`

Sugestão de gêneros para criar:
- **Acadêmico/Didático** — textbooks, livros de curso universitário
- **Biografia/Memórias** — narrativas de vida, em 1ª pessoa
- **Autoajuda prática** — livros de produtividade, hábitos, carreira
- **Relato de viagem** — narrativas de lugares, culturas, experiências
- **HQ/Roteiro** — adaptações do pipeline para roteiros visuais

---

## Limitações conhecidas

- **Custo:** como cada cena passa por validação dupla, o custo de produção é mais alto que "escrever tudo de uma vez". É um trade-off explícito: pagar mais por garantia de qualidade.
- **Tempo:** a granularidade cena por cena é intencionalmente lenta. Para um livro de 30 cenas, espere uma produção que leva algumas horas (dependendo da IA).
- **Dependência de corpus:** o pipeline funciona melhor com corpus robusto. Para ficção sem corpus, a Bible precisa ser muito bem feita antes de começar.
- **Modelo com ferramentas:** a IA produtora precisa ter acesso a ferramentas de leitura/escrita de arquivos. Modelos só-texto não conseguem executar este pipeline.

---

## Origem

Este pacote é a v3 do projeto Greenforge de produção de livros. A v2 era específica para Podbook (livro baseado em transcrições com voz de mentor). A v3 generalizou o pipeline para qualquer gênero, com a v2 virando o perfil `podbook_mentor` em `generos_completos/`.

A v1 não existe publicamente — era a fase de exploração onde o framework Greenforge foi definido.

---

## Próximos passos

1. Leia `LEIA-ME-PRIMEIRO.md` (orientado para a IA, mas útil para você também)
2. Escolha um gênero em `generos_completos/`
3. Leia o `GENERO.md` e o `BIBLE_EXEMPLO.md` do gênero escolhido
4. Se for criar gênero novo, leia `generos_template/TEMPLATE_GENERO_VAZIO.md`
5. Prepare `execucao/` com CONFIG, GENERO, e corpus
6. Passe para a IA e acompanhe cena por cena
