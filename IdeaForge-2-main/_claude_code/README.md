# Adaptador Claude Code — IdeaForge-2


5 papéis convertidos de "roteiro lido na mesma janela" para **subagentes com contexto isolado de verdade**.


| Agente | Papel original | Cérebro |
|---|---|---|
| `if-lider-do-debate` | Líder do Debate (Orquestrador Adaptativo) | `cerebros/lider-do-debate.md` |
| `if-proponente` | Agente Proponente | `cerebros/proponente.md` |
| `if-critico` | Agente Crítico | `cerebros/critico.md` |
| `if-especialista` | Especialista sob Demanda | `cerebros/especialista-sob-demanda.md` |
| `if-sintetizador` | Agente Sintetizador | `cerebros/sintetizador.md` |


## Instalação

> **Já vem instalado.** `.claude/agents/` existe na raiz deste sistema com os
> 5 adaptadores prontos. Rode o instalador só para **reinstalar**,
> **verificar** ou depois de mexer nos arquivos.

```bash
cd "<...>/IdeaForge-2-main"
python3 _claude_code/instalar.py             # instala e verifica
python3 _claude_code/instalar.py --verificar # só confere, não copia
```

**Use a versão Python, não o `.sh`.** Motivo concreto: o bit de execução **não
sobrevive** ao ciclo compactar → `.txt` → restaurar (o restaurador grava tudo em modo
644), então `./_claude_code/instalar.sh` falha com `Permission denied` na sua máquina. E no
Windows sem Git Bash/WSL o `.sh` não roda de jeito nenhum. O `instalar.sh` continua
disponível para quem estiver no Unix, mas chame assim:

```bash
bash _claude_code/instalar.sh
```

O `instalar.py` faz o que o `.sh` não faz: confere que todo adaptador tem frontmatter
válido, que os nomes são únicos, que nenhum campo está na ferramenta errada
(`maxSteps` é do OpenClaude, não do Claude Code),
e que **todo cérebro referenciado existe**. Ele também remove adaptadores órfãos de
papéis renomeados ou removidos, e avisa antes de sobrescrever arquivos com conteúdo
diferente. Sai com código 1 se achar qualquer problema.

Depois, rode o Claude Code **com o diretório de trabalho na raiz do sistema** — os
adaptadores referenciam os cérebros por caminho relativo (`cerebros/<papel>.md`):

```bash
cd "<...>/IdeaForge-2-main"
claude
```

Se preferir escopo pessoal (todos os projetos), copie para `~/.claude/agents/` — mas aí
troque `cerebros/<papel>.md` por um caminho absoluto no corpo de cada adaptador, senão o
agente não acha o cérebro.

## Formato usado (Claude Code)

Cada adaptador é um markdown com frontmatter YAML em `.claude/agents/<nome>.md`
(escopo de projeto) ou `~/.claude/agents/<nome>.md` (escopo pessoal). Campos usados aqui:

| Campo | Uso neste projeto |
|---|---|
| `name` | obrigatório — identificador do subagente |
| `description` | obrigatório — escrito como **condição de gatilho**, porque é o que decide o acionamento automático |
| `tools` | allowlist mínima por papel |
| `model` | `inherit` em todos, para não impor um modelo ao seu plano |
| `color` | cor no transcript |

O **corpo do markdown é o system prompt** do agente. Aqui ele é deliberadamente curto:
ele manda o agente carregar o cérebro correspondente em `cerebros/`. A lógica não é
duplicada no adaptador — ver "Por que o corpo é fino", abaixo.

## Por que o corpo do adaptador é fino

A regra 4 do comando é explícita: não duplicar a lógica em vários lugares que podem
divergir com o tempo. Então o adaptador carrega só a casca — gatilho, ferramentas,
isolamento, artefatos, fronteiras — e a primeira instrução do system prompt é **ler o
cérebro**.

Consequência prática: para mudar o comportamento de um papel, você edita **um** arquivo
(`cerebros/<papel>.md`), e as duas ferramentas passam a se comportar igual no round
seguinte. Os adaptadores só mudam quando muda a *casca* (nome, gatilho, ferramentas).

## Agent Teams — dependência de feature experimental

O par **Crítico ↔ Proponente** não é um par de subagentes comuns. Subagente comum
delega e espera o resultado final; aqui os dois lados precisam **debater diretamente
entre si**, cada um com contexto isolado. Isso é Agent Teams.

Para ativar:

```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
claude
```

Requer Claude Code recente (a feature é experimental e vem **desligada** por padrão).

**Se o time não subir**, não force o padrão errado. O cérebro
`cerebros/lider-do-debate.md` traz, na seção 10, um modo de contingência
("mediação alternada"): o Líder invoca alternadamente os subagentes Crítico e
Proponente, passando o histórico da rodada anterior a cada chamada e salvando o log em
`.forge/debate_log.md`. **Isso não é peer-to-peer** — os dois lados nunca se falam
diretamente, o Líder é sempre o intermediário. Se você rodar assim, diga isso no
relatório final.

## ⚠️ Aviso obrigatório: o que esta conversão abandonou

Esta extração **abandona o processo Python que orquestra o debate hoje**. O Blackboard,
o detector de convergência, o executor de rounds e as guardas de parsing **deixam de
rodar**. O debate passa a ser conduzido inteiramente pelo mecanismo nativo da ferramenta
(Agent Team), a partir dos arquivos em `cerebros/`.

O código Python permanece intacto no repositório (`src/`), mas **não é mais executado por
este caminho**. Ele continua sendo a referência de verdade, e é para onde você deve olhar
se algum comportamento abaixo importar de verdade para você.

Abaixo está, honestamente, o que virou prompt fiel, o que virou aproximação, e o que
simplesmente se perdeu.

### ✅ Traduziu bem (era texto de prompt, virou texto de prompt)

| Peça original | Onde foi parar |
|---|---|
| `EXPANSION_SYSTEM_PROMPT`, `DEFENSE_SYSTEM_PROMPT` | `cerebros/proponente.md` §3 e §4, literais |
| `CRITIQUE_SYSTEM_PROMPT`, `ISSUE_TABLE_HEADER` | `cerebros/critico.md` §2 e §3, literais |
| `SPECIALIST_PROFILES` (4 perfis) + fallback | `cerebros/especialista-sob-demanda.md` §3 e §4, literais |
| Prompt do `SynthesizerAgent` + seções obrigatórias | `cerebros/sintetizador.md` §2 e §3, literais |
| `PT_EN_NORMALIZATION_MAP` | `cerebros/critico.md` §3.1, tabela completa |
| Contratos de estilo (anti-prolixidade, PT-BR) | replicados nos dois cérebros do par |

### ⚠️ Virou aproximação (era cálculo, virou instrução)

1. **Similaridade de Jaccard ≥ 0.65 entre rounds.** Era `len(interseção)/len(união)` sobre
   bag-of-words com stopwords PT removidas — determinístico, reprodutível, com o mesmo
   resultado toda vez. Agora é um LLM **estimando** esse número. A direção do erro é
   previsível e vale registrar: modelos tendem a julgar "isso é a mesma coisa" por
   semântica, enquanto o Jaccard é puramente léxico. Duas críticas sobre o mesmo tema com
   vocabulário diferente dariam ~0.4 no original e podem ser lidas como convergência pelo
   agente. **Efeito prático: risco de o debate encerrar cedo demais.** O cérebro do Líder
   manda contar termos explicitamente e registrar o número, e manda **não** declarar
   saturação textual quando a conta não for confiável — mas isso é mitigação, não
   equivalência.
2. **Deduplicação semântica de issues (limiar 0.65, prefixo de 80 caracteres
   normalizados).** Mesmo problema, mesma direção: o agente pode descartar como duplicata
   um issue que o algoritmo teria aceitado, ou o contrário. Ficou descrito com precisão em
   `cerebros/critico.md` §5 e `cerebros/lider-do-debate.md` §6, inclusive com a
   consequência prática ("comece a descrição pelo que é específico").
3. **Cascata de parsing em 4 níveis** (tabela v4 → tabela legada → bullets → heurística por
   palavra-chave). Descrita na íntegra, mas o original era regex; agora é interpretação.
   Casos de borda vão divergir.
4. **Guarda de sub-extração.** Era: texto ≥ 200 caracteres, 0 issues extraídos e presença
   de uma das palavras `risco/problema/falha/erro/inconsistência/grave` → round marcado como
   parsing falho. Virou instrução de comportamento no cérebro do Crítico. Não há mais um
   detector externo conferindo.
5. **Aplicação de patches por match difuso de heading.** Era regex com normalização
   agressiva contra sete headings canônicos, anexando `> **MELHORIA APLICADA:**` ao fim da
   seção. Descrito no cérebro do Proponente; a fidelidade agora depende de o agente casar
   os nomes de seção como o regex casava.

### ❌ Se perdeu (não tem equivalente em prompt)

1. **Contadores exatos com retomada.** `_round_history` era uma lista em memória do
   processo. Agora o Líder precisa manter o histórico à mão, em `.forge/debate_log.md`. Se
   o log não for escrito a cada round, a saturação por estagnação (2 rounds a zero) fica
   sem base — e ela era o critério **exato** de convergência, o único que não dependia de
   estimativa.
2. **Orçamento de contexto em caracteres.** O `ContextBuilder` truncava cada bloco com
   números fixos (system 600, proposta 800, issues 600, resposta 700, decisões 300; total
   duro de 3000). Isso **não é mais aplicado**. Consequência dupla: os agentes passam a ver
   mais contexto do que viam (o que muda o comportamento observado, para melhor ou pior), e
   o custo por round deixa de ter teto. Os limites estão documentados nos cérebros como
   referência histórica, não como regra ativa.
3. **Guarda de resposta curta (< 50 caracteres).** Era um `if` que descartava o turno e
   preservava a proposta anterior. Virou instrução ("nunca devolva uma defesa vazia"). Não
   há mais nada descartando um turno degenerado.
4. **Retries de expansão** (`MAX_EXPANSION_RETRIES = 3`). O laço de retry não existe mais.
5. **`InvalidStateTransitionError`.** O `ValidationBoard` levantava exceção ao tentar
   resolver um issue já resolvido. Agora é uma regra escrita ("um issue resolvido não volta
   a abrir"), sem exceção que force o respeito.
6. **Fingerprint SHA-256 do snapshot.** Continua descrito e o Líder deve escrevê-lo, mas
   nada mais o recalcula e compara automaticamente.

### O que fazer se alguma dessas peças importa

Elas não são difíceis de trazer de volta **sem** ressuscitar o motor inteiro. O caminho
mais barato: manter um script determinístico pequeno e deixar o Líder chamá-lo por Bash a
cada round, em vez de estimar. `src/core/convergence_detector.py` já é autocontido — 137
linhas, zero chamadas LLM — e recebe dois textos e uma contagem. Um wrapper de CLI em
torno dele devolveria o Jaccard exato e o veredito de estagnação, e o Líder passaria a
**ler um número** em vez de estimar um. O mesmo vale para a deduplicação semântica, que usa
o mesmo `similarity()`.

Isso não está feito aqui porque o comando pediu explicitamente para **não** manter o motor
Python rodando por trás. Fica registrado como a peça que eu recomendaria reimplementar
primeiro, se a precisão da convergência importar.

## Estado em disco: preservado

A conversão **não mexeu** no mecanismo de estado. Os agentes leem e escrevem exatamente os
mesmos artefatos de sempre:

`.forge/validation_board.json` (snapshot do Board com fingerprint SHA-256), `.forge/debate_log.md` (log de rodada), relatório final em markdown

Se você quiser trocar parte disso pela memória nativa do agente
(`memory:` no frontmatter),
dá para fazer — mas isso muda o contrato do pipeline e não foi feito aqui. Os cérebros
instruem os agentes a **propor** essa migração ao usuário em vez de executá-la.

## O que NÃO mudou

- Nenhum arquivo original de skill foi movido, editado ou sobrescrito.
- Nenhuma regra de negócio, pseudocódigo, trava dura ou critério de aprovação foi alterado.
- A conversão trocou a **casca** (como o papel é invocado e isolado), não o **conteúdo**
  (o que o papel decide ou valida).
