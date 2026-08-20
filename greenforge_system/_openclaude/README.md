# Adaptador OpenClaude — Greenforge System


6 papéis convertidos de "roteiro lido na mesma janela" para **subagentes com contexto isolado de verdade**.


| Agente | Papel original | Cérebro |
|---|---|---|
| `gf-orquestrador-mestre` | Orquestrador Mestre | `cerebros/orquestrador-mestre.md` |
| `gf-decompositor` | Decompositor | `cerebros/decompositor.md` |
| `gf-solver` | Solver | `cerebros/solver.md` |
| `gf-proposer` | Proposer | `cerebros/proposer.md` |
| `gf-checker-cego` | Checker Cego (MARCH) | `cerebros/checker-cego.md` |
| `gf-consolidador` | Consolidador | `cerebros/consolidador.md` |


## Instalação

Os adaptadores precisam ficar na **raiz do sistema**, ao lado de `cerebros/`, porque o
corpo de cada agente referencia o cérebro por caminho relativo (`cerebros/<papel>.md`).

```bash
cd "<...>/greenforge_system"
./_openclaude/instalar.sh
```

Isso cria `.openclaude/agents/` na raiz do sistema e copia os 6 adaptadores.
Nada em `_openclaude/` é apagado e **nenhum arquivo original de skill é tocado**.

Depois, rode o OpenClaude **com o diretório de trabalho na raiz do sistema**:

```bash
cd "<...>/greenforge_system"
openclaude
```

Se preferir escopo pessoal (todos os projetos), copie para `~/.openclaude/agents/` — mas aí
troque `cerebros/<papel>.md` por um caminho absoluto no corpo de cada adaptador, senão o
agente não acha o cérebro.

## Formato usado (OpenClaude)

> **Pendências do comando resolvidas — com fonte.** As duas dúvidas em aberto do
> comando original foram confirmadas **lendo o código-fonte do próprio repositório**
> (`github.com/Gitlawb/openclaude`, `main` em 19/08/2026, v0.29.1), não por analogia
> com o Claude Code. Detalhes na seção "Como as pendências foram confirmadas".

Cada adaptador é um markdown com frontmatter YAML em `.openclaude/agents/<nome>.md`
(escopo de projeto) ou `~/.openclaude/agents/<nome>.md` (escopo pessoal).

| Campo | Uso neste projeto |
|---|---|
| `name` | obrigatório |
| `description` | obrigatório — condição de gatilho |
| `tools` | allowlist mínima por papel |
| `maxSteps` | teto de passos de ferramenta do subagente |
| `color` | cor no transcript |

**Roteamento de modelo NÃO vai no frontmatter.** No OpenClaude ele é feito à parte, em
`~/.openclaude/settings.json`, via `agentModels` + `agentRouting`:

```json
{
  "agentModels": {
    "nvidia-grande": {
      "model": "<modelo-nvidia>",
      "base_url": "https://integrate.api.nvidia.com/v1",
      "api_key": "nvapi-..."
    },
    "barato": { "model": "<modelo-menor>" }
  },
  "agentRouting": {
    "gf-orquestrador-mestre": "barato",
    "gf-decompositor": "barato",
    "default": "nvidia-grande"
  }
}
```

Rotas que omitem `base_url`/`api_key` reusam as credenciais do provedor atual — útil
para rodar os papéis baratos (atomizadores, validadores) num modelo menor sem duplicar
credencial.

> ⚠️ **Atenção a um detalhe que mudou:** o comando original citava `~/.openclaude.json`
> como local das configurações de roteamento. Esse arquivo existe, mas é o **config
> global** do OpenClaude. `agentModels` e `agentRouting` são lidos de
> **`~/.openclaude/settings.json`** — a própria documentação do projeto foi corrigida
> para esse caminho no PR #2102 ("Fix settings file path in README.md and
> docs/agent-routing.md from `~/.openclaude.json` to `~/.openclaude/settings.json`
> (the path the runtime actually loads)").

## Por que o corpo do adaptador é fino

A regra 4 do comando é explícita: não duplicar a lógica em vários lugares que podem
divergir com o tempo. Então o adaptador carrega só a casca — gatilho, ferramentas,
isolamento, artefatos, fronteiras — e a primeira instrução do system prompt é **ler o
cérebro**.

Consequência prática: para mudar o comportamento de um papel, você edita **um** arquivo
(`cerebros/<papel>.md`), e as duas ferramentas passam a se comportar igual no round
seguinte. Os adaptadores só mudam quando muda a *casca* (nome, gatilho, ferramentas).

## Como as pendências foram confirmadas

### Pendência 1 — caminho do diretório de agentes customizados ✅ CONFIRMADO

`.openclaude/agents/` (projeto) e `~/.openclaude/agents/` (usuário). A suposição do
comando estava correta, e agora tem lastro:

- `src/tools/AgentTool/loadAgentsDir.ts` chama `loadMarkdownFilesForSubdir('agents', cwd)`.
- `src/utils/markdownConfigLoader.ts` define `PROJECT_CONFIG_DIR_NAMES = ['.openclaude']`
  e monta o diretório de projeto como `<dir>/.openclaude/agents`, subindo de `cwd` até a
  raiz do git.
- O diretório de usuário é `getClaudeConfigHomeDir() + '/agents'`, e
  `src/utils/envUtils.ts` resolve `getClaudeConfigHomeDir()` para `$OPENCLAUDE_CONFIG_DIR`
  ou, na falta dele, `~/.openclaude`.
- Os testes `src/tools/AgentTool/loadAgentsDir.test.ts` exercitam literalmente
  `join(projectDir, '.openclaude', 'agents', '<nome>.md')` e
  `join(userConfigDir, 'agents', '<nome>.md')`.

Confirmado também que **`.claude/` de projeto não é lido**: `PROJECT_CONFIG_DIR_NAMES`
contém apenas `.openclaude`, e há um teste chamado *"prefers .openclaude project agents
over legacy .claude agents"*. Por isso os dois adaptadores coexistem sem conflito.

**Bônus (o comando subestimava o formato):** o frontmatter do OpenClaude aceita bem mais
que `name`/`description`/`maxSteps`. O parser `parseAgentFromMarkdown` também lê `tools`,
`disallowedTools`, `model`, `color`, `background`, `memory`, `isolation`, `effort`,
`permissionMode`, `maxTurns`, `skills`, `hooks` e `mcpServers`. Usei `tools`, `maxSteps` e
`color`; deixei `model` de fora de propósito, porque no OpenClaude o roteamento por agente
é feito em `settings.json` e misturar as duas coisas gera divergência silenciosa.

### Pendência 2 — Agent Teams no OpenClaude ✅ CONFIRMADO QUE EXISTE

A feature **foi portada no fork**. Evidências no código:

- `src/utils/agentSwarmsEnabled.ts` — gate central `isAgentSwarmsEnabled()`, que aceita
  a **mesma** variável do Claude Code, `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`, **ou** a
  flag de CLI `--agent-teams`.
- Ferramentas dedicadas: `src/tools/TeamCreateTool/` e `src/tools/TeamDeleteTool/`, ambas
  com `isEnabled()` amarrado a `isAgentSwarmsEnabled()`.
- Infraestrutura completa de teammates: `src/utils/teammateMailbox.ts` (caixa de entrada
  por agente, mensagens não lidas, pedidos de permissão), `src/utils/teammate.ts`,
  `src/utils/teamDiscovery.ts`, `src/utils/swarm/*` (backends tmux, iTerm e in-process).
- `src/tools/AgentTool/AgentTool.tsx` tem o caminho de spawn de teammate, com os
  parâmetros `name` e `team_name`, retornando `status: 'teammate_spawned'`.

Ou seja: **não foi preciso recorrer à mediação alternada.** O par Crítico/Proponente usa
Agent Team nativo nas duas ferramentas.

> ⚠️ **Ressalva honesta, e ela importa.** Para builds externos, `isAgentSwarmsEnabled()`
> exige **duas** condições: (1) o opt-in local (env var ou `--agent-teams`) **e** (2) um
> killswitch remoto de feature flag (`tengu_amber_flint`, via GrowthBook) que precisa
> estar ligado. O segundo não está sob o seu controle. Se o time não subir mesmo com a
> flag local ligada, é quase certo que o killswitch remoto está fechado — e aí o caminho
> é a contingência descrita abaixo, não uma configuração diferente.
>
> Detalhe adicional: `AgentTool.tsx` **rejeita agentes built-in como teammates**
> ("Built-in agent type cannot be spawned as a teammate"). Os nossos são agentes
> customizados, então isso não afeta este projeto.

## Comunicação: hierárquica, como já era

Todos os 6 papéis deste sistema se comunicam **de forma hierárquica** —
o orquestrador invoca, o papel executa, o resultado volta. Nenhum papel fala lateralmente
com outro. Isso não é uma limitação da conversão: é exatamente como o sistema já
funcionava. A única coisa que mudou é que agora o isolamento de contexto é **real**
(janela separada por subagente) em vez de "leitura sequencial na mesma janela".

Por isso este sistema **não** usa Agent Teams. Subagente comum é o padrão correto aqui.

## Estado em disco: preservado

A conversão **não mexeu** no mecanismo de estado. Os agentes leem e escrevem exatamente os
mesmos artefatos de sempre:

`_ledger_estado.md` (+ `.bak`), `_plano_de_trabalho.md`, worktrees `worktree_uat_NNN/`, `_saida_solver.md`, `_assercoes_para_validar.json`, `_log_prompt_checker.md`, `_resultado_validacao.json`

Se você quiser trocar parte disso pela memória nativa do agente
(`memory:` no frontmatter, também suportado pelo OpenClaude),
dá para fazer — mas isso muda o contrato do pipeline e não foi feito aqui. Os cérebros
instruem os agentes a **propor** essa migração ao usuário em vez de executá-la.

## O que NÃO mudou

- Nenhum arquivo original de skill foi movido, editado ou sobrescrito.
- Nenhuma regra de negócio, pseudocódigo, trava dura ou critério de aprovação foi alterado.
- A conversão trocou a **casca** (como o papel é invocado e isolado), não o **conteúdo**
  (o que o papel decide ou valida).
