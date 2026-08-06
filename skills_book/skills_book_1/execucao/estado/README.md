# estado/ — Checkpoint Operacional

**Versão:** 3.0
**Aplicação:** aqui fica o Estado da obra — o documento operacional que rastreia o progresso cena por cena, validações, checksums, e histórico de retries.

---

## O que é o Estado

O Estado é o **checkpoint operacional** da execução. Ele contém:

- Status de cada cena (PENDENTE, EM_ANDAMENTO, CONCLUÍDA, REPROVADO, PÓS-CIRÚRGICA)
- Validações (MARCH e Continuidade) com seus resultados
- Checksums SHA256 (8 primeiros caracteres) de cada cena CONCLUÍDA
- Tamanho em bytes de cada cena CONCLUÍDA
- Histórico de retries (quantas vezes cada cena foi refeita, por quê)
- Próxima cena a ser produzida

O Estado é atualizado **atomicamente** após cada cena aprovada. Se a execução cair no meio, o Estado permite retomar do ponto exato.

## Quem cria e atualiza

- **Quem cria:** o Orquestrador, no início da execução, usando `estado/ESTADO_TEMPLATE_PIPELINE.md` como base.
- **Quem atualiza:** o Orquestrador, atomicamente, após cada cena CONCLUÍDA ou REPROVADA.

## Round-trip check

Após anotar o checksum de uma cena, o Orquestrador **reabre o arquivo do disco** e recalcula o checksum. Se for diferente do valor registrado, a cena é marcada como INCONSISTENTE e o sistema para. Procedimento completo em `REGRAS_GREENFORGE_PIPELINE.md`, Lei 4.

## Arquivo final

Quando a execução termina, `execucao/estado/ESTADO_DA_OBRA.md` contém o histórico completo da produção: cada cena, cada validação, cada retry. É o documento que você lê para auditar a produção.
