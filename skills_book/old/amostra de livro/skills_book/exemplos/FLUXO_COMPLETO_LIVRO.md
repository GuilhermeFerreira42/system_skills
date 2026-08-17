# Exemplo de Fluxo Completo — Livro

Este exemplo mostra como o sistema orquestra a producao de um livro do inicio ao fim.

---

## Cenario

Usuario quer produzir um **Thriller Psicologico** baseado em pesquisa sobre **memoria, optogenetica e trauma**.
- **Corpus:** 47 artigos cientificos + 3 livros + notas de pesquisa + Bible pre-definida
- **Genero:** `THRILLER_PSICOLOGICO` (personalizado, herda de ROMANCE)
- **Foco do Usuario:** "Foque na experiencia subjetiva da protagonista. O leitor deve duvidar do que e real. Tensao interna > acao externa. Unreliable narrator controlado."

---

## Passo 1 — Orquestrador Le o Estado

```
LER("estado/estado_da_obra.md")
// estado vazio -> iniciar do zero
```

---

## Passo 2 — Orquestrador Analisa Corpus + Genero + Foco -> Cria Bible + Plano

```
corpus = LER_TUDO("corpus/")
genero = LER("generos/GENERO_THRILLER_PSICOLOGICO.md")
foco_usuario = "Foque na experiencia subjetiva..."

bible = CRIAR_BIBLE_DO_CORPUS(corpus, genero, foco_usuario)
// Extrai: personagens (Elena, Marcus, Kieran), conceitos (Projeto Eco, Eco-9, Protocolo 7),
// timeline (dias 1-30), locais (Lab, Casa, Delegacia), fios narrativos

plano = CRIAR_PLANO_CENAS(corpus, genero, foco_usuario, bible)
// 22 capitulos, ~58 cenas, estrutura 3 atos com twist no meio
// Cada cena: ID, Cap, Cena, Titulo, POV, Objetivo, Beats, Palavras_Estimadas

estado = {
  "genero": "THRILLER_PSICOLOGICO",
  "foco_usuario": foco_usuario,
  "bible_versao": "v1.0",
  "plano": plano,
  "cenas_concluidas": 0,
  "status_geral": "EM_ANDAMENTO"
}

SALVAR_ATOMICO("estado/estado_da_obra.md", estado)
SALVAR_ATOMICO("bible/bible_da_obra.md", bible)
```

---

## Passo 3 — Loop de Producao (Cena 1.1: "A Anomalia")

### 3a. Orquestrador Cria Worktree + Invoca Escritor

```
worktree = CRIAR_PASTA("capitulos/capitulo_01/")

INVOCAR(escritor, {
  cena: {id: "1.1", capitulo: 1, cena: 1, titulo: "A Anomalia", pov: "Elena", objetivo: "Descobrir anomalia na amostra", beats: [...]},
  genero: genero,
  bible: bible,
  estado_anterior: null,  // primeira cena
  foco_usuario: foco_usuario
}, worktree)
```

### 3b. Escritor Escreve Prosa (v1)

`capitulos/capitulo_01/_saida_escritor.md`:
```markdown
# Cena 1.1 — A Anomalia

A amostra nao estava onde ela deixou.

Elena parou com a pipeta a meio centimetro do poço B7. O rótulo — *Caso 2024-0847, Hipocampo, T+72h* — estava correto. A posicao na grade, porem, estava errada. Duas fileiras abaixo. Como se alguem a tivesse movido e devolvido no lugar errado. Ou como se ela tivesse movido e nao lembrasse.

O freezer -80C zumbia sua nota grave constante. Fora, o corredor da universidade cheirava a cera de chao e cafe queimado. Aqui dentro, so ozonio e alcool isopropilico.

— Dra. Vasquez? — A voz de Aris veio da porta, abafada pelo vidro fosco. — O relatorio do Caso 847. O delegado ligou duas vezes.

Elena nao virou. O coracao batia no dedo indicador esquerdo — la onde a cicatriz da queimadura formava um mapa em relevo que so ela lia.

— A amostra mudou de lugar, Aris. — A voz saiu mais rouca que o normal. — Eu nao a movi.

Silencio. O zumbido do freezer preencheu a lacuna.

— Voce tem certeza? — Aris entrou, bata branca impecavel, tablet na mao. — O log digital nao mostra acesso nas ultimas 48 horas. So seu login, ontem as 14:23.

Elena virou entao. Os olhos da mentora — castanhos, cansados, afiados — a estudavam com a mesma precisao que ela aplicava as laminas.

— Eu tenho certeza do que vi. — Elena tocou a cicatriz. — O que nao tenho e explicacao.

---

## Metadados da Cena
- capitulo: 1
- cena: 1
- titulo: "A Anomalia"
- pov: "Elena"
- tempo_verbal: "presente"
- pessoa: "3a_limitada"
- palavras_estimadas: 1847
- foco_usuario_aplicado: "Abertura com anomalia fisica imediata (gancho). Interioridade: coracao no dedo/cicatriz. Tensao paranoica: 'como se ela tivesse movido e nao lembrasse'. Dialogo minimo, subtexto maximo. Sem descricao de cenario alem do sensorial necessario."
- bible_versao_usada: "v1.0"
- mudanca_estado: "Elena descobre anomalia fisica -> suspeita de si mesma / da realidade. Objetivo: descobrir quem moveu a amostra."
- gancho_abertura: "A amostra nao estava onde ela deixou."
- fecho_propulsor: "O que nao tenho e explicacao." (abre loop: ela vai buscar a explicacao)
```

### 3c. Orquestrador Invoca Atomizador

```
INVOCAR(atomizador, {cena: worktree})
```

Atomizador le `_saida_escritor.md` + `_metadados_cena.json` + `bible/bible_da_obra.md`

Extrai 23 afirmacoes brutas -> Filtro prioridade -> **12 afirmacoes finais**

`_afirmacoes_para_validar.json` (exemplos):
```json
[
  {"id": "AFC-001", "afirmacao": "Freezer -80C usado para armazenamento de amostras cerebrais", "tipo": "PROTOCOLO", "pergunta": "Amostras de hipocampo humano sao armazenadas em freezer -80C? Responda CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS no corpus."},
  {"id": "AFC-002", "afirmacao": "Ozonio e alcool isopropilico sao cheiros caracteristicos de laboratorio de neurociencia", "tipo": "CONCEITO_TECNICO", "pergunta": "Laboratorios de neurociencia forense tem cheiro de ozonio e alcool isopropilico? Responda CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS no corpus."},
  {"id": "AFC-003", "afirmacao": "Cicatriza de queimadura no dedo indicador esquerdo pode formar mapa em relevo tactil", "tipo": "MECANISMO", "pergunta": "Cicatrizes de queimadura na ponta dos dedos criam padroes tacteis percetiveis? Responda CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS no corpus."}
]
```

### 3d. Orquestrador Invoca Validador MARCH (CEGO)

```
INVOCAR(validador_march, {cena: worktree, corpus: "corpus/"})
```

Validador MARCH **NAO VE** `_saida_escritor.md`. So ve perguntas + corpus.

Resultado `_resultado_march.json`:
```json
{
  "cena_id": "cap_01_cena_01",
  "total_afirmacoes": 12,
  "confirmados": 10,
  "contraditos": 0,
  "nao_encontrados": 2,
  "taxa_confirmados": 0.833,
  "status_geral": "APROVADO",
  "resultados": [
    {"id": "AFC-001", "status": "CONFIRMADO", "evidencia": "Protocolo padrao: tecido neural -80C para preservacao RNA/proteinas [corpus/protocolos/biobanking.md:12]", "tipo": "PROTOCOLO"},
    {"id": "AFC-002", "status": "CONFIRMADO", "evidencia": "Ozonio gerado por equipamentos de eletroforese; isopropilico 70% descontaminacao [corpus/estudos/lab_safety.md:45]", "tipo": "CONCEITO_TECNICO"},
    {"id": "AFC-003", "status": "NAO_ENCONTRADO", "evidencia": null, "tipo": "MECANISMO"}
  ]
}
```

**MARCH APROVADO** (taxa 83.3% > 80%, 0 contraditos, 16.7% NAO_ENCONTRADO < 30%)

### 3e. Orquestrador Invoca Validador Continuidade (CEGO)

Orquestrador **EXTRAI perguntas de continuidade** da prosa do escritor (so o orquestrador le a prosa) e cria `_perguntas_continuidade.json`:

```json
[
  {"id": "CONT-001", "categoria": "VOZ_NARRATIVA", "afirmacao": "Narrativa usa 3a pessoa limitada, presente, distancia claustrofobica", "pergunta": "Genero THRILLER_PSICOLOGICO + Bible definem: 3a limitada, presente, distancia claustrofobica. A prosa confirma? Responda CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS na Bible + Estado Anterior.", "fonte_esperada": "Bible: metadados > voz_narrativa"},
  {"id": "CONT-002", "categoria": "PERSONAGEM_ACAO", "afirmacao": "Elena toca cicatriz no dedo indicador esquerdo quando estressada", "pergunta": "Bible diz: Elena toca cicatriz quando mente/estressada. A acao confirma? Responda CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS na Bible + Estado Anterior.", "fonte_esperada": "Bible: personagens > Elena > maneirismos"},
  {"id": "CONT-003", "categoria": "LOCAL_CENARIO", "afirmacao": "Laboratorio tem freezer -80C, cheiro ozonio/isopropilico, luz fluorescente fria", "pergunta": "Bible define Lab Forense com esses detalhes sensoriais. Confirma? Responda CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS na Bible + Estado Anterior.", "fonte_esperada": "Bible: cenarios > Laboratorio"},
  {"id": "CONT-004", "categoria": "POV_CONSISTENCIA", "afirmacao": "So acessa pensamentos/sensoes de Elena (coracao no dedo, voz rouca, toque cicatriz)", "pergunta": "POV = 3a limitada Elena. Nao ha head-hopping para Aris? Responda CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS na Bible + Estado Anterior.", "fonte_esperada": "Bible: metadados > POV"}
]
```

Validador Continuidade responde `_resultado_continuidade.json`:
```json
{
  "cena_id": "cap_01_cena_01",
  "total_verificacoes": 4,
  "confirmados": 4,
  "contraditos": 0,
  "nao_encontrados": 0,
  "status_geral": "APROVADO",
  "resultados": [
    {"id": "CONT-001", "status": "CONFIRMADO", "evidencia": "Bible: metadados > voz_narrativa: '3a_limitada, presente, distancia claustrofobica'. Prosa: 'Elena parou', 'O coracao batia no dedo indicador esquerdo', 'A voz saiu mais rouca'.", "categoria": "VOZ_NARRATIVA"},
    {"id": "CONT-002", "status": "CONFIRMADO", "evidencia": "Bible: personagens > Elena > maneirismos: 'Toca a cicatriz quando mente ou esta estressada'. Prosa: 'Elena tocou a cicatriz'.", "categoria": "PERSONAGEM_ACAO"},
    {"id": "CONT-003", "status": "CONFIRMADO", "evidencia": "Bible: cenarios > Laboratorio > Descricao_sensorial: 'Cheiro: ozonio + alcool isopropilico... Luz: fria, fluorescente... Freezer -80C zumbia'.", "categoria": "LOCAL_CENARIO"},
    {"id": "CONT-004", "status": "CONFIRMADO", "evidencia": "Bible: metadados > POV: '3a_limitada (Elena)'. Prosa so mostra interno de Elena. Aris so observada externamente.", "categoria": "POV_CONSISTENCIA"}
  ]
}
```

**CONTINUIDADE APROVADA** (0 contraditos)

### 3f. Genero exige Editor -> Orquestrador Invoca Editor

```
INVOCAR(editor, {cena: worktree, genero: genero, bible: bible})
```

Editor poli a prosa (voice consistency, pacing, show-dont-tell, ancoragem, ganchos) -> `_saida_editor.md`

### 3g. Orquestrador Atualiza Bible + Estado (ATOMICAMENTE)

```
bible = ATUALIZAR_BIBLE(bible, saida_final, cena_1.1)
// Adiciona: evento "Anomalia descoberta" na timeline, estado emocional Elena atualizado, fio narrativo "Amostra movida" = ABERTO

estado.cena_1_1 = {status: "CONCLUIDO", march: "APROVADO", cont: "APROVADO", checksum: "e5f6g7h8", palavras: 1847}

SALVAR_ATOMICO("bible/bible_da_obra.md", bible)  // v1.0 -> v1.1
SALVAR_ATOMICO("estado/estado_da_obra.md", estado)
```

---

## Passo 4 — Cena 1.2: "A Rotina Quebrada"

Mesmo fluxo. Escritor recebe `estado_anterior` com resumo da cena 1.1 + bible v1.1.

Escreve cena onde Elena vai para casa, tensao domestica com Marcus, setup do casamento "perfeito por fora".

MARCH valida fatos domesticos (poucos). Continuidade valida: Elena ainda toca cicatriz, Marcus tem anisocoria, casa = Bible, timeline dia 1 manha apos cena 1 noite.

---

## Passo 5 — ... Loop continua ate Cena 22.4 (Epilogo)

Cada cena: Escritor -> Atomizador -> MARCH -> Continuidade -> Editor -> Atualiza Bible/Estado

**Checkpoints automaticos** a cada cena permitem retomada exata se processo cair.

---

## Passo 6 — Consolidacao Final

```
INVOCAR(consolidador, {plano: estado.plano, estado: estado, output: "livro_final.md"})
```

Consolidador:
1. Le todas 58 cenas CONCLUIDAS em ordem
2. Junta com `# Capitulo X: Titulo` + `### Cena Y: Titulo`
3. Adiciona Front Matter YAML
4. **Validacao de Fronteira:**
   - Soma palavras cenas ≈ palavras livro (+-5%)
   - Todas cenas CONCLUIDAS presentes
   - Ordem preservada
   - Checksums conferem
5. Salva `livro_final.md` (95.000 palavras)
6. Opcional: `livro_final.epub`, `livro_final.pdf`

---

## Resumo do Fluxo

| Fase | Agente | Input | Output | Validacao |
|------|--------|-------|--------|-----------|
| 1 | Orquestrador | Corpus, Genero, Foco | Bible v1.0, Plano, Estado | - |
| 2A | Escritor | Cena, Genero, Bible, Estado Anterior, Foco | `_saida_escritor.md`, `_metadados_cena.json` | - |
| 2B | Atomizador | `_saida_escritor.md`, Bible | `_afirmacoes_para_validar.json`, `_perguntas_validador.json` | - |
| 2C | Validador MARCH | Perguntas, Corpus | `_resultado_march.json` | Taxa≥80%, 0 contraditos, ≤30% NAO_ENCONTRADO |
| 2D | Validador Continuidade | Perguntas (extraidas pelo Orq), Bible, Estado Anterior | `_resultado_continuidade.json` | 0 contraditos |
| 2E | Editor (opcional) | `_saida_escritor.md`, Genero, Bible | `_saida_editor.md`, `_metadados_editor.json` | - |
| 2F | Orquestrador | Bible, Estado, Saida Final | Bible vN+1, Estado Atualizado | Checksum round-trip |
| 3 | Consolidador | Plano, Estado, Cenas | `livro_final.md` (+ epub/pdf) | Validacao fronteira |

---

## Diferencas Chave vs Podcast

| Podcast | Livro |
|---------|-------|
| 2 speakers, dialogo | Voz narrativa unica (ou multi-POV controlado) |
| 6 segmentos fixos/ep | Cenas variaveis por genero/capitulo |
| Validador MARCH only | **MARCH + CONTINUIDADE (dupla validacao cega)** |
| Balanceamento speakers | POV consistency, voz, timeline, worldbuilding |
| Audio (TTS) obrigatorio | Markdown final (EPUB/PDF opcional) |
| Episodios isolados | **Continuidade obrigatoria** (Bible + Estado) |
| Nao ha Bible | **Bible viva** atualizada a cada cena |

---

## Arquivos Gerados no Projeto Final

```
projeto_livro/
├── corpus/ (47 artigos + 3 livros + notas)
├── bible/
│   ├── bible_da_obra.md (v3.2, final)
│   └── bible_exemplo_backup.md
├── estado/
│   └── estado_da_obra.md (58 cenas CONCLUIDAS)
├── capitulos/
│   ├── capitulo_01/
│   │   ├── _saida_escritor.md
│   │   ├── _saida_editor.md
│   │   ├── _afirmacoes_para_validar.json
│   │   ├── _perguntas_validador.json
│   │   ├── _perguntas_continuidade.json
│   │   ├── _resultado_march.json
│   │   ├── _resultado_continuidade.json
│   │   ├── _metadados_cena.json
│   │   ├── _metadados_editor.json
│   │   ├── _saida_final.md
│   │   └── rascunhos/
│   └── ... capitulo_22/
├── generos/
│   ├── GENERO_THRILLER_PSICOLOGICO.md
│   └── (outros)
├── livro_final.md (95k palavras)
├── livro_final.epub
├── livro_final.pdf
└── estado_da_obra.md (copia raiz)
```