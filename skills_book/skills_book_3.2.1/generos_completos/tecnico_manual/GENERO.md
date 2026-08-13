# GENERO: TECNICO_MANUAL

**Versão:** 1.0
**Base:** NAO_FICCAO
**Tipo:** MANUAL (How-to, documentação técnica, tutorial estruturado)
**Arquétipo Global:** PROBLEMA_SOLUCAO (ou REFERENCIA, conforme o tipo de manual)

---

## 1. Identidade e Voz Narrativa

- **Pessoa (REGRA OBRIGATÓRIA):**
  - **Padrão:** 2ª pessoa ("você") ou 3ª autoral ("o autor", "nós")
  - **2ª pessoa ("você")** quando o manual é tutorial: "Abra o terminal. Agora digite..."
  - **3ª autoral ("nós")** quando o manual é referência: "Este capítulo cobre..."
  - **PROIBIDO:** 1ª pessoa do autor contando história pessoal (exceto em boxes de aviso), mistura sem critério de pessoa
  - **PROPORÇÃO ESPERADA:** ~80% 2ª pessoa, ~20% 3ª autoral
- **Tom de Voz:** Objetivo, didático, direto, preciso
- **Distância Narrativa:** Instrutiva (como um professor paciente explicando o procedimento)
- **Vocabulário:**
  - **Nível:** Técnico (assume conhecimento básico do domínio)
  - **Termos técnicos:** Introduzir com definição breve na 1ª menção, depois usar sem explicação
  - **Código/Comandos:** SEMPRE em bloco de código formatado
- **Ritmo:**
  - **Tipo:** Linear, procedural (passo a passo)
  - **Extensão típica de frase:** Média (15-25 palavras), sem rodeios
  - **Extensão típica de parágrafo:** Curto (2-4 frases), focando em uma ideia

---

## 2. POV (Point of View)

- **Padrão:** 2ª pessoa (você) ou 3ª autoral
- **Quem fala:** O autor/instrutor (impessoal, técnico)
- **Quem ouve:** O leitor (desenvolvedor, profissional, estudante) que precisa executar o procedimento

---

## 3. Estrutura de "Cena" (Unidade de Produção)

- **Extensão:** 500 a 2.000 palavras por cena
- **Mínimo:** 500 palavras
- **Máximo:** 2.000 palavras
- **Estrutura interna (típica de uma cena/tutorial):**
  - **Título da cena** (reflete o que o leitor vai aprender/fazer)
  - **Contexto breve** (1 parágrafo: por que esse assunto importa)
  - **Conceito principal** (explicação técnica)
  - **Exemplo de código/comando** (bloco formatado)
  - **Explicação do exemplo** (linha por linha, se relevante)
  - **Variação ou caso de borda** (opcional)
  - **Erro comum** (opcional)
- **Beats obrigatórios (no MÍNIMO 3 dos 5 abaixo):**
  1. **Conceito claro** (o que é, para que serve)
  2. **Sintaxe ou exemplo** (código, comando, fórmula)
  3. **Explicação aplicada** (como usar no contexto real)
  4. **Erro comum ou pegadinha** (o que evitar)
  5. **Checklist ou prática** (o que fazer agora)
- **Show mínimo:** 30% (exemplos de código, output real, diagramas)

---

## 4. Formato do Final de Cada Cena (OBRIGATÓRIO)

```markdown
# Capítulo X — [Nome do Capítulo]

[PROSA TÉCNICA: explicações, exemplos, código, diagramas]

---

## Resumo

[2-4 frases em 2ª ou 3ª autoral, recapitulando o que foi ensinado. Tom: "neste capítulo, você aprendeu X, Y, Z. Agora você pode fazer A."]

---

## Checklist

Antes de seguir para o próximo capítulo, confirme que você:

- [ ] [Pré-requisito verificado — ex: "Python 3.10+ instalado"]
- [ ] [Conceito compreendido — ex: "Entendi o que é uma função"]
- [ ] [Prática feita — ex: "Escrevi minha primeira função e ela rodou sem erro"]
- [ ] [Próximo passo claro — ex: "Sei onde buscar documentação oficial"]

---
```

**PROIBIDO no fim:**
- Histórias pessoais do autor
- "Espero que você tenha gostado" (tom motivacional)
- CTAs de venda
- Material de marketing

---

## 5. Regras de Oralidade

**N/A para Técnico Manual.** A prosa técnica NÃO é oral. É precisa e referencial. Frases longas são permitidas em explicações conceituais. Tom conversacional é inadequado.

---

## 6. Estrutura Global (Arquitetura do Livro)

- **Número de capítulos:** Variável (10-30, conforme escopo)
- **Macro-estrutura:** Progressiva, do simples ao complexo, do conceitual ao prático
- **Relação entre capítulos:** Sequencial com pré-requisitos explícitos

---

## 7. Requisitos da Bible

- **Glossário Técnico:** SIM, com termos E regras rígidas (definições canônicas)
- **Protocolos Práticos:** SIM (passos acionáveis, comandos exatos, exemplos de código)
- **Estudos de Caso:** N/A (manual não tem cases de aluno; pode ter casos de uso)
- **Mitos:** N/A (manual não desmitifica; pode ter "erros comuns")
- **Fios Narrativos:** N/A (manual não tem arcos; pode ter dependências entre capítulos)

---

## 8. Regras de Polimento do Editor

- **Precisão:** Todo comando, código ou sintaxe deve estar correto
- **Clareza:** Explicação acessível para o nível do público
- **Progressão:** Cada capítulo assume o anterior como pré-requisito
- **Exemplos funcionais:** Todo bloco de código deve rodar (não pseudo-código quebrado)
- **Terminologia Unificada:** Mesmos termos sempre (não "variável" e "atributo" para a mesma coisa)
- **PROIBIDO:** Adicionar histórias pessoais, promessas exageradas, material de marketing

---

## 9. Validações Extras

- **Exige Editor:** SIM
- **Exige Validação MARCH:** SIM (fatos técnicos devem ser verificáveis)
- **Exige Validação de Continuidade:** SIM (progressão lógica, pré-requisitos)
- **Exige Validação de Fronteira:** SIM

---

## 10. O que Este Gênero NÃO É

- **NÃO é ficção.** Sem personagens, sem arcos, sem narrativa.
- **NÃO é autoajuda.** Sem lição de vida, sem "você consegue".
- **NÃO é material de marketing.** Sem CTA, sem "compre o curso avançado".
- **NÃO é blog post.** É manual estruturado, com profundidade, sequencial.
- **NÃO é referência rápida (cheat sheet).** É tutorial que se lê do começo ao fim.

---

## 11. Notas de Produção para a IA

- A voz é SEMPRE impessoal. O instrutor não aparece como personagem.
- Código é SEMPRE executável. Pseudo-código só se claramente marcado como tal.
- Cada capítulo constrói sobre o anterior. Não há "saltos".
- Termos técnicos são introduzidos UMA VEZ, depois usados sem explicação repetida.
- Quando uma versão específica de software/biblioteca é importante, cite a versão explicitamente.
- Referências externas (documentação oficial, papers) são bem-vindas e incentivadas.
- Se o manual cobrir uma tecnologia que muda rápido (ex: framework JS), mencione a data de referência.
