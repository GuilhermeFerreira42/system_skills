# SKILL DO ATOMIZADOR (PIPELINE GENÉRICO)

**Versão:** 3.0
**Função:** Extrair afirmações factuais verificáveis da prosa do Escritor e transformá-las em perguntas binárias para o Validador MARCH cego.

---

## PSEUDOCÓDIGO OPERACIONAL

```
FUNCAO atomizar_cena(caminho_cena, genero):
    texto = LER(f"{caminho_cena}/_saida_escritor.md")
    bible = LER("execucao/bible/bible_da_obra.md")

    # SE gênero é Ficção pura sem corpus factual
    SE genero.tipo == "FICCAO_PURA":
        SALVAR(f"{caminho_cena}/_afirmacoes_para_validar.json", {"afirmacoes_filtradas": []})
        SALVAR(f"{caminho_cena}/_perguntas_validador.json", [])
        RETORNAR

    # MODO NORMAL (Não-Ficção / Técnico)
    afirmacoes_brutas = []
    paragrafos = DIVIDIR_PARAGRAFOS(texto)
    PARA CADA paragrafo EM paragrafos:
        oracoes = DIVIDIR_ORACOES(paragrafo)
        PARA CADA oracao EM oracoes:
            SE contem_afirmacao_factual(oracao):
                afirmacao = EXTRAIR_AFIRMACAO(oracao, paragrafo, bible, genero)
                SE afirmacao NAO NULA:
                    afirmacoes_brutas.ADICIONAR(afirmacao)

    # Filtro de Prioridade
    SE len(afirmacoes_brutas) > 50:
        limite = 30
    SENAO:
        limite = len(afirmacoes_brutas)

    afirmacoes_filtradas = APLICAR_FILTRO_PRIORIDADE(afirmacoes_brutas, limite)

    # Gerar perguntas
    perguntas = []
    PARA CADA af EM afirmacoes_filtradas:
        perguntas.ADICIONAR({
            "id": af.id,
            "segmento": f"cena_{af.cena:02d}",
            "afirmacao": af.texto,
            "tipo": af.tipo,
            "pergunta_para_validador": CRIAR_PERGUNTA_BINARIA(af)
        })

    # Salvar
    SALVAR(f"{caminho_cena}/_afirmacoes_para_validar.json", {
        "cena_id": f"cap_{af.capitulo:02d}_cena_{af.cena:02d}",
        "capitulo": af.capitulo,
        "cena": af.cena,
        "total_afirmacoes_extraidas": len(afirmacoes_brutas),
        "total_apos_filtro": len(afirmacoes_filtradas),
        "afirmacoes_filtradas": afirmacoes_filtradas,
        "perguntas": perguntas
    })

    SALVAR(f"{caminho_cena}/_perguntas_validador.json", perguntas)
```

---

## 1. O que é uma Afirmação Factual

| Gênero | Quando extrair |
|---|---|
| **Não-Ficção / Podbook / Técnico** | SEMPRE — dados, mecanismos, cases, protocolos, regras |
| **Ficção com base factual** | EXTRAIR referências factuais (datas, eventos, locais) |
| **Ficção pura** | ARRAY VAZIO — não há o que validar contra corpus |

---

## 2. Filtro de Prioridade

### PRIORIDADE ALTA
- Dados numéricos
- Mecanismos
- Causalidades
- Citações de cases/autores
- Protocolos
- Regras
- Definições
- Nomes próprios

### PRIORIDADE BAIXA
- Opiniões
- Transições
- Repetições
- Marcadores orais
- Subjetividades

### Limite
- Cenas longas (>50 orações): NO MÁXIMO 30 afirmações
- Cenas curtas (<30 orações): TODAS as relevantes (mínimo 3)

---

## 3. Tipos de Afirmação

| Tipo | Quando usar |
|---|---|
| `DADO_NUMERICO` | Números, %, medidas |
| `MECANISMO` | Processo operacional |
| `CAUSALIDADE` | Relação causa-efeito |
| `CITACAO_CASE` | Aluno, autor, número |
| `PROTOCOLO` | Passo a passo, configuração |
| `REGRA_MERCADO` | Regra legal, fiscal |
| `CONCEITO_TECNICO` | Definição de termo |
| `NOME_PROPRIO` | Ferramenta, marca, aluno |
| `REFERENCIA_FACTUAL` | (Ficção) Referência a evento real |

---

## 4. Formato de Saída

### `_afirmacoes_para_validar.json`

```json
{
  "cena_id": "cap_03_cena_02",
  "capitulo": 3,
  "cena": 2,
  "total_afirmacoes_extraidas": 12,
  "total_apos_filtro": 7,
  "afirmacoes_filtradas": [
    {
      "id": "AFC-001",
      "segmento": "cena_02",
      "afirmacao": "Validação = R$ 10.000 em vendas + 100 pedidos em 90 dias",
      "tipo": "DADO_NUMERICO",
      "contexto": "Definição da régua de validação",
      "speaker_origem": "Narrador (Mentor)",
      "pergunta_para_validador": "No método, 'validação' significa R$ 10.000 em vendas + 100 pedidos em 90 dias? Responda CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS no corpus."
    }
  ]
}
```

### `_perguntas_validador.json`

```json
[
  {
    "id": "AFC-001",
    "segmento": "cena_02",
    "afirmacao": "Validação = R$ 10.000 em vendas + 100 pedidos em 90 dias",
    "tipo": "DADO_NUMERICO",
    "pergunta_para_validador": "No método, 'validação' significa R$ 10.000 em vendas + 100 pedidos em 90 dias? Responda CONFIRMADO/CONTRADITO/NAO_ENCONTRADO baseado APENAS no corpus."
  }
]
```

---

## 5. Regras

1. NUNCA modifique o texto original. Apenas extraia.
2. NUNCA julgue se a afirmação é verdadeira. Isso é com o Validador MARCH.
3. Mantenha a cena de origem.
4. Transforme cada afirmação em pergunta binária.
5. Inclua o `tipo`.
6. Respeite o limite de 30.

---

## 6. Validação Interna Antes de Salvar

- [ ] JSON tem o formato correto?
- [ ] Entre 3 e 30 afirmações filtradas (ou array vazio se Ficção)?
- [ ] Cada afirmação tem `id`, `afirmacao`, `tipo`, `contexto`, `pergunta_para_validador`?
- [ ] Perguntas são binárias?
- [ ] Não incluiu afirmações de pura opinião?
