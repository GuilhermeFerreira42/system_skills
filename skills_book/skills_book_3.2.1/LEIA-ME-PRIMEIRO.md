# Leia-me primeiro — Skill 3

Este pacote produz livros com uma divisão rígida entre **criação** e **auditoria**.

## Ordem de inicialização

O Orquestrador deve ler, nesta ordem:

1. `execucao/CONFIG.md`
2. `REGRAS_GREENFORGE_PIPELINE.md`
3. `FLUXO_COMPLETO_PIPELINE.md`
4. `nivelamento_editorial/PERGUNTAS_NIVELAMENTO.md`
5. `orquestrador/BOOT_ORQUESTRADOR_PIPELINE.md`
6. `orquestrador/SKILL_ORQUESTRADOR_PIPELINE.md`
7. Bible e Estado da obra, se já existirem
8. O corpus relevante para o capítulo atual

Cada agente lê apenas a sua própria documentação e os insumos explicitamente permitidos.

## Contrato de liberdade do Escritor

O Escritor recebe:

- objetivo da cena;
- contexto anterior resumido;
- recorte relevante da Bible;
- contrato de voz qualitativo;
- foco específico do usuário;
- fatos e fontes que precisam aparecer, quando aplicável.

O Escritor **não recebe e não precisa satisfazer**:

- desvio-padrão de parágrafos;
- porcentagem de parágrafos densos;
- proibição de sequências de frases curtas;
- média de palavras por frase;
- qualquer outra métrica estética punitiva.

A extensão é uma orientação operacional do plano, nunca um molde que force enchimento artificial.

**Nota:** isso não contradiz o piso de densidade descrito em `escritor/SKILL_ESCRITOR_PIPELINE.md`.
Métrica de ritmo (proibida) é regra sobre a *forma* das frases — desvio-padrão de parágrafo,
alternância obrigatória de frase curta/longa. Piso de densidade (permitido) é regra sobre
*completude* — sinaliza quando uma cena provavelmente cortou um beat pela metade. Um governa
como a frase soa; o outro checa se a cena terminou o que começou.

## Contrato de segurança

A segurança não é removida; ela muda de lugar:

- MARCH verifica fatos contra o corpus sem ler a prosa.
- Continuidade verifica coerência contra Bible/Estado sem ler a prosa.
- O Revisor Cego vê a prosa, mas não vê corpus, Bible ou Estado; julga apenas comunicação e fluidez.
- O Vigia lê somente o necessário para comparar bytes, hashes e manifestos. Ele não avalia estilo.
- O Controle da Obra reconcilia o estado lógico com o filesystem e sinaliza drift.

## Proibido

1. Produzir o livro inteiro em uma chamada.
2. Deixar o Editor alterar a prosa depois da última validação.
3. Validar o texto final usando resultados gerados para uma versão anterior.
4. Resolver edição manual com reescrita automática integral.
5. Usar métricas de ritmo como gate de qualidade literária.
6. Marcar uma obra como concluída contendo cenas pendentes ou bloqueadas.
7. Misturar material de marketing ao livro.

## Quando houver falha

- Registre a transição de status no Estado e no Controle.
- Faça uma reescrita cirúrgica, não uma nova obra inteira.
- Reexecute o pipeline desde o Editor/artefato candidato, porque qualquer mutação invalida as validações posteriores.
- Após três retries, marque `BLOQUEADA_REVISAO_HUMANA` e siga apenas com a supervisão registrada.

A Skill 3 deve ser exigente com a verdade e leve com a arte.


==========================================
Conteúdo de livro_final.md (caminho: skills_book_3/livro_final.md) [enc: utf-8]:

==========================================
Conteúdo de GUIA_CALIBRACAO_EMPATIA.md (caminho: skills_book_3/nivelamento_editorial/GUIA_CALIBRACAO_EMPATIA.md) [enc: utf-8]: