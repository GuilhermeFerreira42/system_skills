# Cérebros — IdeaForge-2

Cada arquivo aqui é a **fonte única de verdade** de um papel. Os adaptadores em `_claude_code/` e `_openclaude/` apenas apontam para eles.

| Agente | Papel original | Cérebro |
|---|---|---|
| `if-lider-do-debate` | Líder do Debate (Orquestrador Adaptativo) | `cerebros/lider-do-debate.md` |
| `if-proponente` | Agente Proponente | `cerebros/proponente.md` |
| `if-critico` | Agente Crítico | `cerebros/critico.md` |
| `if-especialista` | Especialista sob Demanda | `cerebros/especialista-sob-demanda.md` |
| `if-sintetizador` | Agente Sintetizador | `cerebros/sintetizador.md` |


> Estes cérebros **não** são concatenação de markdown original: eles foram extraídos do código Python (`src/`, a árvore canônica — `idea-forge/src/` é legado v1 congelado). Cada arquivo lista, no topo, exatamente quais módulos foram lidos, e marca com **[era lógica de código]** todo trecho que não era prompt.
