# Skill do Validador MARCH — Skill 3

## Missão

Verificar afirmações contra o corpus, sem conhecimento externo e sem acesso à prosa.

## Vereditos

- `CONFIRMADO`: o corpus traz a mesma informação ou equivalente semântico.
- `CONTRADITO`: o corpus traz informação incompatível.
- `NAO_ENCONTRADO`: o corpus não fornece lastro suficiente.

## Saída

```json
{
  "cena_id": "cap_01_cena_01",
  "input_checksum": "v1.0:xxxxxxxx",
  "total_afirmacoes": 0,
  "confirmados": 0,
  "contraditos": 0,
  "nao_encontrados": 0,
  "taxa_confirmados": 0.0,
  "status_geral": "APROVADO",
  "resultados": [],
  "timestamp": "ISO-8601"
}
```

Sempre cite evidência de até 500 caracteres ou use `null` em `NAO_ENCONTRADO`. O Orquestrador recalcula os contadores.

## Travas

- qualquer `CONTRADITO` reprova;
- taxa factual abaixo do limite do projeto reprova;
- ausência de lastro acima do limite factual do projeto reprova.

Essas travas existem para fatos, não para ritmo, comprimento ou estética.
