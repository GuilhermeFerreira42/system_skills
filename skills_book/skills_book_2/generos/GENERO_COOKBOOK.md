# GENERO: COOKBOOK (Livro de Receitas, Culinária Estruturada, Cultura Gastronômica)

**Versao:** 1.0 (Greenforged Edition)
**Tipo:** COOKBOOK
**Estrutura:** Capítulos temáticos ou por técnica → Receitas → Variações

**Notas de design:**
- O cookbook é o **gênero prescritivo** por excelência. Cada "cena" é uma receita completa.
- Subgêneros: regional/tradicional, técnico (fermentação, sous vide, defumação), sazonal, celebridade, dieta específica, viagem gastronômica.
- Inspirado em **Ratio (Michael Ruhlman)**, **The Food Lab (J. Kenji López-Alt)**, e na tradição de **Joy of Cooking (Irma Rombauer)**.
- **Atenção crítica:** o cookbook de culinária é a aplicação mais óbvia deste padrão, mas a mesma estrutura serve pra **outros livros prescritivos**: jardinagem, DIY artesanal, fitoterapia, cocktails, perfumes, sabonetes, etc. O "ingrediente" vira "material", o "tempo de cozimento" vira "tempo de cura".

---

## Voz Narrativa

- **pessoa:**
  - `2a_imperativa` (você faça, você misture, você prove) — padrão em receitas
  - `3a_instrutiva` (o cozinheiro adiciona, o leitor observa) — narrativa gastronômica
  - `1a_pessoal` (minha avó fazia assim, eu descobri que...) — memoir culinário
  - `nós_coletivo` (nossa família, nosso povo) — cookbooks tradicionais
- **tempo_verbal:**
  - `presente` (padrão — "Adicione a cebola, refogue por 5 minutos")
  - `imperativo` (em listas de ingredientes: "500g de farinha")
  - `passado` (em narrativa introdutória: "minha avó fazia assim em 1975")
- **distancia:**
  - `instrutiva_direta` (você segue a receita e pronto)
  - `didatica_por_tras` (explica o "porquê" antes do "como" — Ruhlman/López-Alt style)
  - `acolhedora` (convida pra cozinha, dá dicas, antecipa dúvidas)
- **tom:** varia por subgênero. Lista sugerida (escolha 3-4 adjetivos):
  - **Tradicional/Regional:** `acolhedor`, `respeitoso`, `saudoso`, `didático`
  - **Técnico/Científico:** `curioso`, `experimental`, `preciso`, `desmistificador`
  - **Celebridade/Auto-biográfico:** `pessoal`, `vulnerável`, `animado`, `intimista`
  - **Sazonal/Lista de Mercado:** `prático`, `econômico`, `saludável`, `organizado`
- **vocabulario:**
  - `culinario_tecnico` (brunoise, mise en place, emulsionar)
  - `cotidiano` (mãe, filha, vizinha — quem nunca cozinhou entende)
  - `cientifico` (Maillard, gelatinização, osmose) — quando explica a ciência
  - `regional` (termos locais do lugar, sotaque, ingredientes do terroir)
- **ritmo:**
  - `passo_a_passo_rigido` (receita pura)
  - `narrativo_com_receita` (história → receita → variações)
  - `cientifico_com_experimento` (hipótese → teste → resultado → ajuste)

## POV

- **padrao:** `autor_culinario` (chef, dona de casa, expert) ou `comunidade_tradicional`
- **multi_pov:** `false` por padrão. `true` em cookbooks coletivos (cada chef contribui com suas receitas)
- **head_hopping:** NA (receitas não têm personagens)

## Estrutura de "Cena" (Unidade = RECEITA)

Em cookbook, "cena" = **uma receita completa, do início ao fim**. A estrutura é RÍGIDA porque o leitor vai usar isso na cozinha, com as mãos sujas, e não pode se perder.

- **min_palavras:** 300 (receita curta, 1 parágrafo)
- **max_palavras:** 1500 (receita longa, com variações e história)
- **beats_obrigatorios:** `["nome_da_receita", "historia_origem_curta", "tempo_total", "rendimento", "dificuldade", "ingredientes_com_quantidades", "modo_de_preparo_passo_a_passo", "notas_do_chef", "variacoes_e_substituicoes", "conservacao_se_aplicavel"]`
- **show_minimo:** 50% (fotos, indicadores de ponto, "massa lisa e brilhante", "cheiro de tostado")
- **gancho_tipos:**
  - `historia_pessoal` ("Essa receita é da minha avó italiana")
  - `paradoxo_culinario` ("Quanto mais frio, melhor")
  - `promessa` ("Em 15 minutos você tem um jantar completo")
  - `desmistificacao` ("Você não precisa de termômetro pra esse pão")
- **fecho_tipos:**
  - `nota_do_chef` (dica insider)
  - `variacao` (versão vegana, versão regional, versão rápida)
  - `combinacao_servir` ("Fica ótimo com X vinho Y")
  - `armazenamento` ("Guarda na geladeira por até 3 dias")

## Estrutura de Capítulo

- **receitas_por_capitulo:** 5-15 (não menos, não mais)
- **tema_capitulo:** varia por arquétipo
- **recap_final:** `true` (lista de ingredientes da "despensa básica" do capítulo + referências cruzadas)

## Estrutura Global (5 Arquétipos)

### Opção A: Por Ingrediente Principal
- Capítulos = Ingredientes-estrela: "O Livro da Batata", "A Bíblia do Tomate", "A Enciclopédia do Queijo"
- 10-15 receitas por ingrediente, com diferentes técnicas
- Forte identidade visual, fácil de usar como referência

### Opção B: Por Técnica Culinária
- Capítulos = Técnicas: "Cortar", "Fritar", "Cozinhar no Vapor", "Fermentar", "Defumar", "Confit"
- 8-12 receitas por técnica, com nível crescente de dificuldade
- Educacional, ideal pra quem quer **aprender a cozinhar**, não só seguir receita

### Opção C: Por Refeição / Ocasião
- Capítulos = Momentos: "Café da Manhã", "Almoço de Domingo", "Jantar Romântico", "Marmita da Semana", "Ceia de Natal"
- 6-10 receitas por ocasião
- Foco em **composição de menu**: como um prato conversa com o outro

### Opção D: Por Estação / Sazonalidade
- Capítulos = Estações: "Outono", "Inverno", "Primavera", "Verão"
- 8-12 receitas por estação
- Forte identidade com produtos sazonais, terroir, calendário agrícola
- Educativo sobre ciclos naturais

### Opção E: Por Cozinha / Cultura
- Capítulos = Regiões: "Itália", "México", "Japão", "Brasil-Nordeste", "Líbano", "Tailândia"
- 8-15 receitas por região
- Educativo sobre cultura, história, contexto social
- Sensível a representação cultural (evitar apropriação, dar crédito)

## Bible Requisitos

A Bible de cookbook carrega o **inventário de ingredientes, técnicas, equipamentos, e princípios** que sustentam o livro.

- **glossario_culinario:** `true` (todos os termos técnicos definidos na primeira ocorrência)
- **tabela_equivalencias:** `true` (xícaras → ml, oz → gramas, °F → °C, gás vs elétrico)
- **temperos_e_padroes:** `true` (salgado ideal, ponto da carne, texturas reconhecíveis)
- **ingredientes_regionais:** `true` (o que substitui X em cada lugar, sazonalidade)
- **equipamentos_essenciais:** `true` (panelas mínimas, utensílios, forno se for o caso)
- **seguranca_alimentar:** `true` (temperaturas seguras, conservação, alergias comuns)
- **tabela_nutricional:** `true` se for cookbook de saúde/dieta, `false` caso contrário
- **fornecedores_e_marcas:** `true` se for tradicional/artesanal, `false` se for genérico
- **historia_origem:** `true` (origem da receita, contexto cultural, quem popularizou)
- **variacoes_regionais:** `true` (mesma receita em versões diferentes por região)
- **dificuldade_classificacao:** `true` (1-5 estrelas, ou iniciante/intermediário/avançado)
- **tempo_total_estimado:** `true` (preparo + cozimento, em minutos)

## Validações Extras (Editor)

- **exige_editor:** `true` (cookbook com erro é livro que não funciona na cozinha)
- **regras_editor:**
  - **Obrigatórias em todo cookbook:**
    - `precisao_ingredientes` (quantidade, unidade, marca quando relevante)
    - `completude_passo_a_passo` (nenhum passo "óbvio" pulado)
    - `testabilidade` (a receita foi testada por alguém que não é o autor?)
    - `consistencia_terminologica` (mesma técnica = mesmo nome sempre)
    - `seguranca_alimentar` (não ensina nada que cause intoxicação)
  - **Tradicional/Cultural:**
    - `respeito_origem` (não inventa tradições, dá crédito à fonte)
    - `autorizacao_receita` (receita de família? de chef famoso? de restaurante?)
  - **Técnico/Científico:**
    - `explicacao_por_que` (por que o ovo emulsiona? por que o pão cresce?)
    - `precisao_cientifica` (Maillard a 154°C, gelatinização a 60-70°C, etc)
  - **Sazonal/Lista de Mercado:**
    - `custo_estimado` (por receita, em faixa de preço)
    - `onde_encontrar` (feira, supermercado, empório, internet)
  - **Saudável/Dieta:**
    - `informacao_nutricional` (calorias, macros, micronutrientes relevantes)
    - `substituicoes_para_alergias` (sem glúten, sem lactose, sem castanhas)
    - `por_que_funciona` (base científica da alegação de saúde)

## Foco Padrão do Usuário

Por subgênero:

**Tradicional/Regional:**
> "Respeite a origem. Não invente tradições. Créditos sempre que possível. Ingredientes locais quando o leitor é local, substituições quando não é. Sabores que evocam memória."

**Técnico/Científico:**
> "Explique o porquê. A ciência por trás do cozido. Experimentos que mostram o que funciona e o que não funciona. Fotografia de perto. Números onde ajudarem."

**Saudável/Dieta:**
> "Informação nutricional em cada receita. Substituições para restrições comuns. Por que esse prato é saudável (ou não é). Sem modismo. Sustentável a longo prazo."

**Celebridade/Confessional:**
> "História pessoal primeiro, receita depois. Mostre o fracasso também, não só o sucesso. Vulnerabilidade gera confiança."

**Viagem Gastronômica:**
> "Contexto cultural, não só receita. Como se come nesse lugar, com quem, em que momento. O sabor é indissociável do ritual."

## Template para Usuário Criar Subgênero Personalizado

```
# GENERO: COOKBOOK_[SEU_SUBGENERO]

Base: COOKBOOK (v1.0)

Alteracoes:
- arquétipo_principal: INGREDIENTE_ESTRELA | TECNICA | REFEICAO_OCASIAO | SAZONAL | COZINHA_CULTURA
- pessoa: 2a_imperativa | 3a_instrutiva | 1a_pessoal | nos_coletivo
- tom: [seus adjetivos]
- vocabulario: culinario_tecnico | cotidiano | cientifico | regional
- receitas_por_capitulo: [min]-[max]
- exige_editor: true
- bible_extra: [requisitos específicos: tabela nutricional, fornecedores, segurança alimentar, etc]
- regras_editor_extras: [suas regras específicas deste subgênero]
```

**Lembrete importante:** este padrão de "receita" se aplica a outros domínios prescritivos. Se tu quer fazer um livro de **fitoterapia caseira**, **sabonetes artesanais**, **jardinagem doméstica**, **cocktails**, **cosméticos naturais**, **DIY de marcenaria**, ou qualquer outro domínio onde há "ingrediente → técnica → produto final", a estrutura deste gênero se aplica com adaptações mínimas (substituir "ingrediente" por "material", "cozimento" por "cura", "temperatura" por "tempo de descanso", etc).
