# Estado da Obra: [Título]

## Metadados

- **ultima_atualizacao:** ISO-8601
- **status_geral:** EM_ANDAMENTO | CONCLUIDO | INTERROMPIDO
- **tipo_de_obra:** [tipo]
- **foco_usuario:** [texto]
- **perfil_editorial_fonte:** usuario | perfil_existente | padrao_confirmado
- **capitulos_planejados:** [quantidade ou descrição]
- **capitulos_concluidos:** 0
- **cena_atual:** [capítulo/cena]
- **bible_versao:** v1.0
- **bible_checksum:** v1.0:xxxxxxxx
- **controle_status:** EM_PRODUCAO

## Plano de cenas

| ID | Cap | Cena | Título | Objetivo | Status | Retries | MARCH | Continuidade | Revisor | Checksum |
|---|---:|---:|---|---|---|---:|---|---|---|---|
| cap_01_cena_01 | 1 | 1 | [título] | [objetivo] | PENDENTE | 0 | — | — | — | — |

## Status possíveis

`PENDENTE`, `ESCREVENDO`, `REVALIDACAO_NECESSARIA`, `REPROVADO_MARCH`, `REPROVADO_CONTINUIDADE`, `REPROVADO_REVISOR`, `REPROVADO_VIGIA`, `MODIFICADO_MANUALMENTE`, `BLOQUEADA_REVISAO_HUMANA`, `CONCLUIDO`, `INCONSISTENTE`.

## Histórico de retries

| Cena | Tentativa | Origem | Falha | Ação |
|---|---:|---|---|---|

## Checkpoint de retomada

- **Cena:**
- **Status:**
- **Próxima ação:**
- **Versão da Bible:**
- **Checksum do Estado:**

## Regras de retomada

O Estado não deve afirmar `CONCLUIDO` sem o manifesto e o relatório do Vigia correspondentes ao arquivo físico atual. Em caso de divergência, preserve o arquivo e marque revalidação.


==========================================
Conteúdo de bible_da_obra.md (caminho: skills_book_3/execucao/bible/bible_da_obra.md) [enc: utf-8]:

==========================================
Conteúdo de bible_da_obra.md (caminho: skills_book_3/execucao/bible/bible_da_obra.md) [enc: utf-8]: