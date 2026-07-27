# GENERO: NAO-FICCAO (EDUCATIVO / CIENCIA POPULAR / BUSINESS / BIOGRAFIA)

**Versao:** 1.0
**Tipo:** NAO_FICCAO
**Estrutura:** Capítulos temáticos (não necessariamente narrativos), cada um com seções/cenas conceituais

---

## Voz Narrativa

- **pessoa:** `2a` (voce - direto ao leitor) | `3a_autoral` (voz do autor especialista) | `1a` (memoir-style)
- **tempo_verbal:** `presente` (conceitos atemporais) | `passado` (historia/caso)
- **distancia:** `mentor` | `parceiro` | `autoridade_acessivel`
- **tom:** `claro`, `estruturado`, `encorajador`, `baseado_em_evidencia`
- **vocabulario:** `acessivel` (jargao explicado na primeira vez) | `tecnico_leve` (publico informado)
- **ritmo:** `modular` (conceito -> analogia -> aplicacao -> exercicio/reflexao)

## POV

- **padrao:** `autor_especialista` (voz consistente do autor)
- **multi_pov:** `false` (salvo biografia multi-sujeto)
- **head_hopping:** `NA` (nao ha POV de personagem)

## Estrutura de "Cena" (Unidade Conceitual)

Em nao-ficcao, "cena" = **secao conceitual** ou **modulo de aprendizado**.

- **min_palavras:** 800
- **max_palavras:** 4000
- **beats_obrigatorios:** `[gancho_conceitual, explicacao_mecanismo, analogia, evidencia/dado, aplicacao_pratica, resumo/ponte]`
- **show_minimo:** `40%` (estudos de caso, historias, exemplos concretos, dados visuais)
- **gancho_tipos:** `pergunta_provocativa`, `estatistica_chocante`, `historia_rapida`, `paradoxo`, `promessa_beneficio`
- **fecho_tipos:** `resumo_chave`, `exercicio_acao`, `pergunta_reflexao`, `ponte_proximo_conceito`

## Estrutura de Capitulo

- **secoes_por_capitulo:** 3 a 6 (cada secao = uma "cena" no sistema)
- **arco_capitulo:** Um conceito/argumento principal por capitulo, desenvolvido em secoes
- **recap_final:** `true` (resumo do capitulo + acao sugerida)

## Estrutura Global (Arquetipos)

### Opcao A: Problema -> Solucao (How-to / Self-help / Business)
1. **O Problema** (dor, custo, por que importa)
2. **A Causa Raiz** (mecanismo, ciencia, psicologia)
3. **A Solucao** (framework, metodo, passos)
4. **Implementacao** (plano 30/60/90 dias, ferramentas)
5. **Obstaculos Comuns** (troubleshooting)
6. **Manutencao / Vida Longa** (habitos, identidade)

### Opcao B: Grande Ideia (Big Idea / Pop Science)
1. **O Paradigma Atual** (o que todos acham)
2. **A Descoberta/Insight** (o que a ciencia mostra diferente)
3. **O Mecanismo** (como funciona, evidencia)
4. **Implicacoes** (saude, sociedade, futuro)
5. **Protocolo Pratico** (o que fazer hoje)
6. **Perguntas Frequentes / Mitos**

### Opcao C: Biografia / Historia Narrativa
- Cronologico com saltos tematicos
- Cada capitulo = periodo + tema
- Arco narrativo classico (3 atos) aplicado a vida real

### Opcao D: Investigativo / Jornalismo de Longa Forma
- Cena de abertura (gancho humano)
- Investigacao em camadas (cebola)
- Revelacoes escalonadas
- Conclusao com impacto

## Bible Requisitos

- **personagens_detalhados:** `true` se biografico / `false` se conceitual
- **conceitos_chave:** `true` (glossario, definicoes canonicas, frameworks)
- **estudos_citados:** `true` (bibliografia anotada: estudo, n, achado, limitacoes)
- **cronologia_rigida:** `true` se historico/biografico / `false` se conceitual
- **protocolos_praticos:** `true` (passos acionaveis, dosagens, checklists)
- **mitos_comuns:** `true` (lista de misconceptions para desmistificar)

## Validacoes Extras (Editor)

- **exige_editor:** `true` (recomendado para clareza e pacing)
- **regras_editor:**
  - `clareza_conceitual` (conceito novo = analogia + exemplo + definicao)
  - `densidade_evidencia` (cada afirmacao forte tem lastro)
  - `aplicabilidade` (leitor sabe O QUE FAZER ao fim de cada secao)
  - `progressao_dificuldade` (do simples para complexo)
  - `variedade_exemplos` (casos diversos, nao repetitivos)
  - `ancoragem_concreta` (evitar abstrato flutuante)
  - `tom_respeitoso` (nao condescendente, nao academico demais)

## Foco do Usuario (Exemplos tipicos)

> "Traga os dados cientificos mas conte como historia. Cada capitulo = um experimento/descoberta. Humor leve nas transicoes."
> "Foque no protocolo pratico. O leitor quer saber o que fazer segunda-feira de manha. Teoria so o necessario."
> "Desmistifique conceitos errados comuns. Use analogias visuais fortes. Evite jargao."
> "Biografia com foco nas decisoes criticas. Mostre o processo de pensamento, nao so os fatos."

---

## Template para Usuario Criar Subgenero Personalizado

```
# GENERO: NAO_FICCAO_[SEU_SUBGENERO]

Base: NAO_FICCAO

Alteracoes:
- pessoa: 2a | 3a_autoral | 1a
- tom: [seus adjetivos]
- ritmo: [padrao]
- estrutura_global: PROBLEMA_SOLUCAO | GRANDE_IDEIA | BIOGRAFIA | INVESTIGATIVO
- secoes_por_capitulo: [min]-[max]
- show_minimo: [XX%]
- exige_editor: true/false
- bible_extra: [requisitos especificos: estudos, protocolos, mitos, cronologia]
```