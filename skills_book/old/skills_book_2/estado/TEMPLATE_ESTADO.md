# TEMPLATE DO ESTADO DA OBRA

**Versao:** 1.0
**Uso:** Copie para `estado/estado_da_obra.md` e preencha. O Orquestrador atualiza a cada cena.

---

# Estado da Obra: [TITULO DO LIVRO]

## Metadados
- **Ultima_atualizacao:** [ISO8601]
- **Status_geral:** EM_ANDAMENTO | CONCLUIDO | INTERROMPIDO
- **Genero:** [ROMANCE | NAO_FICCAO | MEMOIR | TECNICO | PERSONALIZADO]
- **Subgenero:** 
- **Foco_usuario:** "[Instrucao livre do usuario, ex: 'Foque na tensao psicologica...']"
- **Capitulos_planejados:** [N]
- **Capitulos_concluidos:** [M]
- **Cena_atual:** {capitulo: X, cena: Y}
- **Chamadas_gastas:** [numero]
- **Limite_chamadas:** [numero]
- **Bible_versao:** v[major].[minor]
- **Bible_checksum:** [8 chars]

---

## Plano de Cenas (Granularidade por Cena)

| ID | Cap | Cena | Titulo | POV | Palavras_Est | Status | MARCH | Cont | Retries | Objetivo_Cena |
|----|-----|------|--------|-----|--------------|--------|-------|------|---------|---------------|
| 1.1 | 1 | 1 | [Titulo] | [POV] | [N] | CONCLUIDO | APROVADO | APROVADO | 0 | [Objetivo] |
| 1.2 | 1 | 2 | [Titulo] | [POV] | [N] | CONCLUIDO | APROVADO | APROVADO | 0 | [Objetivo] |
| 1.3 | 1 | 3 | [Titulo] | [POV] | [N] | CONCLUIDO | APROVADO | APROVADO | 1 | [Objetivo] |
| 2.1 | 2 | 1 | [Titulo] | [POV] | [N] | ESCREVENDO | PENDENTE | PENDENTE | 0 | [Objetivo] |
| 2.2 | 2 | 2 | [Titulo] | [POV] | [N] | PENDENTE | - | - | 0 | [Objetivo] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Legenda Status:** PENDENTE | ESCREVENDO | REVISAO_MARCH | REVISAO_CONT | CONCLUIDO | REPROVADO
**Legenda MARCH/Cont:** APROVADO | REPROVADO | PENDENTE | -

---

## Detalhamento do Capítulo Atual (Cap X)

| Cena | Titulo | POV | Status | MARCH | Cont | Palavras | Ultima_Acao |
|------|--------|-----|--------|-------|------|----------|-------------|
| 1 | [Titulo] | [POV] | CONCLUIDO | APROVADO | APROVADO | 2347 | Validado 2026-07-27 10:15 |
| 2 | [Titulo] | [POV] | ESCREVENDO | PENDENTE | PENDENTE | - | Escritor: paragrafo 5 |
| 3 | [Titulo] | [POV] | PENDENTE | - | - | - | Aguardando Cena 2 |
| 4 | [Titulo] | [POV] | PENDENTE | - | - | - | Aguardando Cena 3 |

---

## Pendências e Bloqueios
- Cap X, Cena Y: aguardando conclusao do Escritor
- Cap X+1: bloqueado ate Cap X CONCLUIDO (precisa contexto anterior)
- [Outras pendencias...]

---

## Historico de Retries (por Cena)

| Cena | Tentativa | Validador | Motivo_Falha | Acao_Corretiva |
|------|-----------|-----------|--------------|----------------|
| 1.3 | 1 | MARCH | 2 afirmacoes contraditas (dados estudo) | Reescrita cirurgica paragrafo 7 |
| 1.3 | 2 | CONT | Personagem em local errado (timeline) | Reescrita cirurgica abertura |
| 2.1 | 1 | CONT | Voz narrativa diferente (1a vs 3a) | Reescrita completa cena |

---

## Foco do Usuario (NotebookLM-style)
> "[Texto exato do usuario]"

---

## Checkpoint de Retomada (Para o Orquestrador)
**Se o processo parar AGORA, na proxima execucao comecar EXATAMENTE aqui:**
- Capitulo: [X]
- Cena: [Y]
- Status da cena: [ESCREVENDO | REVISAO_MARCH | REVISAO_CONT | PENDENTE]
- Proxima acao: [INVOCAR_ESCRITOR | INVOCAR_ATOMIZADOR | INVOCAR_MARCH | INVOCAR_CONT | INVOCAR_EDITOR]
- Bible versao no checkpoint: v[major].[minor]
- Estado checksum no checkpoint: [8 chars]