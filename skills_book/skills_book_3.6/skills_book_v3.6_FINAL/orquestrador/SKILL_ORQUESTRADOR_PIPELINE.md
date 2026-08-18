# Skill do Orquestrador — Skill 3

## Responsabilidade

Coordenar o fluxo e manter as provas. O Orquestrador não produz prosa nem toma o lugar dos agentes especializados.

## Loop operacional

```text
para cada cena:
    se CONCLUIDO e reconciliação íntegra:
        continuar

    se BLOQUEADA_REVISAO_HUMANA:
        registrar pendência e continuar apenas se o usuário permitir

    criar/abrir worktree isolada
    registrar ESCREVENDO

    // Isolamento de contexto (quando a ferramenta que executa este pipeline
    // suportar subagente com contexto limpo — ex.: Claude Code, via Agent
    // com subagent_type especificado — "agente fresco"):
    //
    // Invoque o Escritor como um agente fresco, NÃO como continuação da
    // sessão principal. Um LLM tende a puxar o "clima" do texto imediatamente
    // anterior na janela de contexto; se o Escritor escreve logo depois de
    // JSON de validação, parecer da rubrica ("Reprova:", "Aprova:") ou
    // resultado do MARCH da cena anterior, a prosa tende a sair mais fria e
    // clínica mesmo que as instruções digam o contrário. Isso não é falha de
    // regra — é contaminação de registro.
    //
    // O agente fresco do Escritor deve receber SOMENTE:
    //   - DNA_REVELACAO_RESPEITOSA.md
    //   - GENERO.md ativo (se houver)
    //   - O trecho da Bible sobre metáfora central, voz e contrato editorial
    //   - O briefing desta cena específica (o que precisa acontecer nela)
    // E NÃO deve receber: JSONs de validação, texto de rubrica, resultado de
    // cenas anteriores além do que a Bible/Estado já resume, ou o histórico
    // bruto do loop do Orquestrador.
    //
    // Ao final, só o texto da cena (_saida_escritor.md) volta para o
    // Orquestrador — descarte o processo intermediário do subagente.
    //
    // Se a ferramenta em uso NÃO suportar isolamento de subagente (sessão
    // única, sem fork/task/agent separado): registre esse limite no Estado da
    // Obra e, como mitigação parcial, insira um separador visual explícito
    // antes de invocar o Escritor ("--- FIM DA VALIDAÇÃO. RETOMANDO VOZ
    // NARRATIVA. ---") para reduzir o efeito de arrasto de registro, mesmo
    // sem isolamento real.

    invocar Escritor
    verificar _saida_escritor.md

    se Editor ativado:
        invocar Editor
        candidato = _saida_editor.md
    senão:
        candidato = cópia exata de _saida_escritor.md

    salvar candidato em _saida_candidato.md
    candidato_checksum = checksum(_saida_candidato.md)

        // Checkpoint de Ressonancia (substitui o piso de densidade numerico):
    // Antes de passar para os validadores, o Orquestrador verifica se o
    // Lint de Conviccao passou. Depois, o Revisor Cego (com a nova Secao 6
    // — Validador de Ressonancia) avalia os 5 Movimentos Retoricos.
    // Nao ha contagem de palavras. Ha completude de arco.
    //
    // Estagio 1 — Lint (barato, deterministico, 0,2s):
    executar python3 utils/lint_conviccao.py _saida_candidato.md
    se exit_code != 0:
        reprovar com feedback orientado à causa: """Há trechos em que a prosa foge da responsabilidade (ex.: tarefa burocrática no fechamento). Reescreva resolvendo a causa — assuma a descoberta e transforme a ação em gesto físico imediato — em vez de apenas trocar as palavras marcadas."""
        retries += 1
        voltar ao Escritor (correcao cirurgica APENAS nos trechos apontados)
    
    // Estagio 2 — Validacao de Ressonancia (semantica, 5 Movimentos):
    // O Revisor Cego agora usa a RUBRICA_QUALITATIVA_V3.md Secao 6.
    invocar Revisor Cego (que avalia PASS/FAIL nos 5 movimentos)
    se Revisor retornar REPROVADO:
        registrar falha com o feedback especifico do movimento faltante
        retries += 1
        voltar ao Escritor com a instrucao de correcao do movimento
        retries += 1
        fornecer feedback cirúrgico ao Escritor: "cena abaixo do piso — que
            beat foi cortado?" e voltar à escrita, sem passar para os
            validadores abaixo

    gerar afirmações/perguntas a partir do candidato
    gerar perguntas de Continuidade a partir do candidato
    salvar logs de prompts sem a prosa

    invocar MARCH (cego) e Continuidade (cego)
    recalcular agregados do MARCH

    invocar Revisor Cego Editorial sobre o candidato

    se qualquer validação falhar:
        registrar falha atomically
        retries += 1
        se retries > 3:
            status = BLOQUEADA_REVISAO_HUMANA
            não declarar livro concluído
        senão:
            fornecer feedback cirúrgico ao Escritor
            voltar ao Editor

    copiar candidato para _saida_final.md atomically
    escrever manifesto de integridade com status_fisico = FECHAMENTO_EM_VERIFICACAO
    executar Vigia

    se Vigia != exit 0:
        registrar REPROVADO_VIGIA
        retries += 1
        tratar como falha de pacote, nunca como crítica literária
    senão:
        atualizar manifesto para status_fisico = APROVADO e vigia = APROVADO atomically

    atualizar Bible, Estado e Controle atomically
    reler _saida_final.md
    confirmar round-trip do checksum
    status = CONCLUIDO
```

## Pacote candidato

`_saida_candidato.md` é a última mutação. MARCH, Continuidade e Revisor referenciam essa versão. Se ela mudar, todos os resultados derivados ficam obsoletos.

`_saida_final.md` só nasce depois das aprovações. Ela deve ser byte a byte igual ao candidato aprovado.

## Cegueira

O Orquestrador pode ler a prosa para gerar perguntas, mas os validadores não. Antes das invocações:

- salve `_log_prompt_checker.md`;
- salve `_log_prompt_continuidade.md`;
- nunca inclua a prosa integral;
- deixe o Vigia conferir se o candidato não apareceu nesses logs.

## Agregados MARCH

Recalcule a partir de `resultados[]`:

- total;
- CONFIRMADO;
- CONTRADITO;
- NAO_ENCONTRADO;
- taxa factual.

As travas são de segurança factual. Elas não devem ser reutilizadas para aprovar ou reprovar ritmo, extensão ou estilo.

## Política de falha

Qualquer alteração do Escritor, Editor ou candidato exige novo Atomizador, novas perguntas, novos validadores, novo Revisor e novo Vigia. Não reutilize resultados de outra versão.

Após três retries, use `BLOQUEADA_REVISAO_HUMANA`. Não esconda a falha pulando a cena no relatório final.

## Reconciliação manual

Se o disco tiver uma versão diferente da registrada:

```text
status = MODIFICADO_MANUALMENTE
acao = REVALIDACAO_NECESSARIA
```

O Orquestrador não substitui a versão humana sem autorização explícita.

## Fechamento da obra

O Consolidador só pode emitir `CONCLUIDO` quando:

- todas as cenas planejadas estão `CONCLUIDO`;
- não há drift pendente;
- todos os pacotes físicos fecham;
- a fronteira do livro está íntegra;
- a auditoria de marketing passa.

Caso contrário, emita relatório parcial com pendências explícitas.

## Manifesto de Pontos de Ação (v3.6)

Após a obra ser aprovada e consolidada em `_saida_final.md`/`LIVRO_FINAL.md`,
o Orquestrador executa:

```text
python3 utils/gerar_pontos_de_acao.py LIVRO_FINAL.md -o PONTOS_DE_ACAO.md
```

O manifesto lista os fechamentos imperativos (Chamados Táteis) com a medida
citada, como checklist de prioridade para a revisão humana especializada.
Ele NÃO altera o livro — é um espelho externo de apoio à revisão (decisão 8/9
da sessão de 18/08/2026).
