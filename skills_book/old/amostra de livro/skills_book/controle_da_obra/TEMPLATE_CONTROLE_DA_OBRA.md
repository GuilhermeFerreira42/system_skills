# TEMPLATE DO CONTROLE DA OBRA

**Versao:** 1.0
**Uso:** Copie para `CONTROLE_DA_OBRA.md` na raiz do projeto de livro. O agente Controle da Obra reescreve este arquivo a cada atualizacao, usando este template como base.

---

# CONTROLE DA OBRA — Fonte de Verdade Unica

> Este arquivo eh a fonte de verdade para contagem de cenas e palavras.
> A fonte primaria eh o filesystem (pasta `capitulos/`). Este arquivo eh um espelho recalculado periodicamente pelo agente Controle da Obra.
> O `estado/estado_da_obra.md` e a `bible/bible_da_obra.md` ficam secundarios (contexto historico e narrativo).

---

## Ultima atualizacao

**Data:** [ISO8601, sera preenchido pelo agente]
**Metodo:** varredura automatica do diretorio `capitulos/`
**Checksum deste arquivo:** [8 chars, sera preenchido pelo agente]

---

## Cenas finalizadas em disco

> Cenas com `_saida_final.md` OU com `_saida_escritor.md` + ambos os arquivos de validacao (MARCH e Continuidade).

| Capitulo | Cenas finalizadas | Palavras |
|----------|-------------------|----------|
| Cap 1 — [Titulo] | N / N | NNNN |
| Cap 2 — [Titulo] | N / N | NNNN |
| **Subtotal** | **N / N** | **NNNN** |

---

## Cenas escritas, sem validacao completa

> Cenas com `_saida_escritor.md` mas sem os arquivos de validacao. Precisam passar pelo pipeline completo.

| Capitulo | Cenas | Palavras | Decisao |
|----------|-------|----------|---------|
| Cap X — [Titulo] | N | NNNN | Aguardando validacao |
| **Subtotal** | **N** | **NNNN** | — |

---

## Cenas ainda nao iniciadas

> Diretorio `cena_MM/` existe mas nao tem nenhum dos arquivos do pipeline.

| Capitulo | Cenas pendentes | Estimativa |
|----------|-----------------|------------|
| Cap X — [Titulo] | N | NNNN |
| **Subtotal** | **N** | **NNNN** | — |

---

## TOTAIS

| Item | Valor |
|------|-------|
| Total planejado de cenas | **N** |
| Cenas finalizadas | **N** |
| Cenas escritas sem validacao | **N** |
| Cenas nao iniciadas | **N** |
| **Progresso de cenas finalizadas** | **N / N = NN%** |
| **Palavras finalizadas** | **NNNN** |

---

## Regra de ouro

1. Toda vez que o assistente for dar um numero de progresso, vem deste arquivo.
2. Toda vez que uma cena for marcada como CONCLUIDA no `estado_da_obra.md`, o agente Controle da Obra atualiza este arquivo.
3. Se este arquivo e o `estado_da_obra.md` discordarem, **o filesystem vence**. Reconcilie rodando o agente no modo VALIDAR_CONTROLE.
4. Nao edite este arquivo manualmente sem rodar o agente depois. Ele sera sobrescrito na proxima varredura.

---

## Historico de atualizacoes

- **[DATA]** — Criacao do arquivo via template.
