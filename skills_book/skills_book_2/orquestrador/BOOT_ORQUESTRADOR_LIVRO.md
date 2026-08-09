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
   a. Identifique os **temas distintos** no material (ex: "financas", "historia", "metodo").
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

## 3.2 Nivelamento Editorial (OBRIGATORIO)

**POR QUE EXISTE:** o diagnostico do Episodio 03 mostrou que a versao antiga da skill (v1.0) produziu um capitulo-bancada muito melhor que a versao nova (v3.0), porque a antiga tinha um `foco_usuario` muito mais detalhado e especifico. A solucao eh institucionalizar essa captura de preferencias na propria skill: o Orquestrador faz 4 perguntas de multipla escolha ANTES de comecar qualquer projeto novo, e as respostas viram o `perfil_editorial` da Bible.

**REGRA:** este passo eh OBRIGATORIO (definido em `utils/constantes.py` como `NIVELAMENTO_OBRIGATORIO = True`). O Orquestrador NAO passa pro Passo 4 enquanto as 4 respostas nao estiverem registradas. Se o usuario disser "nao sei" ou pular, use o `NIVELAMENTO_DEFAULT` (4 respostas "A" validadas como o perfil editorial padrão) — mas registre explicitamente que o default foi usado, nao finja que o usuario respondeu.

**COMO FAZER:** faca 1 pergunta por mensagem. Espere a resposta (letra unica A, B ou C). So faca a proxima depois de receber a resposta. A ordem dos 4 eixos eh fixa: abertura → densidade → analogias → voz.

**PROMPT DA PERGUNTA 1 — Estilo de Abertura:**

```
Antes de comecar, preciso alinhar 4 preferencias editoriais contigo. 
Sao rapidas (multipla escolha) e vao definir o tom de TODAS as cenas 
do livro, entao pensa com calma. Voce pode mudar depois se quiser, 
mas o ideal eh travar agora pra nao ficar recalibrando cena a cena.

Pergunta 1 de 4 — ESTILO DE ABERTURA das cenas:

A) IMERSAO + PERGUNTA RETORICA — cada capitulo comeca com uma cena 
   mental que coloca o leitor no contexto (ex: "Se voce passasse seis 
   anos na faculdade de medicina, dissecando cadaveres..."), e so 
   depois revela a informacao. Mais lento, mais envolvente, 
   lembra aula boa de professor apaixonado.

B) DIRETO AO PONTO — afirma a tese ou a informacao principal logo na 
   primeira frase. Eficiente, respeita o tempo do leitor que quer 
   informacao rapida, mas pode soar frio.

C) CASO CONCRETO ANTES — comeca com um caso real, uma vinheta de 
   paciente, um exemplo vivido, e so depois generaliza. Bom pra 
   livros de saude, financas, historia.

Responde com a letra (A, B ou C).
```

**PROMPT DA PERGUNTA 2 — Densidade do Livro:**

```
Pergunta 2 de 4 — DENSIDADE DO LIVRO (quantas palavras no total 
e por cena):

A) DENSO — livro grande, ~250 mil palavras, com cenas longas 
   (800-1500 palavras cada). Prosfundidade total, multiplas 
   camadas por cena, analogias, exemplos, contra-argumentos. 
   Pra quem quer o "livro de referencia" definitivo.

B) MEDIO — livro de ~120 mil palavras, cenas de 500-900 palavras. 
   Equilibra profundidade com agilidade. Leitor termina em 
   2-3 semanas se ler 1h por dia.

C) ENXUTO — livro curto, ~60 mil palavras, cenas de 300-600 
   palavras. Objetivo, pouca repeticao, vai direto ao que 
   importa. Pra quem quer um "resumo denso" ou um guia pratico.

Responde com a letra (A, B ou C).
```

**PROMPT DA PERGUNTA 3 — Densidade de Analogias:**

```
Pergunta 3 de 4 — DENSIDADE DE ANALOGIAS (quantas metaforas 
visuais ou casos analogos por cena):

A) ALTA — 1 a 2 analogias por cena, sempre. Pra cada conceito 
   cientifico ou abstrato, uma metafora visual forte (tipo 
   "juros compostos = bola de neve descendo a ladeira" ou 
   "painel do carro com luzes acesas"). Excelente pra nao-ficcao 
   educativa, porque o leitor leigo "vê" o conceito.

B) MEDIA — 0 a 1 analogia por cena. Usa quando faz sentido, 
   nao forca. Bom pra publico que ja tem alguma familiaridade 
   com o tema.

C) BAIXA — nenhuma analogia obrigatoria. O texto assume que 
   o leitor sabe do que esta falando. Mais comum em livros 
   tecnicos, academicos, manuais.

Responde com a letra (A, B ou C).
```

**PROMPT DA PERGUNTA 4 — Voz do Autor:**

```
Pergunta 4 de 4 — VOZ DO AUTOR (como o narrador se posiciona):

A) REVELACAO RESPEITOSA — voz cumplice, precisa e respeitosa. O narrador 
   descobre junto com o leitor ("precisamos entender"), critica o SISTEMA 
   de forma estrutural ("a formacao tem uma lacuna"), nunca pessoas, nunca 
   ocultacao/lucro. Humor leve quando natural, nunca acido nem ataque. Fecho 
   em eco com a abertura. Esta e a voz que produziu o melhor resultado da 
   skill na versao antiga ("Revelacao Respeitosa").

B) NEUTRA ENGAJADA — narrador invisivel (voz de terceira pessoa 
   classica), mas preocupado com clareza e ritmo. Nao polemiza, 
   nao da opiniao, mas tambem nao eh frio. E o "default" da 
   maioria dos livros de nao-ficcao bestseller.

C) ACADEMICA DISTANTE — narrador onisciente, formal, sem opiniao, 
   tom de paper ou tratado. Pra livros universitarios, manuais 
   tecnicos, literatura de referencia. Soberano, porem distante.

Responde com a letra (A, B ou C).
```

**REGISTRO DAS RESPOSTAS:**

Apos receber as 4 letras, construa o dicionario `perfil_editorial`:

```python
perfil_editorial = {
    "estilo_abertura": <A|B|C>,        # resposta 1
    "densidade_livro": <A|B|C>,        # resposta 2
    "densidade_analogias": <A|B|C>,    # resposta 3
    "voz_autor": <A|B|C>,              # resposta 4
    "preenchido_em": "<ISO8601>",
    "fonte": "nivelamento_inicial",    # ou "nivelamento_padrao" se usou default
}
```

Passe esse dicionario pro Passo 4 (que grava na Bible) E pro Passo 3.3 em diante (que usa como input do Escritor).

**SE O USUARIO NAO SOUBER RESPONDER:**

Use o `NIVELAMENTO_DEFAULT` (definido em `utils/constantes.py`): todas as 4 respostas = "A" (4 respostas "A" validadas como o perfil editorial padrão da skill). Mas ANTES de aplicar o default, faca UMA pergunta confirmando:

```
Nao tem problema se voce nao sabe agora. Posso usar o "perfil padrao 
padrao da skill" (4 respostas A: imersao + pergunta retorica, denso, alta analogia, voz 
opinativa com humor) como ponto de partida? Voce pode ajustar depois, 
cena a cena, se quiser. Confirma com "sim" pra eu seguir.
```

Se o usuario confirmar, registre `"fonte": "nivelamento_padrao"`. Se o usuario preferir customizar, refaca as 4 perguntas.

**SE O USUARIO PEDIR PRA PULAR:**

Recuse. O nivelamento eh obrigatorio. Diga:

```
O nivelamento editorial eh obrigatorio porque sem ele o livro fica 
generico e perde a tua voz. Leva 2 minutos, sao 4 perguntas de 
multipla escolha. Bora?
```

So pule se o usuario for EXPLICITO ("pula o nivelamento, eu sei o que quero" — esse caso registra `"fonte": "nivelamento_pulado_usuario_explicito"` e usa o default de qualquer jeito, pra garantir que o Escritor tenha pelo menos alguma direcao).

## 3.3 Capture o Foco do Usuario (COMPLEMENTAR ao Nivelamento)

**IMPORTANTE:** o `foco_usuario` continua existindo. Ele eh COMPLEMENTAR ao `perfil_editorial`, nao substituto. O perfil_editorial captura o "padrao recorrente" (voz, densidade, estilo); o foco_usuario captura os "ajustes finos desta obra especifica" (ex: "neste livro quero focar em saude feminina" ou "capitulo 5 precisa ser polemico").

Apos o nivelamento estar registrado, pergunte:

```
Em quais aspectos especificos desta obra o narrador deve se 
concentrar? (Texto livre. Ex: 'Foque na tensao psicologica do 
protagonista. Evite descricoes longas de cenario. O leitor deve 
sentir a paranoia crescente a cada capitulo. Priorize dialogos 
rapidos e acao interna.')

Se nao houver nada especifico desta obra alem do nivelamento, 
responde "nada" e seguimos com o padrao.
```

**REGRA:** o `foco_usuario` NUNCA sobrescreve o `perfil_editorial`. Se o usuario escrever no foco_usuario algo que contradiz o nivelamento (ex: escolheu voz opinativa no nivelamento mas pede "voz neutra e academica" no foco_usuario), o Escritor prioriza o nivelamento. O Orquestrador deve avisar:

```
Percebi que o foco_usuario desta obra ("voz neutra e academica") 
contradiz o perfil_editorial que tu escolheu no nivelamento 
(voz opinativa com humor). Vou priorizar o perfil_editorial, 
porque ele eh a "voz padrao da tua marca". Se quer mudar a voz 
pra ESTA obra especifica, refaz o nivelamento no Passo 3.2.
```

Registre a resposta do foco_usuario no campo `foco_usuario` do estado E no `perfil_editorial.foco_usuario_adicional` da Bible (pra ficar tudo num lugar so).

## 3.4 Carregue o Genero

Conforme a escolha, carregue o arquivo da pasta `generos/`:
- Romance -> `generos/GENERO_ROMANCE.md`
- Nao-Ficcao -> `generos/GENERO_NAO_FICCAO.md` (v2.0 - agnóstico, abrange self-help, business, saude, financas, filosofia, biografia)
- Memorias -> `generos/GENERO_MEMORIAS.md`
- Tecnico -> `generos/GENERO_TECNICO.md` (v2.0 - agnóstico, abrange software, manuais fisicos, jardinagem, DIY)
- Thriller -> `generos/GENERO_THRILLER.md` (v1.0 - inclui suspense, misterio, espionagem, psicologico, terror)
- Cookbook -> `generos/GENERO_COOKBOOK.md` (v1.0 - culinaria, mas tambem livros prescritivos de outras areas)
- Academico -> `generos/GENERO_ACADEMICO.md` (v1.0 - monografia, livro-texto, paper-derivado, tratado, ensaio de humanities)
- Personalizado -> crie `generos/GENERO_PERSONALIZADO.md` com a descricao do usuario

**NOTA SOBRE GENERO LEGACY:** `generos/GENERO_PODBOOK_LEGACY.md` (nome canônico) ou `generos/GENERO_PODBOOK_BRUNO.md` (alias retrocompatível) é um gênero ESPECÍFICO do projeto de Ecommerce já produzido. Ele herda de NAO_FICCAO v1.0 (antes da refatoração) e NÃO deve ser usado como modelo para novos livros. Continua funcionando para o projeto já produzido. Para novos livros de Ecommerce ou negócios, use NAO_FICCAO v2.0 (agnóstico) e crie um gênero personalizado herdando da v2.0.

**O genero define:**
- Estrutura narrativa (capitulos, cenas, atos)
- Voz narrativa (1a/3a pessoa, onisciente, limitado, multi-POV)
- Tom, pacing, show vs tell, densidade de dialogo
- Validacoes extras (exige Editor? quais regras?)

---

# Passo 4 — Analise o Corpus e Crie/Atualize a Bible

**Se o corpus e MODULAR** (veja Passo 1.1): para cada modulo em `corpus/modulo_NN_*/`, leia os arquivos daquele modulo e extraia os temas, conceitos, citacoes relevantes. Monte um **mapa_corpus_capitulos** que diz qual modulo alimenta qual capitulo do plano (ex: "Capitulo 1-3 → modulo_01_fundamentos, Capitulo 4-5 → modulo_02_aplicacoes, ..."). Esse mapa vai na Bible e e consultado pelo Orquestrador a cada cena pra carregar so o modulo relevante.

**Se o corpus e MONOLITICO** (`corpus_novo.md`): leia o arquivo inteiro e faca a extracao normalmente.

Em ambos os casos, identifique:
- Temas centrais
- Personagens (se ficcao) / Conceitos (se nao-ficcao)
- Estrutura narrativa sugerida pelo material
- Arcos, conflitos, questoes centrais
- Evidencias, dados, citacoes (para MARCH)

**SE Bible nao existe:** Crie `bible/bible_da_obra.md` usando o template (incluindo o campo `mapa_corpus_capitulos` se o corpus for modular E o campo `perfil_editorial` se o nivelamento editorial foi feito no Passo 3.2).
**SE Bible existe:** Atualize com novas informacoes do corpus (personagens novos, locais, cronologia) e ajuste o `mapa_corpus_capitulos` se necessario. **NUNCA sobrescreva o campo `perfil_editorial` existente** — esse campo so muda se o usuario explicitamente responder o nivelamento de novo (Passo 3.2). Se a Bible foi criada antes do Nivelamento ser instituido (Acao 6 do Episodio 03), o Orquestrador roda o nivelamento retroativamente antes de comecar a escrever, pra garantir que o Escritor tenha as 4 respostas.

**4.0.1 — Persistencia do Nivelamento Editorial (Acao 6 do Episodio 03)**

Ao criar ou atualizar a Bible, o Orquestrador DEVE garantir que o campo `perfil_editorial` esteja preenchido com as 4 respostas do Passo 3.2. O fluxo:

1. Apos o Passo 3.2 ter capturado as 4 letras (A/B/C de cada eixo), o Orquestrador monta o dicionario `perfil_editorial` e grava em:
   - `bible/bible_da_obra.md` → secao "Perfil Editorial (NIVELAMENTO)" (template em `BIBLE_TEMPLATE.md`)
   - `estado/estado_da_obra.md` → espelhado no campo `perfil_editorial` (pra o Escritor poder consultar sem precisar abrir a Bible)
2. Se a Bible ja existe e o `perfil_editorial` ja esta preenchido, o Orquestrador PRESERVA os valores (so sobrescreve se o usuario rodar o nivelamento de novo explicitamente).
3. Se a Bible existe mas o `perfil_editorial` NAO esta preenchido (Bible antiga, pre-Acao 6), o Orquestrador PARA e pede pro usuario rodar o Passo 3.2 antes de continuar. NAO invente valores, NAO use o default silenciosamente — pergunte.

O Escritor (`BOOT_ESCRITOR_CAPITULO.md`) consulta o `perfil_editorial` no inicio de cada cena e usa os 4 valores pra calibrar: estilo de abertura da cena 1 do capitulo, palavras-alvo da cena (densidade_livro), numero de analogias (densidade_analogias), voz do narrador (voz_autor).

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

**Alocacao de cenas por capitulo (DINAMICA, nao fixa):**

A quantidade de cenas por capitulo NAO e fixa. Ela e calculada automaticamente pelo Orquestrador usando DOIS fatores:

1. **Densidade do corpus do capitulo** (palavras / numero-de-subtopicos):
   - **Direto** (menos de 3.000 palavras por subtopico) → 1 cena
   - **Medio** (3.000-6.000 palavras por subtopico) → 2 cenas
   - **Denso** (mais de 6.000 palavras por subtopico) → 4 cenas

2. **Arquetipo do genero** (alguns arquetipos tem cadencia rigida):
   - Misterio/Detetive: 4 cenas (crime, pistas, red herring, resolucao)
   - Receita/COOKBOOK: 1 cena por receita
   - Monografia academica: 4 argumentos
   - Guia de campo: 1 procedimento por cena
   - (Lista completa em `utils/constantes.py`, secao CONFIGURACAO_CENAS_POR_ARQUETIPO)

**Combinacao:** o sistema usa o MAIOR valor entre o fixo do arquetipo e o da densidade. Ou seja, se o arquetipo pede 4 cenas mas o material e direto (1 cena), o sistema usa 4 (cadencia do genero). Se o arquetipo pede 1 cena mas o material e denso (4 cenas), o sistema usa 4 (respeita a riqueza do conteudo).

**Limites de seguranca:** minimo 1 cena por capitulo, maximo 6 (anti-monstro). Configuraveis em `utils/constantes.py`.

**Override manual:** se a Bible tem o campo `alocacao_cenas_por_capitulo` preenchido (ex: `{1: 3, 2: 2, 3: 4}`), esse mapeamento sobrescreve o calculo automatico. Use quando quiser forcar uma cadencia especifica (ex: capitulo de fechamento com 1 cena, capitulo de virada com 5).

Salve o plano no `estado_da_obra.md` (secao "Plano de Capítulos"), com a quantidade de cenas calculada pra cada capitulo.

---

# Passo 6 — Execute o Loop de Producao

## INVARIANTE DE LINHAGEM (REGRA DE OURO DO PIPELINE — revisao 2026-08-08)

1. **Toda alteracao em `_saida_escritor.md` ou `_saida_editor.md` INVALIDA todas as validacoes ja feitas na cena** (MARCH, Continuidade, Editor, Revisor Cego, Vigia), porque o `input_checksum` de cada uma deixa de corresponder ao texto atual. Nao existe "reescrita pequena": mudou o texto, mudou o checksum, caiu a linhagem.
2. **Apos QUALQUER reescrita cirurgica, o pipeline recomeca na ETAPA B (Atomizador)** sobre a NOVA versao — MARCH, Continuidade, Editor (que gera novo `_saida_editor.md` e novo `_saida_final.md`) e Revisor Cego (sobre o novo `_saida_final.md`). No pseudocodigo abaixo, onde se le "REPETIR ETAPA A", entenda: **a reescrita cirurgica SUBSTITUI a execucao da Etapa A; o fluxo recomeça na Etapa B.** NUNCA invoque o Escritor duas vezes seguidas e NUNCA deixe validacoes da versao antiga valerem para a versao nova. (Foi exatamente isso que quebrou a linhagem e fez o Vigia sair com exit 1 no teste de 2026-08-08.)
3. **O Estado DEVE ser atualizado a cada transicao de status** — inclusive em cada retry (preencher o Historico de Retries com: tentativa, validador, motivo_falha, acao_corretiva). Um retry sem registro no Estado e um retry que nao aconteceu.
4. **Checksums SOMENTE via script:** `python3 skills_book_2/utils/checksum.py calcular <arquivo>` — saida no formato canonico `v1.0:xxxxxxxx` (8 hex). Nunca digite ou invente o hash manualmente. Se `utils/` nao existir na raiz do projeto, o caminho real e `skills_book_2/utils/`: confira com `ls` antes de executar.
5. **Vigia da Fabrica:** `python3 skills_book_2/utils/vigia_integridade.py <pasta_da_cena>` — a cena so vale com **exit 0**. O script grava `_log_vigia.md` na propria pasta da cena a cada execucao (nao depende de redirecionamento de shell).
6. **Cena CONCLUIDA exige pacote fechado:** MARCH aprovado + Continuidade aprovado + Editor executado (quando exigido) + Revisor Cego APROVADO + Vigia exit 0 — **todos sobre a MESMA versao do texto** (linhagem fechada).

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

    // ETAPA F.5: REVISOR CEGO EDITORIAL (obrigatorio p/ NAO_FICCAO com contrato de voz)
    // NAO pula capitulos 1-3 quando genero.contrato_voz_ativado = true
    SE DEVE_INVOCAR_REVISOR_CEGO(genero, cena, len(saida_final)):
        INVOCAR(revisor_cego_editorial, {cena: worktree, criterios: genero.criterios_revisor OU REVISAO_CRITERIOS_PADRAO})
        VERIFICAR_SE_ARQUIVO_EXISTE(f"{worktree}/_resultado_revisor_cego.json")
        SE NAO: PARAR("Revisor Cego nao executou")
        resultado_revisor = LER(f"{worktree}/_resultado_revisor_cego.json")
        SE resultado_revisor.status_geral != "APROVADO":
            cena.status = "REPROVADO_REVISOR"
            cena.erros = resultado_revisor.problemas_alta + resultado_revisor.problemas_media
            cena.retries = cena.retries + 1
            ATUALIZAR_ESTADO_ATOMICO(cena)
            INVOCAR(escritor, {cena, worktree, falhas: cena.erros, modo: "REESCRITA_CIRURGICA"})
            REPETIR ETAPA A

    // ETAPA H: VIGIA DA FABRICA (Camada A — script, 0 tokens)
    resultado_vigia = EXECUTAR_CLI("python3 utils/vigia_integridade.py " + worktree)
    SALVAR(f"{worktree}/_log_vigia.md", resultado_vigia.saida)
    SE resultado_vigia.exit_code != 0:
        cena.status = "REPROVADO_VIGIA"
        cena.erros = resultado_vigia.saida
        cena.retries = cena.retries + 1
        ATUALIZAR_ESTADO_ATOMICO(cena)
        INVOCAR(escritor, {cena, worktree, falhas: cena.erros, modo: "REESCRITA_CIRURGICA"})
        REPETIR ETAPA A
    cena.validacao_vigia = "APROVADO"

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