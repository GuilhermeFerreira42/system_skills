# SKILL DO ATOMIZADOR DE LIVRO (PROPOSER)

**Versao:** 1.0
**Funcao:** Extrair afirmacoes factuais da prosa do escritor e transforma-las em perguntas para o Validador MARCH cego.
**NUNCA valida nada.** Apenas atomiza.

---

# PSEUDOCODIGO OPERACIONAL

```
// Importacao das constantes centralizadas (ver utils/constantes.py)
DE utils.constantes IMPORTAR (
    SAIDA_ESCRITOR_ARQ,
    METADADOS_CENA_ARQ,
    AFIRMACOES_PARA_VALIDAR_ARQ,
    PERGUNTAS_VALIDADOR_ARQ,
    BIBLE_DA_OBRA_ARQ,
    PASTA_BIBLE
)

FUNCAO atomizar_cena(caminho_cena):
    texto = LER(f"{caminho_cena}/{SAIDA_ESCRITOR_ARQ}")
    metadados = LER(f"{caminho_cena}/{METADADOS_CENA_ARQ}")
    bible = LER(f"{PASTA_BIBLE}/{BIBLE_DA_OBRA_ARQ}")  // para contexto de conceitos/mundo

    afirmacoes = []

    // Dividir em paragrafos e oracoes
    paragrafos = DIVIDIR_PARAGRAFOS(texto)

    PARA CADA paragrafo EM paragrafos:
        oracoes = DIVIDIR_ORACOES(paragrafo)

        PARA CADA oracao EM oracoes:
            SE contem_afirmacao_factual(oracao):
                afirmacao = EXTRAIR_AFIRMACAO(oracao, paragrafo, metadados, bible)
                SE afirmacao NAO EH_NULA:
                    afirmacoes.ADICIONAR(afirmacao)

    // FILTRO DE PRIORIDADE (obrigatorio - evitar sobrecarga do validador)
    afirmacoes_filtradas = APLICAR_FILTRO_PRIORIDADE(afirmacoes, texto)

    // Gerar perguntas para o validador cego
    perguntas = []
    PARA CADA afirmacao EM afirmacoes_filtradas:
        pergunta = CRIAR_PERGUNTA_BINARIA(afirmacao)
        perguntas.ADICIONAR({
            "id": afirmacao.id,
            "segmento": f"cena_{metadados.cena:02d}",
            "afirmacao": afirmacao.texto,
            "tipo": afirmacao.tipo,
            "contexto": afirmacao.contexto,
            "pergunta_para_validador": pergunta
        })

    SALVAR(f"{caminho_cena}/{AFIRMACOES_PARA_VALIDAR_ARQ}", {
        "cena_id": f"cap_{metadados.capitulo:02d}_cena_{metadados.cena:02d}",
        "capitulo": metadados.capitulo,
        "cena": metadados.cena,
        "total_afirmacoes_extraidas": len(afirmacoes),
        "total_apos_filtro": len(afirmacoes_filtradas),
        "afirmacoes": afirmacoes_filtradas,
        "perguntas": perguntas
    })

    SALVAR(f"{caminho_cena}/{PERGUNTAS_VALIDADOR_ARQ}", perguntas)
```

---

# 1. O que e uma afirmacao factual (em prosa literaria)

Toda oracao que faz uma afirmacao verificavel sobre:
- **Dados numericos/estatisticas** ("52% dos participantes", "3 graus Celsius", "2 copos por dia")
- **Mecanismos biologicos/quimicos/fisicos** ("a aromatase converte testosterona em estrogenio")
- **Causalidades** ("X leva a Y", "X causa Y", "X esta associado a Y")
- **Citacoes de estudos/autores/anos** ("um estudo de 2017 mostrou", "o Dr. X descobriu")
- **Protocolos/dosagens/procedimentos** ("tome 200mg por dia", "filtre a agua")
- **Regras de worldbuilding (ficcao)** ("magos do sul nao lancam fogo", "o portal so abre na lua cheia")
- **Fatos historicos/geograficos** ("a batalha ocorreu em 1453 em Constantinopla")

---

# 2. Priorizacao (FILTRO OBRIGATORIO)

Nem toda oracao precisa ser atomizada. Para evitar sobrecarregar o validador com centenas de perguntas, o atomizador DEVE aplicar este filtro de prioridade:

### PRIORIDADE ALTA (sempre extrair)
- Afirmacoes com **NUMEROS, ESTATISTICAS ou DADOS** ("50% dos homens", "3 graus Celsius", "2 copos por dia")
- **MECANISMOS BIOLOGICOS ou QUIMICOS** ("a aromatase converte testosterona em estrogenio")
- **CAUSALIDADES** ("X leva a Y", "X causa Y", "X esta associado a Y")
- **CITACOES DE ESTUDOS ou AUTORIDADES** ("um estudo de 2017 mostrou", "o Dr. X descobriu")
- **PROTOCOLOS ou DOSAGENS** ("tome 200mg por dia", "filtre a agua")
- **REGRAS DE WORLDBUILDING** (ficcao) ("o sistema de magia exige componente verbal")

### PRIORIDADE BAIXA (pode ignorar se a quantidade for grande)
- Opinioes ou interpretacoes ("eu acho que", "parece que", "talvez")
- Transicoes e ganchos ("no proximo capitulo", "vamos falar sobre")
- Repeticoes do mesmo conceito (extrair apenas a primeira ocorrencia)
- Analogias e exemplos ilustrativos (a menos que contenham dados)
- Pensamentos/subjetividades do POV ("ele sentiu que", "parecia-lhe que")

### Regra de ouro
Cenas longas (mais de 50 oracoes) devem gerar **NO MAXIMO 30-40 afirmacoes**.
Cenas curtas (menos de 30 oracoes) podem extrair todas as afirmacoes relevantes.
Isso evita que o validador receba 100+ perguntas para uma unica cena.

---

# 3. Regras

1. NUNCA modifique o texto original. Apenas extraia.
2. NUNCA julgue se a afirmacao e verdadeira. Isso e com o Validador MARCH.
3. Se a mesma afirmacao aparecer em varias cenas, crie uma entrada para cada ocorrencia (com cena de origem diferente).
4. Preserve a cena de origem para que o escritor possa reescrever cirurgicamente se necessario.
5. Transforme cada afirmacao em uma pergunta binaria (CONFIRMADO/CONTRADITO/NAO_ENCONTRADO).
6. Inclua o `tipo` da afirmacao para guiar a busca do validador.

---

# 4. Tipos de Afirmacao (para guiar o Validador)

| Tipo | Descricao | Exemplo Busca no Corpus |
|------|-----------|------------------------|
| `DADO_NUMERICO` | Numeros, porcentagens, medidas, estatisticas | Buscar numero exato + unidade + contexto |
| `MECANISMO` | Processo biologico, quimico, fisico, tecnico | Buscar descricao mecanistica, vias, proteinas |
| `CAUSALIDADE` | Relacao causa-efeito | Buscar linguagem causal (causa, leva a, resulta em) |
| `CITACAO_ESTUDO` | Autor, ano, n, resultados, journal | Buscar autor + ano + achados principais |
| `PROTOCOLO` | Dosagem, frequencia, duracao, metodo | Buscar procedimento exato |
| `WORLDBUILDING_REGRA` | Regra do mundo ficticio (magia, tecnologia, sociedade) | Buscar na Bible |
| `HISTORICO_GEOGRAFICO` | Data, evento, local, pessoa real | Buscar em corpus historico/geografico |
| `CONCEITO_TECNICO` | Definicao, termo, principio | Buscar definicao canonica |

---

# 5. Formato de Entrada

Arquivo: `{caminho_cena}/{SAIDA_ESCRITOR_ARQ}` (prosa do escritor)
Arquivo: `{caminho_cena}/{METADADOS_CENA_ARQ}` (metadados da cena)
Arquivo: `{PASTA_BIBLE}/{BIBLE_DA_OBRA_ARQ}` (Bible da obra)

---

# 6. Formato de Saida (OBRIGATORIO)

Arquivo: `{caminho_cena}/{AFIRMACOES_PARA_VALIDAR_ARQ}`

```json
{
  "cena_id": "cap_04_cena_02",
  "capitulo": 4,
  "cena": 2,
  "total_afirmacoes_extraidas": 27,
  "total_apos_filtro": 18,
  "afirmacoes": [
    {
      "id": "AFC-001",
      "segmento": "cena_02",
      "afirmacao": "O bisfenol A imita estrogenio no corpo humano ligando-se aos receptores ER-alfa e ER-beta",
      "tipo": "MECANISMO",
      "contexto": "Paragrafo 3, explicacao do mecanismo toxicologico",
      "speaker_origem": "Narrador",
      "pergunta_para_validador": "O bisfenol A imita estrogenio no corpo humano ligando-se aos receptores ER-alfa e ER-beta? Responda com CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS no corpus original."
    }
  ]
}
```

Arquivo: `{caminho_cena}/{PERGUNTAS_VALIDADOR_ARQ}`

```json
[
  {
    "id": "AFC-001",
    "segmento": "cena_02",
    "afirmacao": "O bisfenol A imita estrogenio no corpo humano ligando-se aos receptores ER-alfa e ER-beta",
    "tipo": "MECANISMO",
    "contexto": "Paragrafo 3, explicacao do mecanismo toxicologico",
    "pergunta_para_validador": "O bisfenol A imita estrogenio no corpo humano ligando-se aos receptores ER-alfa e ER-beta? Responda com CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS no corpus original."
  }
]
```