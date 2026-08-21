# `_auditoria/` — Fiscal do pipeline

Ferramenta de apoio ao subagente **`book-auditor-de-pipeline`**. Nada aqui altera a obra:
o único arquivo que este diretório escreve é o próprio relatório.

## Uso

```bash
# varredura completa (a obra inteira)
python3 _auditoria/auditar_pipeline.py .

# com a obra consolidada e os parâmetros da Bible
python3 _auditoria/auditar_pipeline.py . --livro LIVRO_FINAL.md --metafora "aquário"

# modo bloqueante: uma cena só, dentro do loop do Orquestrador
python3 _auditoria/auditar_pipeline.py . --cena execucao/capitulos/cap_01/cena_02
```

**Saída:** `_auditoria/relatorio_auditoria.md` e `relatorio_auditoria.json`.
**Exit code:** `0` conforme · `1` não conforme · `2` erro de uso.

Por padrão, as cenas em `capitulos_calibracao/` são **ignoradas** — são amostras de
referência que acompanham a skill, propositalmente incompletas. Use
`--incluir-calibracao` para auditá-las também.

## O que ele faz que os scripts existentes não fazem

**Princípio: não confiar na declaração — reexecutar e comparar.**

| Bloco | Cobertura |
|---|---|
| **A** | 7 artefatos exigidos pelo Vigia + 4 que ele não cobre; linhagem `input_checksum` × candidato; final byte a byte igual ao candidato; `status_fisico` do manifesto |
| **B** | reexecuta `lint_conviccao.py`, `vigia_integridade.py` e `reconciliar_controle.py`, e confronta com o que está registrado |
| **C** | os 7 testes de `regras_negocio/AUTO_AUDITORIA_PIPELINE.md` na obra consolidada |

### Duas lacunas reais que ele fecha

**1. O lint não deixa prova.** `lint_conviccao.py` só escreve em stdout. Se o Orquestrador
pular o Estágio 1, o pacote da cena fica **idêntico** ao de uma cena que passou pelo lint —
não há artefato faltando para denunciar. Por isso o fiscal **sempre reexecuta** o lint, e
recomenda (`B4`) que o Orquestrador passe a persistir a saída `--json` em
`_log_lint_conviccao.json`. Se esse log existir e divergir da reexecução, é bloqueio (`B5`):
ou o candidato mudou depois do lint, ou o log é falso.

**2. O Vigia não exige os logs de cegueira.** A tupla `REQUIRED` de
`vigia_integridade.py` não inclui `_log_prompt_checker.md` nem
`_log_prompt_continuidade.md`, e a checagem de vazamento roda dentro de um
`if path.exists()`. Resultado: **cena sem os logs passa no Vigia com a cegueira nunca
auditada**. Para o fiscal, isso é BLOQUEIO (`A2`).

Há ainda uma interação que ele sinaliza como alerta (`A6`): o Revisor Cego pode devolver
`APROVADO_COM_RESSALVAS`, mas o Vigia testa `status_geral != "APROVADO"` e reprova. O
fiscal não decide por você — força a decisão a ser explícita.

## Por que o Vigia roda em cópia temporária

`vigia_integridade.py` escreve `_log_vigia.md` dentro da cena. Esse artefato é prova de que
**o Orquestrador** executou o Vigia. Se o fiscal o gerasse ao reexecutar, estaria forjando
exatamente a evidência que veio auditar. Então ele copia a cena para um diretório temporário
e roda lá.

`reconciliar_controle.py` regrava `reconciliacao_ultima.json` — esse é um relatório derivado,
é a função declarada do script. O fiscal executa no projeto real e declara isso no relatório.

## O que ele NÃO faz

Crítica literária. Nunca. `AUTO_AUDITORIA_PIPELINE.md` §7 é explícito: nada de média de
frase, porcentagem de parágrafos ou desvio-padrão. Fluidez é do Escritor, do Editor e do
Revisor Cego. **Toda falha do fiscal é falha de pacote**, e deve ser devolvida ao
Orquestrador como tal — que já tem a regra de tratar reprovação do Vigia "como falha de
pacote, nunca como crítica literária".

E ele não corrige nada. Como o Controle da Obra, "registra diferenças sem corrigi-las".
