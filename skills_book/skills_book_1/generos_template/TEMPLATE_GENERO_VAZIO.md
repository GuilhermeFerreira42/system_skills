# TEMPLATE DE GÊNERO VAZIO (PIPELINE GENÉRICO v3)

**Versão:** 3.0
**Aplicação:** copie para `generos_completos/[nome_do_genero]/GENERO.md` e preencha TODAS as seções. A IA produtora lê este arquivo para configurar todo o pipeline.

**INSTRUÇÕES PARA O USUÁRIO:**

1. Leia cada seção abaixo
2. Preencha com valores concretos e específicos do seu gênero
3. Onde não souber, escreva "[definir]" e resolva depois
4. Seja específico. "Voz narrativa envolvente" é genérico e inútil. "Voz em 1ª pessoa do mentor, 2ª pessoa pontual em comandos, com frases de até 25 palavras e marcadores orais ('olha', 'tá', 'beleza')" é útil.

---

# GENERO: [NOME_DO_GENERO]

**Versão:** 1.0
**Base:** [Se for baseado em outro gênero, citar — ex: "Base: NAO_FICCAO"]
**Tipo:** [Tipo do gênero — ex: PODBOOK, FICCAO_LITERARIA, TECNICO_MANUAL, INFANTOJUVENIL, etc.]
**Arquétipo Global:** [PROBLEMA_SOLUCAO | JORNADA_HEROI | KISHOTENKETSU | GRANDE_IDEIA | OUTRO]

---

## 1. Identidade e Voz Narrativa

- **Pessoa (REGRA OBRIGATÓRIA):**
  - **Padrão:** [1ª pessoa | 2ª pessoa | 3ª pessoa limitada | 3ª pessoa onisciente | multi-POV]
  - **Quem fala:** [Descrever quem é o narrador, ex: "O mentor Bruno, contando sua experiência" | "Narrador onisciente, observador externo" | "Personagem X, em 1ª pessoa"]
  - **Quem ouve:** [Descrever quem é o público/leitor, ex: "Empreendedor iniciante querendo validar negócio" | "Jovem adulto buscando ficção de aventura" | "Desenvolvedor aprendendo nova tecnologia"]
  - **PROPORÇÃO ESPERADA:** [Se multi-POV, qual a proporção de cada um — ex: "60% personagem A, 40% personagem B"]
  - **PROIBIDO:** [Listar combinações proibidas — ex: "POV múltiplo na mesma cena" | "Trocar de narrador entre parágrafos"]

- **Tom de Voz:** [Lista de adjetivos — ex: "pragmático, transformador, pé no chão ('campo de batalha'), encorajador" | "poético, introspectivo, melancólico" | "objetivo, técnico, direto"]

- **Distância Narrativa:** [intima | próxima | media | ampla | cinematografica | mentor | instrutiva | personagem]

- **Vocabulário:**
  - **Nível:** [simples | medio | rico | tecnico | construido | acessivel | literario]
  - **Termos técnicos (1ª menção):** [explicar via analogia? citar? assumir conhecimento?]
  - **Dialeto/regionalismo:** [neutro | pt-BR | pt-PT | com regionalismos | sem regionalismos]

- **Ritmo:**
  - **Tipo:** [lento | variado | rapido | modular | ondulatorio | linear | dramatico]
  - **Extensão típica de frase:** [em palavras — ex: "máx 25 palavras para oralidade" | "sem limite, prosa literária"]
  - **Extensão típica de parágrafo:** [em frases — ex: "3-5 frases, parágrafos respiratórios" | "sem limite, fluxo narrativo"]

---

## 2. POV (Point of View)

- **Padrão:** [Como definido acima]
- **Multi-POV:** [sim | nao]
- **Regras de troca (se multi-POV):** [ex: "Troca apenas na quebra de cena/capítulo, nunca no meio de uma cena" | "Cenas alternadas, cada uma com um POV"]
- **PROIBIDO:** [head-hopping, mudança de POV sem aviso, etc.]

---

## 3. Estrutura de "Cena" (Unidade de Produção)

- **Extensão:** [Mínimo e máximo em palavras — ex: "1.000-4.000" | "500-2.000" | "sem limite formal"]
- **Estrutura interna (se aplicável):**
  - **Abertura:** [Obrigatória? Como? — ex: "Comando OU provocação" | "Cena de ação" | "Diálogo" | "Sem requisito"]
  - **Desenvolvimento:** [Como? — ex: "Teoria → Analogia → Caso real" | "Exposição → Conflito → Clímax" | "Problema → Análise → Solução" | "Sem requisito"]
  - **Fecho:** [Obrigatório? Como? — ex: "Gancho para próxima cena" | "Resolução do conflito da cena" | "Sem requisito"]

- **Beats obrigatórios (mínimo N dos listados):**
  1. [Beat 1 — ex: "Abertura forte (comando/provocação)"]
  2. [Beat 2 — ex: "Exposição de mecanismo"]
  3. [Beat 3 — ex: "Analogia de impacto"]
  4. [Beat 4 — ex: "Caso real ou exemplo concreto"]
  5. [Beat 5 — ex: "Checklist prático no fim"]
  6. [Beat 6 — ex: "Fecho propulsor (gancho para próxima cena)"]

- **Show mínimo:** [Porcentagem — ex: "40% (cases, exemplos, números, histórias)" | "70% (cenas vividas, sensações, micro-ações)" | "20% (exemplos de código)"]

---

## 4. Formato do Final de Cada Cena (OBRIGATÓRIO se aplicável)

**Estrutura fixa que toda cena deve ter no fim:**

```markdown
[PROSA DA CENA]

---

## Resumo da cena

[3-5 frases em [pessoa do narrador], recapitulando o que foi apresentado]

---

## Seu checklist desta cena

Antes de ir para a próxima cena, você precisa ter feito ou decidido:

- [ ] [Ação 1]
- [ ] [Ação 2]
- [ ] [Ação 3]
- [ ] [Decisão interna]

---

**Próxima cena:** [título + gancho de 1 frase]
```

**OU, se o gênero NÃO usa este formato:**

```markdown
[PROSA DA CENA]
```

[Descrever qual é o formato alternativo, ex: "Para Ficção: a cena termina naturalmente, sem resumo ou checklist. O fecho é emocional/narrativo, não prático."]

**PROIBIDO no fim de qualquer cena:**
- [Listar o que NÃO pode aparecer — ex: "JSON" | "Metadados técnicos" | "Clichês de coach" | "Material de marketing"]

---

## 5. Regras de Oralidade e Estilo

**Aplicam-se APENAS se o gênero é para áudio/lido em voz alta. Para Ficção, preencher com "N/A".**

- **Frases curtas:** [máximo em palavras, ex: "25 palavras" | "N/A"]
- **Marcadores de oralidade:** [lista — ex: "'olha', 'tá', 'sabe', 'então', 'beleza'" | "N/A"]
- **Parágrafos respiratórios:** [ex: "3-5 frases por parágrafo" | "N/A"]
- **Travessão formal:** [proibido? permitido? em que contexto?]
- **Enumeração explicativa:** [proibido? permitido?]
- **PROIBIDO iniciar parágrafo com:** [lista — ex: "'E aí, tudo bem?'" | "'Nesta aula veremos'" | "'Conforme vimos anteriormente'"]
- **PERMITIDO/ENCOURAJADO iniciar com:** [lista — ex: "Comando direto" | "Provocação" | "Imagem sensorial" | "Citação"]

---

## 6. Estrutura Global (Arquitetura do Livro)

**Como o livro se organiza em capítulos e macro-estrutura:**

- **Número de capítulos:** [estimativa]
- **Macro-estrutura:** [Descrever — ex: "3 atos (fundamentação, operação, escala)" | "12 módulos sequenciais sem volta" | "Parte I (introdução), Parte II (avançado), Parte III (referência)"]
- **Relação entre capítulos:** [sequencial | modular (pode ler em qualquer ordem) | progressivo (cada um pressupõe o anterior)]

---

## 7. Requisitos da Bible (Fonte da Verdade)

**A Bible DEVE conter:**

- **Glossário Técnico:** [sim, com termos | sim, com termos E regras rígidas | não, ficção não tem]
- **Protocolos Práticos:** [sim, se há ações concretas | não, ficção não tem]
- **Estudos de Caso / Characters:** [sim, com casos reais | sim, com personagens e arcos | não]
- **Mitos do Mercado / Equívocos Comuns:** [sim, se for não-ficção com viés didático | não]
- **Fios Narrativos:** [sim, com setups e payoffs | sim, com arcos de personagem | não]

---

## 8. Regras de Polimento do Editor

- **[Regra 1 — específica do gênero, ex: "Show Don't Tell (40%)"]
- **[Regra 2 — ex: "Ancoragem concreta"]
- **[Regra 3 — ex: "Terminologia unificada"]
- **PROIBIDO:** [ex: "Adicionar promessas exageradas" | "Inventar casos fictícios" | "Quebrar POV"]

---

## 9. Validações Extras

- **Exige Editor:** [sim | nao]
- **Exige Validação MARCH:** [sim, se há corpus factual | nao, se for ficção pura]
- **Exige Validação de Continuidade:** [sim, sempre — para qualquer narrativa coesa]
- **Exige Validação de Fronteira:** [sim, no Consolidador — sempre]

---

## 10. O que Este Gênero NÃO É

Para evitar confusão:

- **NÃO é:** [ex: "Ficção científica — não tem worldbuilding futurista" | "Autoajuda motivacional — não tem clichês de coach"]
- **NÃO é:** [...]
- **NÃO é:** [...]

---

## 11. Notas de Produção para a IA

[Espaço livre para observações finais. Ex: "Este gênero tem alta variação de extensão entre cenas — algumas podem ser 500 palavras, outras 5.000. O Orquestrador deve respeitar o que o plano pede." OU "Este gênero é sensível à ordem dos capítulos. NÃO permita reorder."]

---

## Checklist de Preenchimento

Antes de salvar `GENERO.md`, confirme:

- [ ] Todas as seções 1-10 estão preenchidas
- [ ] Nenhuma seção tem "[definir]" ou "[a preencher]"
- [ ] Voz, POV, ritmo estão específicos (não genéricos)
- [ ] Formato do fim de cada cena está claro
- [ ] Bíblia exemplo (se houver) bate com este gênero
- [ ] 1-2 capítulos de calibração foram produzidos para validar

Se marcou todos, salve em `generos_completos/[nome_do_genero]/GENERO.md` e o gênero está pronto pra uso.
