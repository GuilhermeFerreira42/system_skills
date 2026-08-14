# GENERO: NAO_FICCAO_PRATICA

**Versão:** 1.0
**Base:** NAO_FICCAO
**Tipo:** PRATICA (Não-ficção voltada a mudança de comportamento do leitor)
**Arquétipo Global:** RISCO_RESGATE
**Apelido interno:** Modo "Urgente & Imersivo"

**Relação com o DNA global:** este gênero NÃO substitui `escritor/DNA_REVELACAO_RESPEITOSA.md`
— ele adiciona restrições específicas por cima dele. Onde as duas fontes
conversam, este arquivo aponta explicitamente qual regra do DNA está sendo
mantida e qual está sendo restringida para este gênero.

---

## 1. Identidade e Voz Narrativa

- **Pessoa (REGRA OBRIGATÓRIA):**
  - **Padrão:** 2ª pessoa ("você"), exclusiva. Nunca "a gente", "o indivíduo"
    ou voz impessoal como sujeito principal do argumento.
  - **Uso do "você" em 3 momentos por cena, no mínimo:** na descrição do
    erro/hábito atual do leitor, na consequência prática desse hábito, e na
    saída/ação.
  - **PROIBIDO:** trocar "você" por "a pessoa"/"o leitor" sem perda de
    sentido — se a troca não muda nada, a voz não está fazendo o trabalho.
- **Tom de Voz:** Direto, urgente, confrontador — mas honesto. Instala
  desconforto real, não medo inflado ou number fabricado.
- **Distância Narrativa:** Próxima, quase de diagnóstico — o autor fala como
  quem identificou o problema do leitor antes dele.
- **Vocabulário:** Acessível; termo técnico só entra com tradução imediata
  via metáfora doméstica (ver seção 3).
- **Ritmo:**
  - **Tipo:** Alternância de exposição de mecanismo + consequência + ação —
    não é ritmo contemplativo.
  - **Extensão típica de frase:** curtas a médias, priorizando clareza sobre
    cadência poética.

### Figuras de Retórica Obrigatórias

- **Interpelação Direta:** pergunta ou comando que confronta a inércia do
  leitor em tempo real, não uma reflexão distante ("Você vai fechar este
  livro achando que bebeu o suficiente hoje. Bebeu mesmo?").
- **Prolepse (antecipação da objeção):** antecipe a reação cética do leitor
  antes que ela se forme por completo, e responda a ela dentro do próprio
  parágrafo ("Você vai pensar que isso é exagero. Não é — e o próximo
  parágrafo mostra o porquê."). Use pelo menos uma vez por cena, no ponto em
  que a alegação for mais forte e mais fácil de duvidar.

---

## 2. POV (Point of View)

- **Padrão:** Autor invisível, dirigindo-se diretamente ao leitor em 2ª pessoa.
- **Quem fala:** O autor, como quem revela um mecanismo que o leitor vive mas não nomeia.
- **Quem ouve:** O leitor, tratado como responsável por agir, não como espectador.
- **Multi-POV:** false
- **PROIBIDO:** voz de mentor em 1ª pessoa (isso é `podbook_mentor`, não este gênero).

---

## 3. Estrutura de "Cena" (Unidade de Produção)

- **Extensão:** 800 a 1.500 palavras (mesma faixa genérica de não-ficção do
  piso de densidade em `escritor/SKILL_ESCRITOR_PIPELINE.md` — este gênero
  não altera o piso, só a forma como o espaço é usado).
- **Show mínimo:** 40%.
- **Beats obrigatórios:**
  1. **Gancho de paradoxo** — pergunta retórica que expõe uma contradição óbvia
     que o leitor nunca percebeu, seguida de um dado bruto que agrava o
     paradoxo. *(Constrói sobre a seção 7.1 do DNA — mesmo princípio de
     "pergunta, não constatação"; a diferença é a segunda frase, que aqui é
     obrigatoriamente um dado, não uma reflexão.)*
  2. **Metáfora doméstica como fio condutor** — ver seção 8 abaixo.
  3. **Hipotipose (Enargia) — o mecanismo em cena, não em explicação:**
     pelo menos uma vez por cena, o conceito abstrato precisa ser encenado
     com detalhe concreto e sensorial suficiente para criar imagem mental
     imediata — não descrito, **mostrado acontecendo**, como se a câmera
     estivesse ligada. Verbos de ação física, objeto concreto, sequência no
     tempo. **Teste:** se o leitor fechasse os olhos neste trecho, ele
     conseguiria "ver" a cena, ou só entenderia o conceito? Se só entende,
     falta hipotipose.
  4. **Abismo de consequência** — antes de qualquer solução, um parágrafo
     descrevendo o custo prático/físico de não agir. A solução deve chegar
     como resgate, não como upgrade.
  5. **Fechamento com ação mínima e mensurável** — ver seção 4 abaixo.

---

## 4. Formato do Final de Cada Cena (OBRIGATÓRIO)

```markdown
[PROSA DA CENA — exposição + metáfora + abismo de consequência]

---

[ÚLTIMO PARÁGRAFO — deve conter, nesta ordem:
 1. Um verbo no imperativo (faça, beba, anote, pare, caminhe...)
 2. Uma medida exata (número de vezes, quantidade, tempo)
 3. Um critério de sucesso visível/checável pelo próprio leitor]

---
```

**PROIBIDO no fechamento:**
- Frase de efeito puramente poética sem ação embutida (isso é o modo padrão
  do DNA — seção 7.4 — não este gênero).
- Pergunta retórica aberta como último parágrafo ("E você, o que vai fazer?").
- JSON de metadados ou campos técnicos visíveis.

---

## 5. Regras de Oralidade

- Frases priorizam clareza sobre ornamento; evitar subordinação em cascata.
- Parágrafos curtos o suficiente para sustentar o ritmo de exposição→consequência→ação.
- Travessão permitido (diferente do `podbook_mentor`) — este gênero não é transcrição de fala.

---

## 6. Estrutura Global (Arquitetura do Livro)

- **Número de capítulos:** Variável, conforme o tema.
- **Macro-estrutura:** Progressiva — cada capítulo aprofunda o "abismo de
  consequência" e amplia o repertório de ação do leitor.
- **Relação entre capítulos:** Sequencial.

---

## 7. Requisitos da Bible

- **Glossário Técnico:** SIM, com tradução obrigatória via metáfora doméstica.
- **Protocolos Práticos:** SIM — toda alegação prática precisa de uma ação
  correspondente com número e critério de sucesso.
- **Mitos a Desmistificar:** SIM — lista de crenças erradas que o capítulo
  desarma (categórica, não processual — ver seção 8).
- **Metáfora Central da Obra:** SIM, registrada explicitamente na Bible —
  precisa ser de domínio doméstico/mecânico/animal (ver seção 8), e é a
  mesma do início ao fim da obra.

---

## 8. Regras de Polimento do Editor

- **Metáfora Doméstica (Tradução Tangível):** a metáfora central deve vir de
  algo que o leitor manuseia ou vê quebrar no cotidiano (casa, carro,
  ferramenta, animal doméstico, construção). **Proibido** metáfora de domínio
  épico/cósmico (mar, universo, tempestade) como imagem central — isso
  pertence ao modo padrão do DNA, não a este gênero. Teste: se a metáfora não
  permite ao leitor fazer uma pergunta de diagnóstico prático sobre a própria
  vida, ela é poética demais para este modo.
- **Listas de Impacto (Esqueleto Contável):** listas são permitidas e
  encorajadas, com no máximo 5 itens, e **apenas para categorias fechadas**
  (tipos de erro, fases, propriedades) — **nunca para passos de tutorial**
  ("1. Abra, 2. Fecha, 3. Beba"). Essa distinção é o que separa lista útil de
  checklist burocrático; viola-la reintroduz o problema que a v3.1 já teve.
- **Abismo de Consequência:** presente e honesto — baseado em risco real do
  corpus, nunca em número inflado ou dramatização não sustentada pelos fatos.
- **Show Don't Tell (40%):** casos concretos, números com sujeito (ver DNA
  seção 7.3 — essa regra é compartilhada, não específica deste gênero).
- **Teste da Enargia:** em pelo menos um trecho por cena, o mecanismo
  explicado precisa estar encenado com concretude sensorial suficiente para
  formar imagem mental — se todo o texto da cena é conceitual/explicativo,
  devolver para reescrita com a instrução "encene, não explique".
- **Presença de Prolepse:** cena que nunca antecipa e responde a uma objeção
  do leitor perde o efeito de "diálogo mental" que sustenta a imersão deste
  gênero — verificar pelo menos uma ocorrência por cena.

---

## 9. Validações Extras

- **Exige Editor:** SIM
- **Exige Validação MARCH:** SIM (fatos do corpus — abismo de consequência
  não pode inflar dado real)
- **Exige Validação de Continuidade:** SIM (metáfora central, terminologia)
- **Exige Validação de Fronteira:** SIM

---

## 10. O que Este Gênero NÃO É

- **NÃO é o modo padrão do DNA ("Elegância Orgânica").** Não usa metáfora
  épica, não fecha cena em contemplação, não usa "a gente" como voz principal.
- **NÃO é `podbook_mentor`.** Não é voz de mentor em 1ª pessoa, não é
  transcrição de treinamento.
- **NÃO é `ficcao_literaria`.** Não tem personagens fictícios nem arco narrativo.
- **NÃO é checklist burocrático.** Listas são categóricas, nunca processuais;
  cena não termina em tutorial passo-a-passo.
- **NÃO é medo sem lastro.** O abismo de consequência é honesto, ancorado em
  fato validado — não é copy de venda com número inflado.
- **NÃO é explicação pura.** Se o conceito nunca é encenado com hipotipose —
  só definido e discutido — o gênero não foi cumprido, mesmo que todas as
  outras regras estejam certas.

---

## 11. Notas de Produção para a IA

- Escolha UMA metáfora mestra doméstica/mecânica/animal antes de escrever a
  Cena 1, registre na Bible, e repita-a no início, meio e fim da obra —
  mesma regra de persistência da seção 7.2 do DNA, só que restringindo o
  domínio da imagem.
- O gancho de abertura (seção 7.1 do DNA) ganha aqui um segundo passo
  obrigatório: a frase seguinte à pergunta precisa trazer um dado bruto que
  agrava o paradoxo, não uma reflexão.
- Antes de qualquer solução, pague o "abismo de consequência" — o leitor
  precisa sentir o custo da inércia antes de receber o alívio da ação.
- O fechamento de cena deste gênero **substitui** a seção 7.4 do DNA
  (fechamento que cristaliza em frase memorável) por fechamento que ordena
  uma ação mensurável. Os dois fechamentos são bons — são só gêneros diferentes.
- **Hipotipose não é opcional.** Ao escrever qualquer mecanismo (biológico,
  financeiro, físico), pare antes de explicá-lo em abstrato e pergunte: "como
  eu encenaria isso, com um verbo de ação física e um objeto concreto, como
  se estivesse acontecendo agora?". Escreva essa versão primeiro; a
  explicação conceitual, se ainda for necessária, vem depois e é mais curta.
- **Prolepse em pelo menos um ponto por cena:** identifique a alegação mais
  fácil de duvidar naquela cena e antecipe a objeção do leitor antes de
  respondê-la — isso sustenta a sensação de diálogo direto que este gênero
  busca.
- Se o corpus misturar tom poético e tom prático, priorize extrair o dado e o
  mecanismo; a metáfora, a hipotipose e o verbo de ação são construídos por
  você, não copiados do corpus.