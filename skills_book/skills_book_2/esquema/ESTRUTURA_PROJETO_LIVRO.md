# ESTRUTURA DO PROJETO LIVRO

**Versao:** 1.0
**Data:** 2026-07-27

---

## Visão Geral

Esta estrutura define a organização de pastas e arquivos para a produção de livros via sistema de skills Greenforge-style. Cada capítulo é isolado em sua própria worktree (pasta), garantindo que reescritas cirúrgicas não contaminem outros capítulos.

---

## Estrutura de Diretórios

```
projeto_livro/
├── corpus/                          # Material bruto (input do usuário)
│   ├── corpus_principal.md          # Livro fonte, pesquisa, transcrições
│   ├── corpus_supplementary.md      # Material complementar (opcional)
│   └── corpus_references.md         # Referências, citações, bibliografia
├── bible/                           # Bible da Obra - Fonte da Verdade
│   ├── bible_da_obra.md             # Bible principal (atualizada a cada capítulo)
│   ├── bible_personagens.md         # Fichas de personagens (se ficção)
│   ├── bible_cenarios.md            # Worldbuilding, locais, regras do mundo
│   ├── bible_cronologia.md          # Timeline de eventos
│   └── bible_conceitos.md           # Conceitos-chave, termos, definições
├── estado/                          # Estado da Produção (checkpoint único)
│   └── estado_da_obra.md            # Granular por capítulo/cena
├── capitulos/                       # Worktrees isolados por capítulo
│   ├── capitulo_01/
│   │   ├── _saida_escritor.md       # Output do Escritor
│   │   ├── _afirmacoes_para_validar.json  # Output do Atomizador
│   │   ├── _resultado_march.json    # Output do Validador MARCH
│   │   ├── _resultado_continuidade.json   # Output do Validador Continuidade
│   │   ├── _saida_editor.md         # Output do Editor (opcional)
│   │   ├── _metadados_capitulo.json # Metadados para consolidador
│   │   └── rascunhos/               # Material de trabalho descartável
│   ├── capitulo_02/
│   └── capitulo_NN/
├── generos/                         # Definições de gênero (carregadas em runtime)
│   ├── GENERO_ROMANCE.md
│   ├── GENERO_NAO_FICCAO.md
│   ├── GENERO_MEMORIAS.md
│   ├── GENERO_TECNICO.md
│   └── GENERO_PERSONALIZADO.md      # Criado ad-hoc pelo usuário
├── livro_final.md                   # Livro consolidado (Markdown)
├── livro_final.epub                 # EPUB gerado (opcional)
├── livro_final.pdf                  # PDF gerado (opcional)
├── estado_da_obra.md                # Cópia do estado para referência rápida
└── bible_da_obra.md                 # Cópia da bible para referência rápida
```

---

## Detalhamento dos Arquivos Principais

### 1. Bible da Obra (`bible/bible_da_obra.md`)

**Função:** Fonte única da verdade sobre a obra. Atualizada a cada capítulo aprovado.
**Acesso:** Leitura pelo Validador Continuidade, Editor, Consolidador. Escrita pelo Orquestrador.

```markdown
# Bible da Obra: [TÍTULO]

## Metadados
- Titulo: 
- Subtitulo:
- Genero:
- Subgenero:
- Publico_alvo:
- Tom_de_voz:
- POV_padrao: (1ª pessoa / 3ª limitada / 3ª onisciente / múltiplos)
- Tempo_verbal: (presente / passado)

## Premissa & Estrutura
- Logline:
- Tema_central:
- Estrutura_narrativa: (3 atos / jornada do herói / kishotenketsu / outro)
- Numero_estimado_capitulos:

## Personagens Principais
| Nome | Papel | Arquetipo | Objetivo | Conflito_interno | Voz_caracteristica |
|------|-------|-----------|----------|------------------|-------------------|

## Cenários / Worldbuilding
| Local | Descricao | Regras | Relevancia |

## Cronologia
| Capitulo | Data_Evento | Eventos_Principais | Personagens_Presentes |

## Conceitos-Chave & Terminologia
| Termo | Definição | Primeira_Ocorrência |

## Fios Narrativos Abertos
| Fio | Introduzido_em | Status | Resolvido_em |

## Decisões Editoriais Travadas
| Decisao | Capitulo_Origem | Justificativa |
```

---

### 2. Estado da Obra (`estado/estado_da_obra.md`)

**Função:** Checkpoint granular por capítulo/cena. Permite retomada exata.
**Acesso:** Leitura/Escrita pelo Orquestrador. Leitura pelo Escritor (contexto anterior), Editor, Consolidador.

```markdown
# Estado da Obra: [TÍTULO]

## Metadados
- Ultima_atualizacao: 2026-07-27 14:30
- Status_geral: EM_ANDAMENTO | CONCLUIDO | INTERROMPIDO
- Capitulos_planejados: 12
- Capitulos_concluidos: 3
- Capitulo_atual: 4
- Cena_atual: 2
- Chamadas_gastas: 47
- Limite_chamadas: 200

## Progresso por Capítulo (Granularidade por Cena)

| Cap | Titulo | Cenas_Planeadas | Cenas_Concluidas | Status | Validacao_MARCH | Validacao_Cont | Ultima_Acao |
|-----|--------|-----------------|------------------|--------|-----------------|----------------|-------------|
| 01  | O Inicio | 3 | 3 | CONCLUIDO | APROVADO | APROVADO | 2026-07-27 10:15 |
| 02  | A Jornada | 4 | 4 | CONCLUIDO | APROVADO | APROVADO | 2026-07-27 12:30 |
| 03  | O Encontro | 3 | 3 | CONCLUIDO | APROVADO | APROVADO | 2026-07-27 14:00 |
| 04  | A Prova | 4 | 1 | ESCREVENDO | PENDENTE | PENDENTE | Escritor: Cena 2 |
| 05  | O Aliado | 3 | 0 | PENDENTE | - | - | Aguardando Cap 04 |
| ... | ... | ... | ... | ... | ... | ... | ... |

## Detalhamento do Capítulo Atual (Cap 04)

| Cena | Titulo | POV | Status | MARCH | Cont | Palavras | Ultima_Acao |
|------|--------|-----|--------|-------|------|----------|-------------|
| 1 | Chegada | Protagonista | CONCLUIDO | APROVADO | APROVADO | 2.3k | Validado |
| 2 | O Enigma | Protagonista | ESCREVENDO | PENDENTE | PENDENTE | - | Escritor trabalhando |
| 3 | Revelação | Antagonista | PENDENTE | - | - | - | Aguardando Cena 2 |
| 4 | Decisão | Protagonista | PENDENTE | - | - | - | Aguardando Cena 3 |

## Pendências e Bloqueios
- Cap 04, Cena 2: aguardando conclusão do Escritor
- Cap 05: bloqueado até Cap 04 CONCLUIDO (precisa contexto anterior)

## Histórico de Retries (por Capítulo)

| Cap | Tentativa | Motivo_Falha | Acao_Corretiva |
|-----|-----------|--------------|----------------|
| 02  | 1         | MARCH: 2 contraditas | Reescrita cirúrgica Cena 3 |
| 03  | 1         | Continuidade: personagem em local errado | Reescrita Cena 1 |

## Foco do Usuário (NotebookLM-style)
> "Foque na tensão psicológica do protagonista. Evite descrições longas de cenário. 
> O leitor precisa sentir a paranoia crescente a cada capítulo."
```

---

### 3. Output do Escritor (`capitulos/capitulo_NN/_saida_escritor.md`)

```markdown
# Capítulo 04: A Prova — Cena 2: O Enigma

[Texto narrativo completo da cena/capítulo, sem formatação de roteiro,
sem speakers, sem JSON. Apenas prosa literária.]

---

## Metadados da Cena (para o Orquestrador)
- capitulo: 4
- cena: 2
- titulo: "O Enigma"
- pov: "Protagonista (Elena)"
- tempo_verbal: "passado"
- palavras_estimadas: 2800
- foco_usuario_aplicado: "Tensão psicológica, paranoia, sem descrições longas"
- bible_versao_usada: "v3.2 (atualizada pós-Cap 03)"
```

---

### 4. Metadados do Capítulo (`capitulos/capitulo_NN/_metadados_capitulo.json`)

```json
{
  "capitulo": 4,
  "titulo": "A Prova",
  "cenas": [
    {"numero": 1, "titulo": "Chegada", "pov": "Protagonista", "status": "CONCLUIDO", "palavras": 2300},
    {"numero": 2, "titulo": "O Enigma", "pov": "Protagonista", "status": "ESCREVENDO", "palavras": 0},
    {"numero": 3, "titulo": "Revelação", "pov": "Antagonista", "status": "PENDENTE", "palavras": 0},
    {"numero": 4, "titulo": "Decisão", "pov": "Protagonista", "status": "PENDENTE", "palavras": 0}
  ],
  "status_geral": "ESCREVENDO",
  "validacao_march": "PENDENTE",
  "validacao_continuidade": "PENDENTE",
  "bible_checksum": "a1b2c3d4",
  "estado_checksum": "e5f6g7h8",
  "ultima_atualizacao": "2026-07-27T14:30:00Z"
}
```

---

## Convenções de Nomenclatura

| Item | Padrao | Exemplo |
|------|--------|---------|
| Pasta capítulo | `capitulo_{NN:02d}` | `capitulo_01`, `capitulo_12` |
| Cena dentro do capítulo | `cena_{NN:02d}` (se granular) | `cena_01`, `cena_03` |
| Bible version | `v{major}.{minor}` | `v1.0`, `v3.2` |
| Checksums | SHA256 truncado 8 chars | `a1b2c3d4` |
| Timestamps | ISO 8601 UTC | `2026-07-27T14:30:00Z` |

---

## Princípios de Isolamento (Worktree Style)

1. **Cada capítulo = pasta isolada** — Nada vaza entre capítulos
2. **Arquivos de validação ficam DENTRO da pasta do capítulo** — `_resultado_march.json`, `_resultado_continuidade.json`
3. **Bible e Estado são GLOBAIS** — Ficam em `/bible/` e `/estado/`, atualizados atomicamente
4. **Rascunhos são descartáveis** — Pasta `rascunhos/` pode ser apagada a qualquer momento
5. **Consolidador lê apenas `_saida_escritor.md` (ou `_saida_editor.md` se houver) + `_metadados_capitulo.json`**

---

## Fluxo de Arquivos por Capítulo

```
ORQUESTRADOR cria pasta: capitulos/capitulo_04/
        |
        v
ESCRITOR escreve: _saida_escritor.md + _metadados_capitulo.json
        |
        v
ATOMIZADOR le _saida_escritor.md -> cria _afirmacoes_para_validar.json
        |
        v
VALIDADOR_MARCH le _afirmacoes_para_validar.json + corpus -> cria _resultado_march.json
        |
        +-- SE REPROVADO: volta para ESCRITOR (reescrita cirúrgica)
        |
        v
VALIDADOR_CONTINUIDADE le _saida_escritor.md + bible + estado_anterior -> _resultado_continuidade.json
        |
        +-- SE REPROVADO: volta para ESCRITOR (reescrita cirúrgica)
        |
        v
EDITOR (se genero.exige_editor) le _saida_escritor.md + genero + bible -> _saida_editor.md
        |
        v
ORQUESTRADOR atualiza Bible + Estado (atomicamente) -> marca capitulo CONCLUIDO
        |
        v
PROXIMO CAPITULO
```

---

## Validações Obrigatórias por Capítulo

| Validação | Obrigatória? | Quem Executa | Input | Output |
|-----------|--------------|--------------|-------|--------|
| MARCH (Fact-check) | **SIM** | Validador MARCH | `_afirmacoes_para_validar.json` + corpus | `_resultado_march.json` |
| Continuidade | **SIM** | Validador Continuidade | `_saida_escritor.md` + bible + estado_anterior | `_resultado_continuidade.json` |
| Voice Consistency | Se genero.exige_editor | Editor | `_saida_escritor.md` + genero + bible | `_saida_editor.md` |
| Pacing/Structure | Se genero.exige_editor | Editor | `_saida_escritor.md` + genero | `_saida_editor.md` |
| Show Don't Tell | Se genero.exige_editor | Editor | `_saida_escritor.md` + genero | `_saida_editor.md` |

**REGRA:** Capítulo só vira `CONCLUIDO` se **MARCH = APROVADO** E **Continuidade = APROVADO**.