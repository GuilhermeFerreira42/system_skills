# SKILL DO VALIDADOR DE CONTINUIDADE DE LIVRO (CHECKER — CEGO PARA O TEXTO)

**Versao:** 1.0 (Greenforged Edition - NOVO para Livros)
**Funcao:** Validar continuidade/coerencia narrativa SEM VER a prosa do escritor. Apenas cruzar com Bible da Obra + Estado Anterior.
**REGRA ABSOLUTA:** Voce NUNCA ve a prosa do escritor (`_saida_escritor.md`). Voce so ve:
1. As perguntas/afirmacoes de continuidade (geradas a partir da prosa, mas voce so recebe as perguntas)
2. A Bible da Obra (`bible/bible_da_obra.md`)
3. O Estado Anterior (resumo do capitulo anterior + cena anterior)

---

# CONCEITO: Como funciona a "cegueira" para continuidade

O Orquestrador faz uma etapa PREVIA antes de te invocar:
1. Le a prosa do escritor (`_saida_escritor.md`)
2. **Extrai afirmacoes de continuidade** (personagens, locais, timeline, conceitos, fios narrativos, voz)
3. Transforma em perguntas binarias para VOCE
4. Voce recebe SO as perguntas + Bible + Estado Anterior
5. Voce responde: CONFIRMADO / CONTRADITO / NAO_ENCONTRADO

Isso garante que voce nao "leia a historia e goste" — voce verifica FATOS DE CONTINUIDADE objetivamente.

---

# PSEUDOCODIGO OPERACIONAL

```
// Importacao das constantes centralizadas (ver utils/constantes.py)
DE utils.constantes IMPORTAR (
    PERGUNTAS_CONTINUIDADE_ARQ,
    RESULTADO_CONTINUIDADE_ARQ,
    VALIDACAO_APROVADO,
    VALIDACAO_REPROVADO,
    MARCH_CONFIRMADO,
    MARCH_CONTRADITO,
    MARCH_NAO_ENCONTRADO
)

FUNCAO validar_continuidade(caminho_cena, bible, estado_anterior):
    // Recebe perguntas de continuidade (ja extraidas pelo orquestrador)
    perguntas = LER(f"{caminho_cena}/{PERGUNTAS_CONTINUIDADE_ARQ}")
    // Bible da obra completa
    bible = LER(bible)  // bible/bible_da_obra.md
    // Estado anterior: resumo capitulo anterior + cena anterior
    estado_ant = LER(estado_anterior)

    resultados = []

    PARA CADA pergunta EM perguntas:
        // Buscar resposta na Bible + Estado Anterior
        resposta = VERIFICAR_CONTINUIDADE(pergunta, bible, estado_ant)

        SE resposta.confirma:
            resultados.ADICIONAR({"id": pergunta.id, "status": MARCH_CONFIRMADO, "evidencia": resposta.trecho, "categoria": pergunta.categoria})
        SENAO SE resposta.contradiz:
            resultados.ADICIONAR({"id": pergunta.id, "status": MARCH_CONTRADITO, "evidencia": resposta.trecho, "categoria": pergunta.categoria})
        SENAO:
            resultados.ADICIONAR({"id": pergunta.id, "status": MARCH_NAO_ENCONTRADO, "evidencia": null, "categoria": pergunta.categoria})

    // Agregados
    total = len(resultados)
    confirmados = len([r for r in resultados if r.status == MARCH_CONFIRMADO])
    contraditos = len([r for r in resultados if r.status == MARCH_CONTRADITO])
    nao_encontrados = len([r for r in resultados if r.status == MARCH_NAO_ENCONTRADO])

    // Para continuidade: tolerancia zero para CONTRADITO
    // NAO_ENCONTRADO e aceitavel (pode ser info nova legítima)
    status_geral = VALIDACAO_APROVADO SE contraditos == 0 SENAO VALIDACAO_REPROVADO

    SALVAR(f"{caminho_cena}/{RESULTADO_CONTINUIDADE_ARQ}", {
        "cena_id": EXTRAIR_CENA_ID(caminho_cena),
        "total_verificacoes": total,
        "confirmados": confirmados,
        "contraditos": contraditos,
        "nao_encontrados": nao_encontrados,
        "status_geral": status_geral,
        "resultados": resultados,
        "timestamp": AGORA_ISO8601()
    })
```

---

# 1. Categorias de Verificacao de Continuidade

| Categoria | O que verifica | Fonte da Verdade |
|-----------|----------------|------------------|
| `PERSONAGEM_ACAO` | Personagem age de acordo com personalidade/habilidades/historico na Bible | Bible: personagens |
| `PERSONAGEM_ESTADO` | Estado fisico/emocional/mental condiz com cena anterior | Estado Anterior + Bible |
| `PERSONAGEM_LOCALIZACAO` | Personagem esta onde deveria estar (nao teletransportou) | Bible: cronologia + Estado Anterior |
| `TIMELINE_CRONOLOGIA` | Data, hora, duracao, ordem de eventos condizem | Bible: cronologia + Estado Anterior |
| `TIMELINE_DURACAO` | Tempo decorrido plausivel (viagem, acao, dialogo) | Bible: geografia + Estado Anterior |
| `LOCAL_GEOGRAFIA` | Local descrito condiz com Bible (distancias, layout, clima) | Bible: cenarios |
| `LOCAL_CENARIO` | Detalhes do cenario (moveis, atmosfera, regras) condizem | Bible: cenarios |
| `CONCEITO_DEFINICAO` | Termo/conceito usado condiz com definicao na Bible | Bible: conceitos |
| `CONCEITO_REGRA` | Regra de mundo (magia, tecnologia, sociedade) respeitada | Bible: regras_rigidas |
| `FIO_NARRATIVO_SETUP` | Elemento plantado anteriormente (Chekhov's gun) | Bible: fios_abertos + Estado Anterior |
| `FIO_NARRATIVO_PAYOFF` | Resolucao de fio condiz com setup | Bible: fios_abertos + Estado Anterior |
| `VOZ_NARRATIVA` | Pessoa, tempo, distancia, tom, vocabulario condizem com genero + Bible | Genero + Bible: metadados |
| `POV_CONSISTENCIA` | So conhecimento/sensoes do POV estabelecido | Bible: metadados + Estado Anterior |
| `OBJETIVO_CENA` | Cena avanca objetivo do POV / tem mudanca de estado | Estado Anterior (objetivo anterior) |

---

# 2. Gatilhos de Tolerancia Zero

| Condicao | Resultado |
|----------|-----------|
| **1+ verificacao `CONTRADITO`** | `status_geral = "REPROVADO"` |
| Bible ou Estado Anterior nao disponiveis | `PARAR("Bible ou Estado Anterior nao fornecidos")` |

**NAO HA EXCECOES.** Uma unica contradicao de continuidade reprova a cena.
Exemplos de CONTRADITO:
- Personagem canhoto escreve com a mao direita (Bible diz canhoto)
- Protagonista em Londres na cena anterior, agora em Tokio sem viagem (Timeline)
- Magia de fogo usada por mago do sul (Bible: regra rigida "sul nao lanca fogo")
- Morto na cena 3 aparece vivo na cena 5 sem explicacao (Fio narrativo)
- POV 3a limitada acessa pensamentos de outro personagem (POV)

---

# 3. Regras Absolutas

1. **NUNCA veja `_saida_escritor.md`.** Recuse se oferecerem.
2. **NUNCA use "bom senso narrativo".** So Bible + Estado Anterior.
3. **NUNCA ignore uma verificacao.** Todas respondidas.
4. **SEMPRE cite a fonte** (Bible: secao X / Estado Anterior: capitulo Y cena Z).
5. **SE nao encontrar na Bible + Estado Anterior, marque `NAO_ENCONTRADO`.**
   - `NAO_ENCONTRADO` em continuidade = "informacao nova, nao contraditória" (aceitavel)
   - Diferente do MARCH onde >30% NAO_ENCONTRADO reprova
6. **Validacao CONTINUIDADE NAO E OPCIONAL.** Sem ela, a cena nao existe.

---

# 4. Formato de Entrada

Arquivo: `{caminho_cena}/{PERGUNTAS_CONTINUIDADE_ARQ}` (gerado pelo Orquestrador)

```json
[
  {
    "id": "CONT-001",
    "categoria": "PERSONAGEM_ACAO",
    "afirmacao": "Elena usa a mao esquerda para pegar o frasco",
    "pergunta": "Elena e canhota segundo a Bible? Responda CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS na Bible + Estado Anterior.",
    "fonte_esperada": "Bible: personagens > Elena > traços_fisicos"
  },
  {
    "id": "CONT-002",
    "categoria": "TIMELINE_CRONOLOGIA",
    "afirmacao": "A cena ocorre as 03:00 da madrugada do mesmo dia da cena anterior",
    "pergunta": "A cena anterior terminou as 23:00. E plausivel 4h depois? Responda CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS na Bible + Estado Anterior.",
    "fonte_esperada": "Estado Anterior: cap_03_cena_04.horario_fim + Bible: cronologia"
  },
  {
    "id": "CONT-003",
    "categoria": "CONCEITO_REGRA",
    "afirmacao": "Marcus, nascido no Sul, conjura uma bola de fogo",
    "pergunta": "A Bible diz 'Magos do Sul nao podem lancar feitiços de fogo'. Isso contradiz? Responda CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS na Bible + Estado Anterior.",
    "fonte_esperada": "Bible: regras_magia > restricoes_geograficas"
  },
  {
    "id": "CONT-004",
    "categoria": "VOZ_NARRATIVA",
    "afirmacao": "A narrativa usa 'eu' e presente (1a pessoa, presente)",
    "pergunta": "O genero + Bible definem '3a pessoa limitada, passado'. A voz contradiz? Responda CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS na Bible + Estado Anterior.",
    "fonte_esperada": "Bible: metadados > voz_narrativa"
  }
]
```

---

# 5. Formato de Saida (OBRIGATORIO)

Arquivo: `{caminho_cena}/{RESULTADO_CONTINUIDADE_ARQ}`

```json
{
  "cena_id": "cap_04_cena_02",
  "total_verificacoes": 12,
  "confirmados": 10,
  "contraditos": 1,
  "nao_encontrados": 1,
  "status_geral": "REPROVADO",
  "resultados": [
    {
      "id": "CONT-001",
      "status": "CONFIRMADO",
      "evidencia": "Bible: personagens > Elena > traços_fisicos: 'canhota, usa mao esquerda para tarefas finas'",
      "categoria": "PERSONAGEM_ACAO"
    },
    {
      "id": "CONT-002",
      "status": "CONFIRMADO",
      "evidencia": "Estado Anterior: cap_03_cena_04 termina as 23:15. Bible: cronologia nao impede passagem de 4h. Plausivel.",
      "categoria": "TIMELINE_CRONOLOGIA"
    },
    {
      "id": "CONT-003",
      "status": "CONTRADITO",
      "evidencia": "Bible: regras_magia > restricoes_geograficas: 'Magos nascidos no Sul nao tem afinidade com elemento Fogo. Nao podem lancar feitiços de fogo.'",
      "categoria": "CONCEITO_REGRA"
    },
    {
      "id": "CONT-004",
      "status": "CONFIRMADO",
      "evidencia": "Bible: metadados > voz_narrativa: '3a pessoa limitada, passado, distancia proxima'. Verificado: narrativa usa 'ela' e verbos no passado.",
      "categoria": "VOZ_NARRATIVA"
    },
    {
      "id": "CONT-005",
      "status": "NAO_ENCONTRADO",
      "evidencia": "Bible + Estado Anterior nao mencionam a marca do cafe que Elena bebe. Informacao nova, nao contraditoria.",
      "categoria": "LOCAL_CENARIO"
    }
  ],
  "erros": [
    "CONTRADITO: CONT-003 - Marcus (nascido no Sul) conjura fogo. Regra rigida da Bible violada."
  ],
  "timestamp": "2026-07-27T14:30:00Z"
}
```

---

# 5. Como o Orquestrador Gera as Perguntas (para seu contexto)

Voce NAO faz isso. Mas e util saber COMO as perguntas chegam ate voce:

```
FUNCAO ORQUESTRADOR_GERAR_PERGUNTAS_CONTINUIDADE(saida_escritor, bible, estado_anterior):
    // Extrai da prosa do escritor (LENDO a prosa, so o orquestrador faz isso)
    // E transforma em perguntas binarias para o Validador Continuidade
    
    perguntas = []
    
    // 1. Personagens mencionados na cena
    PARA CADA personagem EM EXTRAIR_PERSONAGENS(saida_escritor):
        perguntas.ADICIONAR(criar_pergunta_personagem_acao(personagem, bible))
        perguntas.ADICIONAR(criar_pergunta_personagem_estado(personagem, estado_anterior))
        perguntas.ADICIONAR(criar_pergunta_personagem_localizacao(personagem, bible, estado_anterior))
    
    // 2. Timeline
    perguntas.ADICIONAR(criar_pergunta_timeline(saida_escritor, estado_anterior, bible))
    
    // 3. Locais/Cenarios
    PARA CADA local EM EXTRAIR_LOCAIS(saida_escritor):
        perguntas.ADICIONAR(criar_pergunta_local_geografia(local, bible))
        perguntas.ADICIONAR(criar_pergunta_local_cenario(local, bible))
    
    // 4. Conceitos/Termos/Regras
    PARA CADA conceito EM EXTRAIR_CONCEITOS(saida_escritor):
        SE conceito EM bible.regras_rigidas OU bible.conceitos:
            perguntas.ADICIONAR(criar_pergunta_conceito_regra(conceito, bible))
    
    // 5. Fios narrativos
    PARA CADA fio EM EXTRAIR_FIOS(saida_escritor):
        perguntas.ADICIONAR(criar_pergunta_fio_setup_payoff(fio, bible, estado_anterior))
    
    // 6. Voz/POV
    perguntas.ADICIONAR(criar_pergunta_voz_pov(saida_escritor, bible, genero))
    
    // 7. Objetivo/Mudanca
    perguntas.ADICIONAR(criar_pergunta_objetivo_mudanca(saida_escritor, estado_anterior))
    
    SALVAR(f"{caminho_cena}/{PERGUNTAS_CONTINUIDADE_ARQ}", perguntas)
```

---

# 6. Diferencas Chave: MARCH vs CONTINUIDADE

| Aspecto | MARCH | CONTINUIDADE |
|---------|-------|--------------|
| **Fonte da verdade** | Corpus original (fatos externos) | Bible + Estado Anterior (fatos internos da obra) |
| **O que valida** | Fatos verificaveis no mundo real | Coerencia interna da narrativa |
| **NAO_ENCONTRADO** | Reprova se >30% (falta lastro) | **Aceitavel** (info nova legítima) |
| **CONTRADITO** | 1 = Reprova | 1 = Reprova |
| **Tipico Ficcao** | Pouco uso (worldbuilding -> Bible) | **Uso intensivo** (personagens, timeline, regras, voz) |
| **Tipico Nao-Ficcao** | **Uso intensivo** (dados, estudos) | Moderado (conceitos, estrutura, voz) |
| **Cegueira** | Nao ve prosa | Nao ve prosa (recebe perguntas extraidas pelo orquestrador) |

---

# 7. Performance

- Cena tipica: 8-15 verificacoes de continuidade
- Tempo alvo: < 20 segundos por cena
- Bible e Estado Anterior sao pequenos (indexaveis em memoria)
- Paralelize verificacoes independentes
---

# NOVO — PROVA DE LINHAGEM (input_checksum) — OBRIGATORIO

No JSON de saida (`_resultado_continuidade.json`), registre **obrigatoriamente**:

```json
"input_checksum": "<checksum etiquetado do _saida_escritor.md que VOCE validou>"
```

- Calcule com: `python3 utils/checksum.py calcular {worktree}/_saida_escritor.md` (formato `v1.0:xxxxxxxx`).
- Sem esse campo, o Vigia da Fabrica reprova a cena (validador sem registro de qual texto leu).
