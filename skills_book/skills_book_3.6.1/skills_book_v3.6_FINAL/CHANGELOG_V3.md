# CHANGELOG — Skill 3

## v3.4.0 — Fiação de Gênero + Correção de Sobrecodificação no Modo Prático (2026-08-16)

### Motivação
Diagnóstico externo (3 análises comparando produção real da v3.3.0 contra o
texto de referência "ótimo") revelou dois problemas independentes:

1. **Fiação quebrada (confirmado por inspeção direta dos arquivos):**
   `generos_completos/*/GENERO.md` nunca era lido por padrão — o boot do
   Orquestrador o tratava como "referência opcional", o `CONFIG.md` dizia
   explicitamente "não é necessário escolher um pacote de gênero pesado", e
   `PERGUNTAS_NIVELAMENTO.md` seguia travado na v3.2, sem nenhuma pergunta
   que levasse a um gênero calibrado. Todo teste anterior que usou
   `nao_ficcao_pratica` só funcionou porque o prompt de boot forçava
   manualmente a leitura do gênero — sem esse override, o pipeline sempre
   convergia para o DNA padrão (Elegância Orgânica).
2. **Sobrecodificação recorrente no gênero prático:** exigir todos os
   instrumentos (gancho + metáfora + hipotipose + abismo + ação) em toda
   cena, e "2ª pessoa exclusiva" sem exceção, produzia arquitetura repetida
   e apagava a alternância de pessoa natural do corpus oral — o mesmo erro
   de sobrecodificação que motivou a criação da v3.2, só que disfarçado de
   regra "urgente" em vez de "erudita".

### Mudanças
- **`orquestrador/BOOT_ORQUESTRADOR_PIPELINE.md`:** leitura de `GENERO.md`
  agora é obrigatória quando `execucao/CONFIG.md` indicar um gênero
  diferente de "padrão".
- **`CONFIG.md` (raiz) e `execucao/CONFIG.md`:** novo campo "Gênero
  aplicado"; removida a frase que desencorajava escolher gênero.
- **`nivelamento_editorial/PERGUNTAS_NIVELAMENTO.md`:** nova "Pergunta 0"
  (registro padrão vs. gênero pesado calibrado), cabeçalho atualizado para
  v3.3.0.
- **`generos_completos/nao_ficcao_pratica/GENERO.md`:**
  - Beats obrigatórios por cena viraram "instrumentos disponíveis" — a
    função dramática da cena decide quais usar, não uma lista fixa.
  - Pessoa gramatical: "2ª pessoa exclusiva" virou "2ª pessoa dominante",
    com alternância controlada para 1ª (autoridade/experiência) e 3ª
    (personagem científico/estudo) pessoa.
  - Fechamento com ação mensurável restrito à última cena do
    capítulo/obra (já corrigido antes, mas ausente nesta cópia — sincronizado).
- **Ajustes Finos de Precisão (Autópsia Editorial):**
  - **Rigor Notacional e Científico Exato (LaTeX):** liberada e encorajada a notação em LaTeX ($\text{H}_2\text{O}$, $\text{OH}^-$, $\text{H}^+$, $\text{NaCl}$) e dados percentuais brutos no `DNA_REVELACAO_RESPEITOSA.md`, `GENERO.md` e `RUBRICA_QUALITATIVA_V3.md`, garantindo autoridade científica irrefutável e impedindo que o rigor seja punido como "erudição".
  - **Preservação de Unidade Narrativa (Arco Unificado por Cena):** atualizado `SKILL_ATOMIZADOR_PIPELINE.md`, `GENERO.md` e `RUBRICA_QUALITATIVA_V3.md` (critério 3.8) para proibir a fragmentação de histórias reais/experimentos em metashows bibliográficos frios, forçando cada cena a sustentar um arco narrativo coeso.

---

## v3.3.0 — Gênero Não-Ficção Prática (2026-08-13)

### Motivação
Comparação entre duas produções do mesmo corpus mostrou que o modo padrão do
DNA ("Elegância Orgânica") produz um registro contemplativo/literário, que
não é o único registro válido de não-ficção. Um segundo texto de referência,
mais antigo, usava um registro diferente — direto, urgente, focado em ação —
e conseguia um nível de imersão que o autor considerou superior para esse
propósito. Em vez de misturar os dois registros dentro do mesmo DNA global
(o que forçaria todo livro futuro, inclusive ficção e memórias, a herdar
convenções de autoajuda), foi criado um gênero novo, seguindo o mesmo padrão
dos já existentes (`ficcao_literaria`, `podbook_mentor`, `tecnico_manual`).

### Mudança
- **`generos_completos/nao_ficcao_pratica/GENERO.md`** (novo arquivo, 11
  seções + figuras de retórica): gênero opcional para não-ficção voltada a
  mudança de comportamento do leitor. Regras principais:
  - Voz em 2ª pessoa exclusiva ("você"), nunca "a gente"/impessoal.
  - Beats obrigatórios por cena: gancho de paradoxo + dado bruto, metáfora
    doméstica/mecânica (nunca épica), **hipotipose/enargia** (mecanismo
    encenado com concretude sensorial, não só explicado), abismo de
    consequência honesto, fechamento com ação mensurável.
  - Figuras de retórica nomeadas e obrigatórias: interpelação direta,
    prolepse (antecipação da objeção do leitor).
  - Listas permitidas até 5 itens, só categóricas — nunca processuais
    (evita reintroduzir o problema de sobrecodificação da v3.1).
  - Fechamento de cena **substitui** a seção 7.4 do DNA (cristalização
    poética) por ordem de ação com verbo imperativo + número + critério de
    sucesso — os dois fechamentos continuam válidos, cada um no seu gênero.

Este gênero é **opcional e aditivo**: não altera `DNA_REVELACAO_RESPEITOSA.md`
nem o comportamento padrão de nenhum outro gênero. Um livro só usa este modo
se explicitamente selecionado.

---

## v3.2.2 — Ciclo de Abertura e Fechamento (2026-08-12)

### Diagnóstico
Mesmo com o piso de densidade (v3.2.1) garantindo que as cenas tivessem
desenvolvimento suficiente, uma análise comparativa entre um texto de referência
e a produção da v3.2 mostrou uma segunda lacuna, independente da primeira: cenas
tecnicamente completas ainda soavam "relatório técnico" em vez de "descoberta
compartilhada". A causa era estrutural, não de tom — faltavam quatro técnicas
concretas de arquitetura de obra que o DNA já pedia em espírito, mas não
detalhava em prática: gancho de abertura como pergunta, metáfora central que
persiste do início ao fim, dado estatístico vestido como cena, e fechamento de
cena que cristaliza em vez de recapitular.

### Mudanças
- **`escritor/DNA_REVELACAO_RESPEITOSA.md`:** nova seção 7, "Estrutura de
  Abertura e Fechamento: O Ciclo que Prende o Leitor" (4 subseções). Seções
  seguintes renumeradas (Exemplos → 8, O que Evitar → 9); dois novos sinais de
  alerta adicionados a "O que Evitar".
- **`revisor_cego_editorial/RUBRICA_QUALITATIVA_V3.md`:** critério 3.7, "Ciclo
  de Abertura e Fechamento" — opera no nível da obra, não só da cena.

Nenhum exemplo do corpus de nenhuma obra específica entrou nesses arquivos —
seguem 100% genéricos.

---

## v3.2.1 — Piso de Densidade (2026-08-11)

### Diagnóstico
A remoção total de métricas na v3.2 corrigiu o engessamento da v3.1, mas criou uma
assimetria: nada impedia o oposto — uma cena terminar subdesenvolvida por ter
cortado um beat pela metade. Medição real de produção mostrou cenas variando de
336 a 1003 palavras dentro da mesma obra, sem que a história justificasse a
diferença. A cena mais densa foi a única que recebeu calibração manual iterativa
contra uma referência externa; as demais não tiveram nenhuma rede de segurança.

### Mudanças
- **`escritor/SKILL_ESCRITOR_PIPELINE.md`:** piso de densidade genérico por tipo
  de obra (tabela sem nomes/domínios específicos) + gatilhos de reprovação.
- **`execucao/CONFIG.md`:** piso mínimo de palavras por cena, específico desta obra.
- **`orquestrador/SKILL_ORQUESTRADOR_PIPELINE.md`:** checkpoint de densidade no
  loop, antes dos validadores — cena abaixo do piso volta para o Escritor como
  falha de desenvolvimento, não como crítica de estilo.
- **`revisor_cego_editorial/RUBRICA_QUALITATIVA_V3.md`:** critério 3.6, "Cena
  Subdesenvolvida vs. Cena Genuinamente Concisa" — instintivo, não numérico.
- **`LEIA-ME-PRIMEIRO.md`:** nota distinguindo "métrica de ritmo" (forma da
  frase, permanece proibida) de "piso de densidade" (completude do beat, agora
  permitido).

Nenhuma mudança tocou `DNA_REVELACAO_RESPEITOSA.md` — a voz "Elegância Orgânica"
continua intocada; o ajuste é só a rede de segurança embaixo dela.

---

## v3.2 — Elegância Orgânica (2026)

### Diagnóstico e Motivação
O teste de produção da versão 3.1 demonstrou sobrecodificação qualitativa: diretrizes de sofisticação tornaram-se travas rígidas de parágrafo, fazendo com que o Escritor performasse erudição em vez de descobrir o raciocínio junto com o leitor. A versão 3.2 recalibra o sistema para unir a precisão vocabular da v3.1 com a cumplicidade e o ritmo orgânico da v3.0.

### Principais Mudanças
- **DNA da Revelação Respeitosa (`escritor/DNA_REVELACAO_RESPEITOSA.md`):**
  - Transição de regras métricas para **Princípios de Instinto**.
  - Centralização no princípio cardeal: *"Nunca explique — mostre o objeto em tamanho natural"*, permitindo que a tese emerja como dedução espontânea do leitor.
  - Convicção ativa com **Autoridade Acessível**: autoridade que vem da clareza e do vocabulário exato, eliminando o tom de relator e a afetação acadêmica.
- **Rubrica Qualitativa (`revisor_cego_editorial/RUBRICA_QUALITATIVA_V3.md`):**
  - Implementação do **Filtro de Performance (Verdadeiro vs. Falso)**.
  - Suavização da Rejeição de Mediocridade: proibição expressa de punir a **Simplicidade Lúcida** e a concisão.
- **Perguntas de Nivelamento (`nivelamento_editorial/PERGUNTAS_NIVELAMENTO.md`):**
  - Substituição da ênfase em "erudição acadêmica" por **"Cumplicidade Natural e Autoridade Acessível"** em todas as notas de calibração.
- **Generalização e Segurança:** Todos os exemplos permanecem estritamente multidomínio (Tecnologia, Finanças, Filosofia, Organizações) e alinhados ao padrão GitHub Ready. A infraestrutura técnica de segurança (Vigia, Checksums, Controle da Obra) permanece como palco invisível intocado.

---

## v3.0 — GitHub Ready (2026)

### O que mudou

Esta versão refatora a Skill 3 para ser um framework genérico, livre de referências a autores, obras ou domínios específicos. O objetivo é que qualquer pessoa possa usar a Skill 3 para produzir livros em qualquer tema, com qualquer corpus, sem preocupações de direitos autorais.

### Mudanças na arquitetura

- **Generalização completa:** Todas as referências a autores específicos, obras particulares ou domínios restritos foram removidas. Os documentos descrevem comportamentos e intenções, não nomes ou nichos fixos.
- **Unificação na pasta `skills_book_3`:** Todos os documentos de "Intencionalidade e Alma" (DNA do Escritor, Rubrica do Revisor Cego, Guia de Calibração de Empatia, Perguntas de Nivelamento) agora estão dentro das subpastas correspondentes, tornando a Skill autossuficiente.
- **Templates limpos em `execucao/`:** A pasta `execucao/` contém apenas esqueletos vazios com campos `[PREENCHER]`.
- **Reforço da Lei 6 (Zero Marketing):** A regra de que o livro não é página de venda foi reforçada em múltiplos documentos, protegendo a reputação do framework no GitHub.

---

**Skill 3 v3.2 — Elegância Orgânica — Framework genérico de escrita com intencionalidade.**