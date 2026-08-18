# Autoauditoria da Skill 3

Os testes abaixo verificam fronteiras e vazamentos. Nenhum mede qualidade por contagem.

## 1. Marketing

Procure no livro final por preços, CTAs, ofertas, cupons e chamadas de conversão. Qualquer ocorrência não autorizada reprova.

## 2. Metadados vazados

Procure por JSON operacional, checksums, `bible_versao`, `input_checksum`, `objetivo_cena` ou nomes de agentes no texto destinado ao leitor.

## 3. Ordem

Compare os IDs de cenas presentes no livro com os IDs `CONCLUIDO` no Estado. A sequência deve ser idêntica.

## 4. Duplicatas e omissões

Cada cena concluída deve aparecer uma vez. Nenhuma cena pendente ou bloqueada pode aparecer como concluída.

## 5. Checksums

Para cada cena, compare o checksum do trecho consolidado com o checksum do `_saida_final.md` registrado no Controle. Se o formato de consolidação não permitir comparação byte a byte, o Consolidador deve preservar marcadores de fronteira e registrar a estratégia usada.

## 6. Linhagem

O manifesto, o candidato, o final e os resultados devem apontar para a mesma versão. Qualquer divergência gera `REVALIDACAO_NECESSARIA`.

## 7. Qualidade sem gate estatístico

A fluidez é responsabilidade do Escritor, Editor e Revisor Cego. Não executar teste de média de frase, porcentagem de parágrafos ou desvio-padrão.