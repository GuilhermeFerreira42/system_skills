# GENERO: ROMANCE (Ficcao Literaria / Comercial / Genero)

**Versao:** 1.0
**Tipo:** ROMANCE
**Estrutura:** Capítulos com cenas (2-4 por capítulo), arcos emocionais claros

---

## Voz Narrativa

- **pessoa:** `3a_limitada` (padrão comercial) | `1a` (YA, romance contemporâneo, memoir-ficção) | `3a_onisciente` (literário, épico, vitoriano)
- **tempo_verbal:** `passado` (padrão) | `presente` (YA, thriller, imediatez)
- **distancia:** `proxima` (comercial) | `intima` (literário, YA) | `media` (onisciente)
- **tom:** `envolvente`, `emocional`, `sensorial`, `autentico`, `esperancoso` (mesmo no drama)
- **vocabulario:** `acessivel` (comercial) | `rico` (literário) | `especifico_ao_mundo` (fantasia, histórico)
- **ritmo:** `variado` (respiração: ação -> reflexão -> diálogo -> descrição)

## POV

- **padrao:** `3a_limitada` (alterna entre 2 protagonistas em romance) | `1a` (single POV)
- **multi_pov:** `true` (romance: 2 POVs principais; ensemble: 3-5)
- **regras_troca:** `so_na_quebra_de_cena` | `cada_capitulo_1_pov` | `marcado_explicitamente`

## Estrutura de Cena

- **min_palavras:** 1000
- **max_palavras:** 5000
- **beats_obrigatorios:** `["gancho", "objetivo_cena", "obstaculo", "desenvolvimento", "climax_cena", "mudanca_emocional", "fecho_propulsor"]`
- **show_minimo:** 70%
- **gancho_tipos:** `["pergunta_emocional", "imagem_sensorial", "dialogo_in_media_res", "pensamento_revelador"]`
- **fecho_tipos:** `["gancho_proxima", "revelacao_parcial", "decisao_pendente", "tensao_nao_resolvida"]`

## Estrutura de Capítulo

- **unidades_por_capitulo:** 2-4
- **arco_capitulo:** "Minicoisa: setup -> complicação -> turno -> resolução parcial -> gancho"
- **recap_final:** false

## Estrutura Global (Arquetipos)

### Opção A: Estrutura 3 Atos (Padrão)
- **Ato 1 (25%):** Mundo normal, inciting incident, debate, crossing threshold
- **Ato 2A (30%):** Fun & games, promise of premise, midpoint (false victory/defeat)
- **Ato 2B (20%):** Bad guys close in, all is lost, dark night of soul
- **Ato 3 (25%):** Climax, resolution, new normal

### Opção B: Romance Beat Sheet (Gwen Hayes / Romancing the Beat)
1. Setup / Hook
2. Inciting Incident (Meet Cute / Reunion / Forced Proximity)
3. First Plot Point (Commitment to Goal Together)
4. Pinch Point 1 (Conflict Escalation)
5. Midpoint (Intimacy / Vulnerability / Stakes Raised)
6. Pinch Point 2 (Major Conflict / Breakup / Black Moment)
7. Dark Night of Soul
8. Climax (Grand Gesture / Proof of Love)
9. Resolution (HEA / HFN)

### Opção C: Jornada do Herói (Épico / Fantasia)
12 stages + return with elixir

## Bible Requisitos

- **personagens_detalhados:** `true` (fichas completas: ferida, mentira, desejo, necessidade, arco, voz, maneirismos)
- **worldbuilding_profundo:** `false` (exceto fantasia/histórico/sci-fi)
- **cronologia_rigida:** `true` (timeline de eventos, estações, datas-chave)
- **sistema_magia_regras:** `false` (exceto fantasia)
- **conceitos_chave:** `true` (temas, símbolos, metáforas centrais)
- **estudos_citados:** `false`
- **protocolos_praticos:** `false`
- **glossario_tecnico:** `false`
- **ambiente_referencia:** `false`
- **locais_detalhados:** `true` (casa, trabalho, "terceiro lugar", cenários emocionais)
- **fios_narrativos:** `true` (subplots: amizade, família, carreira, ferida passada)
- **versao_oficial_vs_verdade:** `false`
- **etica_privacidade:** `false`
- **erros_comuns:** `false`
- **checklists_verificacao:** `false`

## Validacoes Extras (Editor)

- **exige_editor:** `true`
- **regras_editor:**
  - `voice_consistency`
  - `pacing`
  - `show_dont_tell`
  - `dialogo_natural`
  - `ancoragem_sensorial`
  - `gancho_abertura_fecho`
  - `arco_emocional_pov`
  - `quimica_personagens` (romance)
  - `tensao_romantica` (romance)
  - `verdade_emocional`
  - `especificidade_sensorial`
  - `consistencia_personagem`
  - `subtexto_dialogo`

## Foco Padrão do Usuário

> "Foque na verdade emocional dos personagens. Cada cena deve mover o relacionamento (romance) OU o arco interno (literário). Diálogos com subtexto. Ancoragem sensorial forte. Evite resumo narrativo - dramatize."