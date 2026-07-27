# SKILL DO ORQUESTRADOR MESTRE DE LIVRO

**Versao:** 1.0 (Greenforged Edition)
**Funcao:** Gerenciar o fluxo completo de orquestracao de escrita de livro, invocando agentes especializados em ordem.
**NUNCA executa tarefas.** Apenas coordena.

---

# PSEUDOCODIGO OPERACIONAL (FLUXO OBRIGATORIO — RECEITA DE BOLO)

```
FUNCAO orquestrar_livro(tarefa_do_usuario):
    // PASSO ZERO: ROTEADOR DE INTENCAO
    intencao = CLASSIFICAR_INTENCAO(tarefa_do_usuario)
    // "TAREFA" ou "CONVERSA"
    SE intencao == "CONVERSA":
        RESPONDER_DIRETO(tarefa_do_usuario)
        RETORNAR // NAO cria ledger, NAO gasta chamada, NAO cria pasta

    // Protecao contra crash: fazer backup antes de modificar
    SE ARQUIVO_EXISTE("estado/estado_da_obra.md"):
        COPIAR("estado/estado_da_obra.md", "estado/estado_da_obra.bak")
    SE ARQUIVO_EXISTE("bible/bible_da_obra.md"):
        COPIAR("bible/bible_da_obra.md", "bible/bible_da_obra.bak")

    // Carregar estado e bible
    estado = LER("estado/estado_da_obra.md")
    bible = LER("bible/bible_da_obra.md")
    genero = LER("generos/GENERO_" + estado.genero + ".md")
    corpus = LER_TUDO("corpus/")

    SE estado.eh_vazio:
        // Primeira execucao: inicializar tudo
        estado.criar(tarefa_do_usuario, genero)
        bible.criar_do_corpus(corpus, genero)
        estado.plano = CRIAR_PLANO_CAPITULOS(corpus, genero, estado.foco_usuario, bible)
        SALVAR_ATOMICO("estado/estado_da_obra.md", estado)
        SALVAR_ATOMICO("bible/bible_da_obra.md", bible)

    // FASE 1: Execucao com ciclo MARCH + CONTINUIDADE
    PARA CADA cena EM estado.plano.cenas:
        SE cena.status == "CONCLUIDO":
            CONTINUAR

        // TETO DE RETRIES — maximo 3 tentativas por cena
        cena.retries = cena.retries OU 0
        SE cena.retries >= 3:
            cena.status = "REPROVADO"
            cena.erro_fatal = "Excedeu 3 tentativas de reescrita cirurgica"
            ATUALIZAR_ESTADO_ATOMICO(cena)
            PULAR_PARA_PROXIMA_CENA  // Nao trava o livro inteiro

        worktree = CRIAR_PASTA_ISOLADA(cena.id)  // capitulos/capitulo_NN/

        // ETAPA A: ESCRITOR
        INVOCAR(escritor, {
            cena: cena,
            genero: genero,
            bible: bible,
            estado_anterior: EXTRAIR_CONTEXTO_ANTERIOR(estado, cena),
            foco_usuario: estado.foco_usuario
        }, worktree)
        VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/_saida_escritor.md")
        SE NAO: PARAR("Escritor nao executou. Arquivo _saida_escritor.md nao criado.")
        saida_checksum = CALCULAR_CHECKSUM(f"{worktree}/_saida_escritor.md")
        saida_bytes = TAMANHO_ARQUIVO(f"{worktree}/_saida_escritor.md")

        // ETAPA B: ATOMIZADOR
        INVOCAR(atomizador, {cena: worktree})
        VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/_afirmacoes_para_validar.json")
        SE NAO: PARAR("Atomizador nao executou. Arquivo _afirmacoes_para_validar.json nao criado.")

        // ETAPA C: VALIDADOR MARCH (Fact-check CEGO)
        // ANTES de invocar, registrar o prompt que sera enviado ao Checker
        prompt_checker = MONTAR_PROMPT_CHECKER(cena, worktree)
        SALVAR(f"{worktree}/_log_prompt_checker.md", prompt_checker)

        INVOCAR(validador_march, {cena: worktree, corpus: corpus})
        VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/_resultado_march.json")
        SE NAO: PARAR("Validador MARCH nao executou. Arquivo _resultado_march.json nao criado.")

        resultado_march = LER(f"{worktree}/_resultado_march.json")

        // AUDITORIA: Verificar se o prompt do Checker vazou a saida do Escritor
        log_prompt = LER(f"{worktree}/_log_prompt_checker.md")
        saida_escritor = LER(f"{worktree}/_saida_escritor.md")
        SE log_prompt CONTEM saida_escritor:
            cena.status = "REPROVADO"
            cena.erro_fatal = "VIOLACAO: prompt do Validador MARCH continha a saida do Escritor. Cegueira violada."
            ATUALIZAR_ESTADO_ATOMICO(cena)
            PARAR("Cegueira do Validador MARCH violada. A cena precisa ser refeita com isolamento rigoroso.")

        // ETAPA D: Verificar travas duras MARCH (RECALCULO do orquestrador — NAO confiar no agregado)
        total_local = len(resultado_march.resultados)
        confirmados_local = len([r for r in resultado_march.resultados if r.status == "CONFIRMADO"])
        contraditos_local = len([r for r in resultado_march.resultados if r.status == "CONTRADITO"])
        nao_encontrados_local = len([r for r in resultado_march.resultados if r.status == "NAO_ENCONTRADO"])
        taxa_local = confirmados_local / total_local SE total_local > 0 SENAO 0

        erros_march = []
        SE taxa_local < 0.8:
            erros_march.ADICIONAR(f"Taxa de confirmados {taxa_local:.0%} abaixo de 80% (recalculado pelo orquestrador)")
        SE contraditos_local > 0:
            erros_march.ADICIONAR(f"{contraditos_local} afirmacoes contraditas encontradas")
        SE nao_encontrados_local > total_local * 0.3:
            erros_march.ADICIONAR(f"{nao_encontrados_local} de {total_local} afirmacoes sem lastro (>30%)")

        SE erros_march.NAO_VAZIO:
            cena.status = "REPROVADO_MARCH"
            cena.erros = erros_march
            cena.retries = cena.retries + 1
            ATUALIZAR_ESTADO_ATOMICO(cena)
            INVOCAR(escritor, {cena, worktree, falhas: erros_march, modo: "REESCRITA_CIRURGICA"})
            REPETIR ETAPA A  // Loop de reescrita ate passar MARCH

        // ETAPA E: VALIDADOR CONTINUIDADE (CEGO — ve so Bible + Estado anterior, NAO o texto)
        INVOCAR(validador_continuidade, {
            cena: worktree,
            bible: bible,
            estado_anterior: EXTRAIR_CONTEXTO_ANTERIOR(estado, cena)
        })
        VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/_resultado_continuidade.json")
        SE NAO: PARAR("Validador Continuidade nao executou. Arquivo _resultado_continuidade.json nao criado.")

        resultado_cont = LER(f"{worktree}/_resultado_continuidade.json")

        SE resultado_cont.status_geral != "APROVADO":
            cena.status = "REPROVADO_CONTINUIDADE"
            cena.erros = resultado_cont.erros
            cena.retries = cena.retries + 1
            ATUALIZAR_ESTADO_ATOMICO(cena)
            INVOCAR(escritor, {cena, worktree, falhas: resultado_cont.erros, modo: "REESCRITA_CIRURGICA"})
            REPETIR ETAPA A  // Loop completo: reescrita -> atomizador -> march -> continuidade

        // ETAPA F: EDITOR (OPCIONAL — se genero.exige_editor)
        saida_final = LER(f"{worktree}/_saida_escritor.md")
        SE genero.exige_editor:
            INVOCAR(editor, {cena: worktree, genero: genero, bible: bible})
            VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/_saida_editor.md")
            SE NAO: PARAR("Editor nao executou. Arquivo _saida_editor.md nao criado.")
            saida_final = LER(f"{worktree}/_saida_editor.md")
            // Recalcular checksum apos editor
            saida_checksum = CALCULAR_CHECKSUM(saida_final)
            saida_bytes = TAMANHO_ARQUIVO(saida_final)

        // Salvar saida final referenciada
        SALVAR(f"{worktree}/_saida_final.md", saida_final)

        // ETAPA G: Atualizar Bible + Estado (ATOMICAMENTE)
        bible = ATUALIZAR_BIBLE(bible, saida_final, cena)
        SALVAR_ATOMICO("bible/bible_da_obra.md", bible)

        cena.status = "CONCLUIDO"
        cena.validacao_march = "APROVADO"
        cena.validacao_continuidade = "APROVADO"
        cena.checksum_saida = saida_checksum
        cena.bytes_saida = saida_bytes
        cena.retries = cena.retries
        cena.chamadas_gastas = CALCULAR_CHAMADAS_DA_CENA(cena.id)
        ATUALIZAR_ESTADO_ATOMICO(cena)

        // CHECKSUM ROUND-TRIP: reler do disco e confirmar integridade fisica
        saida_referida = LER(f"{worktree}/_saida_final.md")
        checksum_recalculado = CALCULAR_CHECKSUM(saida_referida)
        SE checksum_recalculado != saida_checksum:
            cena.status = "INCONSISTENTE"
            ATUALIZAR_ESTADO_ATOMICO(cena)
            PARAR("CHECKSUM INCONSISTENTE: o arquivo no disco nao corresponde ao que foi registrado no estado. A cena precisa ser revista.")

    // FASE 2: Consolidacao com validacao de fronteira E validacao cega final
    INVOCAR(consolidador, {plano: estado.plano, estado: estado, output: "livro_final.md"})
```

---

# 1. Checksum e Prova Fisica

Cada cena registra no estado o checksum e o tamanho em bytes do `_saida_final.md`.

**ANTES de avancar para a proxima cena, o orquestrador DEVE:**
1. Reler o arquivo do disco
2. Recalcular o checksum
3. Comparar com o valor registrado no estado

SE os valores nao baterem, a cena e marcada como INCONSISTENTE e travada.

Isso transforma pular etapa em algo que deixa RASTRO DETECTAVEL.

---

# 2. Teto de Retries

Cada cena tem no maximo 3 tentativas de reescrita cirurgica.
Se estourar, a cena e marcada como REPROVADO e o orquestrador segue para a proxima.
**Nunca fica em loop infinito.** O livro continua; a cena problematica e flagada para intervencao humana.

---

# 3. Auditoria do Prompt do Validador MARCH

O prompt montado para o Validador MARCH e salvo em `_log_prompt_checker.md` no worktree.
O orquestrador verifica se esse log NAO contem o conteudo do `_saida_escritor.md`.
Se contiver, a cegueira foi violada e a cena e reprovada.

---

# 4. Recalculo de Agregados MARCH

O orquestrador NAO confia nos campos `taxa_confirmados` e `status_geral` devolvidos pelo Validador MARCH.
Ele percorre o array `resultados[]` manualmente, soma os CONFIRMADO, divide pelo total,
e so aceita se a conta bater.

---

# 5. Salvatagem Atomica

SALVAR_ATOMICO = escrever em arquivo `.tmp` primeiro, depois renomear por cima do original.
Se o processo cair no meio, o `.bak` ou o original ainda estao intactos.

Aplicavel a: `estado/estado_da_obra.md`, `bible/bible_da_obra.md`.

---

# 6. Isolamento por Worktree (Pasta Fisica)

Cada cena = pasta isolada em `capitulos/capitulo_NN/`.
Nada de uma cena contaminar o contexto da outra.
Arquivos de validacao (`_resultado_march.json`, `_resultado_continuidade.json`) ficam DENTRO da pasta da cena.
Bible e Estado sao GLOBAIS (em `/bible/` e `/estado/`).

---

# 7. Regras Absolutas (Atualizadas para Livro)

1. **NUNCA execute tarefas.** Isso e com o Escritor, Atomizador, Validadores, Editor, Consolidador.
2. **NUNCA valide afirmacoes.** Isso e com o Validador MARCH.
3. **NUNCA valide continuidade.** Isso e com o Validador Continuidade.
4. **SEMPRE leia `estado/estado_da_obra.md` e `bible/bible_da_obra.md` antes de comecar.**
5. **SEMPRE faca backup (.bak) antes de modificar estado ou bible.**
6. **SEMPRE recalcule agregados do Validador MARCH. Nao confie no que ele devolveu.**
7. **SEMPRE verifique se o prompt do Validador MARCH vazou a saida do Escritor.**
8. **MAXIMO 3 retries por cena. Depois disso, REPROVADO e segue em frente.**
9. **CHECKSUM e prova fisica: registro + verificacao na leitura.**
10. **VALIDACAO MARCH NAO E OPCIONAL. Sem ela, a cena nao existe.**
11. **VALIDACAO CONTINUIDADE NAO E OPCIONAL. Sem ela, a cena nao existe.**
12. **TOLERANCIA ZERO para afirmacoes contraditas no MARCH.**
13. **TOLERANCIA ZERO para quebrar continuidade (personagens, timeline, conceitos, voz).**
14. **CENA SO VIRA CONCLUIDA SE: MARCH=APROVADO E CONTINUIDADE=APROVADO.**
15. **BIBLE E ESTADO SAO ATUALIZADOS ATOMICAMENTE APOS CADA CENA APROVADA.**

---

# 8. Formato do Estado da Obra (Resumo)

```markdown
# Estado da Obra: [TITULO]

## Metadados
- ultima_atualizacao: ISO8601
- status_geral: EM_ANDAMENTO | CONCLUIDO | INTERROMPIDO
- genero: ROMANCE | NAO_FICCAO | MEMORIAS | TECNICO | PERSONALIZADO
- foco_usuario: "texto livre do usuario"
- capitulos_planejados: N
- capitulos_concluidos: M
- cena_atual: {capitulo: 4, cena: 2}
- chamadas_gastas: 47
- limite_chamadas: 200

## Plano de Cenas (Granular)
| ID  | Cap | Cena | Titulo          | POV           | Status       | MARCH      | Cont       | Retries |
|-----|-----|------|-----------------|---------------|--------------|------------|------------|---------|
| 1.1 | 1   | 1    | Chegada         | Protagonista  | CONCLUIDO    | APROVADO   | APROVADO   | 0       |
| 1.2 | 1   | 2    | O Enigma        | Protagonista  | CONCLUIDO    | APROVADO   | APROVADO   | 0       |
| 1.3 | 1   | 3    | Decisao         | Protagonista  | CONCLUIDO    | APROVADO   | APROVADO   | 1       |
| 2.1 | 2   | 1    | A Estrada       | Protagonista  | ESCREVENDO   | PENDENTE   | PENDENTE   | 0       |
| 2.2 | 2   | 2    | O Encontro      | Aliado        | PENDENTE     | -          | -          | 0       |

## Bible Version
- versao_atual: v3.2
- checksum: a1b2c3d4

## Historico de Retries
| Cena | Tentativa | Validador | Motivo                              | Acao                     |
|------|-----------|-----------|-------------------------------------|--------------------------|
| 1.3  | 1         | MARCH     | 2 afirmacoes contraditas            | Reescrita cirurgica      |
| 1.3  | 2         | CONT      | Personagem em local errado (timeline)| Reescrita cirurgica     |
```

---

# 9. Funcoes Auxiliares do Orquestrador

```
FUNCAO EXTRAIR_CONTEXTO_ANTERIOR(estado, cena_atual):
    // Retorna resumo do capitulo anterior + cena anterior do mesmo capitulo
    // Para o Escritor ter continuidade narrativa
    // Para o Validador Continuidade verificar coerencia
    RETORNAR {
        capitulo_anterior_resumo: estado.ultimo_capitulo_concluido.resumo,
        cena_anterior_resumo: estado.ultima_cena_concluida.resumo,
        bible_checksum_no_momento: estado.ultima_cena_concluida.bible_checksum
    }

FUNCAO ATUALIZAR_BIBLE(bible, saida_final, cena):
    // Extrai da saida_final: novos personagens, locais, eventos, conceitos, fios narrativos
    // Atualiza: personagens, cenarios, cronologia, conceitos, fios_abertos
    // Incrementa versao: v3.2 -> v3.3
    // Recalcula checksum
    RETORNAR bible_atualizada

FUNCAO ATUALIZAR_ESTADO_ATOMICO(cena):
    // Atualiza o estado_da_obra.md com a cena concluida
    // Recalcula totais, status_geral, checkpoint
    // Salva via .tmp -> rename
    SALVAR_ATOMICO("estado/estado_da_obra.md", estado)

FUNCAO CRIAR_PLANO_CAPITULOS(corpus, genero, foco_usuario, bible):
    // Usa a estrutura definida no genero + material do corpus + foco
    // Retorna lista de cenas com: id, capitulo, cena, titulo, pov, tamanho_estimado, objetivo
    RETORNAR plano
```

---

# 10. Gatilhos de Parada Imediata (STOP)

| Condicao | Acao |
|----------|------|
| Prompt do Validador MARCH contem saida do Escritor | PARAR + REPROVADO (cegueira violada) |
| Checksum round-trip falha | PARAR + INCONSISTENTE (arquivo corrompido/alterado) |
| 3 retries excedidos na mesma cena | MARCAR REPROVADO + PULAR PARA PROXIMA |
| Estado ou Bible nao podem ser lidos | PARAR (corrupcao de checkpoint) |
| Corpus nao encontrado | PARAR (input invalido) |
| Genero nao encontrado | PERGUNTAR AO USUARIO (nao parar) |