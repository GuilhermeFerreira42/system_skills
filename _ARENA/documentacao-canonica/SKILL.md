---
name: documentacao-canonica
description: Organiza, audita e mantém a documentação canônica de um repositório. Define um ponto de entrada, uma fonte oficial por assunto e um fluxo para manter estado, decisões, planejamento, histórico, homologação e testes coerentes. Use ao implantar esse controle em um projeto ou consolidar documentação duplicada ou desatualizada.
---

# Documentação canônica

Mantenha um conjunto pequeno de documentos ativos e um endereço oficial por tipo de informação. A entrada indica a ordem de leitura e o destino de cada assunto. Nos demais arquivos, use referências à fonte oficial sempre que precisar citar uma informação mantida ali.

## Mapa de referência

Use os papéis abaixo para classificar a documentação. Em um projeto sem estrutura, use a numeração e os nomes como padrão inicial em `docs/`. Em um projeto existente, mapeie os arquivos atuais para esses papéis. Um projeto pequeno pode reunir papéis em seções, desde que o índice aponte para a seção oficial de cada assunto.

| Documento | O que mantém |
| --- | --- |
| 01 — Comece aqui | Índice curto, ordem de leitura, regras de trabalho e rotina de atualização. |
| 02 — Visão geral | Propósito, público, escopo do produto, stack e mapa do repositório. |
| 03 — Estado atual | O que existe e em que ponto está, revisão de referência, trabalho ativo, bloqueios e próxima ação. |
| 04 — Arquitetura e regras | Componentes, limites, dependências, contratos e restrições vigentes. |
| 05 — Decisões | Escolhas aprovadas, motivo, impacto e situação. Identifique decisões que substituem anteriores. |
| 06 — Próximas fases e dívidas | Prioridades futuras, especificações, dependências, dívidas e questões em aberto. |
| 07 — Histórico | O que mudou, quando e em qual revisão. Vincule as decisões e evidências pertinentes. |
| 08 — Homologação | Roteiro do avaliador, resultados esperados, critérios de aceite e situação da homologação. |
| 09 — Testes e ambiente | Pré-requisitos, comandos, ambientes, verificações executadas, resultados, limites e referências às evidências. |

## Implantar ou auditar

1. Leia as instruções do repositório e inventarie os documentos existentes. Para cada assunto, identifique a fonte atual, as cópias, as lacunas e os trechos obsoletos. Confira fatos de implementação no código, no Git ou nas verificações disponíveis.
2. Escolha um endereço oficial por assunto e documente o mapa na entrada. Se houver um arquivo de instruções para agentes, use nele uma referência curta para essa entrada, preservando suas instruções existentes. A leitura habitual começa por entrada, visão e estado. Consulte os demais papéis conforme a tarefa.
3. Quando a consolidação fizer parte da tarefa, transfira fatos vigentes para a fonte escolhida, preserve decisões e histórico e atualize os links. Marque material superado com a data e o sucessor, ou mova-o para o arquivo morto conforme a convenção do projeto. Em auditorias, apresente os achados e a origem das divergências.
4. Quando o comportamento observado divergir de uma especificação ou decisão vigente, registre separadamente o que o sistema faz e o que foi acordado. Corrija descrições factuais com base em evidências. Uma alteração no contrato segue o processo de decisão do projeto.

## Manter durante a execução

- **Antes de implementar.** Para trabalho que muda comportamento, registre ou localize o objetivo, os limites de escopo e os critérios verificáveis. Relacione os contratos relevantes e separe decisões aprovadas de questões em aberto.
- **Ao mudar de estado.** Planejamento e dívidas futuras ficam em Próximas fases. Trabalho iniciado aparece no Estado atual, com referência ao plano. Ao concluir, atualize o Estado atual e registre o acontecimento no Histórico. Se uma dívida for resolvida, atualize sua situação na fonte correspondente.
- **Ao decidir.** Registre a escolha aprovada em Decisões. Se ela alterar uma regra vigente, atualize a seção aplicável de Arquitetura e vincule a decisão. Mantenha o motivo e o registro de substituição em Decisões.
- **Ao validar.** Separe a execução técnica em Testes e ambiente do aceite registrado em Homologação. Indique o ambiente, a revisão coberta, o resultado real e as verificações pendentes. Guarde evidências volumosas na localização definida pelo projeto e referencie apenas as relevantes.
- **Ao entregar.** Confirme que o índice e os links afetados funcionam, que cada fato vigente tem uma fonte clara e que o Estado atual permite identificar o próximo passo. Atualize os documentos cujo assunto mudou.
