# tecnico_manual — Perfil de Gênero Completo

**Versão:** 1.0
**Aplicação:** este é o perfil de gênero para manuais técnicos, tutoriais, documentação, livros didáticos de programação, etc.

---

## Quando usar este gênero

Use este perfil quando:
- O livro é um manual didático, não ficção, não marketing
- O conteúdo é procedural (passo a passo) ou conceitual (explica tecnologia/método)
- O público é profissional, estudante, ou entusiasta que quer aprender a fazer algo
- A voz é impessoal, técnica, objetiva
- Há pré-requisitos e dependências entre capítulos

**Exemplos de livros que se encaixam:**
- "Python para Iniciantes" (exemplo deste perfil)
- "Docker na Prática"
- "Excel Avançado"
- "Manual de Marketing Digital"
- "Contabilidade para Empreendedores"
- "Git e GitHub Essencial"
- "Design Thinking Aplicado"

---

## O que tem aqui

- `GENERO.md` — Arquivo principal do gênero (preenchido)
- `BIBLE_EXEMPLO.md` — Bible exemplo com "Python para Iniciantes"
- `capitulos_calibracao/capitulo_01/` — Cap 1 exemplo, 2 cenas (calibração de tom técnico)

---

## Como usar

1. Copie `GENERO.md` para `execucao/GENERO.md` do seu projeto
2. Use `BIBLE_EXEMPLO.md` como referência de estrutura para criar a Bible do SEU livro
3. Olhe `capitulos_calibracao/capitulo_01/` para calibrar tom, formato e nível de detalhe técnico
4. Configure o `CONFIG.md` com título, corpus (documentação, tutoriais, etc.), foco
5. Passe para a IA produtora

---

## Particularidades deste gênero

**Atomizador:** extrai afirmações técnicas (versões de software, sintaxe, APIs) para validação.

**Validador MARCH:** OBRIGATÓRIO. Fatos técnicos devem ser verificáveis (versão, sintaxe, exemplo de código).

**Validador de Continuidade:** OBRIGATÓRIO, com foco em:
- VOZ_NARRATIVA (tom técnico consistente)
- CONCEITO_DEFINICAO (termos técnicos definidos)
- CONCEITO_REGRA (regras rígidas respeitadas)
- TIMELINE_CRONOLOGIA (pré-requisitos respeitados)
- REFERENCIA_FACTUAL (citações a documentação oficial)

**Editor:** Foco em precisão técnica, clareza, progressão lógica. NUNCA inventa sintaxe ou APIs.

**Formato do fim da cena:** ## Resumo + ## Checklist (4 itens, com pré-requisitos verificados).

---

## Calibração disponível

O `capitulos_calibracao/capitulo_01/` contém **2 cenas** de exemplo, mostrando como um capítulo técnico termina — com Resumo, Checklist, e a progressão de pré-requisitos. Serve para a IA produtora entender o formato.