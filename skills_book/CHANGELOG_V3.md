# CHANGELOG v3 — Pipeline Genérico Greenforge

**Versão:** 3.0 (Pipeline Parametrizado)
**Data de fechamento:** 2026-07-29
**Status:** CONCLUÍDO

---

## Resumo executivo

O pacote `skills_book_v3_PIPELINE_GENERICO` é um **pipeline genérico de produção de livros** baseado no framework Greenforge. Ele separa duas responsabilidades:

- **Estrutura do pipeline** (como produzir, validar, atualizar atomicamente) — fixa, em 14 arquivos de skills + 6 templates + 2 regras de negócio
- **Decisões de gênero** (voz, formato, extensão, validações) — parametrizadas, em arquivos `GENERO.md` separados e trocáveis

O pacote inclui 3 perfis de gênero pré-configurados (Podbook, Ficção, Técnico) e instruções para criar gêneros novos.

---

## Camadas de Entrega

### Camada 1 — Foundation (CONCLUÍDA, 2026-07-29)

30 arquivos, 228 KB:

- `LEIA-ME-PRIMEIRO.md` (entrada da IA produtora)
- `REGRAS_GREENFORGE_PIPELINE.md` (6 leis duras)
- `FLUXO_COMPLETO_PIPELINE.md` (FASE 0-3, loop cena-por-cena)
- `CONFIG.md` (template para o usuário)
- `generos_template/TEMPLATE_GENERO_VAZIO.md` (11 seções)
- 14 arquivos de skills (BOOT + SKILL) para 7 agentes:
  - escritor, atomizador, validador_march, validador_continuidade, editor, consolidador, orquestrador
- 3 templates (Bible, Bible esqueleto vazio, Estado)
- 2 regras de negócio (CENAS_PROIBIDAS + AUTO_AUDITORIA, 10 testes)
- 6 templates JSON/MD para worktree
- 1 placeholder de capítulos_exemplo

### Camada 2 — 3 Perfis de Gênero (CONCLUÍDA, 2026-07-29)

70 arquivos, 304 KB totais:

#### `generos_completos/podbook_mentor/`
- `GENERO.md` (160 linhas, 11 seções, baseado no Ecommerce do Zero do Bruno)
- `BIBLE_EXEMPLO.md` (181 linhas, exemplo concreto)
- `README.md` (47 linhas, notas do gênero)
- 5 cenas de calibração (Cap 1):
  - Cena 1.1: A jornada começa agora (APROVADO, 6/7 afirmações, 1320 palavras)
  - Cena 1.2: A versão 3.0 (APROVADO, 4/5 afirmações, 1180 palavras)
  - Cena 1.3: A equipe por trás (APROVADO, 1320 palavras)
  - Cena 1.4: REPROVADA — exemplo de reescrita cirúrgica
  - Cena 1.5: PÓS-CIRÚRGICA — versão final aprovada

#### `generos_completos/ficcao_literaria/`
- `GENERO.md` (141 linhas, 11 seções, perfil genérico de ficção)
- `BIBLE_EXEMPLO.md` (exemplo: romance "A Casa do Cais")
- `README.md` (68 linhas, com particularidades do gênero)
- 1 cena de calibração: Helena chega à casa da avó (POD_A_CENA, fim natural, sem Resumo/Checklist)

#### `generos_completos/tecnico_manual/`
- `GENERO.md` (160 linhas, 11 seções, perfil de manual how-to)
- `BIBLE_EXEMPLO.md` (exemplo: "Python para Iniciantes")
- `README.md` (68 linhas)
- 2 cenas de calibração:
  - Cena 1.1: REPROVADA — sobre criador/ano do Python (mostra gatilho de reprovação)
  - Cena 1.2: APROVADA — sobre instalação, com Resumo + Checklist

### Camada 3 — Finalização (CONCLUÍDA, 2026-07-29)

11 novos arquivos, 60 KB:

- `README.md` (raiz) — overview do pacote, quick start em 5 passos
- `GUIA_DE_USO.md` — tutorial passo a passo para Cenários A, B, C + troubleshooting
- `CHANGELOG_V3.md` (este arquivo)
- `execucao/` (5 arquivos) — pasta de trabalho por projeto, com README explicativo em cada subdiretório
- Ajustes finos nas skills core para garantir parametrização (ver "Auditoria" abaixo)

---

## Auditoria de Parametrização

A Camada 3 incluiu uma auditoria rigorosa para garantir que as **skills core** não têm valores hardcoded de Podbook/Bruno/mentor. Ajustes feitos:

### `escritor/SKILL_ESCRITOR_PIPELINE.md`
- ❌ ANTES: Seção "Adaptação por Gênero" com tabela fixa para Podbook, Ficção, Técnico
- ✅ DEPOIS: Tabela vazia que instrui a IA a ler valores do `GENERO.md` do projeto

### `escritor/BOOT_ESCRITOR_PIPELINE.md`
- ❌ ANTES: "Quem você é depende do gênero: se Podbook → mentor, se Ficção → narrador..."
- ✅ DEPOIS: "Quem você é é definido pelo `GENERO.md`" — menções aos 3 perfis viraram EXEMPLO, não regra

### `consolidador/SKILL_CONSOLIDADOR_PIPELINE.md`
- ❌ ANTES: Tabela "Seções extras conforme gênero" com valores fixos para Podbook, Ficção, Técnico
- ✅ DEPOIS: Tabela marcada como EXEMPLO; instrução para ler do `GENERO.md` do projeto

### `orquestrador/BOOT_ORQUESTRADOR_PIPELINE.md`
- ❌ ANTES: "Se o gênero é Podbook → diretor de produção, se Ficção → editor literário..."
- ✅ DEPOIS: Reframe como EXEMPLO, com regra explícita: "O texto que você segue é o que está em `execucao/GENERO.md`"

### `editor/BOOT_EDITOR_PIPELINE.md`
- ❌ ANTES: 3 perfis fixos (Podbook/Ficção/Técnico)
- ✅ DEPOIS: Reframe como EXEMPLO + instrução para ler `GENERO.md` seções 1, 3, 8

### `atomizador/BOOT_ATOMIZADOR_PIPELINE.md`
- ❌ ANTES: Exemplo "Bruno citou que Patacori fatura alto hoje"
- ✅ DEPOIS: Exemplo genérico "o mentor citou que a aluna X fatura alto hoje"

### `regras_negocio/CENAS_PROIBIDAS_PIPELINE.md`
- ❌ ANTES: "Bruno recomenda" e "Patakori" como exemplos
- ✅ DEPOIS: "O mentor recomenda" e "[nome fictício de negócio]" — genéricos

### `regras_negocio/AUTO_AUDITORIA_PIPELINE.md`
- ❌ ANTES: `grep -E "tipo: (PODBOOK|NÃO_FICÇÃO|TÉCNICO)"` (case-sensitive, restrito)
- ✅ DEPOIS: `grep -iE "^\*\*Tipo:\*\*.*(podbook|não_ficção|nao_ficcao|tecnico|técnico|manual|didatico|didático)"` (case-insensitive, abrangente)

### Resultados da auditoria automatizada

```
=== AUDITORIA 1: Menção a 'Bruno' em skills core ===
  (vazio) → Nenhuma menção a 'bruno' nas skills core ✅

=== AUDITORIA 2: 11 seções em cada GENERO.md ===
  ficcao_literaria: ✅ 11/11
  podbook_mentor:   ✅ 11/11
  tecnico_manual:   ✅ 11/11

=== AUDITORIA 3: [definir] pendente em GENERO.md ===
  Nenhum [definir] em GENERO.md ✅
```

---

## Comparação v2 → v3

| Aspecto | v2 (Podbook Greenforge) | v3 (Pipeline Genérico) |
|---|---|---|
| Gênero | Podbook fixo (Bruno, mentor, Ecommerce) | Parametrizado, escolha do usuário |
| Hardcoded | Valores fixos (1ª pessoa mentor, 1000-4000 palavras, etc.) | Tudo lido do `GENERO.md` |
| Voz da skill | "Você é o mentor Bruno..." | "Quem você é é definido pelo GENERO.md" |
| Bible | Específica do Podbook | Template genérico + 3 exemplos |
| Gêneros | 1 (Podbook) | 3 (Podbook, Ficção, Técnico) + template para criar mais |
| Validação MARCH | Específica para Ecommerce | Genérica, lê tipo do `GENERO.md` |
| Pacote | 1 perfil | Pipeline reutilizável para qualquer gênero |
| Cena de calibração | Cap 1 do Ecommerce | Cap 1 de cada um dos 3 perfis |

---

## Métricas finais do pacote

- **87 arquivos** no total
- **584 KB** total
- **16 diretórios** organizados por papel (escritor, atomizador, validador, editor, etc.)
- **3 perfis de gênero** completos com GENERO.md + BIBLE_EXEMPLO + cenas de calibração
- **14 arquivos de skill** (BOOT + SKILL de 7 agentes)
- **6 templates JSON/MD** para worktree
- **2 arquivos de regras de negócio** (CENAS_PROIBIDAS + AUTO_AUDITORIA com 10 testes)
- **5 READMEs explicativos** (raiz + execucao + 3 perfis)
- **0 violações de parametrização** detectadas na auditoria final

---

## O que o usuário precisa fazer para usar

### Caso 1 — Tenho um corpus e quero produzir um livro em um dos 3 perfis

1. Copie o pacote para uma pasta de projeto
2. Copie `generos_completos/[perfil]/GENERO.md` para `execucao/GENERO.md`
3. Preencha `execucao/CONFIG.md` com título, foco, caminho do corpus
4. Coloque o corpus em `execucao/corpus/`
5. Passe para a IA com a instrução padrão (ver `GUIA_DE_USO.md`)

### Caso 2 — Quero criar um gênero novo

1. Copie `generos_template/TEMPLATE_GENERO_VAZIO.md` para `generos_completos/[nome]/GENERO.md`
2. Preencha todas as 11 seções com valores concretos
3. Crie uma Bible exemplo em `generos_completos/[nome]/BIBLE_EXEMPLO.md`
4. Produza 1-2 capítulos de calibração usando o pipeline
5. Valide e documente

### Caso 3 — Quero auditar a produção

1. Abra `execucao/estado/ESTADO_DA_OBRA.md` para ver histórico cena-por-cena
2. Confira checksums, retries, validações
3. Rode a Auto-Auditoria (10 testes) sobre o livro final

---

## Limitações conhecidas

- **Pipeline lento por design.** Cena-por-cena com validação dupla cega custa mais que "escrever tudo de uma vez". É um trade-off explícito: garantia de qualidade vs. velocidade.
- **Dependência de corpus.** A validação MARCH funciona melhor com corpus robusto. Para Ficção pura sem corpus, a Bible precisa ser muito bem feita antes de começar.
- **Requer modelo com ferramentas de arquivo.** A IA precisa ler/escrever arquivos, executar comandos bash, etc. Modelos só-texto não conseguem.
- **3 perfis são ponto de partida.** Adicionar um gênero novo é trabalho real (preencher 11 seções, criar Bible exemplo, calibrar). Não é geração automática.

---

## Próximas evoluções possíveis (fora do escopo da v3)

- Adicionar perfis pré-configurados para: Acadêmico, Biografia/Memórias, Autoajuda Prática, Relato de Viagem, Roteiro
- Criar ferramenta CLI para automatizar a inicialização (criar `execucao/`, copiar GENERO, etc.)
- Adicionar suporte nativo para worktree git (atualmente é pasta, não branch)
- Painel web para acompanhar a produção cena-por-cena em tempo real
- Teste de integração automatizado que roda o pipeline em um corpus pequeno

---

## Licença e uso

Este pacote foi construído para uso do autor do projeto. É aberto (no sentido de "você pode ler e modificar tudo"), mas não tem licença formal definida. Se quiser usar para projetos próprios, faça — o pipeline é genérico por design.
