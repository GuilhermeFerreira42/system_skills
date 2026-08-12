# Skill do Atomizador — Skill 3

## Função

Extrair do candidato apenas afirmações que precisam de lastro factual. Não julgar estilo e não corrigir a prosa.

## Regras

- Leia `_saida_candidato.md`, não `_saida_escritor.md` como uma versão separada.
- Não transforme toda frase opinativa em fato.
- Separe dado, mecanismo, citação, protocolo, nome próprio e causalidade.
- Para ficção sem corpus factual, entregue lista vazia ou somente afirmações de worldbuilding explicitamente destinadas à Bible.
- Não use conhecimento externo.

## Formato

```json
{
  "cena_id": "cap_01_cena_01",
  "input_checksum": "v1.0:xxxxxxxx",
  "afirmacoes": [
    {
      "id": "AFC-001",
      "texto": "...",
      "tipo": "DADO_NUMERICO",
      "pergunta_para_validador": "O corpus confirma ...?"
    }
  ]
}
```

O Orquestrador recalcula agregados no resultado MARCH. O Atomizador não aprova a cena.


==========================================
Conteúdo de BIBLE_ESQUELETO_VAZIO.md (caminho: skills_book_3/bible/BIBLE_ESQUELETO_VAZIO.md) [enc: utf-8]:

==========================================
Conteúdo de BIBLE_ESQUELETO_VAZIO.md (caminho: skills_book_3/bible/BIBLE_ESQUELETO_VAZIO.md) [enc: utf-8]: