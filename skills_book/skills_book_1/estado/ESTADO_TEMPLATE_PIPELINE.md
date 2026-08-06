# TEMPLATE DO ESTADO DA OBRA (PIPELINE GENÉRICO)

**Versão:** 3.0
**Aplicação:** copie para `execucao/estado/estado_da_obra.md` e preencha. O Orquestrador atualiza após cada cena.

---

# Estado da Obra: [TÍTULO DO LIVRO]

## Metadados
- **Ultima_atualizacao:** [ISO 8601]
- **Status_geral:** EM_ANDAMENTO | CONCLUIDO | INTERROMPIDO
- **Genero:** [do GENERO.md]
- **Subgenero:** [se aplicável]
- **Foco_usuario:** "[do CONFIG.md]"
- **Capitulos_planejados:** [N]
- **Capitulos_concluidos:** [M]
- **Cena_atual:** {capitulo: X, cena: Y}
- **Chamadas_gastas:** [N]
- **Limite_chamadas:** [N]
- **Bible_versao:** v[major].[minor]
- **Bible_checksum:** [8 chars]

---

## Arquétipo e Voz (Travadas — não mudam sem aprovação)
- **Voz:** [do GENERO.md seção 1]
- **Tempo verbal:** [do GENERO.md]
- **Distância:** [do GENERO.md]
- **Tom:** [do GENERO.md]
- **Ritmo por cena:** [do GENERO.md]
- **Extensão por cena:** [do GENERO.md]
- **Show mínimo:** [do GENERO.md]
- **Formato do fim de cena:** [do GENERO.md seção 4]

---

## Plano de Capítulos e Cenas (Granular)

**Legenda:**
- **Status:** PENDENTE | ESCREVENDO | REVISAO_MARCH | REVISAO_CONT | CONCLUIDO | REPROVADO
- **MARCH/Cont:** APROVADO | REPROVADO | PENDENTE | -

| ID | Cap | Cena | Título | POV | Palavras Est | Status | MARCH | Cont | Retries | Objetivo da Cena |
|----|-----|------|--------|-----|--------------|--------|-------|------|---------|------------------|
| 1.1 | 1 | 1 | [Título] | [POV] | [N] | PENDENTE | - | - | 0 | [Objetivo] |
| 1.2 | 1 | 2 | [Título] | [POV] | [N] | PENDENTE | - | - | 0 | [Objetivo] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

---

## Detalhamento do Capítulo Atual (Cap X)

| Cena | Título | POV | Status | MARCH | Cont | Palavras | Última Ação |
|------|--------|-----|--------|-------|------|----------|-------------|
| 1 | [Título] | [POV] | CONCLUIDO | APROVADO | APROVADO | 2.347 | Validado 2026-07-27 10:15 |
| 2 | [Título] | [POV] | ESCREVENDO | PENDENTE | PENDENTE | - | Escritor: parágrafo 5 |
| 3 | [Título] | [POV] | PENDENTE | - | - | - | Aguardando Cena 2 |

---

## Pendências e Bloqueios
- Cap X, Cena Y: aguardando próxima ação do AUTOPILOT
- Caps. X+1 a Z: bloqueados até a cena atual ser CONCLUÍDA
- Próximas ações: Escritor → Atomizador → Validador MARCH → Validador Continuidade → Editor → Bible/Estado update

---

## Histórico de Retries (por Cena)

| Cena | Tentativa | Validador | Motivo_Falha | Acao_Corretiva |
|------|-----------|-----------|--------------|----------------|
| 1.3 | 1 | MARCH | 2 afirmações contraditas (dados estudo) | Reescrita cirúrgica parágrafo 7 |
| 1.3 | 2 | CONT | Personagem em local errado (timeline) | Reescrita cirúrgica abertura |
| 2.1 | 1 | CONT | Voz narrativa diferente do GENERO.md | Reescrita completa cena |

---

## Foco do Usuário (NotebookLM-style)
> "[Texto exato do CONFIG.md]"

---

## Checkpoint de Retomada
**Se o processo parar AGORA, na próxima execução começar EXATAMENTE aqui:**
- **Capítulo:** [X]
- **Cena:** [Y]
- **Status da cena:** [PENDENTE | ESCREVENDO | REVISAO_MARCH | REVISAO_CONT]
- **Próxima acao:** [INVOCAR_ESCRITOR | INVOCAR_ATOMIZADOR | INVOCAR_MARCH | INVOCAR_CONT | INVOCAR_EDITOR]
- **Bible versao no checkpoint:** v[major].[minor]
- **Estado checksum no checkpoint:** [8 chars]

---

## Checksums de Cenas (Rastreabilidade)

| Cena | Checksum (8 chars) | Bytes |
|------|---------------------|-------|
| 1.1 | a1b2c3d4 | 8948 |
| 1.2 | e5f6g7h8 | 7573 |
| ... | ... | ... |

---

## Notas de Operação para o AUTOPILOT

1. A cada cena CONCLUÍDA, recalcular checksum e atualizar Bible/Estado atomicamente.
2. Manter isolamento: cada cena em `execucao/capitulos/capitulo_NN/cena_MM/`.
3. Respeitar 1.000–4.000 palavras por cena (ou range definido em GENERO.md).
4. Show mínimo conforme GENERO.md: priorizar cases reais e exemplos concretos.
5. Validação MARCH cruzada contra o corpus.
6. Validação de Continuidade contra esta Bible e o Estado.
7. Se a cena reprovar 3x, marcar REPROVADO e seguir.
8. Lei 6: zero material de marketing no livro.
