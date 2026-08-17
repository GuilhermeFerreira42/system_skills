# TEMPLATE DA BIBLE DA OBRA

**Versao:** 1.0
**Uso:** Copie este arquivo para `bible/bible_da_obra.md` e preencha progressivamente.
O Orquestrador atualiza automaticamente a cada cena aprovada.

---

# Bible da Obra: [TITULO DO LIVRO]

## Metadados Gerais
- **Titulo:** 
- **Subtitulo:** 
- **Genero:** [ROMANCE | NAO_FICCAO | MEMOIR | TECNICO | PERSONALIZADO]
- **Subgenero:** 
- **Publico_alvo:** 
- **Tom_de_voz:** 
- **POV_padrao:** [1a | 3a_limitada | 3a_onisciente | 3a_multipla | 2a | 3a_autoral | 3a_instrutiva]
- **Tempo_verbal:** [passado | presente | misto_controlado]
- **Distancia_narrativa:** [intima | proxima | media | ampla | cinematografica | mentor | instrutora]
- **Vocabulario_nivel:** [simples | medio | rico | tecnico | construido | pessoal | acessivel]
- **Fonte_nomeada:** [como a prosa deve chamar a fonte do corpus — ex.: "a palestra do Dr. Fulano" | "o relatorio anual" | "as cartas do fundador"; NUNCA "o corpus" nem "a transcricao"]
- **Ritmo_padrao:** [lento | variado | rapido | acelerado | modular | ondulatorio | linear]
- **Versao_bible:** v1.0
- **Checksum:** [auto-preenchido pelo orquestrador]
- **Ultima_atualizacao:** [ISO8601]

## Perfil Editorial (NIVELAMENTO — preenchido pelo Orquestrador no Passo 3.2)

Este campo captura as 4 respostas de nivelamento editorial que o Orquestrador coleta do usuario no inicio de todo projeto novo. Os 4 eixos sao institucionais: garantem que a voz, densidade e estilo sejam consistentes com o que o usuario quer, mesmo quando o `foco_usuario` livre desta obra especifica for generico.

**Quando preencher:** no Passo 4 do BOOT, ao criar/atualizar a Bible a partir do corpus. Se a Bible ja existe, o Orquestrador PRESERVA o perfil existente (so sobrescreve se o usuario responder o nivelamento de novo explicitamente).

**Onde consultar:** o Escritor le este campo no `BOOT_ESCRITOR_CAPITULO.md` e injeta os valores nas instrucoes de cada cena (estilo de abertura, densidade de analogias, voz do autor, palavras-alvo por cena).

**Os 4 eixos (resposta unica por eixo, letra A/B/C):**

- **estilo_abertura:** [A | B | C]
  - A = imersao_pergunta_retorica (cena mental + pergunta antes de revelar a informacao)
  - B = direto_ao_ponto (afirma a tese logo na primeira linha)
  - C = caso_concreto_antes (caso real ou vinheta antes de explicar o conceito)
- **densidade_livro:** [A | B | C]
  - A = denso (~250k palavras, 800-1500/cena)
  - B = medio (~120k palavras, 500-900/cena)
  - C = enxuto (~60k palavras, 300-600/cena)
- **densidade_analogias:** [A | B | C]
  - A = alta (1-2 analogias por cena, sempre)
  - B = media (0-1 analogia por cena)
  - C = baixa (sem analogias obrigatorias)
- **voz_autor:** [A | B | C]
  - A = opinativa_humor_posicionamentos (narrador com opiniao, humor acido, polemicas leves)
  - B = neutra_engajada (narrador invisivel mas preocupado com clareza)
  - C = academica_distante (narrador onisciente, formal, sem opiniao)

**Exemplo preenchido (defaults padrão da skill):**

```
perfil_editorial:
  estilo_abertura: A
  densidade_livro: A
  densidade_analogias: A
  voz_autor: A
  preenchido_em: 2026-08-06
  fonte: nivelamento_inicial
```

**Regras:**
- O Orquestrador NAO comeca a escrever se este campo estiver vazio (NIVELAMENTO_OBRIGATORIO).
- O `foco_usuario` (campo separado) complementa este perfil com instrucoes especificas desta obra. Os dois coexistem.
- O `foco_usuario` NUNCA sobrescreve o nivelamento — ele apenas adiciona granularidade.

---

## Premissa & Estrutura
- **Logline:** (uma frase: protagonista + objetivo + obstaculo + stakes)
- **Tema_central:** 
- **Pergunta_tematica:** (o que o livro explora)
- **Estrutura_narrativa:** [TRES_ATOS | JORNADA_HEROI | KISHOTENKETSU | PROBLEMA_SOLUCAO | GRANDE_IDEIA | BIOGRAFIA | INVESTIGATIVO | CURSO_PROGRESSIVO | COOKBOOK | TEMATICO | CRONOLOGICO | FRAGMENTADO | OUTRO]
- **Numero_estimado_capitulos:** 
- **Numero_estimado_cenas:** 
- **Palavras_estimadas_total:** 

## Mapa Corpus-Capítulos (PREENCHER SE O CORPUS FOR MODULAR)

Se o corpus do projeto esta organizado em `corpus/modulo_NN_*/` (um modulo por tema), preencha esta tabela pra dizer qual modulo alimenta qual capitulo. O Orquestrador consulta isso a cada cena pra carregar so o corpus relevante (reduz custo de tokens e melhora precisao da validacao MARCH).

**Exemplo:**

| Capitulo | Modulo(s) do Corpus | Tamanho Aprox | Notas |
|----------|----------------------|---------------|-------|
| Cap 1 | `corpus/modulo_01_fundamentos/` | 2 MB | Material-base do tema principal |
| Cap 2 | `corpus/modulo_01_fundamentos/` | 2 MB | Continua no mesmo tema |
| Cap 3 | `corpus/modulo_02_aplicacoes/` | 3 MB | Muda de tema |
| Cap 4-5 | `corpus/modulo_03_avancado/` | 5 MB | Tema avancado, requer conhecimento previo do tema base |

**Regra:** se uma cena cair em capitulo nao mapeado, o Orquestrador usa `INFERIR_MODULOS` (fuzzy match por palavras-chave do titulo da cena com titulos dos modulos) como fallback.

**Se o corpus for MONOLITICO** (`corpus_novo.md` unico arquivo), deixe esta secao vazia ou escreva "NAO APLICAVEL — corpus monolitico".

## Alocacao de Cenas por Capítulo (OPCIONAL, OVERRIDE MANUAL)

Por padrao, o Orquestrador calcula quantas cenas cada capitulo merece automaticamente, usando densidade do corpus + arquetipo do genero (definido em `utils/constantes.py`, secoes `CONFIGURACAO_ALOCACAO_CENAS` e `CONFIGURACAO_CENAS_POR_ARQUETIPO`).

Se voce quiser forçar uma cadencia especifica pra este projeto (ex: capitulo de abertura com 1 cena, capitulo de virada com 5), preencha o dicionario abaixo. O Orquestrador usa esses valores em vez do calculo automatico.

**Formato:** YAML-like, com ID do capitulo e numero de cenas.

```
alocacao_cenas_por_capitulo:
  cap_01: 1     # abertura, so contexto
  cap_02: 3     # tema denso, requer 3 cenas
  cap_03: 4     # cancer (muito denso, controverso, 4 cenas)
  cap_04: 2     # vitamina D3 (intermediario, 2 cenas)
  cap_05: 1     # oleo de coco (direto, 1 cena)
```

**Quando usar override:**
- Capitulo de abertura/fechamento que precisa de cadencia especial
- Capitulo que mistura 2 modulos e voce quer garantir que ambos sejam bem cobertos
- Capitulo de "respiro" entre capitulos densos
- Quando o calculo automatico erra (raro, mas acontece em corpus nao-padronizado)

**Quando NAO usar override:** na duvida, deixe o sistema calcular. A heuristica de densidade funciona bem em 90% dos casos.

---

## Personagens Principais (Ficcao/Memoir) OU Conceitos-Chave (Nao-Ficcao/Tecnico)

### Personagem: [NOME]
| Campo | Valor |
|-------|-------|
| Papel | Protagonista / Antagonista / Interesse Amoroso / Mentor / Aliado / Figurante |
| Arquetipo | (ex: Heroi Relutante, Sombra, Trickster, Mae, etc.) |
| Idade |  |
| Aparencia_fisica | (detalhes especificos: altura, cabelo, olhos, marcas, jeito de andar) |
| Maneirismos | (tiques, frases repetidas, gestos, jeito de falar) |
| Voz_dialogo | (vocabulario, ritmo, giria, formalidade, tic verbal) |
| Ferida_nuclear | (o trauma/acontecimento que moldou a mentira) |
| Mentira_que_acredita | (ex: "Nao sou amavel", "Preciso controlar tudo", "Ninguem fica") |
| Desejo_externo | (o que quer CONSCIENTEMENTE: objetivo da trama) |
| Necessidade_interna | (o que PRECISA aprender/aceitar: arco emocional) |
| Medo_primordial |  |
| Valor_não_negociavel |  |
| Relacoes_chave | (nome: tipo_relacao + dinamica) |
| Arco_resumido | (onde comeca -> onde termina) |
| Status_vivo_morto |  |
| Localizacao_atual | (atualizado pelo orquestrador) |
| Estado_emocional_atual | (atualizado pelo orquestrador) |
| Conhecimento_atual | (o que sabe/nao sabe - atualizado pelo orquestrador) |

---

### Personagem: [NOME 2]
(Repetir estrutura acima)

---

## Cenários / Worldbuilding / Locais

### Local: [NOME]
| Campo | Valor |
|-------|-------|
| Tipo | Casa / Trabalho / Cidade / Pais / Planeta / Sala / Navio / Digital |
| Descricao_sensorial | (cheiro, som, luz, textura, temperatura, atmosfera) |
| Layout_importante | (mapa mental: onde fica o que, rotas, visibilidade) |
| Regras_do_local | (ex: "nao se fala alto na biblioteca", "porta tranca so por fora") |
| Historia_relevante |  |
| Personagens_associados |  |
| Eventos_ocorridos_aqui | (capitulo.cena) |
| Mudancas_ao_longo_livro |  |

---

## Cronologia Mestre (Timeline)

| Data/Cap.Cena | Evento | Personagens | Local | Duracao | Notas |
|---------------|--------|-------------|-------|---------|-------|
| Dia 1 / Cap 1 Cena 1 | Evento inciting | Protagonista | Quarto | 30 min | Gancho abertura |
| Dia 1 / Cap 1 Cena 2 | Descoberta | Protagonista, Aliado | Cozinha | 45 min | Revelacao chave |
| ... | ... | ... | ... | ... | ... |

**Regra:** O Orquestrador preenche/atualiza esta tabela a cada cena aprovada.

---

## Conceitos-Chave, Terminologia & Regras do Mundo

| Termo/Conceito | Definicao Canonica | Tipo | Primeira_Ocorrencia | Regra_Rigida? |
|----------------|-------------------|------|---------------------|---------------|
| Ex: "A Mana" | Energia vital que flui Norte->Sul | Worldbuilding | Cap 1 Cena 1 | SIM |
| Ex: "BPA" | Bisfenol A, disruptor endocrino | Conceito_Tecnico | Cap 2 Cena 1 | NA |
| Ex: "Protocolo 7" | Sequencia de 3 passos para reset | Protocolo | Cap 5 Cena 3 | SIM |

**Tipos:** `Worldbuilding` | `Conceito_Tecnico` | `Protocolo` | `Termo_Especial` | `Regra_Sociedade` | `Tecnologia` | `Magia` | `Biology`

---

## Fios Narrativos Abertos (Chekhov's Guns / Setups / Payoffs)

| Fio | Tipo | Introduzido_em | Detalhe | Status | Resolvido_em | Payoff_Descricao |
|-----|------|----------------|---------|--------|--------------|------------------|
| Ex: Carta na gaveta | Setup | Cap 1 Cena 3 | Protagonista encontra carta nao aberta | ABERTO | Cap 12 Cena 2 | Revela identidade do pai |
| Ex: Medo de agua | Tema | Cap 2 Cena 1 | Flashback afogamento irmao | EM_DESENVOLVIMENTO | Cap 15 Cena 1 | Protagonista mergulha para salvar |

**Tipos:** `Setup` | `Payoff` | `Tema_Recorrente` | `Misterio` | `Promessa` | `Ameaca` | `Segredo`

---

## Decisoes Editoriais Travadas (Nao Mudar Sem Aprovaçao)

| Decisao | Capitulo_Origem | Justificativa | Quem_Decidiu |
|---------|-----------------|---------------|--------------|
| Ex: Protagonista nao sabe nadar | Cap 2 Cena 1 | Necessario para climax no lago | Usuario + Orquestrador |
| Ex: Magia de fogo = proibida no Sul | Bible v1.0 | Regra rigida worldbuilding | Genero + Usuario |

---

## Estudos, Fontes & Referencias (Nao-Ficcao/Tecnico)

| Citacao | Tipo | Achado_Principal | Relevancia | Arquivo_Corpus |
|---------|------|------------------|------------|----------------|
| Swan et al. 2017 | Estudo_Humano | Ftalatos reduzem distancia anogenital | Alta | corpus/estudos/swan2017.md |
| Rochester 2009 | Estudo_Mecanismo | BPA liga ER-alfa/beta | Alta | corpus/estudos/rochester2009.md |

---

## Glossario Tecnico (Tecnico)

| Termo | Definicao | Sinonimos | Nao_Usar |
|-------|-----------|-----------|----------|
| Deploy | Colocar em producao | Release, Rollout | "Subir" (informal) |

---

## Checklist de Integridade (Preenchido pelo Orquestrador)

- [ ] Todos personagens principais tem ficha completa
- [ ] Timeline cobre todos capitulos planejados
- [ ] Regras rigidas de worldbuilding marcadas
- [ ] Fios narrativos tem setup E payoff planejado
- [ ] Conceitos-chave definidos antes de usar
- [ ] Glossario tecnico completo (se tecnico)
- [ ] Estudos citados tem arquivo no corpus (se nao-ficcao)
- [ ] Versao e checksum atualizados