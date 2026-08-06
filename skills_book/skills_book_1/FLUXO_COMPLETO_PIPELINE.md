# FLUXO COMPLETO DO PIPELINE GENÉRICO — Passo a Passo para o Orquestrador

**Versão:** 3.0
**Aplicação:** O Orquestrador é o único agente que lê este arquivo.

---

## 🎯 Visão Geral

O fluxo de produção de um livro com este pipeline genérico tem 7 fases:

1. Inicialização (ler CONFIG, GENERO, criar Bible, Estado, Plano)
2. Para cada cena do plano: loop de produção
3. Validação cega dupla (MARCH + Continuidade)
4. Atualização atômica (Bible + Estado)
5. Checksum + round-trip
6. Consolidação final (gera livro_final.md)
7. Validação de fronteira (integridade do livro consolidado)

Tempo total esperado: depende do tamanho do livro, mas **cada cena leva entre 15 e 25 minutos** do pipeline completo.

---

## FASE 0 — Pré-execução (uma vez, antes de tudo)

### 0.1 Carregar contexto
- Ler `execucao/CONFIG.md` (preenchido pelo usuário)
- Ler `execucao/GENERO.md` (o gênero do livro)
- Identificar a pasta do corpus (`execucao/corpus/`)
- Ler a SKILL do seu papel (Orquestrador)
- Se o gênero tem capítulos de calibração, ler pelo menos 1 cena completa

### 0.2 Identificar recursos
- **Corpus:** o usuário forneceu em `execucao/corpus/`. Identificar todos os arquivos `.md`/`.txt`. **NÃO incluir** páginas de venda, e-mails marketing, PDFs de preços.
- **Gênero:** `execucao/GENERO.md` (preenchido pelo usuário)
- **Foco do usuário:** vem do `CONFIG.md`
- **Bible exemplo:** vem do gênero escolhido (em `generos_completos/[perfil]/BIBLE_EXEMPLO.md`)

### 0.3 Criar estrutura de pastas em `execucao/`

```
execucao/
├── CONFIG.md                    ← já existe, preenchido pelo usuário
├── GENERO.md                    ← já existe, preenchido pelo usuário
├── corpus/                      ← já existe, com as fontes
├── bible/
│   └── bible_da_obra.md         ← você cria
├── estado/
│   └── estado_da_obra.md        ← você cria
├── capitulos/                   ← você cria vazia, popula cena a cena
│   ├── capitulo_01/
│   │   ├── cena_01/
│   │   ├── cena_02/
│   │   └── ...
└── livro_final.md               ← você gera no final (via Consolidador)
```

---

## FASE 1 — Inicialização

### 1.1 Criar Bible da Obra
Abrir `execucao/bible/bible_da_obra.md` e preencher a partir de `bible/BIBLE_TEMPLATE_PIPELINE.md`.

**O que colocar na Bible (versão inicial):**

- **Metadados Gerais:** título, subtítulo, gênero, subgênero, público-alvo, tom de voz, POV, tempo verbal, distância narrativa, vocabulário, ritmo, versão 1.0.
- **Premissa & Estrutura:** logline, tema central, pergunta temática, estrutura narrativa, número estimado de capítulos e cenas, palavras estimadas.
- **Trilha Selecionada:** quais módulos do corpus entram no livro.
- **Glossário Técnico:** extrair do corpus todos os termos técnicos com definição canônica. Marcar quais são "regra rígida".
- **Conceitos-Chave do Método:** marcos centrais do que o livro ensina.
- **Cases / Estudos de Caso:** nomes, produtos, números.
- **Personas do Leitor:** quem é o público-alvo.
- **Cenários / Locais:** onde a "ação" se passa.
- **Cronologia do Método:** linha do tempo.
- **Mitos do Mercado:** lista de equívocos a desconstruir (se aplicável ao gênero).
- **Fios Narrativos:** setups e payoffs planejados.
- **Decisões Editoriais Travadas:** regras que não mudam.
- **Fontes do Corpus:** mapeamento por capítulo.

### 1.2 Criar Estado da Obra
Abrir `execucao/estado/estado_da_obra.md` e preencher a partir de `estado/ESTADO_TEMPLATE_PIPELINE.md`.

**O que colocar no Estado (versão inicial):**

- **Metadados:** timestamp, status geral (EM_ANDAMENTO), gênero, subgênero, foco do usuário, capítulos planejados, capítulos concluídos (0), cena atual, chamadas gastas, limite de chamadas, versão da Bible, checksum da Bible.
- **Arquétipo e Voz (Travadas):** repete as decisões da Bible sobre voz, tempo verbal, distância, tom, ritmo.
- **Plano de Capítulos e Cenas (Granular):** tabela com 1 linha por cena planejada.
- **Detalhamento do Capítulo Atual:** tabela vazia.
- **Pendências e Bloqueios:** lista de pendências.
- **Histórico de Retries:** tabela vazia.
- **Foco do Usuário:** texto literal passado pelo usuário.
- **Checkpoint de Retomada:** cena onde começar.

### 1.3 Salvar atomicamente
Bible e Estado devem ser salvos usando o procedimento atômico.

---

## FASE 2 — Loop de Produção por Cena

Para cada cena do plano, na ordem:

### 2.1 Criar worktree isolada

```bash
mkdir -p execucao/capitulos/capitulo_NN/cena_MM
```

### 2.2 ETAPA A — INVOCAR Escritor

**Input para o Escritor:**
- ID da cena, título, objetivo, POV, palavras estimadas
- Gênero (`execucao/GENERO.md`)
- Bible (versão atual)
- Resumo da cena anterior (se houver)
- Foco do usuário

**Output esperado:**
- `_saida_escritor.md` (1.000–4.000 palavras, com `## Resumo` e `## Seu checklist` no fim)
- `_metadados_cena.json` (opcional)

**Verificação:** o Orquestrador confirma que `_saida_escritor.md` existe, tem entre 1.000 e 4.000 palavras, e o formato do fim está correto (conforme o gênero define).

### 2.3 ETAPA B — INVOCAR Atomizador

**Input:**
- `_saida_escritor.md` (cena atual)

**Output esperado:**
- `_afirmacoes_para_validar.json` (afirmações factuais extraídas, com filtro de prioridade)
- `_perguntas_validador.json` (perguntas binárias para MARCH)

### 2.4 ETAPA C — Salvar log do prompt do Validador MARCH

**Antes de invocar o MARCH**, salvar o prompt em `_log_prompt_checker.md`.

### 2.5 ETAPA D — INVOCAR Validador MARCH (cego)

**Input:**
- `_perguntas_validador.json`
- Caminho do corpus
- **NÃO** `_saida_escritor.md` (cegueira!)

**Output esperado:**
- `_resultado_march.json`

### 2.6 ETAPA E — Auditoria de Cegueira

```python
log = LER(f"{worktree}/_log_prompt_checker.md")
prosa = LER(f"{worktree}/_saida_escritor.md")
SE prosa in log:
    REPROVADO por violação de cegueira
    PARAR
```

### 2.7 ETAPA F — Recalcular Agregados MARCH

```python
total = len(resultados)
confirmados = sum(1 for r in resultados if r["status"] == "CONFIRMADO")
contraditos = sum(1 for r in resultados if r["status"] == "CONTRADITO")
nao_encontrados = sum(1 for r in resultados if r["status"] == "NAO_ENCONTRADO")
taxa = confirmados / total if total > 0 else 0
```

**Travas:**
- `contraditos > 0` → REPROVADO
- `taxa < 0.80` → REPROVADO
- `nao_encontrados > total * 0.30` → REPROVADO

**Se REPROVADO:** registrar motivo, incrementar retries, reescrita cirúrgica, voltar para 2.2.

### 2.8 ETAPA G — INVOCAR Validador de Continuidade (cego)

**Input:**
- Perguntas de continuidade (geradas pelo Orquestrador)
- Bible + Estado
- **NÃO** `_saida_escritor.md`

**Output esperado:**
- `_resultado_continuidade.json`

**Travas:**
- `contraditos > 0` → REPROVADO
- (NAO_ENCONTRADO é OK)

### 2.9 ETAPA H — INVOCAR Editor

**Input:**
- `_saida_escritor.md` (prosa validada)
- Gênero + Bible

**Output esperado:**
- `_saida_editor.md` (prosa polida)
- `_metadados_editor.json`

### 2.10 ETAPA I — Copiar para `_saida_final.md` e calcular checksum

```python
import shutil
import hashlib

shutil.copy(f"{worktree}/_saida_editor.md", f"{worktree}/_saida_final.md")

with open(f"{worktree}/_saida_final.md", "rb") as f:
    conteudo = f.read()

checksum = hashlib.sha256(conteudo).hexdigest()[:8]
bytes_size = len(conteudo)
```

### 2.11 ETAPA J — Atualizar Bible (atomicamente)

Adicione à Bible:
- Novos conceitos introduzidos
- Mudanças no estado da obra
- Cases citados pela primeira vez
- Fios abertos ou resolvidos
- Versão incrementada

### 2.12 ETAPA K — Atualizar Estado (atomicamente)

Atualize o Estado:
- `cena.status = "CONCLUIDO"`
- MARCH + Cont APROVADO
- Checksum + bytes
- Retries gastos
- Próxima cena como cena_atual
- Histórico de Retries (se houve reescrita)
- Versão da Bible (sincronizada)

### 2.13 ETAPA L — Round-trip Check

```python
with open(f"{worktree}/_saida_final.md", "rb") as f:
    conteudo_re_lido = f.read()
checksum_re_lido = hashlib.sha256(conteudo_re_lido).hexdigest()[:8]

SE checksum_re_lido != checksum:
    cena.status = "INCONSISTENTE"
    PARAR
```

Se OK, cena CONCLUÍDA. Avançar.

---

## FASE 3 — Consolidação (uma vez, ao final)

### 3.1 INVOCAR Consolidador

**Input:** plano + estado + Bible + Gênero

**Output:** `execucao/livro_final.md` (com front matter, sumário, cenas, glossário, checklist, agradecimentos)

### 3.2 Validação de Fronteira
- Total de palavras do livro vs soma das cenas (tolerância 5%)
- Todas as cenas CONCLUÍDAS estão presentes
- Ordem narrativa preservada
- Nenhuma cena PENDENTE/REPROVADA
- Checksums das cenas conferem

### 3.3 Auto-Auditoria Lei 6
- Grep por padrões de marketing
- Se retornar matches, REPROVADO, voltar e limpar

### 3.4 Salvar
- `execucao/livro_final.md`
- Atualizar Estado com `status_geral = "CONCLUIDO"`

---

## 🚦 Critérios de Parada Imediata

| Condição | Ação |
|---|---|
| Prompt MARCH contém prosa do Escritor | PARAR + REPROVADO (cegueira violada) |
| Checksum round-trip falha | PARAR + INCONSISTENTE |
| 3 retries excedidos | MARCAR REPROVADO + PULAR (não trava) |
| Bible ou Estado ilegíveis | PARAR (corrupção) |
| Corpus não encontrado | PARAR (input inválido) |
| Gênero não encontrado | PARAR (input inválido) |

---

## 📊 Estimativa de Tempo

- Cena simples (1.000-1.500 palavras): 12-18 min
- Cena complexa (3.000-4.000 palavras): 20-30 min
- Reescrita cirúrgica: +5-10 min
- Validação MARCH: 1-2 min
- Validação Continuidade: 1-2 min
- Editor: 2-3 min
- Atualização atômica: <1 min
- Consolidação: 5-10 min

Para um livro de 50 cenas, espere entre 12 e 20 horas de execução total, espalhadas em múltiplas sessões.
