# Skill 3 — Framework de Escrita de Alta Qualidade com Intencionalidade

**Status:** Versão v3.1 — Alta Escrita (High Writing)

---

## O que é a Skill 3

A Skill 3 é um framework de produção de livros que separa rigorosamente **criação** de **auditoria**. Ela foi desenhada para que a tecnologia (Vigia, Checksum, Controle da Obra) seja o palco invisível que protege a liberdade criativa do Escritor.

O objetivo da Skill 3 não é controlar como o Escritor escreve. É garantir que, quando ele escrever, o resultado seja rastreável, coerente e autêntico — sem que o Escritor precise calcular métricas ou se preocupar com checksums.

A Skill 3 está agora na sua versão de **Alta Escrita (High Writing)**, desenhada para produzir textos com:
- **Sofisticação acadêmica** — o leitor sente que existe domínio do tema sem que o texto se torne árido ou excessivamente técnico.
- **Elegância literária** — variação de tessitura, ritmo intencional, frases que ecoam.
- **Profundidade reveladora** — o Escritor não relata, ele descobre e convida o leitor a descobrir junto.
- **100% genérica** — aplicável a qualquer tema, qualquer idioma, qualquer corpus, sem menção a autores, obras ou domínios específicos nos arquivos core.

---

## Princípios Fundamentais

### 1. Criação × Auditoria

A criação e a auditoria são modos diferentes:

- **Criação:** O Escritor recebe intenção, contexto e insumos, e escreve com liberdade.
- **Auditoria:** Validadores (MARCH, Continuidade, Revisor Cego, Vigia) verificam fatos, coerência, clareza e integridade física — sem ler a prosa quando não precisam.

### 2. O Escritor como Intelectual Provocador

O Escritor não é um relator do corpus. Ele é um descobridor. Sua função é fazer o leitor descobrir algo que está nos materiais, não repetir o que está nos materiais. Ele conduz o leitor por conceitos complexos sem subestimá-lo, usando clareza precisa e convicção ativa.

### 3. Variação de Tessitura

Um texto competente informa. Um texto excelente oscila. Ele alterna entre parágrafos densos, analíticos, que carregam o peso do raciocínio — e frases curtas, precisas, que cortam e ficam. Isso não é cálculo. É respiro.

### 4. Convicção Ativa

O Escritor não se esconde atrás de "segundo a literatura" quando tem convicção do que está dizendo. Ele assume a informação como sua, porque a encontrou nos materiais e está convencido dela. Ele usa a intenção de revelar, não a intenção de relatar.

### 5. Intencionalidade antes de execução

Antes da primeira palavra ser escrita, o boot da Skill 3 pergunta: como você quer que o leitor se sinta? Essas respostas configuram a voz do mentor, o ritmo das cenas, a forma como as analogias são usadas — tudo isso sem transformar preferências em métricas ocultas.

---

## Estrutura da Skill 3

```
skills_book_3/
├── README.md                          # Este arquivo
├── CHANGELOG_V3.md                    # Histórico de versões
├── CONFIG.md                          # Configuração global do framework
├── LEIA-ME-PRIMEIRO.md                # Instruções de uso da Skill
├── REGRAS_GREENFORGE_PIPELINE.md     # As 6 leis duras
├── FLUXO_COMPLETO_PIPELINE.md        # Visão geral do fluxo
├── GUIA_DE_USO.md                     # Guia de uso geral
├── nivelamento_editorial/            # Perguntas e calibração de empatia
│   ├── PERGUNTAS_NIVELAMENTO.md      # Perguntas de boot (foco em intenção emocional)
│   └── GUIA_CALIBRACAO_EMPATIA.md    # Exemplos contrastantes (verdadeiro vs. falso)
├── escritor/                          # DNA da Revelação Respeitosa
│   ├── BOOT_ESCRITOR_PIPELINE.md
│   ├── SKILL_ESCRITOR_PIPELINE.md
│   └── DNA_REVELACAO_RESPEITOSA.md   # Manual do Escritor (voz, estilo, convicção ativa)
├── revisor_cego_editorial/           # Rubrica de qualidade
│   ├── BOOT_REVISOR_CEGO_EDITORIAL.md
│   ├── SKILL_REVISOR_CEGO_EDITORIAL.md
│   └── RUBRICA_QUALITATIVA_V3.md     # Critérios + Rejeição de Mediocridade
├── orquestrador/                     # Lógica do Orquestrador
│   ├── BOOT_ORQUESTRADOR_PIPELINE.md
│   └── SKILL_ORQUESTRADOR_PIPELINE.md
├── editor/                           # Pipeline do Editor
│   ├── BOOT_EDITOR_PIPELINE.md
│   └── SKILL_EDITOR_PIPELINE.md
├── validador_march/                  # Pipeline MARCH
│   ├── BOOT_VALIDADOR_MARCH_PIPELINE.md
│   └── SKILL_VALIDADOR_MARCH_PIPELINE.md
├── validador_continuidade/           # Pipeline de Continuidade
│   ├── BOOT_VALIDADOR_CONTINUIDADE_PIPELINE.md
│   └── SKILL_VALIDADOR_CONTINUIDADE_PIPELINE.md
├── atomizador/                       # Pipeline de atomização
│   ├── BOOT_ATOMIZADOR_PIPELINE.md
│   └── SKILL_ATOMIZADOR_PIPELINE.md
├── consolidador/                     # Pipeline de consolidação
│   └── SKILL_CONSOLIDADOR_PIPELINE.md
├── controle_da_obra/                 # Template de Controle
│   ├── BOOT_CONTROLE_DA_OBRA.md
│   ├── SKILL_CONTROLE_DA_OBRA.md
│   ├── README.md
│   └── TEMPLATE_CONTROLE_DA_OBRA.md
├── estado/                           # Template de Estado
│   └── ESTADO_TEMPLATE_PIPELINE.md
├── bible/                            # Template de Bible
│   ├── BIBLE_TEMPLATE_PIPELINE.md
│   └── BIBLE_ESQUELETO_VAZIO.md
├── execucao/                         # Espaço do projeto específico (APENAS TEMPLATES)
│   ├── README.md
│   ├── CONFIG.md                      # Template de configuração
│   ├── bible/
│   │   ├── README.md
│   │   └── bible_da_obra.md           # Template vazio
│   ├── capitulos/
│   │   └── README.md
│   ├── controle/
│   │   └── README.md
│   ├── corpus/
│   │   └── README.md
│   └── estado/
│       └── README.md
├── generos_completos/                # Perfis de gênero completos (referenciais)
│   ├── ficcao_literaria/
│   ├── podbook_mentor/
│   └── tecnico_manual/
├── generos_template/                 # Template vazio de gênero
│   └── TEMPLATE_GENERO_VAZIO.md
└── utils/                            # Ferramentas de integridade
    ├── README.md
    ├── atomic.py
    ├── checksum.py
    ├── reconciliar_controle.py
    └── vigia_integridade.py
```

---

## Como usar na prática

### Iniciar um novo projeto

1. Crie uma pasta para o seu livro fora do repositório da Skill 3.
2. Dentro dessa pasta, crie a estrutura `execucao/` com os templates vazios.
3. Rode o boot da Skill 3, respondendo às perguntas de nivelamento.
4. O Orquestrador coordena a produção cena por cena.
5. Todo artefato aprovado recebe checksum e manifesto.

### O que NÃO fazer

- Não use a Skill 3 para gerar spam ou material de marketing (Lei 6).
- Não modifique artefatos aprovados sem registrar o drift.
- Não pule etapas de validação.
- Não transforme preferências em métricas ocultas.
- Não use nomes de autores, obras ou domínios específicos nos arquivos core da Skill.

### Segurança e Liberdade Criativa

A Skill 3 foi desenhada para que a tecnologia sirva à criatividade, não a substitua. O Vigia, o Checksum e o Controle da Obra são invisíveis para o Escritor. Eles garantem que, quando o Escritor escrever, ele saiba que o que ele escreveu é o que está no disco — e que ninguém o modificou sem registrar.

Isso libera o Escritor para se concentrar no que importa: descobrir algo fascinante e fazê-lo descobrir para o leitor.

---

## Os quatro pilares da Alta Escrita na Skill 3

### 1. DNA da Revelação Respeitosa

O Escritor é instruído a ser um **Intelectual Provocador** — alguém que convence com clareza precisa, assume a convicção com coragem, e desafia o óbvio sem subestimar o leitor. Ele usa a **Variação de Tessitura** para alternar entre densidade analítica e impacto de frase curta. Ele escreve com **Narrativa de Evidência**, tratando casos históricos e prêmios como "Assinaturas da Verdade" — com detalhes específicos, não generalizações.

### 2. Nivelamento Editorial com Intenção Emocional

As perguntas de boot não perguntam apenas o que o texto deve fazer. Elas perguntam como o leitor deve *sentir*. As opções de resposta descrevem a **voz Erudita e Fluida** — autoridade pela clareza, não pela imposição. Desafiar sem atacar. Convidar sem condescender. Voz que soa como companheiro de viagem, não como sábio no pico da montanha.

### 3. Calibração de Empatia por Exemplos Contrastantes

O Escritor é apresentado a exemplos de texto que soa **verdadeiro** (descobridor revelando com clareza e profundidade) e texto que soa **falso** (performer tentando parecer profundo). O objetivo não é copiar o ritmo, é capturar a intenção. Exemplos genéricos em múltiplos contextos (finanças, tecnologia, educação, produtos, filosofia, desenvolvimento humano) mostram que o princípio é transversal.

### 4. Rubrica que Exige Excelência, Não Conformidade

O Revisor Cego não julga por métrica. Ele julga por sensação de autenticidade. Além dos gatilhos de rejeição tradicionais (tom conspiratório, voz imperativa dominante, fechos repetitivos), agora ele também rejeita:
- **Texto excessivamente escolar/simplista** — palavras grandes sem clareza, densidade só para parecer denso.
- **Texto excessivamente simplista** — explicações desnecessárias, linguagem condescendente, tratamento do leitor como quem precisa de simplificação excessiva.

O texto que a Skill 3 quer é a voz do Intelectual Provocador: erudito e acessível ao mesmo tempo.

---

## Direitos Autorais e Uso

Este framework é genérico e pode ser usado para qualquer tipo de obra, em qualquer idioma, com qualquer tipo de corpus.

**Importante:** O usuário é responsável por garantir que tem direitos sobre o corpus que usar. A Skill 3 não valida direitos autorais do corpus. Ela apenas processa o que recebe.

**Uso comercial:** Este framework pode ser usado para produzir livros comerciais, desde que o usuário tenha os direitos sobre o corpus e o conteúdo gerado.

---

## Contribuindo

Sinta-se à vontade para contribuir com melhorias na lógica da Skill 3. Ao contribuir:

1. Mantenha a separação entre criação e auditoria.
2. Não adicione métricas estéticas que possam restringir o Escritor.
3. Teste as mudanças com projetos reais antes de submeter.
4. Documente claramente qualquer nova regra ou procedimento.
5. Mantenha os arquivos core 100% genéricos — sem menções a autores, obras ou domínios específicos.

---

## Licença

Este framework é fornecido como está, sem garantias de qualquer kind. O usuário é responsável pelo uso que fizer dele.

---

**Skill 3 — Onde a tecnologia é o palco invisível, e o Escritor é o bailarino de elite.**
