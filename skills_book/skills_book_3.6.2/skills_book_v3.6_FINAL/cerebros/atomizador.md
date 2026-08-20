# CÉREBRO — Atomizador (Skills Book v3.6 FINAL)


---

> **Este arquivo é a fonte única de verdade deste papel.**
> Ele reúne, **verbatim e sem alteração de lógica**, o conteúdo original das skills
> abaixo. Os arquivos originais continuam intactos nos seus caminhos de origem —
> este é um espelho de leitura para o subagente, não uma substituição.
>
> Se você precisar mudar o comportamento deste papel, mude aqui **e** no original,
> ou regenere este arquivo com `gerar_subagentes.py`.
>
> **Fontes concatenadas, nesta ordem:**
> 1. `atomizador/BOOT_ATOMIZADOR_PIPELINE.md`
> 2. `atomizador/SKILL_ATOMIZADOR_PIPELINE.md`

---

<!-- ===== INÍCIO: atomizador/BOOT_ATOMIZADOR_PIPELINE.md ===== -->

## ⟦Fonte original: `atomizador/BOOT_ATOMIZADOR_PIPELINE.md`⟧

# Boot do Atomizador — Skill 3

Leia somente `_saida_candidato.md` e as instruções do tipo de obra. Não leia resultados MARCH, Continuidade, Bible ou Estado para confirmar o que o texto diz.

Produza:

- `_afirmacoes_para_validar.json`;
- `_perguntas_validador.json`.

O pacote deve carregar o `input_checksum` fornecido pelo Orquestrador, mas isso não revela a prosa ao Validador MARCH.

<!-- ===== FIM: atomizador/BOOT_ATOMIZADOR_PIPELINE.md ===== -->

---

<!-- ===== INÍCIO: atomizador/SKILL_ATOMIZADOR_PIPELINE.md ===== -->

## ⟦Fonte original: `atomizador/SKILL_ATOMIZADOR_PIPELINE.md`⟧

# Skill do Atomizador — Skill 3

## Função

Extrair do candidato apenas afirmações que precisam de lastro factual. Não julgar estilo e não corrigir a prosa.

## Regras

- Leia `_saida_candidato.md`, não `_saida_escritor.md` como uma versão separada.
- Não transforme toda frase opinativa em fato.
- Separe dado, mecanismo, citação, protocolo, nome próprio e causalidade.
- Preserve o vínculo narrativo dos dados: vincule nomes próprios, histórias de vida e experimentos às suas respectivas teses/mecanismos (ex: não desvincule a história do médico e da prisão dos 4 mitos de desidratação que ele tratou).
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

<!-- ===== FIM: atomizador/SKILL_ATOMIZADOR_PIPELINE.md ===== -->
