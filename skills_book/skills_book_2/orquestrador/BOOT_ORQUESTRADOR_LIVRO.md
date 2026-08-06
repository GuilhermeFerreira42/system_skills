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

## 1.1 — Estrategia de Corpus: Modular OU Monolitico (DECISAO POR PROJETO)

**REGRA:** o pipeline NAO assume formato fixo de corpus. A escolha entre **corpus modular** (pastas separadas por tema) e **corpus monolitico** (arquivo unico) depende do **tamanho e da estrutura** do material fornecido.

### Como decidir

Pergunte-se: o corpus total tem **mais de 1MB** OU cobre **mais de 3 temas distintos**?

- **SIM** → use **MODULAR** (default recomendado)
- **NAO** → use **MONOLITICO** (consolide em `corpus_novo.md`)

### Opcao A — Corpus MODULAR (recomendado para projetos grandes ou multi-tema)

Estrutura esperada:

```
projeto_livro/
├── corpus/
│   ├── README.md                       # INDICE do corpus (obrigatorio)
│   ├── modulo_01_[tema_a]/             # pasta do primeiro tema
│   │   ├── fonte_1.txt
│   │   ├── fonte_2.md
│   │   └── ...
│   ├── modulo_02_[tema_b]/
│   │   └── ...
│   └── modulo_03_[tema_c]/
│       └── ...
```

**O que fazer:**

1. Se o usuario ja forneceu o corpus nessa estrutura (com `corpus/README.md` indice), pule esta etapa e va direto pro Passo 2.
2. Se o usuario forneceu arquivos soltos (na raiz, em pastas sem indice, com formatos misturados), **organize em modulos**:
   a. Identifique os **temas distintos** no material (ex: "agua", "hormonios", "cancer").
   b. Crie uma pasta `corpus/modulo_NN_[tema]/` para cada tema.
   c. Mova os arquivos relacionados pra dentro da pasta do tema correspondente.
   d. Crie `corpus/README.md` com o indice, no formato:
      ```markdown
      # Indice do Corpus

      ## Modulo 01: [tema_a]
      - caminho: corpus/modulo_01_[tema_a]/
      - arquivos: fonte_1.txt (12MB), fonte_2.md (3MB)
      - capitulos que usam: 1, 2, 3

      ## Modulo 02: [tema_b]
      - caminho: corpus/modulo_02_[tema_b]/
      - arquivos: fonte_3.pdf (8MB)
      - capitulos que usam: 4, 5
      ```
3. O Orquestrador usara o `corpus/README.md` + o campo `mapa_corpus_capitulos` da Bible para carregar **so o modulo relevante** em cada cena (ver Passo 6, funcao `EXTRAIR_CORPUS_PARA_CENA`).

**Por que modular e melhor para projetos grandes:**
- Cada chamada de API recebe so os arquivos relevantes (1-2MB em vez de 7MB+).
- A IA nao se confunde com informacao de outros temas.
- Custos de token caem 70-90% em projetos grandes.
- Validacao MARCH fica mais precisa (cruza com fonte certa, nao com fonte parecida de outro tema).

### Opcao B — Corpus MONOLITICO (para projetos pequenos e coesos)

Se o corpus tem **menos de 1MB** e cobre **1-2 temas relacionados**, consolide em arquivo unico:

```
projeto_livro/
├── corpus_novo.md                       # tudo num arquivo so
```

**Como consolidar:**
1. Identifique todos os arquivos do corpus na pasta do projeto.
2. Leia cada arquivo completamente.
3. Crie (ou sobrescreva) `corpus_novo.md` com o conteudo de todos concatenados.
4. **Preserve** a formatacao markdown (titulos, paragrafos, listas).
5. **Adicione separadores claros** entre fontes (ex: `## Fonte 1: <nome_do_arquivo>`).
6. **Mantenha fidelidade**: nao resuma, nao omita, nao corrija. E copy-paste estruturado.

**Excecao:** se o usuario ja forneceu um unico arquivo `corpus_novo.md` (ou similar), pule esta etapa e va direto pro Passo 2.

### Regra absoluta independente da escolha

- **NUNCA** invente conteudo de corpus. Se o material fornecido nao cobre um topico, a cena sobre esse topico nao pode ser produzida (ou sera produzida sem validacao MARCH).
- **SEMPRE** preserve a fonte original. Se o usuario deu transcricoes, nao resuma, nao corrija gramatica, nao omita partes.
- **SEMPRE** registre o caminho do corpus no campo `corpus_origem` do estado, pra saber depois de onde veio cada informacao.

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

## 2.1 — Checksum do Estado (registrar como prova de leitura)

Ao ler (ou criar) o estado, **calcule o checksum real dele** pra ter prova de leitura integra.

Comando real: `python3 utils/checksum.py calcular estado/estado_da_obra.md`

O retorno (formato `v1.0:a1b2c3d4`) deve ser registrado no log da sessao atual. Se nao conseguir executar, registre `PENDENTE`, nunca um placeholder.

---

# Passo 3 — Consulte o Usuario (Formato, Genero, Foco)

## 3.1 Selecione o Genero

Pergunte ao usuario (se nao veio no input):

```
Qual o genero do livro?

1. Romance (ficcao literaria, comercial, genero)
2. Nao-Ficcao (educativo, business, ciencia popular, biografia, saude, financas, filosofia)
3. Memorias / Autobiografia
4. Tecnico / Manual / How-To / Procedimento
5. Thriller (suspense, misterio, espionagem, psicologico, terror)
6. Cookbook (receitas, culinaria estruturada, cultura gastronomica)
7. Academico (livro universitario, tratado, paper-derivado, ensaio de humanities)
8. Personalizado — voce descreve a estrutura e voz
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
- Nao-Ficcao -> `generos/GENERO_NAO_FICCAO.md` (v2.0 - agnóstico, abrange self-help, business, saude, financas, filosofia, biografia)
- Memorias -> `generos/GENERO_MEMORIAS.md`
- Tecnico -> `generos/GENERO_TECNICO.md` (v2.0 - agnóstico, abrange software, manuais fisicos, jardinagem, DIY)
- Thriller -> `generos/GENERO_THRILLER.md` (v1.0 - inclui suspense, misterio, espionagem, psicologico, terror)
- Cookbook -> `generos/GENERO_COOKBOOK.md` (v1.0 - culinaria, mas tambem livros prescritivos de outras areas)
- Academico -> `generos/GENERO_ACADEMICO.md` (v1.0 - monografia, livro-texto, paper-derivado, tratado, ensaio de humanities)
- Personalizado -> crie `generos/GENERO_PERSONALIZADO.md` com a descricao do usuario

**NOTA SOBRE GENERO LEGACY:** `generos/GENERO_PODBOOK_BRUNO.md` e um genero ESPECIFICO do projeto Ecommerce do Bruno de Oliveira. Ele herda de NAO_FICCAO v1.0 (antes da refatoracao) e NAO deve ser usado como modelo pra outros livros. Continua funcionando pra o projeto Ecommerce ja produzido, mas se o Bruno quiser refazer o livro do zero usando a skill v2.0, ele precisara criar um GENERO_PODBOOK_V3.md atualizado.

**O genero define:**
- Estrutura narrativa (capitulos, cenas, atos)
- Voz narrativa (1a/3a pessoa, onisciente, limitado, multi-POV)
- Tom, pacing, show vs tell, densidade de dialogo
- Validacoes extras (exige Editor? quais regras?)

---

# Passo 4 — Analise o Corpus e Crie/Atualize a Bible

**Se o corpus e MODULAR** (veja Passo 1.1): para cada modulo em `corpus/modulo_NN_*/`, leia os arquivos daquele modulo e extraia os temas, conceitos, citacoes relevantes. Monte um **mapa_corpus_capitulos** que diz qual modulo alimenta qual capitulo do plano (ex: "Capitulo 1-3 → modulo_01_agua, Capitulo 4-5 → modulo_02_hormonios, ..."). Esse mapa vai na Bible e e consultado pelo Orquestrador a cada cena pra carregar so o modulo relevante.

**Se o corpus e MONOLITICO** (`corpus_novo.md`): leia o arquivo inteiro e faca a extracao normalmente.

Em ambos os casos, identifique:
- Temas centrais
- Personagens (se ficcao) / Conceitos (se nao-ficcao)
- Estrutura narrativa sugerida pelo material
- Arcos, conflitos, questoes centrais
- Evidencias, dados, citacoes (para MARCH)

**SE Bible nao existe:** Crie `bible/bible_da_obra.md` usando o template (incluindo o campo `mapa_corpus_capitulos` se o corpus for modular).
**SE Bible existe:** Atualize com novas informacoes do corpus (personagens novos, locais, cronologia) e ajuste o `mapa_corpus_capitulos` se necessario.

## 4.1 — Checksum da Bible (registrar no estado)

Apos criar/atualizar a Bible, **registre o checksum real dela no campo `bible_checksum` do estado**.

Comando real: `python3 utils/checksum.py calcular bible/bible_da_obra.md`

O retorno (formato `v1.0:a1b2c3d4`) deve ser gravado no estado. **NUNCA invente valores** tipo `v1.0-init` ou `init-v1.0`. Se nao conseguir executar o comando, registre `PENDENTE` explicito, nunca um placeholder.

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

    worktree = CRIAR_PASTA_ISOLADA(cena.id)  // capitulos/capitulo_NN/cena_MM/ (subpasta por cena!)

    // GERA CHECKSUM INICIAL DO WORKTREE VAZIO (para baseline de integridade)
    // Use a CLI: python3 utils/checksum.py calcular <worktree>/_saida_escritor.md (sera recriado depois)
    // Isso garante que a skill tem rastreabilidade desde o inicio.

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

    // CHECKSUM DA SAIDA FINAL: USE A CLI EXPLICITA, NAO INVENTE HASH
    // Comando real: python3 utils/checksum.py calcular <caminho_do_arquivo>
    // O retorno vem no formato v1.0:a1b2c3d4 (com etiqueta de versao).
    // NUNCA invente valores como "c1s3-955b" ou "init-v1.0". Use o comando.
    // Para gerar baseline de uma pasta inteira (caso queira):
    //   python3 utils/checksum.py baseline skills_book/ -o .checksums.json
    cena.checksum_saida = EXECUTAR_CLI("python3 utils/checksum.py calcular " + saida_final)
    cena.bytes_saida = TAMANHO_ARQUIVO(saida_final)
    cena.retries = cena.retries
    cena.chamadas_gastas = CALCULAR_CHAMADAS_DA_CENA(cena.id)
    ATUALIZAR_ESTADO_ATOMICO(cena)

    // CHECKSUM ROUND-TRIP: reler do disco e confirmar
    saida_referida = LER(f"{worktree}/_saida_final.md")  // _saida_editor.md ou _saida_escritor.md
    checksum_recalculado = EXECUTAR_CLI("python3 utils/checksum.py calcular " + saida_referida)
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