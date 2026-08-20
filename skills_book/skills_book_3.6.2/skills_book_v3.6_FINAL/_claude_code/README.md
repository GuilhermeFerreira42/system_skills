# Adaptador Claude Code — Skills Book v3.6 FINAL


9 papéis convertidos de "roteiro lido na mesma janela" para **subagentes com contexto isolado de verdade**.


| Agente | Papel original | Cérebro |
|---|---|---|
| `book-orquestrador` | Orquestrador | `cerebros/orquestrador.md` |
| `book-escritor` | Escritor | `cerebros/escritor.md` |
| `book-editor` | Editor | `cerebros/editor.md` |
| `book-revisor-cego-editorial` | Revisor Cego Editorial | `cerebros/revisor-cego-editorial.md` |
| `book-atomizador` | Atomizador | `cerebros/atomizador.md` |
| `book-validador-march` | Validador MARCH | `cerebros/validador-march.md` |
| `book-validador-continuidade` | Validador de Continuidade | `cerebros/validador-continuidade.md` |
| `book-consolidador` | Consolidador | `cerebros/consolidador.md` |
| `book-controle-da-obra` | Controle da Obra | `cerebros/controle-da-obra.md` |


## Instalação

Os adaptadores precisam ficar na **raiz do sistema**, ao lado de `cerebros/`, porque o
corpo de cada agente referencia o cérebro por caminho relativo (`cerebros/<papel>.md`).

```bash
cd "<...>/skills_book_v3.6_FINAL"
./_claude_code/instalar.sh
```

Isso cria `.claude/agents/` na raiz do sistema e copia os 9 adaptadores.
Nada em `_claude_code/` é apagado e **nenhum arquivo original de skill é tocado**.

Depois, rode o Claude Code **com o diretório de trabalho na raiz do sistema**:

```bash
cd "<...>/skills_book_v3.6_FINAL"
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

Todos os 9 papéis deste sistema se comunicam **de forma hierárquica** —
o orquestrador invoca, o papel executa, o resultado volta. Nenhum papel fala lateralmente
com outro. Isso não é uma limitação da conversão: é exatamente como o sistema já
funcionava. A única coisa que mudou é que agora o isolamento de contexto é **real**
(janela separada por subagente) em vez de "leitura sequencial na mesma janela".

Por isso este sistema **não** usa Agent Teams. Subagente comum é o padrão correto aqui.

## Estado em disco: preservado

A conversão **não mexeu** no mecanismo de estado. Os agentes leem e escrevem exatamente os
mesmos artefatos de sempre:

Bible da Obra (`execucao/bible/bible_da_obra.md`), Estado da Obra, Controle da Obra (`execucao/controle/controle_da_obra.json`), worktrees por cena com `_saida_escritor.md`, `_saida_editor.md`, `_saida_candidato.md`, `_saida_final.md`, `_afirmacoes_para_validar.json`, `_perguntas_continuidade.json`, `_resultado_march.json`, `_resultado_continuidade.json`, `_resultado_revisor_cego.json`, `_manifesto_integridade.json`, `_log_prompt_checker.md`, `_log_prompt_continuidade.md`

Se você quiser trocar parte disso pela memória nativa do agente
(`memory:` no frontmatter),
dá para fazer — mas isso muda o contrato do pipeline e não foi feito aqui. Os cérebros
instruem os agentes a **propor** essa migração ao usuário em vez de executá-la.

## O que NÃO mudou

- Nenhum arquivo original de skill foi movido, editado ou sobrescrito.
- Nenhuma regra de negócio, pseudocódigo, trava dura ou critério de aprovação foi alterado.
- A conversão trocou a **casca** (como o papel é invocado e isolado), não o **conteúdo**
  (o que o papel decide ou valida).
