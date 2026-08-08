# GENERO: NAO-FICCAO (Educativo, Ciencia Popular, Business, Biografia, Self-Help, Saude, Financas, Filosofia Pratica)

**Versao:** 2.0 (Greenforged Edition - Agnóstico de tema)
**Tipo:** NAO_FICCAO
**Estrutura:** Capítulos temáticos com cenas conceituais. A "cena" é uma seção de aprendizado (não tem personagem nem ação dramática).

**Mudanças da v1.0 pra v2.0:**
- Removido viés implícito pra temas de ecommerce/negócios (que estava na v1).
- Adicionados subgêneros mais amplos (saúde, finanças, filosofia prática, história).
- Mantidos os 4 arquétipos clássicos (Problema→Solução, Grande Ideia, Biografia, Investigativo).
- Adicionado arquétipo novo: "Sabedoria Acumulada" (filosofia prática, ensaio reflexivo).
- Show mínimo ajustado por arquétipo.

---

## Voz Narrativa

- **pessoa:**
  - `2a` (voce - direto ao leitor) — padrão em self-help, business, saúde
  - `3a_autoral` (voz do autor especialista) — padrão em ciência popular, finanças
  - `1a` (memoir-style) — quando a não-ficção tem viés autobiográfico
- **tempo_verbal:**
  - `presente` (conceitos atemporais) — padrão em ciência, filosofia
  - `passado` (história, caso) — biografia, jornalismo investigativo
  - `misto_controlado` — alternância presente (conceito) + passado (caso)
- **distancia:**
  - `mentor` — quem te guia com experiência
  - `parceiro` — quem descobre junto contigo
  - `autoridade_acessivel` — quem sabe muito mas fala simples
  - `amigo_intelectual` — quem te faz pensar sem te dar respostas
- **tom:** varia por subgênero. Lista sugerida (escolha 3-4 adjetivos):
  - Ciência/Saúde: `claro`, `evidência-baseado`, `desmistificador`, `cauteloso`
  - Business/Self-help: `direto`, `pragmatico`, `encorajador`, `acionavel`
  - Filosofia: `reflexivo`, `provocativo`, `humilde`, `inquieto`
  - Biografia/História: `narrativo`, `intimo`, `respeitoso`, `vulneravel`
- **vocabulario:**
  - `acessivel` (jargão explicado na primeira vez) — padrão
  - `tecnico_leve` (público informado)
  - `cientifico_preciso` (papers, papers revisados)
- **ritmo:**
  - `modular` (conceito → analogia → aplicação → exercício/reflexão) — padrão
  - `narrativo` (caso real → lição → aplicação) — biografia, jornalismo
  - `reflexivo` (premissa → argumento → exemplo → questionamento) — filosofia

## POV

- **padrao:** `autor_especialista` (voz consistente do autor) ou `narrador_jornalista` (em investigativo)
- **multi_pov:** `false` por padrão. `true` APENAS em biografia multi-sujeito (ex: "Steve Jobs e Bill Gates")
- **head_hopping:** NA (não há POV de personagem)

## Estrutura de "Cena" (Unidade Conceitual)

Em não-ficção, "cena" = **seção conceitual** ou **módulo de aprendizado**. Não há personagem, não há ação dramática. Há **ideia → explicação → prova → aplicação**.

- **min_palavras:** 800 (cenas menores viram listas, não capítulos)
- **max_palavras:** 5000 (acima disso, o leitor cansa)
- **beats_obrigatorios:** (varia por arquétipo, ver abaixo)
- **show_minimo:** 40% por padrão (estudos de caso, histórias, exemplos concretos, dados visuais)
- **gancho_tipos:**
  - `pergunta_provocativa` ("E se a sua memória não existisse?")
  - `estatistica_chocante` ("40% dos brasileiros estão desidratados, e não sabem")
  - `historia_rapida` ("Em 1971, um cirurgião francês...")
  - `paradoxo` ("Quanto mais você dorme, mais cansado fica")
  - `promessa_beneficio` ("Ao fim deste capítulo, você vai entender por que...")
- **fecho_tipos:**
  - `resumo_chave` (3 bullets do que foi aprendido)
  - `exercicio_acao` (faça X antes de dormir hoje)
  - `pergunta_reflexao` (e você, o que faria?)
  - `ponte_proximo_conceito` ("No próximo capítulo, a gente vai ver...")

## Beats por Arquétipo

| Arquétipo | Beats da cena |
|-----------|---------------|
| **Problema → Solução** (self-help, business, saúde) | gancho_dor, paradigma_atual, causa_raiz, solucao_revelada, **ANALOGIA**, evidencia, aplicacao_acao, resumo |
| **Grande Ideia** (ciência popular, filosofia) | **gancho_conceitual**, descoberta_insight, mecanismo, **ANALOGIA**, evidencia, implicacao, resumo_ponte |
| **Biografia** (história de vida, memoir não-ficção) | cenario_epoca, personagem_em_jogo, virada_dramatica, licao_extraida, ponte_tematica |
| **Investigativo** (jornalismo de longa forma) | gancho_humano, investigacao_camada_1, revelacao_parcial, escalada, virada_final, impacto |
| **Sabedoria Acumulada** (filosofia prática, ensaio) | observacao_cotidiana, pergunta_filosofica, argumento_principal, contraargumento, exemplo, reflexao_pessoal |

**REGRA DE OURO (contrato de voz):** todo conceito técnico/abstrato exige **analogia obrigatória** com 3 movimentos (familiar → complicação → mapeamento explícito). O beat `ANALOGIA` é obrigatório e não pode ser omitido por "economia de espaço".

## Estrutura de Capítulo

- **secoes_por_capitulo:** 3 a 6 (cada seção = uma "cena" no sistema)
- **arco_capitulo:** Um conceito/argumento principal por capítulo, desenvolvido em seções que progridem do simples para o complexo, ou da pergunta para a resposta
- **recap_final:** `true` (resumo do capítulo + ação sugerida + lista de referências)

## Estrutura Global (5 Arquétipos)

### Opção A: Problema → Solução (How-to / Self-help / Business / Saúde Prática)
1. **O Problema** (dor, custo, por que importa)
2. **A Causa Raiz** (mecanismo, ciência, psicologia)
3. **A Solução** (framework, método, passos)
4. **Implementação** (plano 30/60/90 dias, ferramentas, dosagens, frequências)
5. **Obstáculos Comuns** (troubleshooting, por que o método falha em alguns casos)
6. **Manutenção / Vida Longa** (hábitos, identidade, identidade, o que muda depois de 1 ano)

### Opção B: Grande Ideia (Big Idea / Pop Science / Filosofia)
1. **O Paradigma Atual** (o que todos acham)
2. **A Descoberta/Insight** (o que a ciência ou a filosofia mostra diferente)
3. **O Mecanismo** (como funciona, evidência, lógica)
4. **Implicações** (saúde, sociedade, futuro, sentido)
5. **Protocolo Prático** (o que fazer hoje, se aplicável)
6. **Perguntas Frequentes / Mitos** (desmistificação)

### Opção C: Biografia / História Narrativa
- Cronológico com saltos temáticos
- Cada capítulo = período + tema
- Arco narrativo clássico (3 atos) aplicado a vida real
- Persona é o biografado, não o autor

### Opção D: Investigativo / Jornalismo de Longa Forma
- Cena de abertura (gancho humano)
- Investigação em camadas (cebola)
- Revelações escalonadas
- Conclusão com impacto social

### Opção E: Sabedoria Acumulada (Filosofia Prática / Ensaio Reflexivo) — NOVO
- Coleta de observações da vida
- Cada capítulo = uma pergunta filosófica
- Argumentos contra e a favor
- Reflexão pessoal do autor
- Não há "resposta certa" — há desenvolvimento de pensamento
- Exemplos: Meditações de Marco Aurélio, A Arte de Viver (Epicteto), ensaios de Montaigne

## Bible Requisitos

A Bible de não-ficção carrega o **conteúdo verificável** que a obra vai abordar. A profundidade varia por arquétipo:

- **personagens_detalhados:** `true` se biográfico / `false` se conceitual
- **conceitos_chave:** `true` (glossário, definições canônicas, frameworks) — sempre
- **estudos_citados:** `true` (bibliografia anotada: estudo, n, achado, limitações) — em ciência/saúde/finanças
- **cronologia_rigida:** `true` se histórico/biográfico / `false` se conceitual
- **protocolos_praticos:** `true` (passos acionáveis, dosagens, frequências, checklists) — em self-help/business/saúde
- **mitos_comuns:** `true` (lista de misconceptions para desmistificar) — em ciência/saúde/finanças
- **referencias_bibliograficas:** `true` (papers, livros, fontes primárias) — em todos os arquétipos, com profundidade variável
- **glossario_termos:** `true` (siglas, jargões, termos técnicos) — sempre que houver jargão

## Validações Extras (Editor)

- **exige_editor:** `true` (recomendado para clareza e pacing)
- **regras_editor:** (varia por arquétipo)
  - **Todos os arquétipos:**
    - `clareza_conceitual` (conceito novo = analogia + exemplo + definição)
    - `densidade_evidencia` (cada afirmação forte tem lastro)
    - `variedade_exemplos` (casos diversos, não repetitivos)
    - `ancoragem_concreta` (evitar abstrato flutuante)
    - `tom_respeitoso` (não condescendente, não acadêmico demais)
  - **Problema→Solução, Grande Ideia:**
    - `aplicabilidade` (leitor sabe O QUE FAZER ao fim de cada seção)
    - `progressao_dificuldade` (do simples para complexo)
  - **Biografia, Investigativo:**
    - `narrative_hook` (cada abertura prende o leitor)
    - `transicao_entre_cenas` (não é切り, é costura)
  - **Sabedoria Acumulada:**
    - `profundidade_nao_superficialidade` (evita frases de almanaque)
    - `originalidade_pensamento` (não é coleção de citações famosas)

## Foco do Usuário (Exemplos típicos por subgênero)

**Saúde/Ciência Popular:**
> "Traga dados mas conte como história. Cada capítulo = um experimento/descoberta. Use analogias visuais. Evite jargão sem explicação. Desmistifique mitos comuns."

**Business/Self-Help:**
> "Foque no protocolo prático. O leitor quer saber o que fazer segunda-feira de manhã. Teoria só o necessário. Inclua checklists e frameworks nomeados."

**Finanças/Economia:**
> "Números antes de tudo. Cada afirmação tem tabela, gráfico ou simulação. Cuidado com promessas. Histórico de mercado, não achismo."

**Filosofia/Ensaio:**
> "Voz de quem pensa, não de quem sabe. Pergunte mais do que responda. Contra-argumentos antes de fechar. Não é autoajuda, é pensamento."

**Biografia/História:**
> "Foco nas decisões críticas. Mostre o processo de pensamento, não só os fatos. Contextualize a época. Use documentos primários quando possível."

**Jornalismo Investigativo:**
> "Cada fato com fonte. Cada personagem com contexto. Revelações escalonadas. A conclusão muda alguma coisa no mundo."

## Template para Usuário Criar Subgênero Personalizado

```
# GENERO: NAO_FICCAO_[SEU_SUBGENERO]

Base: NAO_FICCAO (v2.0)

Alteracoes:
- arquétipo_principal: PROBLEMA_SOLUCAO | GRANDE_IDEIA | BIOGRAFIA | INVESTIGATIVO | SABEDORIA_ACUMULADA
- pessoa: 2a | 3a_autoral | 1a
- tom: [seus adjetivos]
- ritmo: modular | narrativo | reflexivo
- secoes_por_capitulo: [min]-[max]
- show_minimo: [XX%]
- exige_editor: true/false
- bible_extra: [requisitos específicos: estudos, protocolos, mitos, cronologia, glossario]
- regras_editor_extras: [suas regras específicas deste subgênero]
```

**Importante:** este gênero é herança de NAO_FICCAO v1.0. Subgêneros específicos que dependiam de v1 (como `PODBOOK_BRUNO`, dedicado a ecommerce) continuam funcionando com v1 e não devem ser migrados pra v2 sem revisão manual.
