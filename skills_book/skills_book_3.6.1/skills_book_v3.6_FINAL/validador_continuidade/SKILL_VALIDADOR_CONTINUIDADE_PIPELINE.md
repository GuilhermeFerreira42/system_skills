# Skill do Validador de Continuidade — Skill 3

## Missão

Verificar se as afirmações de continuidade extraídas pelo Orquestrador são compatíveis com Bible e Estado, sem ler a prosa.

## Categorias

- voz e POV;
- conceito e definição;
- regra rígida;
- timeline;
- personagem ou local;
- fio narrativo;
- objetivo e mudança de estado;
- terminologia.

## Vereditos

- `CONFIRMADO`: Bible/Estado sustentam a afirmação.
- `CONTRADITO`: Bible/Estado dizem o oposto.
- `NAO_ENCONTRADO`: informação nova que ainda não está registrada; não é contradição por si só.

## Saída

```json
{
  "cena_id": "cap_01_cena_01",
  "input_checksum": "v1.0:xxxxxxxx",
  "total_verificacoes": 0,
  "confirmados": 0,
  "contraditos": 0,
  "nao_encontrados": 0,
  "status_geral": "APROVADO",
  "resultados": [],
  "erros": [],
  "timestamp": "ISO-8601"
}
```

Um `CONTRADITO` reprova a cena. Não use métricas de ritmo, tamanho ou estilo.

---

## Adendo v3.6 — Checagem de cadência da metáfora-mestra (mantido da v3.5)

Além de terminologia e fatos entre cenas, este validador passa a verificar, na
consolidação da obra:

1. a imagem-mãe registrada na Bible aparece na **cena 1**;
2. aparece em **pelo menos uma cena de cada capítulo** posterior;
3. é **retomada explicitamente na última cena**;
4. **nenhuma segunda imagem estrutural** concorrente foi introduzida (imagens
   que sejam extensão declarada da imagem-mãe não contam como concorrentes).

Falha em qualquer um dos quatro itens → `REPROVADO_CONTINUIDADE` com o campo
`tipo: "METAFORA_DESCARTAVEL"`.

