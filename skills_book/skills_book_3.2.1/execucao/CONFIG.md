# Configuração do projeto — Skill 3

## Identidade

- **Título:** O Poder Fisiológico da Água
- **Subtítulo:** O nutriente mais abundante do corpo humano — uma revelação em cenas
- **Tipo de obra:** não-ficção (divulgação científica técnico-popular)
- **Público:** leitor adulto de língua portuguesa, sem formação técnica obrigatória
- **Idioma:** pt-BR

## Fontes

- **Corpus:** `execucao/corpus/` (3 fontes; originais preservados em `Desktop/corpus/`)
- **Organização:** automática; o Orquestrador cria o mapa de módulos na Bible
- **Fontes excluídas:** nenhum arquivo excluído; trechos de marketing do corpus são
  excluídos da prosa conforme a Lei 6 (zero marketing) e registrados como decisão editorial

## Foco do usuário

> Obra composta por **um único capítulo**, dividido em cenas sequenciais que **esgotem
> o tema do corpus fornecido** (o poder fisiológico da água). Objetivo: transformar o
> conhecimento técnico em uma **revelação iminente**, tratando o leitor como um
> **cúmplice intelectual**. Nivelamento concluído no boot (A/A/A/A — fonte: usuario).

## Operação

- **Nivelamento editorial:** `OBRIGATORIO_NO_BOOT` — concluído em 2026-08-11
- **Editor:** `ATIVADO_POR_PADRAO`
- **Validação MARCH:** `OBRIGATORIA_QUANDO_HOUVER_FATOS`
- **Validação de Continuidade:** `OBRIGATORIA`
- **Revisor Cego Editorial:** `ATIVADO`
- **Máximo de retries por cena:** `3`
- **Consolidação parcial:** `PERMITIDA_COM_AVISO`

## Piso de densidade desta obra

- **Tipo:** não-ficção / divulgação científica → ver tabela genérica em `escritor/SKILL_ESCRITOR_PIPELINE.md`.
- **Piso mínimo por cena:** 800 palavras. Abaixo disso, a cena é tratada como
  incompleta e volta para desenvolvimento — não é reprovação de estilo, é sinal
  de que um beat (objetivo, obstáculo, evidência ou mudança de estado) foi
  cortado pela metade.
- **Referência de calibração:** a Cena 1 desta obra (~1000 palavras, aprovada
  após 3 tentativas) é o padrão de densidade a mirar nas demais cenas.

## Observação

O contrato de voz nasce das respostas do nivelamento e está salvo na Bible.
O piso acima é uma rede de segurança operacional (evita cena subdesenvolvida),
não uma fórmula de parágrafo nem uma meta de enchimento artificial.