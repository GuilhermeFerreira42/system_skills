# LEIA-ME-PRIMEIRO — Pipeline Genérico Greenforge v3

**Versão:** 3.0 (Pipeline Parametrizado)
**Aplicação:** framework genérico de produção de livros. Não tem gênero embutido — o usuário fornece.

---

## 🚨 LEIA ANTES DE FAZER QUALQUER COISA

Você está prestes a produzir um livro usando o pipeline Greenforge. Este pacote é **genérico** — não tem gênero embutido, não tem voz definida, não tem extensão por cena fixada. Tudo isso vem do **arquivo de gênero** que o usuário fornece.

A vantagem é que o mesmo pipeline serve para Podbook de Não-Ficção, Ficção Literária, Técnico Manual, ou qualquer outro gênero. A desvantagem é que **você precisa ler o arquivo de gênero antes de começar**, senão não vai saber o que produzir.

---

## 📦 O que tem dentro deste pacote

```
skills_book_v3_PIPELINE_GENERICO/
├── LEIA-ME-PRIMEIRO.md                          ← VOCÊ ESTÁ AQUI
├── REGRAS_GREENFORGE_PIPELINE.md                ← LEIA EM SEGUNDO
├── FLUXO_COMPLETO_PIPELINE.md                    ← LEIA EM TERCEIRO
├── CONFIG.md                                    ← O USUÁRIO PREENCHE ANTES
│
├── generos_template/
│   └── TEMPLATE_GENERO_VAZIO.md                  ← Estrutura padrão de gênero
│
├── generos_completos/                           ← Repositório de gêneros prontos
│   ├── README.md                                ← Lista de gêneros disponíveis
│   ├── podbook_mentor/                          ← Perfil Podbook (do Bruno)
│   │   ├── GENERO.md
│   │   ├── BIBLE_EXEMPLO.md
│   │   └── capitulos_calibracao/
│   ├── ficcao_literaria/                        ← Perfil Ficção
│   │   ├── GENERO.md
│   │   ├── BIBLE_EXEMPLO.md
│   │   └── capitulos_calibracao/
│   └── tecnico_manual/                          ← Perfil Técnico
│       ├── GENERO.md
│       ├── BIBLE_EXEMPLO.md
│       └── capitulos_calibracao/
│
├── escritor/
│   ├── BOOT_ESCRITOR_PIPELINE.md
│   └── SKILL_ESCRITOR_PIPELINE.md
│
├── atomizador/
│   ├── BOOT_ATOMIZADOR_PIPELINE.md
│   └── SKILL_ATOMIZADOR_PIPELINE.md
│
├── validador_march/
│   ├── BOOT_VALIDADOR_MARCH_PIPELINE.md
│   └── SKILL_VALIDADOR_MARCH_PIPELINE.md
│
├── validador_continuidade/
│   ├── BOOT_VALIDADOR_CONTINUIDADE_PIPELINE.md
│   └── SKILL_VALIDADOR_CONTINUIDADE_PIPELINE.md
│
├── editor/
│   ├── BOOT_EDITOR_PIPELINE.md
│   └── SKILL_EDITOR_PIPELINE.md
│
├── consolidador/
│   └── SKILL_CONSOLIDADOR_PIPELINE.md
│
├── orquestrador/
│   ├── BOOT_ORQUESTRADOR_PIPELINE.md
│   └── SKILL_ORQUESTRADOR_PIPELINE.md
│
├── bible/
│   ├── BIBLE_TEMPLATE_PIPELINE.md
│   └── BIBLE_ESQUELETO_VAZIO.md
│
├── estado/
│   └── ESTADO_TEMPLATE_PIPELINE.md
│
├── regras_negocio/
│   ├── CENAS_PROIBIDAS_PIPELINE.md
│   └── AUTO_AUDITORIA_PIPELINE.md
│
├── templates_bible_worktree/
│   ├── _afirmacoes_para_validar.template.json
│   ├── _resultado_march.template.json
│   ├── _perguntas_continuidade.template.json
│   ├── _resultado_continuidade.template.json
│   ├── _log_prompt_checker.template.md
│   └── _saida_final.template.md
│
├── capitulos_exemplo/                          ← Calibração (vazio por padrão)
│   └── README.md
│
└── execucao/                                    ← Onde a IA produtora coloca seu trabalho
    ├── CONFIG.md                                ← Cópia de CONFIG.md da raiz
    ├── GENERO.md                                ← Cópia do gênero escolhido
    ├── corpus/                                  ← Onde o corpus fica
    ├── bible/                                   ← Bible da obra
    ├── estado/                                  ← Estado da obra
    └── capitulos/                               ← Cenas produzidas
```

---

## 🎯 COMO USAR ESTE PACOTE

### Cenário A: O usuário quer produzir um livro com um gênero já existente (ex: Podbook)

1. **Copie este pacote inteiro** para uma pasta de projeto, ex: `livro_ecommerce_do_zero/`
2. **Abra o `CONFIG.md`** e preencha:
   - Gênero escolhido (aponte para um dos perfis em `generos_completos/`)
   - Caminho do corpus (pasta com transcrições ou fontes)
   - Foco do usuário (instrução NotebookLM-style)
   - Título do livro
   - Subtítulo (opcional)
3. **Copie o `generos_completos/[perfil_escolhido]/GENERO.md` para `execucao/GENERO.md`**
4. **Copie o corpus para `execucao/corpus/`**
5. **Passe a pasta `execucao/` para a IA produtora** com a instrução: "Leia o `CONFIG.md`, depois o `GENERO.md`, depois o `REGRAS_GREENFORGE_PIPELINE.md` e o `FLUXO_COMPLETO_PIPELINE.md`, depois as SKILLs do seu papel. Comece pelo Passo 1 do BOOT do Orquestrador."
6. A IA segue o pipeline cena por cena, valida, atualiza atomicamente, até o livro estar pronto.

### Cenário B: O usuário quer criar um gênero NOVO (que não existe nos exemplos)

1. **Copie este pacote inteiro** para uma pasta de desenvolvimento de gênero, ex: `dev_genero_poesia/`
2. **Passe a pasta `generos_template/` para a IA** com a instrução: "Leia o `TEMPLATE_GENERO_VAZIO.md` e preencha todas as seções para o gênero [nome do gênero]. Seja específico e baseie-se em exemplos concretos de livros publicados nesse gênero."
3. A IA produz um `GENERO.md` preenchido
4. **Tu revisa o GENERO.md**, ajusta o que precisar
5. **Tu cria uma Bíblia exemplo** (opcional mas recomendado) usando `bible/BIBLE_ESQUELETO_VAZIO.md` como base
6. **Tu cria 1-2 capítulos de calibração** (mesmo sem ter o livro completo) usando a IA produtora nesse gênero novo, pra validar que o pipeline funciona
7. Se funcionar, tu move o gênero novo para `generos_completos/[nome_do_genero]/` e ele tá disponível pra uso futuro

---

## 🚦 ORDEM DE LEITURA PARA A IA PRODUTORA

Quando a IA for executar a produção do livro, ela DEVE ler nesta ordem:

### Passo 1 — Contexto do projeto
- `execucao/CONFIG.md` (preenchido pelo usuário)
- `execucao/GENERO.md` (o gênero do livro)
- `execucao/corpus/` (as fontes)

### Passo 2 — Framework
- `LEIA-ME-PRIMEIRO.md` (este arquivo)
- `REGRAS_GREENFORGE_PIPELINE.md` (as 6 leis duras)
- `FLUXO_COMPLETO_PIPELINE.md` (passo a passo do loop)

### Passo 3 — Skill do papel
- **Orquestrador:** `orquestrador/SKILL_ORQUESTRADOR_PIPELINE.md`
- **Escritor:** `escritor/SKILL_ESCRITOR_PIPELINE.md`
- **Atomizador:** `atomizador/SKILL_ATOMIZADOR_PIPELINE.md`
- **Validador MARCH:** `validador_march/SKILL_VALIDADOR_MARCH_PIPELINE.md`
- **Validador de Continuidade:** `validador_continuidade/SKILL_VALIDADOR_CONTINUIDADE_PIPELINE.md`
- **Editor:** `editor/SKILL_EDITOR_PIPELINE.md`
- **Consolidador:** `consolidador/SKILL_CONSOLIDADOR_PIPELINE.md`

### Passo 4 — Calibração
- Se o gênero escolhido tem capítulos de calibração em `generos_completos/[perfil]/capitulos_calibracao/`, a IA DEVE ler pelo menos 1 cena completa para calibrar tom, formato e nível de detalhe.

### Passo 5 — Bíblia exemplo
- `generos_completos/[perfil]/BIBLE_EXEMPLO.md` (para entender a estrutura da fonte da verdade)

### Passo 6 — Templates e regras
- `bible/BIBLE_TEMPLATE_PIPELINE.md` (para criar a Bible da obra)
- `estado/ESTADO_TEMPLATE_PIPELINE.md` (para criar o Estado)
- `regras_negocio/CENAS_PROIBIDAS_PIPELINE.md` (o que NÃO fazer)
- `regras_negocio/AUTO_AUDITORIA_PIPELINE.md` (testes de validação automática)

---

## 🚫 O QUE NÃO FAZER (sob nenhuma circunstância)

1. **NÃO invente um gênero.** Se o `CONFIG.md` aponta para um gênero que não existe em `generos_completos/`, PARE e peça orientação ao usuário.
2. **NÃO produza o livro inteiro em uma única chamada.** Cena por cena. Sempre.
3. **NÃO misture o corpus com material de marketing** (páginas de venda, e-mails, preços, CTAs). Se o corpus tiver os dois, use só o conteúdo didático.
4. **NÃO use valores hardcoded nas skills.** Todas as skills leem do `GENERO.md`. Se uma skill tiver valor fixo (ex: "voz de mentor em 1ª pessoa"), está desatualizada.
5. **NÃO pule a validação MARCH ou a validação de Continuidade.** As duas são obrigatórias.
6. **NÃO viole a cegueira dos validadores.** Validador MARCH vê só perguntas + corpus. Validador de Continuidade vê só perguntas + Bible + Estado. Nunca vê a prosa.
7. **NÃO atualize a Bible ou o Estado sem atomicidade** (escrever em `.tmp` e renomear).
8. **NÃO marque uma cena como CONCLUÍDA sem calcular checksum SHA256 e fazer round-trip.**
9. **NÃO use prosa "tudo em um capítulo só"** (5 objetivos misturados em 1 cena).
10. **NÃO invente números, datas, fatos que não estão no corpus.** Se precisar e o corpus não der, use formulação conservadora.

---

## 📞 DÚVIDAS DURANTE A EXECUÇÃO

- Se a Bíblia ou o Estado não existir, crie com os templates.
- Se o corpus não confirmar uma afirmação, faça reescrita cirúrgica com formulação mais conservadora.
- Se a prosa do Escritor ficar vazando JSON ou metadados, rejeite e peça reescrita.
- Se uma cena reprovar 3 vezes seguidas, marque como REPROVADO, siga para a próxima, registre no Histórico de Retries.
- Se o corpus tiver mistura de transcrições e material de marketing, use só as transcrições.
- Se sobrar dúvida sobre formato ou tom, leia os capítulos de calibração do gênero escolhido.

---

## ✅ CHECKLIST ANTES DE COMEÇAR

Confirme cada item:

- [ ] Li este arquivo inteiro
- [ ] Li `REGRAS_GREENFORGE_PIPELINE.md` inteiro
- [ ] Li `FLUXO_COMPLETO_PIPELINE.md` inteiro
- [ ] Li a SKILL do meu papel inteiro
- [ ] Li o `CONFIG.md` (preenchido pelo usuário)
- [ ] Li o `GENERO.md` (escolhido pelo usuário)
- [ ] Identifiquei o corpus (caminho, formato, conteúdo)
- [ ] Se o gênero tem capítulos de calibração, li pelo menos 1 cena
- [ ] Entendi: este pipeline é genérico, tudo vem do GENERO.md
- [ ] Entendi: cena por cena, validação dupla cega, atualização atômica, checksum
- [ ] Entendi: zero mistura de material de marketing
- [ ] Entendi: reescrita cirúrgica quando reprovado, máximo 3 retries

Se você marcou todos, pode começar.
