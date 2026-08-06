# SKILL DO ORQUESTRADOR MESTRE DE LIVRO

**Versao:** 1.0 (Greenforged Edition)
**Funcao:** Gerenciar o fluxo completo de orquestracao de escrita de livro, invocando agentes especializados em ordem.
**NUNCA executa tarefas.** Apenas coordena.

---

# PSEUDOCODIGO OPERACIONAL (FLUXO OBRIGATORIO — RECEITA DE BOLO)

```
// Importacao das constantes centralizadas (ver utils/constantes.py)
DE utils.constantes IMPORTAR (
    SAIDA_ESCRITOR_ARQ,
    SAIDA_EDITOR_ARQ,
    SAIDA_FINAL_ARQ,
    METADADOS_CENA_ARQ,
    AFIRMACOES_PARA_VALIDAR_ARQ,
    PERGUNTAS_VALIDADOR_ARQ,
    PERGUNTAS_CONTINUIDADE_ARQ,
    RESULTADO_MARCH_ARQ,
    RESULTADO_CONTINUIDADE_ARQ,
    RESULTADO_REVISOR_CEGO_ARQ,
    LOG_PROMPT_CHECKER_ARQ,
    BIBLE_DA_OBRA_ARQ,
    ESTADO_DA_OBRA_ARQ,
    PASTA_BIBLE,
    PASTA_ESTADO,
    PASTA_GENEROS,
    PASTA_CAPITULOS,
    VALIDACAO_APROVADO,
    VALIDACAO_REPROVADO,
    STATUS_CENA_CONCLUIDO,
    STATUS_CENA_REPROVADO,
    STATUS_CENA_INCONSISTENTE,
    STATUS_CENA_REPROVADO_MARCH,
    STATUS_CENA_REPROVADO_CONTINUIDADE,
    STATUS_CENA_REPROVADO_REVISOR,
    MARCH_TAXA_CONFIRMACAO_MINIMA,
    MARCH_TAXA_NAO_ENCONTRADO_MAXIMA,
    MARCH_TOLERANCIA_CONTRADITO,
    MARCH_CONFIRMADO,
    MARCH_CONTRADITO,
    MARCH_NAO_ENCONTRADO,
    MAX_RETRIES_POR_CENA,
    ERRO_CHECKSUM_INCONSISTENTE,
    ERRO_CEGUEIRA_VIOLADA_MARCH,
    ERRO_RETRIES_EXCEDIDOS,
    ERRO_ARQUIVO_NAO_ENCONTRADO,
    GENERO_TECNICO,
    GENEROS_BASE_VALIDOS,
    REVISAO_CRITERIOS_PADRAO,
    caminho_bible,
    caminho_estado,
    caminho_capitulos,
    caminho_capitulo,
    caminho_cena,
    caminho_arquivo_cena,
    caminho_tmp,
    caminho_backup
)

FUNCAO orquestrar_livro(tarefa_do_usuario):
    // PASSO ZERO: ROTEADOR DE INTENCAO
    intencao = CLASSIFICAR_INTENCAO(tarefa_do_usuario)
    // "TAREFA" ou "CONVERSA"
    SE intencao == "CONVERSA":
        RESPONDER_DIRETO(tarefa_do_usuario)
        RETORNAR // NAO cria ledger, NAO gasta chamada, NAO cria pasta

    // Protecao contra crash: fazer backup antes de modificar
    SE ARQUIVO_EXISTE(caminho_estado(projeto_path)):
        COPIAR(caminho_estado(projeto_path), caminho_backup(caminho_estado(projeto_path)))
    SE ARQUIVO_EXISTE(caminho_bible(projeto_path)):
        COPIAR(caminho_bible(projeto_path), caminho_backup(caminho_bible(projeto_path)))

    // Carregar estado e bible
    estado = LER(caminho_estado(projeto_path))
    bible = LER(caminho_bible(projeto_path))
    genero = LER(f"{PASTA_GENEROS}/GENERO_" + estado.genero + ".md")

    // Carregar corpus: detecta se e modular (corpus/README.md presente)
    // ou monolitico (corpus_novo.md). Em ambos os casos, o corpus
    // completo fica disponivel em disco, mas o pipeline so carrega o
    // modulo relevante por cena (ver funcao EXTRAIR_CORPUS_PARA_CENA).
    SE ARQUIVO_EXISTE(f"{projeto_path}/{PASTA_CORPUS}/corpus_README.md OU corpus/index.md"):
        // CORPUS MODULAR: corpus estruturado em pastas por tema
        corpus = CARREGAR_CORPUS_MODULAR(f"{projeto_path}/{PASTA_CORPUS}/")
        corpus.tipo = "MODULAR"
    SENAO:
        // CORPUS MONOLITICO: arquivo unico
        corpus = LER(f"{projeto_path}/corpus_novo.md")
        corpus.tipo = "MONOLITICO"

    SE estado.eh_vazio:
        // Primeira execucao: inicializar tudo
        estado.criar(tarefa_do_usuario, genero)
        bible.criar_do_corpus(corpus, genero)
        estado.plano = CRIAR_PLANO_CAPITULOS(corpus, genero, estado.foco_usuario, bible)
        // Se o corpus for modular, o mapa_corpus_capitulos ja foi extraido
        // no Passo 4 e salvo na Bible. O Orquestrador usa ele abaixo.
        SALVAR_ATOMICO(caminho_estado(projeto_path), estado)
        SALVAR_ATOMICO(caminho_bible(projeto_path), bible)

    // FASE 1: Execucao com ciclo MARCH + CONTINUIDADE
    PARA CADA cena EM estado.plano.cenas:
        SE cena.status == "CONCLUIDO":
            CONTINUAR

        // TETO DE RETRIES — maximo 3 tentativas por cena
        cena.retries = cena.retries OU 0
        SE cena.retries >= MAX_RETRIES_POR_CENA:
            cena.status = STATUS_CENA_REPROVADO
            cena.erro_fatal = ERRO_RETRIES_EXCEDIDOS
            ATUALIZAR_ESTADO_ATOMICO(cena)
            PULAR_PARA_PROXIMA_CENA  // Nao trava o livro inteiro

        worktree = CRIAR_PASTA_ISOLADA(cena.id)  // capitulos/capitulo_NN/cena_MM/ (subpasta por cena!)

        // EXTRAIR CORPUS ESPECIFICO DESTA CENA (modular OU monolitico)
        // Se o corpus e modular, esta funcao retorna so o modulo do mapa_corpus_capitulos
        // que contem os arquivos relevantes. Se e monolitico, retorna o corpus inteiro
        // (custo maior, mas funciona). Ver funcao EXTRAIR_CORPUS_PARA_CENA no final.
        corpus_cena = EXTRAIR_CORPUS_PARA_CENA(cena, corpus, bible)
        // corpus_cena tem o mesmo formato de corpus (MODULAR com subset, ou MONOLITICO completo)
        // Esse corpus_cena e o que vai ser passado pro Escritor, Atomizador, e MARCH

        // ETAPA A: ESCRITOR
        INVOCAR(escritor, {
            cena: cena,
            genero: genero,
            bible: bible,
            estado_anterior: EXTRAIR_CONTEXTO_ANTERIOR(estado, cena),
            foco_usuario: estado.foco_usuario,
            corpus: corpus_cena
        }, worktree)
        VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/{SAIDA_ESCRITOR_ARQ}")
        SE NAO: PARAR(f"Escritor nao executou. Arquivo {SAIDA_ESCRITOR_ARQ} nao criado.")
        saida_checksum = CALCULAR_CHECKSUM(f"{worktree}/{SAIDA_ESCRITOR_ARQ}")
        saida_bytes = TAMANHO_ARQUIVO(f"{worktree}/{SAIDA_ESCRITOR_ARQ}")

        // ETAPA B: ATOMIZADOR
        INVOCAR(atomizador, {cena: worktree})
        VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/{AFIRMACOES_PARA_VALIDAR_ARQ}")
        SE NAO: PARAR(f"Atomizador nao executou. Arquivo {AFIRMACOES_PARA_VALIDAR_ARQ} nao criado.")

        // ETAPA C: VALIDADOR MARCH (Fact-check CEGO)
        // ANTES de invocar, registrar o prompt que sera enviado ao Checker
        prompt_checker = MONTAR_PROMPT_CHECKER(cena, worktree)
        SALVAR(f"{worktree}/{LOG_PROMPT_CHECKER_ARQ}", prompt_checker)

        INVOCAR(validador_march, {cena: worktree, corpus: corpus})
        VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/{RESULTADO_MARCH_ARQ}")
        SE NAO: PARAR(f"Validador MARCH nao executou. Arquivo {RESULTADO_MARCH_ARQ} nao criado.")

        resultado_march = LER(f"{worktree}/{RESULTADO_MARCH_ARQ}")

        // AUDITORIA: Verificar se o prompt do Checker vazou a saida do Escritor
        log_prompt = LER(f"{worktree}/{LOG_PROMPT_CHECKER_ARQ}")
        saida_escritor = LER(f"{worktree}/{SAIDA_ESCRITOR_ARQ}")
        SE log_prompt CONTEM saida_escritor:
            cena.status = STATUS_CENA_REPROVADO
            cena.erro_fatal = ERRO_CEGUEIRA_VIOLADA_MARCH
            ATUALIZAR_ESTADO_ATOMICO(cena)
            PARAR("Cegueira do Validador MARCH violada. A cena precisa ser refeita com isolamento rigoroso.")

        // ETAPA D: Verificar travas duras MARCH (RECALCULO do orquestrador — NAO confiar no agregado)
        total_local = len(resultado_march.resultados)
        confirmados_local = len([r for r in resultado_march.resultados if r.status == MARCH_CONFIRMADO])
        contraditos_local = len([r for r in resultado_march.resultados if r.status == MARCH_CONTRADITO])
        nao_encontrados_local = len([r for r in resultado_march.resultados if r.status == MARCH_NAO_ENCONTRADO])
        taxa_local = confirmados_local / total_local SE total_local > 0 SENAO 0

        erros_march = []
        SE taxa_local < MARCH_TAXA_CONFIRMACAO_MINIMA:
            erros_march.ADICIONAR(f"Taxa de confirmados {taxa_local:.0%} abaixo de {MARCH_TAXA_CONFIRMACAO_MINIMA:.0%} (recalculado pelo orquestrador)")
        SE contraditos_local > MARCH_TOLERANCIA_CONTRADITO:
            erros_march.ADICIONAR(f"{contraditos_local} afirmacoes contraditas encontradas")
        SE nao_encontrados_local > total_local * MARCH_TAXA_NAO_ENCONTRADO_MAXIMA:
            erros_march.ADICIONAR(f"{nao_encontrados_local} de {total_local} afirmacoes sem lastro (>{MARCH_TAXA_NAO_ENCONTRADO_MAXIMA:.0%})")

        SE erros_march.NAO_VAZIO:
            cena.status = STATUS_CENA_REPROVADO_MARCH
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
        VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/{RESULTADO_CONTINUIDADE_ARQ}")
        SE NAO: PARAR(f"Validador Continuidade nao executou. Arquivo {RESULTADO_CONTINUIDADE_ARQ} nao criado.")

        resultado_cont = LER(f"{worktree}/{RESULTADO_CONTINUIDADE_ARQ}")

        SE resultado_cont.status_geral != VALIDACAO_APROVADO:
            cena.status = STATUS_CENA_REPROVADO_CONTINUIDADE
            cena.erros = resultado_cont.erros
            cena.retries = cena.retries + 1
            ATUALIZAR_ESTADO_ATOMICO(cena)
            INVOCAR(escritor, {cena, worktree, falhas: resultado_cont.erros, modo: "REESCRITA_CIRURGICA"})
            REPETIR ETAPA A  // Loop completo: reescrita -> atomizador -> march -> continuidade

        // ETAPA F: EDITOR (OPCIONAL — se genero.exige_editor)
        saida_final = LER(f"{worktree}/{SAIDA_ESCRITOR_ARQ}")
        SE genero.exige_editor:
            INVOCAR(editor, {cena: worktree, genero: genero, bible: bible})
            VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/{SAIDA_EDITOR_ARQ}")
            SE NAO: PARAR(f"Editor nao executou. Arquivo {SAIDA_EDITOR_ARQ} nao criado.")
            saida_final = LER(f"{worktree}/{SAIDA_EDITOR_ARQ}")
            // Recalcular checksum apos editor
            saida_checksum = CALCULAR_CHECKSUM(saida_final)
            saida_bytes = TAMANHO_ARQUIVO(saida_final)

        // Salvar saida final referenciada
        SALVAR(f"{worktree}/{SAIDA_FINAL_ARQ}", saida_final)

        // ETAPA F.5: REVISOR CEGO EDITORIAL (Acao 4 — OPCIONAL, genero-gated)
        // Roda depois do Editor (se houve) ou do Escritor. So pra generos narrativos.
        // Pula pra TECNICO, capitulos 1-3, e cenas < 500 palavras.
        SE DEVE_INVOCAR_REVISOR_CEGO(genero, cena, len(saida_final)):
            INVOCAR(revisor_cego_editorial, {cena: worktree, criterios: genero.criterios_revisor OU REVISAO_CRITERIOS_PADRAO})
            VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/{RESULTADO_REVISOR_CEGO_ARQ}")
            SE NAO: PARAR(f"Revisor Cego nao executou. Arquivo {RESULTADO_REVISOR_CEGO_ARQ} nao criado.")

            resultado_revisor = LER(f"{worktree}/{RESULTADO_REVISOR_CEGO_ARQ}")

            SE resultado_revisor.status_geral != VALIDACAO_APROVADO:
                cena.status = STATUS_CENA_REPROVADO_REVISOR
                cena.erros = resultado_revisor.problemas_alta + resultado_revisor.problemas_media
                cena.retries = cena.retries + 1
                ATUALIZAR_ESTADO_ATOMICO(cena)
                INVOCAR(escritor, {cena, worktree, falhas: cena.erros, modo: "REESCRITA_CIRURGICA"})
                REPETIR ETAPA A  // Loop: reescrita -> atomizador -> march -> continuidade -> editor -> revisor

        // ETAPA G: Atualizar Bible + Estado (ATOMICAMENTE)
        bible = ATUALIZAR_BIBLE(bible, saida_final, cena)
        SALVAR_ATOMICO(caminho_bible(projeto_path), bible)

        cena.status = STATUS_CENA_CONCLUIDO
        cena.validacao_march = VALIDACAO_APROVADO
        cena.validacao_continuidade = VALIDACAO_APROVADO
        cena.validacao_revisor_cego = resultado_revisor.status_geral SE resultado_revisor EXISTE SENAO "PULADO"
        cena.checksum_saida = saida_checksum
        cena.bytes_saida = saida_bytes
        cena.retries = cena.retries
        cena.chamadas_gastas = CALCULAR_CHAMADAS_DA_CENA(cena.id)
        ATUALIZAR_ESTADO_ATOMICO(cena)

        // CHECKSUM ROUND-TRIP: reler do disco e confirmar integridade fisica
        saida_referida = LER(f"{worktree}/{SAIDA_FINAL_ARQ}")
        checksum_recalculado = CALCULAR_CHECKSUM(saida_referida)
        SE checksum_recalculado != saida_checksum:
            cena.status = STATUS_CENA_INCONSISTENTE
            ATUALIZAR_ESTADO_ATOMICO(cena)
            PARAR(ERRO_CHECKSUM_INCONSISTENTE)

    // FASE 2: Consolidacao com validacao de fronteira E validacao cega final
    INVOCAR(consolidador, {plano: estado.plano, estado: estado, output: LIVRO_FINAL_ARQ})
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
    SALVAR_ATOMICO(caminho_estado(projeto_path), estado)

FUNCAO CRIAR_PLANO_CAPITULOS(corpus, genero, foco_usuario, bible):
    // Usa a estrutura definida no genero + material do corpus + foco
    // Retorna lista de cenas com: id, capitulo, cena, titulo, pov, tamanho_estimado, objetivo
    // Se corpus e MODULAR, o plano leva em conta o mapa_corpus_capitulos
    // pra agrupar cenas que usam o mesmo modulo de corpus
    RETORNAR plano

FUNCAO EXTRAIR_CORPUS_PARA_CENA(cena, corpus, bible):
    // Decide qual parte do corpus passar pro pipeline desta cena.
    // Dois casos: corpus MODULAR (pastas por tema) ou MONOLITICO (arquivo unico).

    SE corpus.tipo == "MONOLITICO":
        // Corpus pequeno e coeso, retorna o arquivo inteiro
        RETORNAR corpus

    SE corpus.tipo == "MODULAR":
        // Corpus dividido em pastas por tema.
        // Consulta o mapa_corpus_capitulos da Bible pra saber qual(is) modulo(s)
        // alimenta(m) o capitulo desta cena.
        mapa = bible.mapa_corpus_capitulos  // {capitulo_id: [lista_de_modulos]}
        // Se a cena nao tem mapeamento explicito, tenta inferir por palavras-chave
        // do titulo da cena vs titulos dos modulos (fuzzy match simples).
        modulos_relevantes = mapa.get(cena.capitulo, INFERIR_MODULOS(cena, corpus))

        // Constroi um corpus_cena com apenas os arquivos dos modulos relevantes
        corpus_cena = {tipo: "MODULAR", arquivos: []}
        PARA CADA modulo EM modulos_relevantes:
            PARA CADA arquivo EM corpus.modulos[modulo].arquivos:
                corpus_cena.arquivos.ADICIONAR(arquivo)

        // Registra no log qual subset foi usado (auditoria)
        LOG("Cena {cena.id} usou corpus: {modulos_relevantes}")
        RETORNAR corpus_cena

    // Fallback: se o tipo nao foi detectado, retorna corpus inteiro (modo seguro)
    RETORNAR corpus

FUNCAO INFERIR_MODULOS(cena, corpus):
    // Inferencia de fallback quando o mapa_corpus_capitulos nao cobre a cena.
    // Faz match simples: se o titulo da cena menciona palavra do titulo do modulo,
    // esse modulo e considerado relevante.
    modulos_match = []
    titulo_cena_normalizado = normalizar(cena.titulo)
    PARA CADA modulo EM corpus.modulos:
        titulo_modulo_normalizado = normalizar(modulo.titulo)
        SE tem_palavra_em_comum(titulo_cena_normalizado, titulo_modulo_normalizado):
            modulos_match.ADICIONAR(modulo.id)
    SE modulos_match.VAZIO:
        // Se nao achou nada, retorna o primeiro modulo como fallback
        // (ainda melhor que o corpus inteiro)
        modulos_match.ADICIONAR(corpus.modulos[0].id)
    RETORNAR modulos_match

FUNCAO DEVE_INVOCAR_REVISOR_CEGO(genero, cena, n_palavras):
    // Decide se o Revisor Cego deve rodar pra essa cena.
    // Regra padrao: sim pra generos narrativos, nao pra TECNICO.
    // Pula tambem capitulos 1-3 e cenas curtas.

    // 1. Genero TECNICO: nunca invoca (clareza tecnica e do Editor)
    SE genero.id == GENERO_TECNICO:
        RETORNAR FALSO

    // 2. Cenas curtas (< 500 palavras): pula por performance
    SE n_palavras < 500:
        RETORNAR FALSO

    // 3. Capitulos 1-3: aceita mais ambiguidade, pula
    SE cena.capitulo <= 3:
        RETORNAR FALSO

    // 4. Genero narrativo (ROMANCE, NAO_FICCAO, MEMORIAS, PERSONALIZADO): sempre invoca
    SE genero.id EM GENEROS_BASE_VALIDOS:
        RETORNAR VERDADEIRO

    // 5. Fallback: se nao reconheceu o genero, pergunta ao usuario
    PERGUNTAR_USUARIO("Invocar Revisor Cego Editorial pra esta cena? (recomendado sim)")
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