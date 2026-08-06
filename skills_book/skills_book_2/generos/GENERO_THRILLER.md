# GENERO: THRILLER (Suspense, Mistério, Crime, Espionagem, Psicológico, Terror)

**Versao:** 1.0 (Greenforged Edition)
**Tipo:** THRILLER
**Estrutura:** Capítulos com cenas (2-3 por capítulo), arcos de tensão cumulativos, cliffhangers entre capítulos

**Notas de design:**
- Subgêneros: thriller psicológico, mistério/crime, espionagem/político, legal thriller, thriller médico, terror.
- O que une todos: **tensão** é o motor principal. Cada cena deve aumentar a aposta.
- Inspirado em Save the Cat (Blake Snyder), Story Grid (Shawn Coyne), e 20 Master Plots.

---

## Voz Narrativa

- **pessoa:**
  - `3a_limitada` (padrão — permite claustrofobia, acesso à mente do protagonista)
  - `1a` (thriller confessional, unreliable narrator, atmosfera íntima)
  - `3a_multipla` (thriller de conspiração, vários ângulos do mesmo evento)
  - `1a + 3a_limitada` (híbrido raro, protagonista em 1a + antogonista em 3a)
- **tempo_verbal:**
  - `presente` (padrão moderno — urgência, "isto está acontecendo agora")
  - `passado` (thriller clássico, distância segura, "lembro daquela noite")
- **distancia:**
  - `claustrofobica` (1a ou 3a colada no protagonista, sem ar)
  - `cinematografica` (3a mais ampla, montagem, ação visível)
  - `intima` (thriller psicológico, foco em pensamento)
- **tom:** varia por subgênero. Lista sugerida (escolha 3-5 adjetivos):
  - **Psicológico:** `tenso`, `paranoico`, `analítico`, `visceral`, `claustrofóbico`
  - **Crime/Mistério:** `investigativo`, `cínico`, `hard-boiled`, `paciente`, `meticuloso`
  - **Espionagem:** `paranoico`, `cinético`, `geopolítico`, `frio`, `sofisticado`
  - **Terror:** `assustador`, `atmosférico`, `grotesco`, `psicológico`, `sombrio`
- **vocabulario:**
  - `medio` (acessível mas com algum jargão de domínio)
  - `cinematografico` (frases curtas e longas alternadas como num filme)
  - `tecnico_dominio` (médico: termos médicos; legal: termos jurídicos; espionagem: termos de inteligência)
- **ritmo:**
  - `acelerado_com_pausas_respiratorias` (padrão — tensão sobe, alívio momentâneo, tensão sobe mais)
  - `tique_taque` (alternância entre cena de ação e cena de planejamento, como ticking clock)
  - `escalada_ininterrupta` (thriller de um só fôlego, sem trégua)

## POV

- **padrao:** `3a_limitada` em protagonista, ou `1a` (unreliable narrator)
- **multi_pov:** varia por subgênero:
  - Thriller psicológico: `false` (manter claustrofobia)
  - Espionagem: `true` (2-3 POVs alternados)
  - Crime procedimental: `true` (policial + vilão, "perseguição em dois lados")
- **regras_troca:**
  - Thriller psicológico: NA
  - Espionagem/Procedimental: `cada_capitulo_1_pov` (POV do protagonista da vez)
  - Híbrido: `marcado_explicitamente` (data, hora, nome do POV no header)

## Estrutura de Cena (Unidade de Tensão)

Em thriller, "cena" = **uma unidade de tensão que termina com mudança de estado na estaca**. Sem mudança, não é cena de thriller.

- **min_palavras:** 1200 (thrillers exigem densidade)
- **max_palavras:** 4000 (acima disso, dividir em duas cenas)
- **beats_obrigatorios:** `["gancho_tensao", "objetivo_personagem", "ameaca_imediata", "complicacao_inesperada", "decisao_forcada", "consequencia_inevitavel", "fecho_cliffhanger"]`
- **show_minimo:** 75% (cena de thriller sem ação concreta, sem感官, sem urgência é morta)
- **gancho_tipos:**
  - `pensamento_intrusivo` (protagonista obcecado com algo)
  - `som_ambiguo` (passos no corredor, porta que range)
  - `lacre_de_memoria` (o protagonista lembra um detalhe crucial)
  - `percepcao_distorcida` (algo está fora do lugar, mas ele não sabe o quê)
  - `ticking_clock` ("faltam 4 horas pra o helicóptero pousar")
  - `acao_em_andamento` (cena abre com o protagonista já em perigo)
- **fecho_tipos:**
  - `nova_ameaca` (acaba de resolver uma coisa e outra aparece)
  - `duvida_sobre_realidade` (o leitor não sabe se aquilo aconteceu de verdade)
  - `revelacao_parcial` (descobre 30% da verdade, o resto fica pra depois)
  - `contagem_regressiva` (agora ele tem X horas/minutos)
  - `decisao_irreversivel` (o protagonista faz uma escolha da qual não tem volta)
  - `cliffhanger_visual` (termina com uma imagem potente, uma frase curta)

## Estrutura de Capítulo

- **unidades_por_capitulo:** 2-3 (thrillers têm capítulos curtos, gancho-rápido-cliffhanger)
- **arco_capitulo:** "Tensão sobe → Pico → Queda falsa (respiração mínima) → Nova ameaça maior"
- **recap_final:** `false` (thriller não dá respiro, recapitular mata tensão)
- **dica de design:** termine cada capítulo com um gancho que force o leitor a abrir o próximo. Os 3 melhores ganchos: pergunta não respondida, personagem em perigo imediato, revelação que contradiz o que o leitor achava que sabia.

## Estrutura Global (5 Arquétipos)

### Opção A: Thriller 3 Atos com Twist no Meio (Padrão Moderno)
- **Ato 1 (25%):** Apresentar o protagonista, seu mundo, o evento incitante (crime, descoberta, ameaça). Tensão sobe.
- **Ato 2A (25%):** Protagonista entra no jogo, faz aliados, descobre pistas. Stakes sobem. Midpoint: revelação que muda tudo.
- **Ato 2B (25%):** Vilão contra-ataca, protagonista perde aliados, descobre que o inimigo está mais perto do que pensava. **All is lost.**
- **Ato 3 (25%):** Climax: confronto direto, geralmente físico. Resolução parcial (nem tudo volta ao normal). Gancho para potencial sequência.

### Opção B: Estrutura de Mistério (Detetive-style)
1. **O Crime** (acontece nas primeiras páginas ou é citado logo)
2. **A Investigação** (protagonista-detetive coleta pistas, suspeitos)
3. **A Pista Errada** (red herring que desvia o leitor)
4. **A Descoberta** (protagonista vê o que ninguém viu)
5. **A Confrontação** (acusa o culpado, geralmente em cena pública)
6. **A Revelação Final** (motivo do crime, dimensão maior, por que importa)

### Opção C: Thriller Psicológico (Tensão Interna)
- POV fechado no protagonista (1a ou 3a limitada)
- Antagonista é interno (trauma, vício, memória) ou externo mas invisível (manipulador)
- Estrutura: Normal → Rachadura → Investigação interna → Revelação de si mesmo → Decisão de mudar
- Foco: unreliable narrator, o leitor descobre junto que o protagonista não é confiável

### Opção D: Thriller de Espionagem / Conspiração
- Estrutura: **Múltiplos POVs alternados** (operador, controlador, peça do tabuleiro)
- Cena final de cada capítulo é frequentemente em POV do vilão, mostrando que ele sabe o que o protagonista está fazendo
- Estrutura: Missão → Complicação geopolítica → Traição interna → Sacrifício → Vitória ambígua
- Inspiração: le Carré, John le Carré, Frederick Forsyth, Tom Clancy (pre-2000)

### Opção E: Thriller de Horror/Terror Psicológico
- **Não é horror puro** (que é mais sobre repulsa/susto). É terror com suspense.
- Estrutura: **Construção lenta → evento catalisador → escalada de manifestações → confronto com o "Outro" → resolução ambígua (vitória parcial, custo alto)**
- A "ameaça" pode ser sobrenatural, psicológica (demônio interno), ou real (serial killer, gaslighting)
- Inspiração: Shirley Jackson, Stephen King (sobrenatural), Gillian Flynn (psicológico)

## Bible Requisitos

A Bible de thriller carrega o **mundo das ameaças** e a **psicologia dos personagens**. Quanto mais detalhada, melhor a tensão é mantida.

- **personagens_detalhados:** `true` (fichas profundas, especialmente do protagonista e do vilão)
- **worldbuilding_profundo:** `false` na maioria, `true` em thriller de espionagem ou sci-fi
- **cronologia_rigida:** `true` (thrillers dependem de timing — relógios, contagens regressivas, alibis)
- **sistema_magia_regras:** `true` se thriller sobrenatural (regras do "Outro")
- **conceitos_chave:** `true` (temas centrais — paranoia, confiança, identidade, verdade)
- **mapa_de_ameacas:** `true` (quem quer o quê, como, por que, quais recursos)
- **arvore_de_revelacoes:** `true` (o que o leitor sabe vs o que o protagonista sabe vs o que é verdade, em cada capítulo)
- **linha_do_tempo_paralela:** `true` (POVs diferentes podem estar em tempos diferentes, ex: vilão 2 dias antes do protagonista)
- **locais_detalhados:** `true` (casa do protagonista, esconderijo do vilão, rota de fuga, etc)
- **fios_narrativos:** `true` (subplots devem servir a tensão, não serem ornamento)
- **armadilhas_e_red_herrings:** `true` (planejar onde o leitor vai ser enganado)
- **glossario_tecnico:** depende do subgênero (médico, legal, espionagem)

## Validações Extras (Editor)

- **exige_editor:** `true` (essencial para thriller)
- **regras_editor:**
  - **Obrigatórias em todo thriller:**
    - `pacing_tensao_crescente` (cada cena aumenta a aposta)
    - `show_dont_tell_tensao` ("estava nervoso" é TELL; "a caneta escapou da mão" é SHOW)
    - `ancoragem_sensorial` (claustrofobia vem de感官 detalhe: cheiro de cigarro frio, luz piscando)
    - `cliffhanger_funcional` (o gancho do capítulo não pode ser gratuito, tem que ser consequencial)
    - `consistencia_personagem` (vilão coerente com a motivação declarada)
    - `verdade_emocional` (protagonista em perigo precisa parecer real, não cinematográfico)
  - **Específicas de mistério:**
    - `pistas_plantadas_justas` (Fair Play de Ronald Knox: o leitor tem acesso a todas as pistas, mas não vê o padrão)
    - `red_herring_com_propósito` (pista falsa convincente, mas que não é gratuita)
  - **Específicas de thriller psicológico:**
    - `unreliable_narrator_consistente` (as mentiras do narrador são coerentes com o que ele quer esconder)
    - `escalada_interna_proporcional` (a paranoia cresce organicamente, não de repente)
  - **Específicas de espionagem:**
    - `multi_pov_balanceado` (POVs rivais têm tempo de tela comparável)
    - `geopolitica_consistente` (não inventa países, não inventa tecnologias)

## Foco Padrão do Usuário

> "Cada capítulo deve terminar com o leitor OBRIGADO a abrir o próximo. Tensão é cumulativa, não decorativa. O protagonista pode errar, pode duvidar de si mesmo, pode perder, mas nunca pode ser chato. Ameaça real, consequências reais, custo emocional real. O vilão não é mau porque sim, ele tem lógica interna. Diálogos com subtexto — o que se diz é menos importante que o que não se diz."

## Template para Usuário Criar Subgênero Personalizado

```
# GENERO: THRILLER_[SEU_SUBGENERO]

Base: THRILLER (v1.0)

Alteracoes:
- arquétipo_principal: TRES_ATOS_TWIST | MISTERIO_DETETIVE | PSICOLOGICO | ESPIONAGEM | TERROR
- pessoa: 3a_limitada | 1a | 3a_multipla
- tom: [seus adjetivos]
- ritmo: acelerado_com_pausas | tique_taque | escalada_ininterrupta
- multi_pov: true/false
- unidades_por_capitulo: [min]-[max]
- exige_editor: true
- bible_extra: [requisitos específicos: árvore de revelações, red herrings, mapa de ameaças]
- regras_editor_extras: [suas regras específicas deste subgênero]
```
