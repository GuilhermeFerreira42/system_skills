# GUIA DE USO PRÁTICO — Pipeline Genérico Greenforge v3

**Versão:** 3.0
**Aplicação:** tutorial passo a passo para você usar este pacote pela primeira vez.

---

## Antes de começar: o que você precisa ter

1. **Corpus** — transcrições, documentos, anotações, ou rascunhos que serão a fonte do livro. Quanto mais rico, melhor.
2. **Decisão de gênero** — qual dos 3 perfis prontos usar, ou se vai criar um novo.
3. **Decisão de escopo** — quantos capítulos/cenas, qual o público, qual o tom.
4. **Acesso a uma IA com ferramentas de arquivo** — Claude Sonnet/Opus, GPT-4 com Code Interpreter, Gemini Advanced, etc.

---

## Cenário A — Tenho um gênero pronto (dos 3 incluídos)

### Passo 1: Copie o pacote

```bash
cp -r skills_book_v3_PIPELINE_GENERICO/ meu_projeto_livro/
cd meu_projeto_livro/
```

### Passo 2: Veja os gêneros disponíveis

```bash
ls generos_completos/
# podbook_mentor/  ficcao_literaria/  tecnico_manual/
```

Para cada gênero, leia em ordem:

1. `generos_completos/[perfil]/GENERO.md` — o que define o gênero
2. `generos_completos/[perfil]/BIBLE_EXEMPLO.md` — exemplo de Bible preenchida
3. `generos_completos/[perfil]/README.md` — notas específicas
4. `generos_completos/[perfil]/capitulos_calibracao/capitulo_01/` — pelo menos 1 cena para ver o tom

### Passo 3: Preencha a pasta execucao/

```bash
cp CONFIG.md execucao/CONFIG.md
cp generos_completos/podbook_mentor/GENERO.md execucao/GENERO.md
cp -r /caminho/para/seu/corpus/* execucao/corpus/
```

Abra `execucao/CONFIG.md` e preencha:

- **Título do Livro:** "Ecommerce do Zero 3.0"
- **Gênero escolhido:** `generos_completos/podbook_mentor/GENERO.md`
- **Caminho do Corpus:** `execucao/corpus/`
- **Foco do Usuário:** "Foco no método completo do Bruno, com exemplos práticos, tom de conversa, ganchos entre cenas."
- **Público-alvo principal:** "Empreendedores iniciantes em e-commerce"
- **Tom específico (opcional):** "Tom encorajador, com humor leve"

### Passo 4: Verifique o corpus

Abra alguns arquivos em `execucao/corpus/` e confirme:
- É conteúdo didático (não marketing)
- Tem informação suficiente para os capítulos planejados
- Está em formato legível (.md preferencialmente)

Se houver mistura com marketing, separe.

### Passo 5: Passe para a IA

Diga para a IA:

> "Você vai produzir um livro usando o pipeline Greenforge v3. Comece lendo nesta ordem:
> 1. `execucao/CONFIG.md` (configuração do projeto)
> 2. `execucao/GENERO.md` (gênero escolhido)
> 3. `LEIA-ME-PRIMEIRO.md` (orientações gerais)
> 4. `REGRAS_GREENFORGE_PIPELINE.md` (as 6 leis duras)
> 5. `FLUXO_COMPLETO_PIPELINE.md` (passo a passo)
> 6. `orquestrador/SKILL_ORQUESTRADOR_PIPELINE.md` (sua skill)
> 7. `orquestrador/BOOT_ORQUESTRADOR_PIPELINE.md` (inicialização)
>
> Comece pelo Passo 1 do BOOT do Orquestrador. Trabalhe de forma autônoma, cena por cena. Pare e me avise quando o livro estiver pronto ou se travar em algum momento."

### Passo 6: Acompanhe

A IA vai trabalhar por um tempo. Você pode:
- Pedir updates periódicos ("como está o progresso?")
- Auditar uma cena específica quando terminar ("me mostra a cena 1.3 e suas validações")
- Interromper e ajustar o `GENERO.md` se achar o tom errado (mas só no início, antes da cena 3)

### Passo 7: Receba o livro

Quando a IA terminar, ela vai te entregar:
- O livro final (gerado pelo Consolidador)
- A Bible da Obra (fonte da verdade completa)
- O Estado da Obra (histórico de produção)

Você pode então revisar, pedir ajustes pontuais (reforma de cena específica), ou considerar o livro pronto.

---

## Cenário B — Quero criar um gênero novo

### Passo 1: Copie o template

```bash
cp generos_template/TEMPLATE_GENERO_VAZIO.md generos_completos/meu_genero/GENERO.md
```

### Passo 2: Preencha o GENERO.md

Leia o `TEMPLATE_GENERO_VAZIO.md` e preencha todas as 11 seções:

1. **Identidade e Voz** — quem é o narrador, como fala, qual o registro
2. **POV** — 1ª, 2ª, 3ª, limitada, onisciente
3. **Estrutura de Cena** — extensão, beats, ritmo
4. **Formato do Final** — Resumo/Checklist, natural, código
5. **Oralidade** — para narração, conversação, ou leitura silenciosa
6. **Estrutura Global** — quantos capítulos, como se divide
7. **Requisitos da Bible** — que tipo de fonte da verdade esse gênero precisa
8. **Polimento do Editor** — que tipo de ajustes o Editor faz
9. **Validações Extras** — tem alguma validação especial além de MARCH + Continuidade?
10. **O que NÃO é** — esse gênero não é X, Y, Z
11. **Notas de Produção para a IA** — instruções finais

Baseie-se em livros publicados do gênero. Pegue 2-3 exemplos e descreva o que eles têm em comum.

### Passo 3: Crie uma Bible exemplo (opcional mas recomendado)

```bash
cp bible/BIBLE_ESQUELETO_VAZIO.md generos_completos/meu_genero/BIBLE_EXEMPLO.md
```

Abra e preencha com um exemplo concreto de livro do gênero (pode ser inventado, mas realista).

### Passo 4: Crie um README do gênero

```bash
touch generos_completos/meu_genero/README.md
```

Documente:
- Quando usar esse gênero
- Que tipo de corpus serve melhor
- Que armadilhas evitar
- 1-2 exemplos de livros que se encaixam

### Passo 5: Produza 1-2 cenas de calibração

Use o pipeline (Cenário A) com um corpus pequeno (1-2 arquivos) e peça 1-2 cenas. Valide que o tom, formato, e extensão estão certos. Ajuste o `GENERO.md` se necessário.

### Passo 6: Adicione ao índice

Abra `generos_completos/README.md` e adicione uma linha na tabela:

```markdown
| **Meu Gênero** | `meu_genero/` | Para que serve... |
```

Pronto, gênero novo criado e validado.

---

## Cenário C — Tenho um corpus específico mas nenhum gênero pronto encaixa

Use o Cenário B com mais ênfase na etapa de Bible exemplo. Se o gênero for muito específico (ex: livro-jogo, livro de colorir para adultos, livro de receitas), pode ser que o template padrão precise de ajustes. As 11 seções são uma base, não camisa-de-força. Adicione seções se precisar.

---

## Troubleshooting

### "A IA está demorando demais"

É normal. Cena por cena é lento por design. Para um livro de 30 cenas, espere algumas horas. Se a IA está travada em uma cena há muito tempo, peça o status:

> "Mostre o estado atual da execução. Qual cena está em andamento? Quantos retries ela já teve?"

### "A IA está pulando etapas"

Aponte a violação específica:

> "Você pulou a validação de Continuidade na cena 1.2. Isso viola a Lei 2. Refaça a cena seguindo o FLUXO_COMPLETO_PIPELINE.md."

### "O tom está errado"

Leia o `GENERO.md` e a cena de calibração. Ajuste o `GENERO.md` para ser mais específico sobre tom, voz, ritmo. Pode ser que o gênero escolhido não é o melhor para o seu corpus.

### "O corpus é confuso / mistura idiomas"

Antes de passar para a IA, limpe o corpus:
- Separe transcrições em arquivos individuais
- Normalize idioma (tudo em PT-BR, ou tudo em EN, sem mistura)
- Remova cabeçalhos, rodapés, timestamps desnecessários

### "A validação MARCH reprova muito"

Pode ser que:
- O corpus é pequeno para a quantidade de informação que o gênero pede
- O gênero exige afirmações factuais densas mas o corpus é opinativo
- A IA está inventando detalhes que não estão no corpus

Soluções:
- Aumentar o corpus
- Trocar para um gênero que combine mais com o corpus
- Aceitar taxa maior de NAO_ENCONTRADO (é informação não verificada, mas não contradita)

### "Quero mudar o gênero no meio da produção"

**Não faça isso.** Trocar de gênero no meio invalida todas as cenas já produzidas (tom, voz, formato do final). Se precisar trocar, comece do zero com o novo gênero.

### "A IA está misturando material de marketing"

Aponte a violação:

> "A cena 2.3 contém 'clique aqui para garantir sua vaga'. Isso viola a Lei 6. Refaça a cena removendo todo material de marketing."

Se for recorrente, verifique se o `execucao/corpus/` está limpo. Às vezes o corpus tem e-mails de venda misturados com transcrições.

---

## Quando o livro está pronto

A IA vai te entregar:

1. **Livro final** (gerado pelo Consolidador) — em formato Markdown, pronto para diagramação ou exportação
2. **Bible da Obra** — fonte da verdade completa
3. **Estado da Obra** — histórico de produção cena por cena

Próximos passos sugeridos:

1. **Revisão humana** — leia o livro inteiro. Anote inconsistências, ajustes de tom, correções factuais.
2. **Revisão técnica** (se aplicável) — para livros técnicos, peça a um especialista para revisar os exemplos de código.
3. **Revisão de continuidade** — abra a Bible e a prosa, e verifique se a história faz sentido do início ao fim.
4. **Diagramação** — passe o Markdown para um designer ou ferramenta de diagramação (InDesign, Pandoc, etc.)
5. **Publicação** — decida o formato (e-book, impresso, audiobook) e a plataforma.

---

## Suporte

Este é um framework open (no sentido de "você pode ver e modificar tudo"). Se travar:

1. Releia o `LEIA-ME-PRIMEIRO.md` — muita dúvida é resolvida lá
2. Releia a SKILL do papel que está travando
3. Releia o `FLUXO_COMPLETO_PIPELINE.md` — pode ser que a IA pulou uma etapa
4. Se quiser, abra o `execucao/estado/ESTADO_DA_OBRA.md` e veja o histórico de retries
