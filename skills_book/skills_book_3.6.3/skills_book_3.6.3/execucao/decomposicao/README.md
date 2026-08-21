# execucao/decomposicao/

Artefatos da **Fase 0 — Decomposição e Validação** (v3.6.3). A pasta nasce vazia:
os dois arquivos abaixo são criados durante a execução, antes de qualquer cena.

| Arquivo | Quem escreve | O que contém |
|---|---|---|
| `_decomposicao_ufi.json` | `book-analista-de-decomposicao` | listas de UFIs por classe, agrupamento em cenas, número proposto e justificativa densitométrica |
| `_resultado_verificacao_decomposicao.json` | `book-verificador-de-decomposicao` | análise independente (por extenso), checklist, decisão e omissões |

**Trava dura:** nenhuma cena pode ser iniciada sem `_resultado_verificacao_decomposicao.json` com `decisao = "APROVADO"`. O `book-auditor-de-pipeline` verifica isso no Bloco A0 e bloqueia a obra inteira caso falhe.

Ver a seção *"CÁLCULO DO NÚMERO DE CENAS — MÉTODO UNIVERSAL DE DECOMPOSIÇÃO (v3.6.3)"* em `COMANDO_PADRAO_INICIALIZACAO.md`.
