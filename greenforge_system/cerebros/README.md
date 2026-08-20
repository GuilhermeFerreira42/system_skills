# Cérebros — Greenforge System

Cada arquivo aqui é a **fonte única de verdade** de um papel. Os adaptadores em `_claude_code/` e `_openclaude/` apenas apontam para eles.

| Agente | Papel original | Cérebro |
|---|---|---|
| `gf-orquestrador-mestre` | Orquestrador Mestre | `cerebros/orquestrador-mestre.md` |
| `gf-decompositor` | Decompositor | `cerebros/decompositor.md` |
| `gf-solver` | Solver | `cerebros/solver.md` |
| `gf-proposer` | Proposer | `cerebros/proposer.md` |
| `gf-checker-cego` | Checker Cego (MARCH) | `cerebros/checker-cego.md` |
| `gf-consolidador` | Consolidador | `cerebros/consolidador.md` |


> Estes cérebros são **concatenação verbatim** dos arquivos originais de skill, com um cabeçalho de proveniência. Nenhuma regra, pseudocódigo ou critério de aprovação foi alterado. Os originais seguem intactos nos seus caminhos.
> Para regenerar: `python3 gerar_subagentes.py`.
