# GENERO: MEMORIAS / AUTOBIOGRAFIA

**Versao:** 1.0
**Tipo:** MEMOIR (hibrido: narrativa pessoal + reflexao + verdade emocional)
**Estrutura:** Capítulos temáticos-cronológicos (não estritamente lineares)

---

## Voz Narrativa

- **pessoa:** `1a` (obrigatorio - voz do autor)
- **tempo_verbal:** `passado` (memoria) + `presente` (reflexao atual) - alternancia controlada
- **distancia:** `intima`, `vulneravel`, `retrospectiva`
- **tom:** `honesto`, `reflexivo`, `especifico`, `universal_no_pessoal`
- **vocabulario:** `pessoal`, `sensorial`, `evocativo` (nao academico)
- **ritmo:** `ondulatorio` (memoria viva <-> reflexao presente)

## POV

- **padrao:** `1a_autoral` (o autor como protagonista E narrador)
- **dual_temporalidade:** `true` (eu-do-passado vs eu-do-presente)
- **regras_troca:** Marcada explicitamente (quebra de linha, transicao, ou marcador temporal)

## Estrutura de Cena (Unidade de Memoria)

- **min_palavras:** 1000
- **max_palavras:** 5000
- **beats_obrigatorios:** `[gatilho_memoria, cena_vivida_detalhada, sensacao_corporal, reflexao_atual, significado/ponte]`
- **show_minimo:** `80%` (memoria VIVIDA, nao resumo)
- **gancho_tipos:** `objeto_gatilho`, `cheiro_som`, `frase_ouvida`, `lugar_revisitado`, `pergunta_filha`
- **fecho_tipos:** `insight_atual`, `pergunta_aberta`, `conexao_tema_central`, `imagem_final`

## Estrutura de Capitulo

- **memorias_por_capitulo:** 2 a 4 (cada memoria = uma "cena")
- **tema_capitulo:** Cada capitulo orbita um tema (pai, vergonha, primeira vez, perda, identidade)
- **arco_capitulo:** Memoria(s) -> Reflexao -> Insight -> Ponte pro proximo tema

## Estrutura Global (Arquetipos)

### Opcao A: Tematico (Mais comum em memoir literario)
- Capitulos por tema: "A Cozinha da Mae", "O Silencio do Pai", "A Primeira Mentira", "O Corpo que Muda"
- Cronologia interna a cada capitulo, mas ordem dos capitulos = logica tematica

### Opcao B: Cronologico com Saltos (Coming of Age)
- Infancia -> Adolescencia -> Juventude -> Adultez
- Mas com flashforwards/flashbacks controlados para tema

### Opcao C: Investigativo (Memoir + Jornalismo)
- Autor investiga proprio passado (arquivos, entrevistas, lugares)
- Cada capitulo = uma investigacao + o que descobriu sobre si

### Opcao D: Fragmentado / Mosaico (Experimental)
- Vignettes curtas, ordem nao-linear, leitor monta o quebra-cabeca
- Requer Bible rigorosa de fios narrativos

## Bible Requisitos (CRITICOS para Memoir)

- **personagens_detalhados:** `true` (pessoas reais = fichas: nome, relacao, personalidade, falas tipicas, arco na vida do autor)
- **cronologia_rigida:** `true` (timeline mestre: datas, idades, locais, eventos historicos paralelos)
- **locais_detalhados:** `true` (casa da avo, rua da escola, quarto do hospital - mapa sensorial)
- **fios_narrativos:** `true` (temas recorrentes: abandono, busca por voz, relacao com dinheiro, corpo)
- **versao_oficial_vs_verdade:** `true` (o que a familia conta vs o que autor lembra vs o que documentos mostram)
- **etica_privacidade:** `true` (nomes alterados? composites? consentimentos? notas de rodapé?)

## Validacoes Extras (Editor)

- **exige_editor:** `true` (essencial para memoir)
- **regras_editor:**
  - `verdade_emocional` (fatos servem a verdade emocional, nao inverso)
  - `especificidade_sensorial` (cheiro, textura, som, sabor, propriocepcao - NAO generico)
  - `reflexao_nao_explicacao` (mostre o momento, refleta depois; nao explique o sentimento)
  - `dual_temporalidade_clara` (leitor sempre sabe: isto e memoria OU isto e reflexao agora)
  - `personagens_reais_3d` (ninguem e so vilao ou heroi; complexidade)
  - `arco_transformacao` (autor muda do inicio ao fim - qual a mudanca?)
  - `universalidade` (o especificissimo toca o universal)
  - `etica_narrativa` (nao explora terceiros; fair to subjects)

## Foco do Usuario (Exemplos tipicos)

> "Voz de avo contando pro neto. Calor, pausas, repeticoes carinhosas. Nao use palavras dificeis."
> "Foque na relacao mae-filha. Tensoes nao-ditas. O que NAO foi dito importa mais."
> "Memoir medico: sou medico que adoeceu. Duas vozes: a do medico e a do paciente. Contraste."
> "Investigue o desaparecimento do meu pai. Cada capitulo = uma pista. Mistério + memoir."

---

## Template para Usuario Criar Subgenero Personalizado

```
# GENERO: MEMOIR_[SEU_SUBGENERO]

Base: MEMOIR

Alteracoes:
- dual_temporalidade: true/false (como marcar a troca)
- estrutura_global: TEMATICO | CRONOLOGICO | INVESTIGATIVO | FRAGMENTADO
- memorias_por_capitulo: [min]-[max]
- show_minimo: [XX%]
- exige_editor: true
- bible_extra: [etica_privacidade, versao_oficial_vs_verdade, documentos_fonte]
```