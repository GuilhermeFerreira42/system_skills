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

## Criterio de Completude e Extensão

Uma cena está completa quando o leitor consegue responder a estas 3 perguntas:

1. **O que estava em jogo?** (O leitor identifica o conflito, a tensão ou a pergunta da cena).
2. **Que nova peça do quebra-cabeça eu recebi?** (O leitor identifica o novo dado, mecanismo ou virada que a cena entregou).
3. **Como isso mudou o que eu sabia?** (O leitor percebe a mudança de estado — sua própria visão ou a do personagem foi alterada).

**Extensão operacional:** a faixa média histórica para não-ficção prática é de 800 a 1.500 palavras por cena. Cada gênero pode definir sua própria faixa no `GENERO.md`. Este não é um piso duro — é um sinal de desenvolvimento: se a cena saiu com menos de 600 palavras, muito provavelmente um movimento retórico inteiro foi pulado. Antes de considerar a cena pronta, verifique se todos os movimentos previstos para ela foram executados.
## Gatilhos de reprovação (retorno cirúrgico, não reescrita total)

| Gatilho | O que verificar |
|---|---|
| Cena sem mudança de estado perceptível | O leitor termina a cena no mesmo lugar onde começou |
| Densidade muito abaixo da faixa do gênero sem justificativa | Verificar se algum movimento retórico foi pulado |
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