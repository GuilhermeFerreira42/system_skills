# Adaptador Claude Code — Greenforge System


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

> **Já vem instalado.** `.claude/agents/` existe na raiz deste sistema com os
> 6 adaptadores prontos. Rode o instalador só para **reinstalar**,
> **verificar** ou depois de mexer nos arquivos.

```bash
cd "<...>/greenforge_system"
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
cd "<...>/greenforge_system"
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
(`memory:` no frontmatter),
dá para fazer — mas isso muda o contrato do pipeline e não foi feito aqui. Os cérebros
instruem os agentes a **propor** essa migração ao usuário em vez de executá-la.

## O que NÃO mudou

- Nenhum arquivo original de skill foi movido, editado ou sobrescrito.
- Nenhuma regra de negócio, pseudocódigo, trava dura ou critério de aprovação foi alterado.
- A conversão trocou a **casca** (como o papel é invocado e isolado), não o **conteúdo**
  (o que o papel decide ou valida).
