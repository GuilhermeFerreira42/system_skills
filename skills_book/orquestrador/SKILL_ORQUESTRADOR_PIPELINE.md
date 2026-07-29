# SKILL DO ORQUESTRADOR (PIPELINE GENÉRICO) — Pseudocódigo Completo

**Versão:** 3.0
**Função:** Coordenar o fluxo completo de produção cena a cena, com validação dupla cega, atualização atômica, checksum e round-trip.

---

## PSEUDOCÓDIGO OPERACIONAL COMPLETO

```
FUNCAO orquestrar_livro():
    # PASSO ZERO: Backup antes de modificar
    SE ARQUIVO_EXISTE("execucao/estado/estado_da_obra.md"):
        COPIAR("execucao/estado/estado_da_obra.md", "execucao/estado/estado_da_obra.bak")
    SE ARQUIVO_EXISTE("execucao/bible/bible_da_obra.md"):
        COPIAR("execucao/bible/bible_da_obra.md", "execucao/bible/bible_da_obra.bak")
    
    # Carregar contexto
    config = LER("execucao/CONFIG.md")
    genero = LER("execucao/GENERO.md")
    corpus = LER_TUDO("execucao/corpus/")
    estado = LER("execucao/estado/estado_da_obra.md")
    bible = LER("execucao/bible/bible_da_obra.md")
    
    # Validar GENERO.md (não pode ter "[definir]")
    SE GENERO_TEM_CAMPOS_VAZIOS(genero):
        PARAR("GENERO.md tem campos não preenchidos. Peça ao usuário completar.")
    
    # Inicialização (se estado vazio)
    SE estado.eh_vazio:
        estado.criar(config, genero)
        bible.criar_do_corpus(corpus, genero)
        estado.plano = CRIAR_PLANO_CAPITULOS(corpus, genero, config.foco_usuario, bible)
        SALVAR_ATOMICO("execucao/estado/estado_da_obra.md", estado)
        SALVAR_ATOMICO("execucao/bible/bible_da_obra.md", bible)
    
    # LOOP POR CENA
    PARA CADA cena EM estado.plano.cenas:
        SE cena.status == "CONCLUIDO":
            CONTINUAR
        
        # Teto de retries
        cena.retries = cena.retries OU 0
        SE cena.retries >= 3:
            cena.status = "REPROVADO"
            cena.erro_fatal = "Excedeu 3 tentativas"
            ATUALIZAR_ESTADO_ATOMICO(cena)
            CONTINUAR
        
        worktree = f"execucao/capitulos/capitulo_{cena.capitulo:02d}/cena_{cena.cena:02d}/"
        os.makedirs(worktree, exist_ok=True)
        
        # ETAPA A: ESCRITOR
        INVOCAR(escritor, {
            cena: cena,
            genero: genero,
            bible: bible,
            contexto_anterior: EXTRAIR_CONTEXTO_ANTERIOR(estado, cena),
            foco_usuario: config.foco_usuario
        }, worktree)
        VERIFICAR(f"{worktree}/_saida_escritor.md")
        SE NAO EXISTE:
            PARAR("Escritor não executou")
        
        # ETAPA B: ATOMIZADOR
        INVOCAR(atomizador, {cena: worktree, genero: genero})
        # Se Ficção pura, atomizador pode produzir array vazio — ok
        
        # ETAPA C: LOG DO PROMPT DO VALIDADOR
        prompt_checker = MONTAR_PROMPT_CHECKER(cena, worktree, corpus)
        SALVAR(f"{worktree}/_log_prompt_checker.md", prompt_checker)
        
        # ETAPA D: VALIDADOR MARCH (cego)
        INVOCAR(validador_march, {cena: worktree, corpus: corpus})
        VERIFICAR(f"{worktree}/_resultado_march.json")
        SE NAO EXISTE:
            PARAR("Validador MARCH não executou")
        
        # ETAPA E: AUDITORIA DE CEGUEIRA
        log_prompt = LER(f"{worktree}/_log_prompt_checker.md")
        prosa = LER(f"{worktree}/_saida_escritor.md")
        SE prosa in log_prompt:
            cena.status = "REPROVADO"
            cena.erro_fatal = "VIOLAÇÃO DE CEGUEIRA"
            ATUALIZAR_ESTADO_ATOMICO(cena)
            PARAR("Cegueira violada")
        
        # ETAPA F: RECALCULAR AGREGADOS MARCH
        resultado_march = LER(f"{worktree}/_resultado_march.json")
        resultados = resultado_march.resultados
        total = len(resultados)
        confirmados = sum(1 for r in resultados if r["status"] == "CONFIRMADO")
        contraditos = sum(1 for r in resultados if r["status"] == "CONTRADITO")
        nao_encontrados = sum(1 for r in resultados if r["status"] == "NAO_ENCONTRADO")
        taxa = confirmados / total if total > 0 else 0
        
        erros_march = []
        SE contraditos > 0:
            erros_march.ADICIONAR(f"{contraditos} afirmações CONTRADITAS")
        SE taxa < 0.80:
            erros_march.ADICIONAR(f"Taxa {taxa:.0%} abaixo de 80%")
        SE nao_encontrados > total * 0.30:
            erros_march.ADICIONAR(f"{nao_encontrados}/{total} sem lastro (>30%)")
        
        SE erros_march NAO vazio:
            cena.status = "REPROVADO_MARCH"
            cena.erros = erros_march
            cena.retries = cena.retries + 1
            ATUALIZAR_ESTADO_ATOMICO(cena)
            INVOCAR(escritor, {cena, worktree, falhas: erros_march, modo: "REESCRITA_CIRURGICA"})
            CONTINUAR
        
        # ETAPA G: GERAR PERGUNTAS DE CONTINUIDADE
        perguntas_cont = GERAR_PERGUNTAS_CONTINUIDADE(worktree, genero, bible, estado)
        SALVAR(f"{worktree}/_perguntas_continuidade.json", perguntas_cont)
        
        # ETAPA H: VALIDADOR CONTINUIDADE (cego)
        INVOCAR(validador_continuidade, {
            cena: worktree,
            genero: genero,
            bible: bible,
            estado_anterior: EXTRAIR_CONTEXTO_ANTERIOR(estado, cena)
        })
        VERIFICAR(f"{worktree}/_resultado_continuidade.json")
        SE NAO EXISTE:
            PARAR("Validador Continuidade não executou")
        
        resultado_cont = LER(f"{worktree}/_resultado_continuidade.json")
        SE resultado_cont.status_geral != "APROVADO":
            cena.status = "REPROVADO_CONTINUIDADE"
            cena.erros = resultado_cont.erros
            cena.retries = cena.retries + 1
            ATUALIZAR_ESTADO_ATOMICO(cena)
            INVOCAR(escritor, {cena, worktree, falhas: resultado_cont.erros, modo: "REESCRITA_CIRURGICA"})
            CONTINUAR
        
        # ETAPA I: EDITOR
        INVOCAR(editor, {cena: worktree, genero: genero, bible: bible})
        VERIFICAR(f"{worktree}/_saida_editor.md")
        SE NAO EXISTE:
            PARAR("Editor não executou")
        
        # ETAPA J: COPIAR PARA _saida_final.md
        shutil.copy(f"{worktree}/_saida_editor.md", f"{worktree}/_saida_final.md")
        
        # ETAPA K: CHECKSUM
        with open(f"{worktree}/_saida_final.md", "rb") as f:
            conteudo = f.read()
        checksum = hashlib.sha256(conteudo).hexdigest()[:8]
        bytes_size = len(conteudo)
        
        # ETAPA L: ATUALIZAR BIBLE
        bible = ATUALIZAR_BIBLE(bible, worktree, cena)
        bible.versao = INCREMENTAR_VERSAO(bible.versao)
        SALVAR_ATOMICO("execucao/bible/bible_da_obra.md", bible)
        
        # ETAPA M: ATUALIZAR ESTADO
        cena.status = "CONCLUIDO"
        cena.validacao_march = "APROVADO"
        cena.validacao_continuidade = "APROVADO"
        cena.checksum_saida = checksum
        cena.bytes_saida = bytes_size
        cena.retries = cena.retries
        ATUALIZAR_ESTADO_ATOMICO(cena)
        
        # ETAPA N: ROUND-TRIP CHECK
        with open(f"{worktree}/_saida_final.md", "rb") as f:
            conteudo_re_lido = f.read()
        checksum_re_lido = hashlib.sha256(conteudo_re_lido).hexdigest()[:8]
        SE checksum_re_lido != checksum:
            cena.status = "INCONSISTENTE"
            ATUALIZAR_ESTADO_ATOMICO(cena)
            PARAR("Checksum mismatch")
    
    # FIM DO LOOP
    
    # CONSOLIDAÇÃO
    INVOCAR(consolidador, {plano: estado.plano, estado: estado, genero: genero, saida: "execucao/livro_final.md"})
    
    estado.status_geral = "CONCLUIDO"
    SALVAR_ATOMICO("execucao/estado/estado_da_obra.md", estado)
```

---

## 1. Checksum e Prova Física

Cada cena registra no Estado o checksum (8 primeiros chars SHA256) e o tamanho em bytes do `_saida_final.md`.

**ANTES** de avançar para a próxima cena, o Orquestrador DEVE:
1. Reler o arquivo do disco
2. Recalcular o checksum
3. Comparar com o valor registrado no Estado

---

## 2. Teto de Retries

Cada cena tem no máximo **3 tentativas** de reescrita cirúrgica.
Se estourar, a cena é marcada como `REPROVADO` e o Orquestrador segue para a próxima.

---

## 3. Auditoria do Prompt do Validador MARCH

O prompt montado para o Validador MARCH é salvo em `_log_prompt_checker.md` no worktree.
O Orquestrador verifica se esse log **NÃO contém** o conteúdo do `_saida_escritor.md`.
Se contiver, a cegueira foi violada e a cena é reprovada.

---

## 4. Recálculo de Agregados MARCH

O Orquestrador **NÃO confia** nos campos `taxa_confirmados` e `status_geral` devolvidos pelo Validador MARCH.
Ele percorre o array `resultados[]` manualmente, conta CONFIRMADO, divide pelo total, e só aceita se a conta bater.

---

## 5. Salvamento Atômico

`SALVAR_ATOMICO = escrever em arquivo .tmp primeiro, depois renomear por cima do original.`
Se o processo cair no meio, o `.bak` ou o original ainda estão intactos.

---

## 6. Isolamento por Worktree

Cada cena = pasta isolada em `execucao/capitulos/capitulo_NN/cena_MM/`.
Nada de uma cena contaminar o contexto da outra.
Bible e Estado são GLOBAIS (em `execucao/bible/` e `execucao/estado/`), atualizados atomicamente.

---

## 7. Regras Absolutas

1. NUNCA execute tarefas. Isso é com Escritor, Atomizador, Validadores, Editor, Consolidador.
2. NUNCA valide afirmações. Isso é com o Validador MARCH.
3. NUNCA valide continuidade diretamente (você extrai perguntas, mas o veredito é do Validador).
4. SEMPRE leia `estado/estado_da_obra.md` e `bible/bible_da_obra.md` antes de começar.
5. SEMPRE faça backup (.bak) antes de modificar estado ou bible.
6. SEMPRE recalcule agregados do Validador MARCH.
7. SEMPRE verifique se o prompt do Validador MARCH vazou a saída do Escritor.
8. MÁXIMO 3 retries por cena.
9. CHECKSUM e prova física: registro + verificação.
10. VALIDAÇÃO MARCH não é opcional.
11. VALIDAÇÃO CONTINUIDADE não é opcional.
12. TOLERÂNCIA ZERO para afirmações contraditas no MARCH.
13. TOLERÂNCIA ZERO para quebrar continuidade.
14. CENA SÓ VIRA CONCLUÍDA SE: MARCH=APROVADO E CONTINUIDADE=APROVADO.
15. BIBLE E ESTADO SÃO ATUALIZADOS ATOMICAMENTE.
16. LEI 6 (MATERIAL DE MARKETING): zero no livro.
17. SEMPRE leia o GENERO.md — valores hardcoded nas skills são bugs.

---

## 8. Formato do Estado da Obra (Resumo)

```markdown
# Estado da Obra: [TITULO]

## Metadados
- ultima_atualizacao: ISO8601
- status_geral: EM_ANDAMENTO | CONCLUIDO | INTERROMPIDO
- genero: [do GENERO.md]
- foco_usuario: "[do CONFIG.md]"
- capitulos_planejados: N
- capitulos_concluidos: M
- cena_atual: {capitulo: X, cena: Y}
- chamadas_gastas: N
- limite_chamadas: N
- bible_versao: v[major].[minor]
- bible_checksum: 8chars

## Plano de Cenas
| ID | Cap | Cena | Titulo | POV | Palavras Est | Status | MARCH | Cont | Retries | Objetivo |
|...

## Pendências
- ...

## Histórico de Retries
| Cena | Tentativa | Validador | Motivo | Acao |
|...

## Foco do Usuario
> "..."

## Checkpoint de Retomada
- Capitulo: X
- Cena: Y
- Status: PENDENTE | ESCREVENDO | REVISAO_MARCH | REVISAO_CONT
- Proxima acao: ...
- Bible versao: vX.Y
- Estado checksum: 8chars
```

---

## 9. Gatilhos de Parada Imediata (STOP)

| Condição | Ação |
|---|---|
| Prompt MARCH contem prosa do Escritor | PARAR + REPROVADO (cegueira) |
| Checksum round-trip falha | PARAR + INCONSISTENTE |
| 3 retries excedidos | MARCAR REPROVADO + PULAR |
| Estado ou Bible ilegíveis | PARAR |
| Corpus não encontrado | PARAR |
| Gênero não encontrado ou com campos vazios | PARAR (peça ao usuário) |
| Validação de Fronteira falha no Consolidador | PARAR |
| Auto-auditoria Lei 6 detecta marketing | PARAR + LIMPAR |
