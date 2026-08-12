# Controle da Obra

O Controle da Obra é o espelho operacional do filesystem. Ele registra o que existe fisicamente e compara com o Estado lógico.

Ele não substitui:

- a Bible como fonte semântica;
- o Estado como checkpoint de intenção;
- o usuário como autoridade para editar o texto.

Arquivos de projeto:

```text
execucao/controle/
├── controle_da_obra.json       # índice de máquina
├── controle_da_obra.md         # visão humana
└── reconciliacao_ultima.json   # último relatório, quando houver
```

Uma divergência não é corrigida pelo Controle. Ela vira `MODIFICADO_MANUALMENTE`, `DRIFT_DE_CHECKPOINT` ou `REVALIDACAO_NECESSARIA`.

