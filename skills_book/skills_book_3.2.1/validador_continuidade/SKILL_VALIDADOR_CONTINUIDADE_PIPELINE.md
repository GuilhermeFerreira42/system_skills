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


==========================================
Conteúdo de BOOT_VALIDADOR_MARCH_PIPELINE.md (caminho: skills_book_3/validador_march/BOOT_VALIDADOR_MARCH_PIPELINE.md) [enc: utf-8]:

==========================================
Conteúdo de BOOT_VALIDADOR_MARCH_PIPELINE.md (caminho: skills_book_3/validador_march/BOOT_VALIDADOR_MARCH_PIPELINE.md) [enc: utf-8]: