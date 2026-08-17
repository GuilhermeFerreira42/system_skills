# BOOT DO ORQUESTRADOR DE LIVRO

## Instrucoes de Inicializacao

---

# Passo 1 — Identifique o Projeto

Leia a pasta do projeto fornecida pelo usuario.

Identifique:
- **Corpus** (arquivo(s) em `corpus/` — leia TUDO)
- **Genero** (arquivo `generos/GENERO_*.md` — carregue em runtime)
- **Bible** (leia `bible/bible_da_obra.md` se existir, senão crie)
- **Estado** (leia `estado/estado_da_obra.md` se existir, senão crie vazio)
- **Foco do usuario** (fornecido pelo usuario, similar ao NotebookLM)

Se nao houver arquivo de genero, pergunte ao usuario qual genero deseja (liste os disponiveis em `generos/`).

---

# Passo 2 — Carregue o Estado Anterior

Procure por `estado/estado_da_obra.md` na pasta do projeto.

**SE existir:**
- Leia o estado completo
- Identifique o ultimo capitulo CONCLUIDO
- Identifique o capitulo atual (ESCREVENDO ou PENDENTE)
- Continue EXATAMENTE de onde parou (mesma cena, mesmo capitulo)

**SE nao existir:**
- Crie estado vazio com estrutura do template
- Inicie do capitulo 1, cena 1

---

# Passo 3 — Consulte o Usuario (Formato, Genero, Foco)

## 3.1 Selecione o Genero

Pergunte ao usuario (se nao veio no input):

```
Qual o genero do livro?

1. Romance (ficcao literaria, comercial, genero)
2. Nao-Ficcao (educativo, business, ciencia popular, biografia)
3. Memorias / Autobiografia
4. Tecnico / Manual / How-to
5. Personalizado — voce descreve a estrutura e voz
```

## 3.2 Capture o Foco do Usuario

Pergunte ao usuario:

```
Em quais aspectos o narrador deve se concentrar neste livro?
(Texto livre. Ex: 'Foque na tensao psicologica do protagonista. 
Evite descricoes longas de cenario. O leitor deve sentir a paranoia 
crescente a cada capitulo. Priorize dialogos rapidos e acao interna.')

Registre a resposta no campo `foco_usuario` do estado e passe para o Escritor.
```

## 3.3 Carregue o Genero

Conforme a escolha, carregue o arquivo da pasta `generos/`:
- Romance -> `generos/GENERO_ROMANCE.md`
- Nao-Ficcao -> `generos/GENERO_NAO_FICCAO.md`
- Memorias -> `generos/GENERO_MEMORIAS.md`
- Tecnico -> `generos/GENERO_TECNICO.md`
- Personalizado -> crie `generos/GENERO_PERSONALIZADO.md` com a descricao do usuario

**O genero define:**
- Estrutura narrativa (capitulos, cenas, atos)
- Voz narrativa (1a/3a pessoa, onisciente, limitado, multi-POV)
- Tom, pacing, show vs tell, densidade de dialogo
- Validacoes extras (exige Editor? quais regras?)

---

# Passo 4 — Analise o Corpus e Crie/Atualize a Bible

Leia TODO o corpus fornecido. Identifique:
- Temas centrais
- Personagens (se ficcao) / Conceitos (se nao-ficcao)
- Estrutura narrativa sugerida pelo material
- Arcos, conflitos, questoes centrais
- Evidencias, dados, citacoes (para MARCH)

**SE Bible nao existe:** Crie `bible/bible_da_obra.md` usando o template.
**SE Bible existe:** Atualize com novas informacoes do corpus (personagens novos, locais, cronologia).

---

# Passo 5 — Crie/Atualize o Plano de Capítulos

**SE `estado.plano_nao_criado` OU usuario pediu novo plano:**

Gere um plano de capitulos baseado em:
- Genero (estrutura padrao do genero)
- Corpus (material disponivel)
- Foco do usuario (direcionamento)
- Bible (personagens, arcos, cronologia)

O plano deve ter granularidade de **CENA** (nao so capitulo), pois a validacao continua acontece por cena.

Salve o plano no `estado_da_obra.md` (secao "Plano de Capítulos").

---

# Passo 6 — Execute o Loop de Producao

Siga **RIGOROSAMENTE** o pseudocodigo da `SKILL_ORQUESTRADOR_LIVRO.md` (versao 1.0).

**FLUXO POR CENA/CAPITULO:**

```
PARA CADA cena EM plano.cenas:
    SE cena.status == "CONCLUIDO": CONTINUAR

    // TETO DE RETRIES — maximo 3 tentativas por cena
    cena.retries = cena.retries OU 0
    SE cena.retries >= 3:
        cena.status = "REPROVADO"
        cena.erro_fatal = "Excedeu 3 tentativas de reescrita"
        ATUALIZAR_ESTADO_ATOMICO(cena)
        PARAR("Cena reprovada apos 3 retries. Intervencao humana necessaria.")

    worktree = CRIAR_PASTA_ISOLADA(cena.id)  // capitulos/capitulo_NN/

    // ETAPA A: ESCRITOR
    INVOCAR(escritor, {cena, genero, bible, estado_anterior, foco_usuario}, worktree)
    VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/_saida_escritor.md")
    SE NAO: PARAR("Escritor nao executado")

    // ETAPA B: ATOMIZADOR
    INVOCAR(atomizador, {cena: worktree})
    VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/_afirmacoes_para_validar.json")
    SE NAO: PARAR("Atomizador nao executado")

    // ETAPA C: VALIDADOR MARCH (Fact-check CEGO)
    // ANTES de invocar, registrar prompt que sera enviado
    prompt_checker = MONTAR_PROMPT_CHECKER(cena, worktree)
    SALVAR(f"{worktree}/_log_prompt_checker.md", prompt_checker)

    INVOCAR(validador_march, {cena: worktree, corpus})
    VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/_resultado_march.json")
    SE NAO: PARAR("Validador MARCH nao executado")

    resultado_march = LER(f"{worktree}/_resultado_march.json")

    // AUDITORIA: Verificar se prompt do Checker vazou saida do Escritor
    log_prompt = LER(f"{worktree}/_log_prompt_checker.md")
    saida_escritor = LER(f"{worktree}/_saida_escritor.md")
    SE log_prompt CONTEM saida_escritor:
        cena.status = "REPROVADO"
        cena.erro_fatal = "VIOLACAO: prompt do Checker continha a saida do Escritor. Cegueira violada."
        ATUALIZAR_ESTADO_ATOMICO(cena)
        PARAR("Cegueira do Validador MARCH violada. Cena precisa ser refeita com isolamento rigoroso.")

    // ETAPA D: Verificar travas duras MARCH (RECALCULO do orquestrador)
    erros_march = []
    total = len(resultado_march.resultados)
    confirmados = len([r for r in resultado_march.resultados if r.status == "CONFIRMADO"])
    contraditos = len([r for r in resultado_march.resultados if r.status == "CONTRADITO"])
    nao_encontrados = len([r for r in resultado_march.resultados if r.status == "NAO_ENCONTRADO"])
    taxa = confirmados / total SE total > 0 SENAO 0

    SE taxa < 0.8:
        erros_march.ADICIONAR(f"Taxa de confirmados {taxa:.0%} abaixo de 80% (recalculado pelo orquestrador)")
    SE contraditos > 0:
        erros_march.ADICIONAR(f"{contraditos} afirmacoes contraditas encontradas")
    SE nao_encontrados > total * 0.3:
        erros_march.ADICIONAR(f"{nao_encontrados} de {total} afirmacoes sem lastro (>30%)")

    SE erros_march.NAO_VAZIO:
        cena.status = "REPROVADO_MARCH"
        cena.erros = erros_march
        cena.retries = cena.retries + 1
        ATUALIZAR_ESTADO_ATOMICO(cena)
        INVOCAR(escritor, {cena, worktree, falhas: erros_march})  // REESCRITA CIRURGICA
        REPETIR ETAPA A

    // ETAPA E: VALIDADOR CONTINUIDADE (CEGO — ve so Bible + Estado anterior)
    INVOCAR(validador_continuidade, {cena: worktree, bible, estado_anterior})
    VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/_resultado_continuidade.json")
    SE NAO: PARAR("Validador Continuidade nao executado")

    resultado_cont = LER(f"{worktree}/_resultado_continuidade.json")

    SE resultado_cont.status_geral != "APROVADO":
        cena.status = "REPROVADO_CONTINUIDADE"
        cena.erros = resultado_cont.erros
        cena.retries = cena.retries + 1
        ATUALIZAR_ESTADO_ATOMICO(cena)
        INVOCAR(escritor, {cena, worktree, falhas: resultado_cont.erros})  // REESCRITA CIRURGICA
        REPETIR ETAPA A

    // ETAPA F: EDITOR (OPCIONAL — se genero.exige_editor)
    SE genero.exige_editor:
        INVOCAR(editor, {cena: worktree, genero, bible})
        VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/_saida_editor.md")
        SE NAO: PARAR("Editor nao executado")
        saida_final = LER(f"{worktree}/_saida_editor.md")
    SENAO:
        saida_final = LER(f"{worktree}/_saida_escritor.md")

    // ETAPA G: Atualizar Bible + Estado (ATOMICAMENTE)
    bible = ATUALIZAR_BIBLE(bible, saida_final, cena)
    SALVAR_ATOMICO("bible/bible_da_obra.md", bible)

    cena.status = "CONCLUIDO"
    cena.validacao_march = "APROVADO"
    cena.validacao_continuidade = "APROVADO"
    cena.checksum_saida = CALCULAR_CHECKSUM(saida_final)
    cena.bytes_saida = TAMANHO_ARQUIVO(saida_final)
    cena.retries = cena.retries
    cena.chamadas_gastas = CALCULAR_CHAMADAS_DA_CENA(cena.id)
    ATUALIZAR_ESTADO_ATOMICO(cena)

    // CHECKSUM ROUND-TRIP: reler do disco e confirmar
    saida_referida = LER(f"{worktree}/_saida_final.md")  // _saida_editor.md ou _saida_escritor.md
    checksum_recalculado = CALCULAR_CHECKSUM(saida_referida)
    SE checksum_recalculado != cena.checksum_saida:
        cena.status = "INCONSISTENTE"
        ATUALIZAR_ESTADO_ATOMICO(cena)
        PARAR("CHECKSUM INCONSISTENTE: arquivo no disco nao corresponde ao registrado no estado.")

// FIM DO LOOP

// Passo 7: Consolidacao
INVOCAR(consolidador, {plano, estado, output: "livro_final.md"})
```

---

# Passo 7 — Pos-Producao

1. Consolidador gera `livro_final.md`
2. (Opcional) Consolidador gera `livro_final.epub` e `livro_final.pdf`
3. Entregue ao usuario

---

# Lembrete

**O Orquestrador NAO escreve. O Orquestrador COORDENA.**
Cada subagente recebe apenas o insumo necessario, nunca o projeto inteiro.
O Estado da Obra e a Bible sao os checkpoints unicos. Leia e escreva sempre.
**VALIDACAO MARCH E CONTINUIDADE SAO OBRIGATORIAS.** Sem elas, o capitulo nao existe.