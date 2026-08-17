# GENERO: ACADEMICO (Livro Universitário, Tratado, Paper-Derivado, Ensaio de Humanities, Manual Didático Superior)

**Versao:** 1.0 (Greenforged Edition)
**Tipo:** ACADEMICO
**Estrutura:** Argumento → Evidência → Contra-argumento → Síntese → Avanço do conhecimento

**Notas de design:**
- O gênero acadêmico é o mais **rígido** em termos de forma, porque tem convenções disciplinares seculares.
- Subgêneros: monografia acadêmica, tratado técnico, livro-texto universitário, ensaio de humanities, paper-derivado (vários papers viram livro), manual didático, coletânea editada.
- Inspirado em **The Craft of Research (Wayne Booth)**, **The Elements of Style (Strunk & White)**, **How to Write a Thesis (Umberto Eco)**, e nas normas **APA / Chicago / ABNT**.
- **Atenção crítica:** apesar do nome "ACADÊMICO", o que define o gênero é o **rigor argumentativo e a estrutura de evidência**, não a formalidade excessiva. Um ensaio de humanities bem escrito é acadêmico; um manual chato não é.

---

## Voz Narrativa

- **pessoa:**
  - `3a_onisciente` (voz autoral, padrão em humanities)
  - `3a_instrutiva` (livro-texto, didática)
  - `1a_academica` (memoir intelectual, "quando eu era pós-graduando...")
  - `nós_coletivo` (paper-derivado, "nossa equipe descobriu...")
- **tempo_verbal:**
  - `presente` (conceitos, leis, princípios — atemporais)
  - `passado` (pesquisas anteriores, histórico do campo)
  - `misto_controlado` (presente pra princípios, passado pra história)
- **distancia:**
  - `academica_formal` (humans, ciências sociais — distante, respeitosa)
  - `cientifica_objetiva` (ciências naturais, exatas — impessoal)
  - `intelectual_honesta` (reconhece limitações, debate interno)
  - `didatica_superior` (livro-texto, fala com aluno de graduação)
- **tom:** varia por subgênero. Lista sugerida (escolha 3-4 adjetivos):
  - **Humanities/Ensaio:** `rigoroso`, `nuançado`, `crítico`, `reverente`
  - **Ciências Naturais/Exatas:** `objetivo`, `preciso`, `cauteloso`, `metódico`
  - **Ciências Sociais:** `crítico`, `contextualizado`, `auto-reflexivo`, `ético`
  - **Livro-texto:** `didático`, `paciente`, `progressivo`, `inclusivo`
- **vocabulario:**
  - `cientifico_preciso` (terminologia técnica do campo, definida no primeiro uso)
  - `academico_denso` (sem jargão desnecessário, mas com rigor terminológico)
  - `formal_controlado` (evita coloquialismo, mas não é árido)
- **ritmo:**
  - `argumentativo_sequencial` (tese → argumento → evidência → objeção → resposta)
  - `analitico_progressivo` (do simples ao complexo, do conhecido ao novo)
  - `dialectico` (tese, antítese, síntese — Hegel/marxiano, comum em humanities)

## POV

- **padrao:** `autor_academico` (pesquisador, professor, especialista) ou `comunidade_cientifica` (paper-derivado, vários autores)
- **multi_pov:** `false` em monografia individual. `true` em coletânea editada (cada capítulo pode ter POV de autor diferente, claramente demarcado)
- **head_hopping:** NA (acadêmico não é narrativa)

## Estrutura de "Cena" (Unidade Argumentativa)

Em acadêmico, "cena" = **uma unidade argumentativa autocontida**, com premissa, evidência, e conclusão. É o equivalente funcional de um parágrafo de paper ou uma seção curta de capítulo.

- **min_palavras:** 1500 (seções acadêmicas exigem densidade)
- **max_palavras:** 5000 (acima disso, vira capítulo)
- **beats_obrigatorios:** `["tese_ou_pergunta", "contexto_literatura_anterior", "argumento_principal", "evidencia_dados_citacoes", "contra_argumento_e_resposta", "conclusao_parcial", "ponte_proximo_secao"]`
- **show_minimo:** 20% (gráficos, tabelas, equações, diagramas — acadêmico é mais "tell" do que "show")
- **gancho_tipos:**
  - `pergunta_de_pesquisa` ("Por que X aconteceu?")
  - `paradoxo_empirico` ("Os dados mostram Y, mas a teoria prevê Z")
  - `lacuna_na_literatura` ("Ninguém até agora estudou...")
  - `citacao_provocativa` ("Como disse Foucault, ...")
- **fecho_tipos:**
  - `sintese_parcial` (resumo do argumento)
  - `implicacao_teorica` (o que isso significa para o campo)
  - `questao_aberta` (pergunta para a próxima seção)
  - `reconhecimento_limitacao` (o que esse argumento NÃO faz)

## Estrutura de Capítulo

- **secoes_por_capitulo:** 3-6 (cada seção = um argumento autocontido, NÃO uma "cena" narrativa)
- **arco_capitulo:** "Pergunta central → Argumentos convergentes → Síntese → Implicações"
- **recap_final:** `true` (resumo dos argumentos + transição pro próximo capítulo)

## Estrutura Global (5 Arquétipos)

### Opção A: Monografia Acadêmica (Padrão)
- **Capítulo 1:** Introdução, problema de pesquisa, justificativa
- **Capítulo 2-3:** Revisão de literatura, estado da arte
- **Capítulo 4-6:** Argumentos centrais, com evidência empírica ou teórica
- **Capítulo 7:** Discussão, contra-argumentos, limitações
- **Capítulo 8:** Conclusões, implicações, agenda de pesquisa futura

Inspiração: teses de doutorado virando livro, papers conceituais.

### Opção B: Livro-Texto Universitário (Didático Superior)
- Estrutura progressiva: do fundamento ao avançado
- Cada capítulo tem objetivos de aprendizagem, exercícios, leituras recomendadas
- Boxes laterais: "Para Saber Mais", "Exercício", "Estudo de Caso", "Atenção"
- Ao fim de cada parte: resumo + questões para revisão
- Inspiração: manuais de graduação (ex: OpenStax, Springer Undergraduate)

### Opção C: Paper-Derivado (Livro que Vem de Vários Papers)
- Estrutura segue a **linha de pesquisa**, não a lógica de um único paper
- Cada capítulo = um paper ou estudo, com capítulo integrador no início e no fim
- Fortemente referenciado (cada capítulo tem 50-100 citações)
- Inspiração: coletâneas acadêmicas (Handbooks da Elsevier, Cambridge Companions)

### Opção D: Tratado Técnico (Manual de Referência Definitivo)
- Livro de referência que se consulta, não que se lê do início ao fim
- Estrutura por tópico, com encadeamento lógico
- Pesado em equações, tabelas, diagramas
- Índice remissivo denso, glossário de termos
- Inspiração: Handbook of Mathematical Functions (Abramowitz & Stegun), tratadis de física

### Opção E: Ensaio de Humanities (Argumentativo Reflexivo)
- Mais literário que o paper, mais rigoroso que o jornalismo
- Estrutura: **tese provocativa → contexto histórico → debate com a tradição → defesa original → implicações para o presente**
- Sem dados quantitativos, mas com fontes primárias citadas com rigor
- Cita muito, mas também pensa em voz alta
- Inspiração: ensaios de Edward Said, Susan Sontag, Judith Butler, Giorgio Agamben

## Bible Requisitos

A Bible acadêmica carrega o **arcabouço teórico, metodologia, e estado da arte** do campo. É a parte mais formal e rigorosa de todas.

- **glossario_tecnico:** `true` (todos os termos definidos na primeira ocorrência, com etimologia se relevante)
- **bibliografia_completa:** `true` (todas as citações, com formatação consistente, ex: APA 7ª, Chicago, ABNT)
- **referencias_bibliograficas:** `true` (papers, livros, fontes primárias)
- **conceitos_chave:** `true` (definições canônicas dos conceitos centrais)
- **autores_principais:** `true` (quem são as vozes canônicas do campo, quem são os críticos)
- **debates_em_aberto:** `true` (o que está sendo discutido AGORA no campo, quem defende o quê)
- **metodologia:** `true` (se for paper-derivado ou tratado, qual foi o método de pesquisa, quais as limitações)
- **fontes_primarias:** `true` (documentos, dados, entrevistas, experimentos que fundamentam o argumento)
- **etica_pesquisa:** `true` (consentimento informado, aprovação IRB/comitê de ética, conflitos de interesse)
- **historia_do_campo:** `true` (como o campo se constituiu, quais foram as viradas teóricas, quem são os pais fundadores)
- **cruzamento_interdisciplinar:** `true` (o que outros campos podem contribuir, ex: filosofia + IA)
- **normas_formatacao:** `true` (qual norma usar: APA, Chicago, ABNT, Vancouver, IEEE, custom)

## Validações Extras (Editor)

- **exige_editor:** `true` (revisão por pares é a alma do acadêmico)
- **regras_editor:**
  - **Obrigatórias em todo acadêmico:**
    - `rigor_argumentativo` (cada afirmação forte tem evidência ou fonte)
    - `citacao_correta` (fonte primária, não Wikipedia, não "ouvi dizer")
    - `consistencia_terminologica` (mesmo conceito = mesmo termo em todo o livro)
    - `anti_plagio` (paráfrase marcada, citação direta em aspas, fonte explícita)
    - `coerencia_interna` (capítulos não se contradizem, terminologia evolui se necessário, com aviso)
    - `reconhecimento_limitacoes` (todo argumento tem escopo, condições de validade, contra-exemplos)
  - **Por subgênero:**
    - **Monografia, Paper-derivado:**
      - `metodologia_transparente` (o leitor pode reproduzir o estudo)
      - `etica_declarada` (financiamento, conflitos de interesse)
    - **Livro-texto:**
      - `progressao_didatica` (do simples ao complexo, com pré-requisitos explícitos)
      - `exercicios_com_gabarito` (não é exercício sem resposta)
      - `caixa_de_erros_comuns` (antecipa onde o aluno vai tropeçar)
    - **Tratado técnico:**
      - `rigor_matematico` (demonstrações completas, sem "fica óbvio que...")
      - `notacao_consistente` (mesmo símbolo = mesma coisa sempre)
    - **Ensaio de humanities:**
      - `voz_propria` (não é só revisão de literatura, é pensamento original)
      - `engajamento_etico` (reconhece a posição do autor, não finge neutralidade impossível)
      - `citacao_primaria_quando_possivel` (cita o original, não quem cita o original)

## Foco Padrão do Usuário

Por subgênero:

**Monografia acadêmica:**
> "Cada argumento precisa de evidência. Cada citação precisa de fonte primária. Cada capítulo avança a tese. Sem achismo, sem 'todo mundo sabe que', sem Wikipedia. Reconheça as limitações do próprio argumento."

**Livro-texto universitário:**
> "O aluno de graduação tem que entender. Conceito novo = analogia + exemplo + definição. Exercícios com gabarito. Pré-requisitos explícitos. Sem 'é óbvio que' — o óbvio pra você não é óbvio pro aluno."

**Paper-derivado / Coletânea:**
> "Cada capítulo é auto-contido, mas o todo conta uma história. Editor que mantém a coerência. Citações cruzadas entre capítulos. Introdução integradora que dá o 'fio condutor'."

**Tratado técnico:**
> "Precisão absoluta. Demonstrações completas. Notação consistente. Índice remissivo denso. Glossário de termos. Sem floreio, sem retórica — só o que é necessário, e tudo o que é necessário."

**Ensaio de humanities:**
> "Pensa em voz alta, mas com rigor. Cita os clássicos E os contemporâneos. Posiciona-se, debate, responde a objeções. Sem 'neutro' falso — o ensaio é do autor, e a voz dele é parte do argumento."

## Template para Usuário Criar Subgênero Personalizado

```
# GENERO: ACADEMICO_[SEU_SUBGENERO]

Base: ACADEMICO (v1.0)

Alteracoes:
- arquétipo_principal: MONOGRAFIA | LIVRO_TEXTO | PAPER_DERIVADO | TRATADO_TECNICO | ENSAIO_HUMANITIES
- pessoa: 3a_onisciente | 3a_instrutiva | 1a_academica | nos_coletivo
- tom: [seus adjetivos]
- vocabulario: cientifico_preciso | academico_denso | formal_controlado
- normas_formatacao: APA_7 | CHICAGO | ABNT | VANCOUVER | IEEE | CUSTOM
- secoes_por_capitulo: [min]-[max]
- exige_editor: true
- bible_extra: [requisitos específicos: metodologia, ética, fontes primárias, etc]
- regras_editor_extras: [suas regras específicas deste subgênero]
```

**Lembrete importante:** a qualidade "acadêmica" de um texto é definida pelo **rigor argumentativo e procedência das fontes**, não pela complexidade do jargão. Um texto simples mas rigoroso é acadêmico. Um texto complexo mas sem fontes não é.
