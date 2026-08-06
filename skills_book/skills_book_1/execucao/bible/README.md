# bible/ — Fonte da Verdade da Obra

**Versão:** 3.0
**Aplicação:** aqui fica a Bible do livro sendo produzido. É o documento canônico que define personagens, arcos, conceitos, timeline, e tudo que precisa ser consistente entre cenas.

---

## O que é a Bible

A Bible é a **fonte da verdade** do livro. Ela contém:

- Premissa central
- Estrutura global (capítulos e cenas planejadas)
- Personagens ou conceitos-chave (com definições, não arcos)
- Threads narrativos abertos e fechados
- Decisões de tom, voz, escopo

A Bible é referenciada pelo Validador de Continuidade em cada cena. Por isso, tudo que aparece na prosa tem que estar (ou ser adicionável) na Bible.

## Quem cria e atualiza

- **Quem cria:** o Orquestrador, no início da execução, usando `bible/BIBLE_TEMPLATE_PIPELINE.md` como base.
- **Quem atualiza:** o Orquestrador, atomicamente, após cada cena CONCLUÍDA.

A Bible é um arquivo vivo. Cada cena que introduz conceito novo, personagem novo, ou thread novo, gera uma atualização atômica da Bible.

## Procedimento de atualização atômica

A Bible é atualizada com `os.replace` (rename atômico) — nunca `write` direto. Procedimento completo em `REGRAS_GREENFORGE_PIPELINE.md`, Lei 3.

## Validação contra a Bible

A cada cena, o Validador de Continuidade checa se a cena é consistente com a Bible (personagens consistentes, sem contradição com eventos anteriores, etc.). Se a cena introduzir algo novo que ainda não está na Bible, o Orquestrador adiciona à Bible após a cena ser aprovada.

## Arquivo final

Quando a execução termina, `execucao/bible/BIBLE_DA_OBRA.md` contém a fonte da verdade completa do livro. É o documento que você lê se quiser entender a estrutura lógica do que foi escrito.
