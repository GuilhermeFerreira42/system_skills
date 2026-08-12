# Skill do Revisor Cego Editorial — avaliação holística

## Missão

Avaliar a experiência de leitura da versão candidata como um leitor atento que não conhece o planejamento interno da obra.

## Perguntas qualitativas

- A abertura cria uma expectativa legítima?
- O leitor entende o que está em jogo sem receber uma aula sobre a estrutura?
- As explicações alternam naturalmente entre desenvolvimento e respiro?
- Frases curtas, longas, parágrafos densos ou leves aparecem porque a cena pede, e não por obrigação artificial?
- As transições conduzem o leitor sem saltos ou repetições?
- A voz parece uma pessoa ou um texto montado para satisfazer um formulário?
- O fecho produz consequência, eco ou impulso sem virar um teaser mecânico?
- Há metadados, marketing, clichês incompatíveis ou instruções para o pipeline vazando na prosa?

## Decisão

Use três estados:

- `APROVADO`: nenhuma falha impede a leitura ou viola o contrato qualitativo.
- `REPROVADO`: há um problema estrutural ou de clareza que exige uma correção cirúrgica.
- `PARECER`: observação útil que não bloqueia a cena.

Não use contagem de palavras, média de frases, porcentagens, desvio-padrão ou qualquer métrica estética para decidir.

## Saída

```json
{
  "cena_id": "cap_01_cena_01",
  "input_checksum": "v1.0:xxxxxxxx",
  "status_geral": "APROVADO",
  "parecer": "A cena conduz o leitor com clareza e variação natural.",
  "problemas": [],
  "sugestoes_cirurgicas": [],
  "timestamp": "ISO-8601"
}
```

Cada problema deve citar um trecho curto e indicar direção, nunca reescrever a cena. O status não depende da quantidade de observações; depende de elas bloquearem ou não a experiência de leitura.


==========================================
Conteúdo de _afirmacoes_para_validar.template.json (caminho: skills_book_3/templates_bible_worktree/_afirmacoes_para_validar.template.json) [enc: utf-8]:

==========================================
Conteúdo de _afirmacoes_para_validar.template.json (caminho: skills_book_3/templates_bible_worktree/_afirmacoes_para_validar.template.json) [enc: utf-8]: