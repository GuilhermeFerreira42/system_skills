# GENERO: PODBOOK_MENTOR

**Versão:** 1.0
**Base:** NAO_FICCAO
**Tipo:** PODBOOK (Estrutura de livro com alma de treinamento em áudio)
**Arquétipo Global:** PROBLEMA_SOLUCAO

---

## 1. Identidade e Voz Narrativa

- **Pessoa (REGRA OBRIGATÓRIA):**
  - **Padrão:** 1ª pessoa do mentor como base ("eu, Bruno", "na minha experiência", "quando eu comecei")
  - **2ª pessoa ("você") APENAS em:** comandos diretos, provocações, perguntas retóricas, instruções de ação
  - **PROIBIDO:** alternar entre 1ª e 2ª no meio da mesma frase
  - **PROPORÇÃO ESPERADA:** ~75% 1ª pessoa, ~25% 2ª pessoa
- **Tom de Voz:** Pragmático, transformador, pé no chão ("campo de batalha"), encorajador
- **Distância Narrativa:** Mentor/Consultor de negócios; proximidade de uma mentoria particular
- **Vocabulário:** Acessível e desmistificador; termos técnicos (SKU, EAN, ERP, etc.) DEVEM ser explicados via analogia na primeira menção
- **Ritmo:**
  - **Tipo:** Modular e ondulatório (Teoria → Analogia → Campo de Batalha/Ação)
  - **Extensão típica de frase:** máximo 25 palavras
  - **Extensão típica de parágrafo:** 3-5 frases, com pausas naturais

---

## 2. POV (Point of View)

- **Padrão:** Mentor (voz do mentor baseada em transcrições reais)
- **Quem fala:** O mentor (ex: Bruno, ou outro especialista)
- **Quem ouve:** Empreendedor / aluno / leitor que quer aprender o método
- **Multi-POV:** false
- **PROIBIDO:** POV de personagem fictício, head-hopping, múltiplos narradores

---

## 3. Estrutura de "Cena" (Módulo de Áudio)

- **Extensão:** 1.000 a 4.000 palavras por cena
- **Mínimo:** 1.000 palavras
- **Máximo:** 4.000 palavras
- **Estrutura interna:**
  - **Abertura (1-2 parágrafos):** comando OU provocação OU afirmação forte. PROIBIDO começar com "E aí, tudo bem?"
  - **Desenvolvimento (70% da cena):** teoria + analogia + caso real
  - **Fecho (1-2 parágrafos):** resumo do ganho + gancho para a próxima cena
- **Beats obrigatórios (no MÍNIMO 3 dos 6 abaixo):**
  1. **Abertura forte** (comando, provocação ou afirmação categórica)
  2. **Exposição de mecanismo** (como o conceito funciona)
  3. **Analogia de impacto** (comparação com algo físico ou cotidiano)
  4. **Caso real ou exemplo concreto** (case de aluno, do mentor, ou da marca)
  5. **Checklist prático** (no fim, formato "## Seu checklist desta cena")
  6. **Fecho propulsor** (gancho para a próxima cena)
- **Show mínimo:** 40% (cases, exemplos concretos, números reais, histórias do mentor)

---

## 4. Formato do Final de Cada Cena (OBRIGATÓRIO)

```markdown
[PROSA DA CENA]

---

## Resumo da cena

[3-5 frases em primeira pessoa do mentor, recapitulando o que foi apresentado.
Tom: "olha, o que a gente viu aqui foi..." — conversacional, não formal.]

---

## Seu checklist desta cena

Antes de ir para a próxima cena, você precisa ter feito ou decidido:

- [ ] [Ação 1 — concreta, executável hoje]
- [ ] [Ação 2 — concreta, executável hoje]
- [ ] [Ação 3 — concreta, executável hoje]
- [ ] [Decisão mental ou posicionamento interno]

---

**Próxima cena:** [título da próxima cena + gancho curto de uma frase]
```

**PROIBIDO colocar no final da cena:**
- JSON de metadados
- Tabelas de "palavras_estimadas", "POV", "bible_versao"
- Campos técnicos visíveis ao leitor
- Qualquer estrutura que não seja prosa + resumo + checklist

---

## 5. Regras de Oralidade

- **Frases curtas:** máximo 25 palavras por frase
- **Marcadores de oralidade:** use "olha", "tá", "sabe", "então", "olha só", "beleza", "pra" (em vez de "para")
- **Parágrafos respiratórios:** 3-5 frases por parágrafo
- **PROIBIDO travessão formal** ("—") dentro de frases — usar vírgula, ponto, ou dois pontos
- **PROIBIDO enumeração explicativa longa** ("X, Y, Z. Todos eles...")
- **PROIBIDO iniciar parágrafo com "E aí"** ou "Então" sem motivo narrativo
- **PERMITIDO e ENCORAJADO:** início direto ("Olha, o que a gente vai ver aqui é...", "Tá começando agora. Senta aí.")

---

## 6. Estrutura Global (Arquitetura do Livro)

- **Número de capítulos:** 10-15 (depende do método)
- **Macro-estrutura:** Sequencial, progressiva (cada capítulo pressupõe o anterior)
- **Relação entre capítulos:** Sequencial (não modular)

---

## 7. Requisitos da Bible

- **Glossário Técnico:** SIM, com termos E regras rígidas
- **Protocolos Práticos:** SIM (passos acionáveis, dosagens, checklists)
- **Estudos de Caso:** SIM (referências reais, com números e contexto)
- **Mitos do Mercado:** SIM (lista para desmistificar)
- **Fios Narrativos:** SIM (setups e payoffs, especialmente o tema central)

---

## 8. Regras de Polimento do Editor

- **Conversational Pacing:** Texto lido com facilidade, sem frases longas que cansam
- **Show Don't Tell (40%):** Usar exemplos de "campo de batalha" e histórias reais
- **Ancoragem Concreta:** Evitar abstrações; cada estratégia com ferramenta ou ação real
- **Terminologia Unificada:** Garantir consistência de termos (ex: "Impulsão" não "Ads")
- **PROIBIDO:** promessas exageradas, números inventados, casos fictícios, "garanta sua vaga", CTA de venda

---

## 9. Validações Extras

- **Exige Editor:** SIM
- **Exige Validação MARCH:** SIM (fatos do corpus)
- **Exige Validação de Continuidade:** SIM
- **Exige Validação de Fronteira:** SIM

---

## 10. O que Este Gênero NÃO É

- **NÃO é ficção.** Não tem personagens inventados, arcos narrativos fictícios, "ferida nuclear", "mentira que acredita", diálogos dramáticos.
- **NÃO é autoajuda motivacional.** Não tem "você consegue", "acredite no seu potencial", "o segredo é". É método aplicado.
- **NÃO é material de marketing.** Não tem CTA de venda, preço de outros cursos, "última chance".
- **NÃO é transcrição literal.** A transcrição é BASE, não OUTPUT. Reescrita com ritmo e tom próprios.
- **NÃO é enciclopédia.** Foca no método validado, não cobre todo o conhecimento.

---

## 11. Notas de Produção para a IA

- A voz é SEMPRE a do mentor, mesmo quando o mentor cita alunos ou terceiros (em 3ª pessoa, como fatos)
- Cases reais são o coração do Show — sem cases, a cena perde força
- Termos técnicos são explicados na 1ª menção via analogia (Zappos, food truck, RPG, etc.)
- O método PROGRIDE — cada cena prepara a próxima, sem pular degraus
- Se o corpus tiver mistura de transcrições e material de marketing, use SÓ as transcrições
- O checklist no fim é concreto e executável HOJE (não "compreender o conceito")