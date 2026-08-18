# CHANGELOG v3.5 FINAL — Ciclo de Calibração Autônoma contra o Padrão Ouro

**Data:** 16/08/2026
**Base:** `skill_zerada_v3.4.0`
**Padrão Ouro usado como referência:** `otimo_livro_final.md`
**Obra de calibração produzida:** `O Aquário Invisível` (3 capítulos, 9 cenas, 7.162 palavras)
**Obra reprovada que motivou o ciclo:** `livro_final.md` (saída do pipeline v3.4, 6 cenas)

---

## Por que houve um ciclo v3.5

A v3.4 produziu seis cenas com status `APROVADO` no Revisor Cego, `APROVADO` na
Continuidade e `APROVADO_COM_RESSALVAS` no MARCH — e mesmo assim entregou um
livro que perde para o Padrão Ouro em **cinco dos seis vetores de maestria**.

O diagnóstico não é de regra faltando. Quase todas as regras violadas **já
estavam escritas** no `GENERO.md` v1.0 e no DNA v3.2. O que faltava eram três
coisas:

1. **Pisos mensuráveis** onde havia só princípio qualitativo (o Escritor
   cumpria a regra "na intenção" e ninguém conseguia provar o contrário);
2. **Uma saída legítima para alegações delicadas** — sem ela, o Escritor tinha
   um incentivo estrutural para hedgear, e hedgeou seis vezes em seis cenas;
3. **Uma avaliação de OBRA**, e não só de cena — seis cenas aprovadas uma a uma
   somaram um livro sem imagem-mãe, sem personagem e sem fechamento elétrico.

---

## Mudanças por arquivo

### `generos_completos/nao_ficcao_pratica/GENERO.md` → **v2.0**

| § | Mudança | Falha da v3.4 que a originou |
|---|---|---|
| 1 | **Piso de storytelling heroico:** ≥1 cientista nomeado por cena, com 2 de 3 âncoras (data, lugar, obstáculo) | 6 cenas, 0 cientistas nomeados — com Carrel, Batmanghelidj, Agre, Brownstein, Coandă e Jhon disponíveis no corpus |
| 1 | **Piso de notação:** ≥1 mecanismo por capítulo em notação explícita; números na precisão do corpus | 0 ocorrências de LaTeX; 66%/26%/8% viraram "não existe percentual universal" |
| 1 | **Cadência da metáfora-mestra:** instalação (cena 1) → eco por capítulo → retomada explícita no fim; proibida imagem estrutural concorrente | 3 imagens diferentes em 3 cenas, nenhuma retomada |
| 4 | **Regra posicional esclarecida:** ação mensurável só na última cena **da obra**; fim de capítulo usa cristalização | toda cena fechava com tarefa |
| 4 | **Léxico de dever de casa bloqueado** (`registre`, `anote`, `monitore`, janelas > 24h) + **teste dos 30 segundos** | fechamento final era um diário de 7 dias |
| 4 | **Critério de sucesso não pode ser terceirizado** ("procure orientação" não é critério) | fechamento delegava a verificação a terceiros |
| **12** | **Nova seção — Regra da Atribuição Narrativa:** atribuir / reduzir / aparato, e a proibição de converter ressalva em advérbio de dúvida | as 6 ressalvas do MARCH foram todas "resolvidas" dentro da prosa |

### `escritor/DNA_REVELACAO_RESPEITOSA.md` → **v3.3**

- **§10 — Léxico de Perda de Convicção:** sete famílias de construção proibidas
  no corpo da obra (fonte visível, disclaimer, hedge empilhado, ressalva
  pré-evidência, número desidratado, ação burocrática, metáfora descartável),
  com a instrução expressa de usá-las **como auditoria depois da escrita**,
  nunca como checklist durante — para não recriar a sobrecodificação que a
  v3.2 corretamente eliminou.
- **§11 — Convicção Sem Falsificação:** tabela de conversão que demonstra o
  princípio central do ciclo — *quanto mais específica a atribuição, mais forte
  soa a frase e mais honesta ela é ao mesmo tempo*. Convicção e rigor deixam de
  ser um trade-off e passam a ser o mesmo movimento.

### `revisor_cego_editorial/RUBRICA_QUALITATIVA_V3.md` → **v3.3**

- **§6 — Matriz dos 6 Vetores de Ouro:** avaliação obrigatória **de obra**,
  nota 0–10 por vetor com evidência textual citada.
- **§6.1 — Hard gates:** qualquer vetor < 8 reprova; média < 9,0 reprova;
  **vetor 5 (Convicção Ativa) é eliminatório na primeira ocorrência** do léxico
  do DNA §10.
- **§6.2/6.3 —** formato JSON do parecer de obra + auditoria literal obrigatória
  (a única etapa do pipeline onde a contagem substitui o julgamento, porque foi
  aqui que o julgamento sozinho falhou).

### `validador_march/SKILL_VALIDADOR_MARCH_PIPELINE.md`

- **Adendo v3.5:** toda ressalva sai do validador com um **destino obrigatório**
  (`ATRIBUIR` | `REDUZIR` | `APARATO`). Ressalva sem destino passa a ser erro
  do validador, não do Escritor.

### `validador_continuidade/SKILL_VALIDADOR_CONTINUIDADE_PIPELINE.md`

- **Adendo v3.5:** checagem de cadência da metáfora-mestra em 4 pontos, com
  reprovação tipada `METAFORA_DESCARTAVEL`.

### `bible/BIBLE_TEMPLATE_PIPELINE.md`

- Novo bloco obrigatório **Registro da Metáfora-Mestra** (imagem, domínio,
  pergunta de diagnóstico, cena de instalação, cenas de eco, cena de retomada,
  extensões permitidas, imagens concorrentes proibidas).

### `templates_bible_worktree/_aparato_de_fontes.template.md` *(novo)*

- Template do **Aparato de Fontes**, publicado depois do corpo da obra. É a peça
  que torna a convicção total do texto sustentável: o livro não hedgeia porque
  o aparato existe.

### `utils/lint_conviccao.py` *(novo)*

- Auditor executável dos 6 vetores + das 7 famílias de léxico proibido.
  `python3 utils/lint_conviccao.py <obra.md>` devolve nota por vetor, média,
  ocorrências literais com linha, e código de saída 1 em caso de reprovação.

---

## Regressões que este ciclo deliberadamente NÃO cometeu

- **Não aumentou a sobrecodificação criativa.** Todos os novos pisos são
  verificáveis por busca ou contagem **depois** da cena pronta. A ordem de
  escrita continua sendo a da v3.4: internalizar a voz, escrever de uma vez,
  auditar depois.
- **Não transformou "sem disclaimer" em "sem verdade".** A saída não foi
  afrouxar o MARCH: foi criar dois canais (atribuição narrativa e aparato) que
  entregam **mais** informação epistêmica ao leitor do que o hedge entregava,
  com força narrativa em vez de medo.
- **Não obrigou os 5 instrumentos da §3 em toda cena.** A função dramática
  continua escolhendo os instrumentos; só os pisos de obra (personagem, notação,
  metáfora, fechamento) viraram obrigatórios.

---

# CHANGELOG v3.5.1 — Manutenção: Fingerprint de Estilo (2026-08-17)

## Motivação

O ciclo v3.5 provou que o Padrão Ouro funciona como régua — mas a régua é um
arquivo único, preso ao tema da água. Para calibrar uma IA de escrita **sem**
depender do arquivo ouro, foi destilada a obra calibrada (`LIVRO_FINAL.md`,
*O Aquário Interno*, 10/10 nos 6 vetores) em métricas operacionais: o
fingerprint positivo.

## Mudanças

- **`escritor/FINGERPRINT_ESTILO_v1.md`** *(novo)* — régua positiva de
  calibração: métricas quantificadas (voz, ritmo de frase, interpelação,
  densidade de notação, personagem por cena, cadência da metáfora-mãe,
  estrutura de cena, listas), regras qualitativas, trechos-modelo da obra
  calibrada e limites explícitos da régua.

## O que NÃO mudou

- **Nenhuma regra dos três normativos foi alterada.** O fingerprint é
  **aditivo**: o lint continua sendo o verificador negativo (rejeição); o
  fingerprint passa a ser o calibrador positivo (geração). Um sem o outro
  é incompleto.
- A ordem de escrita continua a mesma: internalizar a voz, escrever de uma
  vez, auditar depois — a régua mede o que já foi escrito, nunca dirige o
  que está sendo escrito.


---

# CHANGELOG v3.5.2 — Refatoracao para Arquitetura Hibrida (Lint + Ressonancia) (2026-08-17)

## Decisao

Substituir a abordagem de **metricas quantitativas** (Fingerprint de Estilo, Piso de Densidade numerico) por uma arquitetura **hibrida** de dois estagios:

1. **Lint de Conviccao (mantido):** rede de seguranca deterministica contra prosa defensiva (7 familias do DNA §10).
2. **Validador de Ressonancia (novo):** avaliacao semantica dos **5 Movimentos Retoricos** (PASS/FAIL), substituindo a Matriz dos 6 Vetores.

## Mudancas por arquivo

### Criado
- `revisor_cego_editorial/RUBRICA_QUALITATIVA_V3.md` — Secao 6 substituida pelo **Validador de Ressonancia**: 5 movimentos, PASS/FAIL sem nota parcial, regras por tipo de cena.

### Modificado
- `bible/BIBLE_TEMPLATE_PIPELINE.md` — Adicionadas duas secoes: **Arquitetura Retorica** (os 5 movimentos) e **Assinatura Estilistica** (qualitativa, sem metricas).
- `escritor/SKILL_ESCRITOR_PIPELINE.md` — Piso de densidade (tabela numerica) substituido por **Criterio de Completude** (3 perguntas qualitativas).
- `editor/SKILL_EDITOR_PIPELINE.md` — Adicionado **Principio Cardinal do Editor v4.0**: preservar rugosidade intencional.
- `orquestrador/SKILL_ORQUESTRADOR_PIPELINE.md` — Checkpoint de densidade substituido pelo **fluxo Lint → Ressonancia**.
- `CONFIG.md` e `execucao/CONFIG.md` — Piso de densidade substituido por Criterio de Completude qualitativo.

### Deprecado
- `escritor/FINGERPRINT_ESTILO_v1.md` → renomeado para `FINGERPRINT_ESTILO_DEPRECATED_v1.md`. O fingerprint numerico (medias de frase, contagem de pronomes) nao captura alma; seu papel e assumido pela **Assinatura Estilistica** qualitativa na Bible.

### Mantido (nao modificado)
- `utils/lint_conviccao.py` — Mantido integralmente como rede de seguranca deterministica. Roda antes do Validador de Ressonancia.
- `DNA_REVELACAO_RESPEITOSA.md` — Inalterado (o DNA ja contem os principios que o lint verifica).
- `GENERO.md` v2.0 — Inalterado (a arquitetura dos 5 movimentos complementa, nao substitui, as regras de genero).

## Notas
- Nenhuma regra existente foi removida ou enfraquecida. O lint continua verificando as 7 familias do DNA §10.
- O fingerprint numerico foi deprecado, nao deletado — permanece no repositorio como registro historico.
- A ordem de escrita continua a mesma (instinto → lint → validador). O lint e a rede de seguranca; o validador e o juiz de arquitetura.
