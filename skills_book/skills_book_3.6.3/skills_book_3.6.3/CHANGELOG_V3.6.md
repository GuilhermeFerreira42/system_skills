# CHANGELOG v3.6 — Refatoração: Arquitetura Híbrida + Fidelidade à Fonte (2026-08-18)

**Base:** v3.5.2 (arquitetura híbrida Lint + Ressonância)
**Decisões aplicadas:** sessão de calibração de 18/08/2026 (17 itens avaliados com revisão externa)

---

## Decisões estruturais da sessão

A sessão partiu de duas constatações:

1. **A IA não chega ao nível desejado sem um capítulo de referência** — regras delimitam (espaço negativo); o exemplo calibra a voz (espaço positivo). Mantido o princípio: referência = VOZ, corpus = CORPO.
2. **Métricas não capturam alma** — e, quando viram gate, empurram a IA para otimizar o score em vez de escrever bem. Por isso o lint deixou de ser juiz de conteúdo e virou guardião de estrutura.

Adicionalmente, o usuário revelou uma camada externa que muda o cálculo de risco: **existe um segundo script que percorre o livro inserindo as fontes, e haverá revisão humana especializada antes da publicação.** A atribuição de fontes e a cautela médica deixam de ser responsabilidade da prosa.

---

## O que mudou na v3.6

### `utils/lint_conviccao.py` — reescrito

| Vetor | v3.5.2 | v3.6 |
|---|---|---|
| F1 (fonte visível) | infração eliminatória | **removida** — citar fonte é permitido (fidelidade) |
| F2 (disclaimer) | infração eliminatória | **removida** — ressalva específica permitida quando há risco |
| F3 (hedge) | teto de 2 por cena | **removido** — hedge livre, especialmente em alegação contestada |
| F5 (quantificador vago) | infração | **removida** — vago permitido quando a fonte não tem número |
| F6 (ação burocrática) | bloqueio duro | **mantida** — única família que permanece como bloqueio |
| Vetor 1 (notação) | exige LaTeX em 100% dos capítulos | **afrouxado** — nota 10 com notação presente + ≥3 percentuais, sem exigência por capítulo |
| Vetor 2 (cientistas) | lista `CIENTISTAS_PADRAO` hardcoded (Carrel, Batmanghelidj, Agre...) | **genérico** — detecção de nome próprio (título+nome ou sobrenome duplo) + `--nomes` por projeto |
| Vetor 4 (listas) | nota 10 exigia 6+ listas | **afrouxado** — nota 10 com ≥2 listas bem usadas; sem teto de 5 (fiel à fonte) |
| Correções | apontavam a regex disparada | **orientadas à causa** (opção 2) — o feedback diz o problema de fundo, não o padrão |

### `utils/gerar_pontos_de_acao.py` — novo

Gera `PONTOS_DE_ACAO.md`: manifesto externo dos **Chamados Táteis** (fechamentos imperativos com verbo + medida + critério). Checklist de prioridade para a revisão humana especializada — o revisor não relê a obra inteira, vai direto nos pontos onde o leitor é instruído a agir com o corpo. Não altera o livro.

### `generos_completos/nao_ficcao_pratica/GENERO.md`

- **§1:** "PROIBIDO disclaimers" → "EVITE ressalva genérica de rodapé; **PERMITIDO** ressalva específica e pertinente quando a alegação envolve risco real (dosagem, condição clínica, substituição de tratamento), mantendo a forma da fonte".
- **§8:** teto de 5 itens em listas → **fiel à fonte** (se a fonte lista 10, mantém 10); única limitação: categórica, nunca tutorial.

### `escritor/DNA_REVELACAO_RESPEITOSA.md`

- **§10 reescrito:** apenas **F6 (ação burocrática)** permanece como bloqueio duro; F1, F2, F3, F4, F5 viram **direção preferencial** (permitidas quando a fonte/risco pedem); F7 (metáfora descartável) mantida como regra de obra.
- **§11:** tabela de exemplos **reescrita com exemplos fictícios genéricos** (método de estudo, material de construção, leitura diária) — removeu os exemplos específicos do corpus da água (úlcera/Batmanghelidj) que contaminavam um arquivo global.

### `revisor_cego_editorial/RUBRICA_QUALITATIVA_V3.md`

- **§3.9:** reprova apenas ressalva **genérica de rodapé** sem função; aprova ressalva **específica e pertinente** quando há risco real.

### `orquestrador/SKILL_ORQUESTRADOR_PIPELINE.md`

- Correção do lint **orientada à causa** (opção 2 da sessão): o feedback diz "reescreva resolvendo a causa — assuma a descoberta, transforme a ação em gesto físico", não "troque a palavra X".
- Novo passo final: **gerar `PONTOS_DE_ACAO.md`** via `utils/gerar_pontos_de_acao.py`.

### Mantido (sem alteração)

- Piso de densidade 800–1500 (não-ficção) — restaurado na v3.5.2, mantido.
- 5 Movimentos Retóricos na Bible (Arquitetura Retórica) — mantido.
- Separação referência = VOZ / corpus = CORPO — mantido.
- Vetor 6 (fechamento de 30s) + F6 — mantido.
- `FINGERPRINT_ESTILO_DEPRECATED_v1.md` — mantido como registro histórico (substituído pela Assinatura Estilística qualitativa na Bible).

---

## Validação executada na v3.6

- `python3 utils/lint_conviccao.py uploads/LIVRO_FINAL.md --metafora aquário` → **10/10 nos seis vetores, APROVADO, exit 0** (com o lint reescrito).
- `python3 utils/gerar_pontos_de_acao.py uploads/LIVRO_FINAL.md` → **5 Chamados Táteis** detectados (cenas 2, 3, 5, 7, 9), com a medida citada e o fechamento final marcado com "· critério".

---

## Notas

- O lint v3.6 é **genérico**: pode rodar em qualquer obra de qualquer tema sem lista de cientistas fixa. Para obras com elenco próprio, use `--nomes "Personagem1,Personagem2"`.
- A fidelidade à fonte tornou-se o princípio transversal: o texto reproduz o conteúdo como a fonte apresenta; fontes e ressalvas formais vivem no Aparato e no script externo de atribuição.

---

# CHANGELOG v3.6.1 — Fechamento em TODA cena (2026-08-18)

## Decisão

Toda cena deve terminar com um **fechamento próprio** que conclui o que abriu — não apenas a última cena da obra. A diferença está no tipo:

- **Cenas do meio:** parágrafo de cristalização (1 a 3 frases que nomeiam a implicação mais funda, amarram o fio aberto e ecoam a metáfora-mestra).
- **Última cena da obra:** além da cristalização, recebe o Chamado Tátil de 30 segundos (verbo + medida + critério).

## Arquivos alterados

- `generos_completos/nao_ficcao_pratica/GENERO.md` — §4 reescrito: "TODA cena termina com um fechamento próprio"; cenas do meio fecham com parágrafo de cristalização.
- `revisor_cego_editorial/RUBRICA_QUALITATIVA_V3.md` — §6 Movimento 5: "Fechamento de Cena" exige PASS em TODAS as cenas (cristalização nas do meio; chamado tátil na última).
- `utils/lint_conviccao.py` — Vetor 6 verifica que toda cena tem fechamento (heurística: último bloco contido, termina em pontuação de fechamento, sem nota vazada no corpo; chamado tátil na última cena). Cabeçalhos internos colados são tratados corretamente.
- `COMANDO_PADRAO_INICIALIZACAO.md` — regra de fechamento em toda cena explicitada.

## Validação

- Livro v3.5 (9 cenas, fechamento em todas): Vetor 6 = 10/10, média 10.0.
- Livro v3.6 teste 2 (6 cenas): Vetor 6 = 10/10, média 10.0.

---

# CHANGELOG v3.6.2 — Metáfora e Personagem Opcionais + Cálculo de Cenas (2026-08-18)

## Decisões

1. **Metáfora NÃO é obrigatória.** O livro pode ter UMA imagem central, OU várias (uma por capítulo/módulo), OU nenhuma. Nada é forçado: prosa direta e fiel à fonte vale mais que metáfora fabricada.
2. **Personagem NÃO é obrigatório.** Se a fonte traz pessoas reais, apresente-as com data/lugar/obstáculo; se não traz, escreva sem — **nunca inventar personagem** para preencher.
3. **Cálculo de cenas baseado no corpus.** A IA deve calcular quantas cenas o livro inteiro exige (cada mecanismo/personagem/mito relevante = uma cena), com referência de 6 a 9 cenas para não-ficção prática, e **apresentar o cálculo ao usuário, justificando e conversando** antes de escrever.
4. **Liberdade de conversa.** A IA pode e deve discutir com o usuário as escolhas estruturais (gênero, número de cenas, metáfora) — nada de decisões silenciosas.

## Arquivos alterados

- `generos_completos/nao_ficcao_pratica/GENERO.md` — §1 (metáfora flexível por capítulo; personagem opcional, nunca inventar), §8 (metáfora doméstica quando usada), §11 (cálculo de cenas + justificativa).
- `revisor_cego_editorial/RUBRICA_QUALITATIVA_V3.md` — §6 Movimento 2 (Herói com Atrito = NA quando não há personagem; FAIL só por personagem inventado ou vazio) e Movimento 3 (Mecanismo Concreto sem metáfora obrigatória).
- `utils/lint_conviccao.py` — Vetor 2 (personagem opcional; com `--nomes`, reprova personagem fora da lista = possível invenção) e Vetor 3 (sem `--metafora` = 10 automático; com `--metafora` = consistência no escopo, com regra especial para obras de 1 capítulo).
- `COMANDO_PADRAO_INICIALIZACAO.md` — regras de metáfora/personagem opcionais + cálculo de cenas com justificativa + liberdade de conversa.

## Validação

- Livro v3.5 (9 cenas, metáfora aquário, personagens): **10/10 APROVADO**.
- Livro v3.6 teste 2 (6 cenas, 1 capítulo, metáfora aquário): **10/10 APROVADO**.
- Livro sintético SEM metáfora e SEM personagem: Vetor 2 = 10, Vetor 3 = 10 (sem `--metafora`), reprovação apenas onde o fechamento/chamado tátil realmente falta — confirmando que ausência de imagem e de personagem não penaliza mais.

---

# CHANGELOG v3.6.3 — Decomposição Universal de Cenas + Validação por Subagente Cego (2026-08-21)

## Decisão

A lógica de cálculo do número de cenas estava fragmentada em três trechos do
`COMANDO_PADRAO_INICIALIZACAO.md` (linhas 62, 113 e 117), que já divergiam entre si —
um dizia "material rico → mais", o outro cravava "8–10". Pior: **os agentes não tinham
essa regra**. O cálculo acontecia no boot, não no pipeline, permitindo que a IA usasse
atalhos matemáticos arbitrários (divisão de tamanho de arquivo, multiplicação de DVDs,
chutes) em vez de análise real do conteúdo. O resultado eram números insuficientes e
arbitrários.

A solução substitui a lógica fragmentada por um **framework universal de decomposição de
conteúdo**, aplicável a qualquer gênero, com validação obrigatória por subagente cego,
alinhado à filosofia de auditoria do restante da skill.

## Mudanças

### Novos arquivos

- `cerebros/analista-de-decomposicao.md` — cérebro do Agente 1 (mapeamento de UFIs)
- `cerebros/verificador-de-decomposicao.md` — cérebro do Agente 2 (validação cega)
- Adaptadores em `.claude/agents/` e `.openclaude/agents/` (e nas árvores-fonte
  `_claude_code/` e `_openclaude/`):
  - `book-analista-de-decomposicao.md`
  - `book-verificador-de-decomposicao.md`

### Arquivos modificados

- `COMANDO_PADRAO_INICIALIZACAO.md` — os três trechos fragmentados foram substituídos
  pela seção única "CÁLCULO DO NÚMERO DE CENAS — MÉTODO UNIVERSAL DE DECOMPOSIÇÃO
  (v3.6.3)".
- `orquestrador/SKILL_ORQUESTRADOR_PIPELINE.md` — nova **Fase 0: Decomposição e
  Validação**, antes do loop de cenas.
- `cerebros/auditor-de-pipeline.md` — novo **Bloco A0**: nenhuma cena pode ser auditada
  sem decomposição verificada e aprovada.
- `_auditoria/auditar_pipeline.py` — implementa o Bloco A0 (a trava é executável, não
  apenas declarada).

### Regras revogadas ou substituídas

- **PROIBIDO:** atalhos matemáticos — tamanho de arquivo ÷ N, nº de DVDs × N, divisões
  arbitrárias, chute.
- **REMOVIDO:** a referência "800 a 1.500 palavras" **do cálculo de cenas**. Completude
  é por arco e função dramática, não por contagem — coerente com a autoauditoria §7, que
  proíbe gate estatístico. A faixa continua existindo como sinal operacional de
  desenvolvimento (bullet "Extensão operacional de cada cena"), nunca como insumo do
  cálculo nem critério de aprovação.
- **REVISADO:** "6 a 9 cenas" passa a ser referência contextual explicitamente
  desancorada — não é limite, não é teto, não é meta.
- **SUBSTITUÍDO:** as categorias específicas de saúde (mecanismos / personagens / mitos)
  deram lugar às 4 classes universais de UFI.

### Novas regras

- **UFIs (Unidades Fundamentais de Informação):** 4 classes universais e autoajustáveis
  pelo gênero — Eventos/Pontos de Mutação, Entidades/Agentes de Ação,
  Tensões/Contrapontos/Paradigmas, Blocos Instrucionais/Unidades Explicativas.
- **Método dos 5 passos:** Passo 0 leitura integral → Passo 1 mapeamento de UFIs →
  Passo 2 agrupamento lógico → Passo 3 cálculo base → Passo 4 justificativa
  densitométrica.
- **Validação por subagente cego em duas fases:** o verificador mapeia as próprias UFIs
  vendo **somente o corpus**, e só depois recebe a análise do Agente 1 para comparar.
- **Matriz de decisão:** até 1 UFI de diferença sem omissão estrutural = APROVADO;
  2 UFIs = ressalva/devolução; 3+ UFIs ou omissão estrutural grave = rejeição
  obrigatória; agrupamento incoerente = rejeição.
- **Pré-requisito duro:** nenhuma cena começa sem
  `_resultado_verificacao_decomposicao.json` com `decisao = "APROVADO"`.

## Notas

- O fluxo é agnóstico a gênero: não-ficção, ficção, técnico, biográfico, autoajuda etc.
  Não há cláusula separada para ficção — as classes se traduzem pelo contexto (blocos
  instrucionais viram unidades de desenvolvimento dramático). Classe legitimamente vazia
  não é omissão.
- O verificador é cético por definição: não pode apenas concordar com o Agente 1.
- O auditor de pipeline detecta as três formas de burlar a trava: auto-aprovação do
  Agente 1, violação de cegueira do verificador, e análise independente não gravada por
  extenso (que torna a cegueira inauditável).
