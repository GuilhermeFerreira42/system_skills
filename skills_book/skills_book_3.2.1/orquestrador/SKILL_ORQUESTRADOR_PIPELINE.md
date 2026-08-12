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

    invocar Escritor
    verificar _saida_escritor.md

    se Editor ativado:
        invocar Editor
        candidato = _saida_editor.md
    senão:
        candidato = cópia exata de _saida_escritor.md

    salvar candidato em _saida_candidato.md
    candidato_checksum = checksum(_saida_candidato.md)

    // Checkpoint de densidade (ver piso em execucao/CONFIG.md e na tabela
    // genérica de escritor/SKILL_ESCRITOR_PIPELINE.md). Isto não é gate de
    // ritmo ou estilo — é apenas: a cena tem desenvolvimento suficiente para
    // ter cumprido objetivo, obstáculo e mudança de estado?
    se contar_palavras(candidato) < piso_da_obra:
        tratar como falha de desenvolvimento (não como crítica literária)
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

