# Regras Greenforge da Skill 3 — As 6 leis duras

Estas leis protegem a rastreabilidade sem transformar a prosa em um formulário estatístico.

## Lei 1 — Cena por cena

Uma cena é uma unidade de produção isolada. O Orquestrador só avança quando a cena atual tem um pacote físico aprovado ou é explicitamente bloqueada para revisão humana.

## Lei 2 — Validação dupla cega

Toda cena factual passa por:

- **MARCH:** perguntas + corpus; nunca a prosa.
- **Continuidade:** perguntas + Bible + Estado; nunca a prosa.

O Orquestrador salva os prompts e verifica que nenhum contém o texto integral do Escritor ou do candidato. A cegueira é uma propriedade verificável, não uma promessa textual.

Os gates numéricos do MARCH são de **lastro factual**, não de estética: contradição factual reprova; afirmações sem lastro acima do limite definido para o projeto reprovam. Nenhuma dessas contagens governa o ritmo literário.

## Lei 3 — Atualização atômica

Bible, Estado e Controle da Obra são escritos em arquivo temporário no mesmo diretório e substituídos por `os.replace`. Antes de modificar um checkpoint existente, crie backup.

## Lei 4 — Prova física e linhagem

O artefato final aprovado recebe checksum SHA-256 etiquetado. O manifesto registra:

- checksum do candidato validado;
- checksum do arquivo final;
- tentativa;
- resultados dos validadores;
- timestamp;
- origem da edição, quando houver.

O round-trip relê o arquivo do disco. Se os bytes não forem os mesmos, a cena não está concluída.

## Lei 5 — Worktree isolada

Cada cena tem sua própria pasta. Os agentes recebem apenas os arquivos necessários. Uma cena não pode contaminar a prosa, as perguntas ou os resultados de outra.

## Lei 6 — Zero marketing

O livro não é uma página de venda. Preços, CTAs, ofertas, cupons e instruções de conversão são proibidos no texto final, salvo se forem objeto documental explícito da obra e estiverem autorizados no foco do projeto.

## Princípios não numéricos de qualidade

Estes princípios orientam Escritor, Editor e Revisor, mas não são métricas de bloqueio:

- clareza antes de ornamentação;
- variação natural de densidade;
- respiro quando o leitor precisa processar uma ideia;
- frase curta quando a cena pede impacto;
- parágrafo desenvolvido quando o raciocínio pede espaço;
- analogia concreta quando a abstração não se sustenta sozinha;
- fecho que ecoa a pergunta ou imagem da própria cena;
- crítica a sistemas sem acusações conspiratórias gratuitas.

## Autoridade dos registros

A Bible decide o que é verdadeiro dentro da obra. O Estado decide o que o sistema pretendia fazer. O disco decide quais bytes existem. O Controle da Obra compara os três e registra divergências; ele não reescreve a história nem corrige o usuário silenciosamente.

## Política de drift manual

Se o checksum de um artefato concluído mudar fora do pipeline:

```text
MODIFICADO_MANUALMENTE
→ preservar o arquivo e o histórico anterior
→ invalidar apenas os artefatos derivados
→ marcar REVALIDACAO_NECESSARIA
→ não iniciar reescrita automática
```

## Política de retries

Cada cena tem no máximo três retries de correção. Depois disso:

```text
BLOQUEADA_REVISAO_HUMANA
```

A consolidação pode produzir um relatório parcial, mas não pode declarar `CONCLUIDO` enquanto houver qualquer cena bloqueada, reprovada ou pendente.