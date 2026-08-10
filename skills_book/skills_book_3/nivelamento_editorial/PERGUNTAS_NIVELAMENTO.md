# Perguntas do nivelamento editorial

Faça as perguntas no boot, uma por vez, se o usuário ainda não tiver um perfil salvo. Aceite uma resposta livre além de A/B/C quando ela for mais informativa; nesse caso, o Orquestrador resume a preferência sem inventar uma regra numérica.

## Abertura

**Como você quer que a obra abra suas cenas?**

- **A — Imersão e pergunta:** coloque o leitor dentro de uma situação, imagem ou pergunta antes de explicar a tese.
- **B — Direto ao ponto:** apresente a ideia central cedo, com eficiência e pouca preparação.
- **C — Caso ou ação:** comece por um caso concreto, ação, cena vivida ou exemplo e extraia a ideia depois.

## Profundidade

**Como deve ser a profundidade da explicação?**

- **A — Ampla:** desenvolva camadas, contexto, contraexemplos e consequências quando forem úteis.
- **B — Equilibrada:** explique o suficiente para compreensão e avance sem repetições.
- **C — Enxuta:** privilegie o essencial, com transições rápidas e pouca digressão.

## Analogias e exemplos

**Qual papel analogias, casos e exemplos devem desempenhar?**

- **A — Guias visuais:** use uma imagem ou exemplo físico sempre que um conceito abstrato pedir ajuda.
- **B — Uso seletivo:** empregue analogias quando elas realmente clarificarem o raciocínio.
- **C — Referência direta:** prefira definição, evidência e procedimento; use analogias apenas quando inevitáveis.

## Voz do autor

**Como o narrador deve se posicionar?**

- **A — Revelação respeitosa:** descubra junto com o leitor, seja claro e humano, critique sistemas sem atacar pessoas.
- **B — Neutra engajada:** mantenha o narrador discreto, interessado e acessível, sem polemizar.
- **C — Distante e técnica:** adote uma voz formal, precisa e referencial, adequada a manuais e tratados.

## Registro

Depois das respostas, salve algo equivalente a:

```json
{
  "estilo_abertura": "A",
  "profundidade": "B",
  "uso_analogias": "A",
  "voz_autor": "A",
  "foco_livre": "...",
  "fonte": "usuario",
  "preenchido_em": "ISO-8601"
}
```

O campo `fonte` deve dizer a verdade: `usuario`, `perfil_existente` ou `padrao_confirmado`. O perfil pode ser refeito quando o usuário pedir explicitamente.
