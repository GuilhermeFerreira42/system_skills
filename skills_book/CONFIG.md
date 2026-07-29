# CONFIG — Configuração do Projeto de Livro

**Versão:** 3.0
**Aplicação:** O USUÁRIO preenche este arquivo ANTES de passar o pacote para a IA produtora. A IA lê este arquivo como PRIMEIRO passo da execução.

---

## ⚠️ INSTRUÇÕES PARA O USUÁRIO

1. Preencha TODOS os campos marcados com `[preencher]`
2. Não deixe nenhum campo vazio
3. Se não souber, escreva "[definir]" e resolva antes de prosseguir
4. Salve e copie o pacote completo para a IA produtora

---

## Dados do Projeto

- **Título do Livro:** [preencher]
- **Subtítulo (opcional):** [preencher ou deixar em branco]
- **Gênero escolhido:** [preencher — caminho para o gênero, ex: `generos_completos/podbook_mentor/GENERO.md`]
- **Caminho do Corpus:** [preencher — caminho para a pasta com as fontes, ex: `execucao/corpus/` ou `corpus/`]
- **Foco do Usuário (instrução NotebookLM-style):**
  > [preencher — instrução livre, ex: "Foco no método Ecommerce do Zero 3.0 completo. Linguagem acessível. Texto fluido para narração em áudio. Ganchos entre cenas. Ideal para quem vai ouvir o livro."]

---

## Configurações Opcionais

- **Número estimado de capítulos:** [preencher ou deixar em branco — o Orquestrador decide]
- **Número estimado de cenas:** [preencher ou deixar em branco]
- **Palavras estimadas total:** [preencher ou deixar em branco]
- **Público-alvo principal:** [preencher — quem vai ler/ouvir o livro]
- **Tom específico (se diferente do gênero):** [preencher ou deixar em branco]

---

## Notas Adicionais

[Espaço livre para contexto extra que a IA deve considerar. Ex: "O livro é para alunos que já compraram o curso Ecommerce do Zero, então pode assumir que conhecem termos básicos de e-commerce." OU "O livro é a versão escrita do podcast [nome], então mantenha o tom de conversa do podcast."]

---

## Checklist Antes de Passar para a IA

Confirme cada item:

- [ ] Título preenchido
- [ ] Gênero escolhido e o arquivo `generos_completos/[genero]/GENERO.md` existe
- [ ] Corpus existe no caminho indicado e contém apenas conteúdo didático (sem material de marketing)
- [ ] Foco do usuário está escrito em texto claro
- [ ] Se for adicionar gênero novo, o `GENERO.md` foi criado seguindo o `generos_template/TEMPLATE_GENERO_VAZIO.md`
- [ ] Se o gênero tem capítulos de calibração, a IA vai ter acesso a eles
- [ ] O pacote `execucao/` está pronto (CONFIG.md, GENERO.md, corpus/ disponíveis)

Se marcou todos, pode passar para a IA produtora com a instrução:

> "Leia o `execucao/CONFIG.md` primeiro, depois o `execucao/GENERO.md`, depois o `LEIA-ME-PRIMEIRO.md` e o `REGRAS_GREENFORGE_PIPELINE.md` e o `FLUXO_COMPLETO_PIPELINE.md`, depois as SKILLs do seu papel. Comece pelo Passo 1 do BOOT do Orquestrador."
