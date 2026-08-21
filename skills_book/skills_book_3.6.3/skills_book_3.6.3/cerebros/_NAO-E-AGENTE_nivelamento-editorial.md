# NÃO É UM AGENTE — Nivelamento Editorial

O **Nivelamento Editorial** aparece no `skills_book_v3.6_FINAL/nivelamento_editorial/`
ao lado dos papéis, mas ele **não foi convertido em subagente**, por decisão explícita.

## Por quê

Nivelamento Editorial é **configuração e estado**, não um papel de agente:

- É um **questionário humano único**, respondido pelo usuário no início da obra
  (`PERGUNTAS_NIVELAMENTO.md`), com apoio do `GUIA_CALIBRACAO_EMPATIA.md`.
- O resultado dele **alimenta a Bible da Obra** — e é a Bible que os agentes leem.
- Ele não tem turno no loop, não recebe invocação do Orquestrador, não produz artefato
  intermediário por cena e não tem critério de aprovação a executar.

Transformá-lo em subagente criaria um agente que roda uma vez, faz perguntas ao humano e
nunca mais é chamado — ou seja, um formulário fantasiado de agente, com a desvantagem de
sugerir que ele participa do pipeline.

## Onde ele vive na conversão

Nada mudou:

| Artefato | Papel |
|---|---|
| `nivelamento_editorial/PERGUNTAS_NIVELAMENTO.md` | questionário respondido pelo humano |
| `nivelamento_editorial/GUIA_CALIBRACAO_EMPATIA.md` | guia de apoio à calibração |
| `bible/BIBLE_TEMPLATE_PIPELINE.md` → `execucao/bible/bible_da_obra.md` | **onde o resultado é gravado** |

Os agentes convertidos — em especial `book-escritor`, `book-editor` e
`book-revisor-cego-editorial` — leem o **resultado** do nivelamento pela Bible, exatamente
como já faziam. O contrato editorial que o nivelamento define continua sendo entregue ao
Escritor como "o trecho da Bible sobre metáfora central, voz e contrato editorial", que é
o que o Orquestrador passa ao agente fresco.

## Se você quiser automatizar o preenchimento

Isso seria uma **mudança de escopo**, não parte desta conversão. O caminho natural seria
um comando (slash command) que conduz o questionário e escreve na Bible — não um
subagente no pipeline. Fica registrado como possibilidade, não como pendência.
