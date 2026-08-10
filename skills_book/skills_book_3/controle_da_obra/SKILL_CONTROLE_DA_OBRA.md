# Skill do Controle da Obra

## Estados físicos

- `AUSENTE`: worktree ou artefato esperado não existe.
- `EM_PRODUCAO`: cena ainda está sendo produzida.
- `PACOTE_ABERTO`: existem artefatos, mas a linhagem não fechou.
- `CONCLUIDO`: final, manifestos e validadores apontam para a mesma versão.
- `MODIFICADO_MANUALMENTE`: checksum atual difere do registrado fora de uma transição conhecida.
- `REVALIDACAO_NECESSARIA`: artefatos derivados estão obsoletos.
- `BLOQUEADA_REVISAO_HUMANA`: teto de retries alcançado.

## Reconciliação

Para cada cena:

1. leia o registro esperado;
2. confira existência dos arquivos;
3. recalcule hashes no disco;
4. compare com o manifesto e com o Estado;
5. registre diferenças sem corrigi-las;
6. invalide apenas o que depende da versão alterada;
7. entregue ao Orquestrador uma ação explícita.

## Regra de não-loop

Uma divergência de bytes não é uma falha literária. Ela não convoca o Escritor sozinha. Primeiro preserve o arquivo, registre a origem da mudança e solicite revalidação.
