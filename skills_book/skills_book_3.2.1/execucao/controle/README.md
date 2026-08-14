# Controle físico da execução

O Orquestrador pode criar:

```text
controle_da_obra.json
controle_da_obra.md
reconciliacao_ultima.json
```

O índice registra os artefatos físicos e seus checksums. Use `python3 utils/reconciliar_controle.py <raiz-do-projeto>` para comparar o registro com o disco.