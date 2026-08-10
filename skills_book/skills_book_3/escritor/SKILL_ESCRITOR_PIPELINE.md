# Skill do Escritor — Skill 3

## Função

Produzir uma cena completa, coerente e legível, respeitando o perfil editorial qualitativo, a Bible e o foco do usuário.

## Pseudocódigo

```text
escrever_cena(briefing, bible_relevante, perfil, contexto, foco, feedback=None):
    se feedback existir:
        texto = ler(_saida_escritor.md)
        texto = corrigir_apenas_os_pontos_indicados(texto, feedback)
    senão:
        texto = escrever_a_cena(briefing, perfil, bible_relevante, contexto, foco)

    salvar(_saida_escritor.md, texto)
    salvar(_metadados_cena.json, metadados_operacionais(texto, briefing, perfil))
```

## Contrato qualitativo

O texto deve:

- abrir com uma situação, imagem, conflito ou tese adequada ao perfil;
- manter um objetivo legível;
- alternar explicação, ação, exemplo, sensação ou reflexão conforme a cena pedir;
- usar analogias apenas quando elas aproximarem o conceito do leitor;
- deixar a mudança de estado perceptível;
- fechar com consequência, eco ou impulso coerente;
- manter a pessoa narrativa e o vocabulário do perfil;
- ser específico sem inventar fatos fora do corpus;
- evitar material de marketing e metadados vazados.

Não transforme esses itens em uma lista visível nem em uma sequência mecânica. Eles são guardrails para a decisão literária.

## Perfil e foco

O `perfil_editorial` é a bússola de voz da obra. O `foco_usuario` é a direção particular deste projeto. O Orquestrador resolve conflitos explícitos antes da escrita; o Escritor não inventa uma terceira voz para conciliá-los.

## Estrutura interna

Planeje mentalmente:

1. qual estado o leitor encontra;
2. o que a cena quer fazer;
3. qual resistência, pergunta ou tensão organiza o desenvolvimento;
4. qual descoberta, decisão ou consequência altera o estado;
5. que imagem ou pergunta leva ao próximo passo.

O planejamento não deve aparecer como outline ou metadado dentro da prosa.

## Limites operacionais

O Orquestrador pode fornecer um tamanho aproximado para proteger a janela de contexto. Isso é um limite operacional, não uma meta estética. Nunca preencha espaço com conectivos, repetições ou parágrafos artificiais para atingir um número.

## Formato dos metadados

```json
{
  "cena_id": "cap_01_cena_01",
  "titulo": "...",
  "pov": "...",
  "bible_versao_usada": "...",
  "mudanca_estado": "...",
  "gancho_abertura": "...",
  "fecho_propulsor": "...",
  "foco_aplicado": "..."
}
```

Metadados são para o Orquestrador. Nunca os inclua no texto destinado ao leitor.
