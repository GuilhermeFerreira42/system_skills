# Skills Book — Sistema de Escrita de Livros (Greenforged Edition)

**Versao:** 1.0
**Data:** 2026-07-27
**Baseado em:** Skills Podcast 4.0.1 (Greenforged Edition) + Greenforge System

---

## Visao Geral

Sistema completo para produção de livros (ficcao, nao-ficcao, memorias, tecnico, personalizado) com:
- **Orquestracao Greenforge-style** (worktrees isolados, state tracking granular, checkpoint atomic)
- **Dual Validacao Cega Obrigatoria**: MARCH (fact-check vs corpus) + Continuidade (coerencia vs Bible+Estado)
- **Generos Carregados em Runtime** (usuario escolhe/cria genero na hora)
- **Bible Viva** (fonte da verdade atualizada a cada cena)
- **Output:** Markdown final + EPUB/PDF opcional

---

## Estrutura de Pastas

```
skills_book/
├── inicializador.txt                    # Este arquivo
├── orquestrador/                        # Coordenador mestre
│   ├── BOOT_ORQUESTRADOR_LIVRO.md
│   └── SKILL_ORQUESTRADOR_LIVRO.md
├── escritor/                            # Solver: escreve prosa por cena
│   ├── BOOT_ESCRITOR_LIVRO.md
│   └── SKILL_ESCRITOR_LIVRO.md
├── atomizador/                          # Proposer: extrai afirmacoes factuais
│   ├── BOOT_ATOMIZADOR_LIVRO.md
│   └── SKILL_ATOMIZADOR_LIVRO.md
├── validador_march/                     # Checker: fact-check cego vs corpus
│   ├── BOOT_VALIDADOR_MARCH_LIVRO.md
│   └── SKILL_VALIDADOR_MARCH_LIVRO.md
├── validador_continuidade/              # Checker: coerencia cega vs Bible+Estado (NOVO)
│   ├── BOOT_VALIDADOR_CONTINUIDADE_LIVRO.md
│   └── SKILL_VALIDADOR_CONTINUIDADE_LIVRO.md
├── editor/                              # Solver opcional: polimento (voz, pacing, show-dont-tell)
│   ├── BOOT_EDITOR_LIVRO.md
│   └── SKILL_EDITOR_LIVRO.md
├── consolidador/                        # Junta cenas -> livro_final.md
│   ├── BOOT_CONSOLIDADOR_LIVRO.md
│   └── SKILL_CONSOLIDADOR_LIVRO.md
├── generos/                             # Carregados em runtime pelo usuario
│   ├── GENERO_ROMANCE.md
│   ├── GENERO_NAO_FICCAO.md
│   ├── GENERO_MEMORIAS.md
│   ├── GENERO_TECNICO.md
│   └── GENERO_PERSONALIZADO.md          # Template para usuario criar o seu
├── bible/                               # Templates da Bible da Obra
│   ├── BIBLE_TEMPLATE.md
│   └── BIBLE_EXEMPLO.md
├── estado/                              # Template do Estado da Obra
│   └── TEMPLATE_ESTADO.md
├── esquema/                             # Documentacao estrutural
│   └── ESTRUTURA_PROJETO_LIVRO.md
└── exemplos/                            # Fluxo completo documentado
    └── FLUXO_COMPLETO_LIVRO.md
```

---

## Fluxo Principal (Pseudocodigo Resumido)

```
ORQUESTRADOR
  1. Carrega Genero (runtime) + Corpus + Foco Usuario
  2. Cria/Le Bible + Estado
  3. Gera Plano de Cenas (granular)
  4. PARA CADA CENA:
       A. ESCRITOR -> _saida_escritor.md
       B. ATOMIZADOR -> _afirmacoes_para_validar.json
       C. VALIDADOR_MARCH (cego) -> _resultado_march.json
          SE REPROVADO -> REESCRITA CIRURGICA (volta A) [max 3x]
       D. VALIDADOR_CONTINUIDADE (cego) -> _resultado_continuidade.json
          SE REPROVADO -> REESCRITA CIRURGICA (volta A) [max 3x]
       E. EDITOR (se genero.exige_editor) -> _saida_editor.md
       F. ATUALIZA BIBLE + ESTADO (atomico)
  5. CONSOLIDADOR -> livro_final.md (+ epub/pdf)
```

---

## Diferencas-Chave vs Podcast

| Podcast | Livro |
|---------|-------|
| 2 speakers, dialogo | Voz narrativa unica / multi-POV controlado |
| 6 segmentos fixos/ep | Cenas variaveis por genero (2-6 por capitulo) |
| MARCH only | **MARCH + CONTINUIDADE (dupla travas)** |
| Balanceamento speakers | POV, voz, timeline, worldbuilding, fios narrativos |
| Audio obrigatorio | Markdown final (EPUB/PDF opcional) |
| Episodios isolados | **Continuidade global obrigatoria** |
| Nao ha Bible | **Bible viva** (personagens, timeline, regras, fios) |

---

## Validacoes Obrigatorias (Travas Duras)

### MARCH (Fact-Check)
- 1 CONTRADITO = REPROVADO
- Taxa CONFIRMADO < 80% = REPROVADO
- NAO_ENCONTRADO > 30% = REPROVADO

### Continuidade (Coerencia Interna)
- 1 CONTRADITO = REPROVADO
- NAO_ENCONTRADO = ACEITAVEL (info nova legítima)
- Verifica: personagens, timeline, locais, conceitos, regras, voz, POV, fios narrativos

---

## Generos Suportados (Base)

1. **ROMANCE** — Ficcao literaria/comercial/genero (3 atos, beats emocionais, 2 POVs tipico)
2. **NAO_FICCAO** — Educativo, ciencia popular, business, biografia (problema->solucao, modular)
3. **MEMORIAS** — Autobiografia, memoir literario (dual temporalidade, verdade emocional, 80% show)
4. **TECNICO** — Manual, how-to, documentacao, cookbook (precisao, reproduzibilidade, escaneavel)
5. **PERSONALIZADO** — Usuario cria seu genero copiando template

---

## Como Usar

1. Usuario fornece: `corpus/`, `genero` (nome), `foco_usuario` (texto livre)
2. Orquestrador carrega `generos/GENERO_{genero}.md`
3. Sistema roda loop cena a cena com checkpoints
3. Output final: `livro_final.md` (validado MARCH + Continuidade em TODAS cenas)

---

## Arquivos de Estado (Checkpoints)

- `estado/estado_da_obra.md` — Progresso granular por cena, retries, foco, plano
- `bible/bible_da_obra.md` — Fonte da verdade viva (personagens, timeline, regras, fios)
- `capitulos/capitulo_NN/` — Worktree isolado por cena (arquivos de validacao dentro)

**Retomada exata:** Se cair no meio, proxima execucao comeca EXATAMENTE na cena/checkpoint parado.

---

## Regras de Ouro (Greenforge)

1. **Orquestrador NAO escreve, NAO valida. So COORDENA.**
2. **Cada agente recebe SO o insumo necessario. Nunca o projeto inteiro.**
3. **Validacao MARCH + Continuidade SAO OBRIGATORIAS. Sem elas, cena nao existe.**
4. **CEGUEIRA ABSOLUTA:** Validadores NAO veem prosa do escritor.
5. **MAX 3 RETRIES por cena. Depois: REPROVADO + segue (flag para humano).**
6. **CHECKSUM ROUND-TRIP:** Orquestrador relê arquivo do disco e confere checksum.
7. **SALVAMENTO ATOMICO:** .tmp -> rename. Crash no meio nao corrompe estado/bible.
8. **BIBLE + ESTADO = CHECKPOINTS UNICOS. Leia e escreva sempre.**