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

## Piso de densidade (genérico, por tipo de obra)

Isto não é fórmula de parágrafo nem molde de enchimento. É um **piso mínimo abaixo do qual uma cena deve ser tratada como incompleta**, não como concisa — porque densidade insuficiente costuma ser sintoma de desenvolvimento raso (objetivo, obstáculo, mudança de estado ou evidência cortados pela metade), não de disciplina estilística.

| Tipo de obra | Mínimo de mostrar (SHOW) | Faixa orientativa de palavras por cena |
|---|---|---|
| Ficção literária / romance | ~70% | 1200–3000 |
| Não-ficção / divulgação científica | ~40% | 800–1500 |
| Memórias | ~80% | 1000–2500 |
| Técnico / manual | ~30% | 600–1200 |

Se uma cena sair abaixo da faixa, o Escritor deve perguntar a si mesmo: *o objetivo da cena foi cumprido, ou eu encerrei cedo?* Concisão legítima (uma cena que genuinamente termina em menos espaço, tendo cumprido gancho, desenvolvimento e mudança de estado) é aceitável. Cena curta porque um beat foi pulado não é.

## Gatilhos de reprovação (retorno cirúrgico, não reescrita total)

| Gatilho | O que verificar |
|---|---|
| Cena sem mudança de estado perceptível | O leitor termina a cena no mesmo lugar onde começou |
| Densidade abaixo do piso sem justificativa | Ver tabela acima |
| Tell excessivo onde o tipo de obra pede show | Afirmação de emoção/conclusão sem a cena que a sustente |
| Analogia legendada | "Imagine que...", "É como se fosse...", "Para ilustrar..." |
| Voz ou pessoa narrativa inconsistente com a cena anterior | Checar contra a Bible |
| Fecho sem propulsão | Termina em conclusão fechada, não em eco/pergunta/consequência |

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

