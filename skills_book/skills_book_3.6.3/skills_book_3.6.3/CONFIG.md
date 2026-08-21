# Configuração do projeto — Skill 3

Preencha este arquivo antes de iniciar o Orquestrador. O nivelamento
editorial captura o contrato de voz no boot; a escolha de gênero abaixo é
independente disso e é lida obrigatoriamente pelo Orquestrador (ver
`orquestrador/BOOT_ORQUESTRADOR_PIPELINE.md`, Passo 1).

## Identidade

- **Título:** [preencher]
- **Subtítulo:** [opcional]
- **Tipo de obra:** [ficção | não-ficção | técnico | memórias | personalizado]
- **Público:** [preencher]
- **Idioma:** pt-BR

## Gênero aplicado

- **Gênero aplicado:** [padrão | nao_ficcao_pratica | ficcao_literaria | podbook_mentor | tecnico_manual | outro em `generos_completos/`]
- **Se "padrão":** o DNA global (`DNA_REVELACAO_RESPEITOSA.md`, registro
  "Elegância Orgânica") governa a voz sozinho.
- **Se outro valor:** o Orquestrador lê `generos_completos/<gênero>/GENERO.md`
  obrigatoriamente antes da Cena 1, e suas regras têm precedência sobre o DNA
  onde o próprio arquivo indicar restrição/substituição.

## Fontes

- **Corpus:** `execucao/corpus/`
- **Organização:** [automática; o Orquestrador cria o mapa de módulos]
- **Fontes excluídas:** [listar, se houver]

## Foco do usuário

> [Escreva aqui o que esta obra deve priorizar. Pode ser "nada além do nivelamento".]

## Operação

- **Nivelamento editorial:** `OBRIGATORIO_NO_BOOT`
- **Editor:** `ATIVADO_POR_PADRAO`
- **Validação MARCH:** `OBRIGATORIA_QUANDO_HOUVER_FATOS`
- **Validação de Continuidade:** `OBRIGATORIA`
- **Revisor Cego Editorial:** `ATIVADO`
- **Máximo de retries por cena:** `3`
- **Consolidação parcial:** `PERMITIDA_COM_AVISO`

## Criterio de Completude e Extensao

A faixa operacional de palavras por cena e definida pelo GENERO.md do genero escolhido (ex: 800-1500 para nao_ficcao_pratica). Este nao e um piso duro, mas um sinal de desenvolvimento.


A faixa operacional de palavras por cena e definida pelo GENERO.md do genero escolhido (ex: 800-1.500 para nao_ficcao_pratica). Este nao e um piso duro, mas um sinal de desenvolvimento: se a cena sair muito abaixo da faixa, verifique se faltou um movimento retorico.

A completude da cena e avaliada pelo Revisor Cego (Validador de Ressonancia — RUBRICA §6) atraves das 3 perguntas:

1. **O que estava em jogo?** (O leitor identifica o conflito/tensao da cena).
2. **Que nova peca do quebra-cabeca eu recebi?** (O leitor identifica o novo dado/virada).
3. **Como isso mudou o que eu sabia?** (O leitor percebe a mudanca de estado).

## Observação

Os campos acima descrevem o projeto. Eles não são um contrato estético numérico.
O contrato de voz nasce das respostas do nivelamento e é salvo na Bible.
O piso de densidade acima é uma rede de segurança operacional (evita cena
subdesenvolvida), não uma fórmula de parágrafo nem uma meta de enchimento artificial.