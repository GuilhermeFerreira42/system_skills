# Comparativo: Skills Book — Versão 1 vs Versão 2

> As pastas têm nomes `skills_book_1` e `skills_book_2`, mas o conteúdo revelado nos READMEs indica que:
> - **`skills_book_1`** = Pipeline Genérico Greenforge **v3** (data de fechamento: 2026-07-29)
> - **`skills_book_2`** = Skills Book Greenforged Edition **v1.0** com melhorias pós-diagnóstico (data: 2026-07-27, com ações completadas até 2026-08-05)

---

## Tabela Comparativa

| Dimensão | `skills_book_1` (Pipeline Genérico v3) | `skills_book_2` (Greenforged Edition v1.0+) |
|---|---|---|
| **Nome oficial** | Pipeline Genérico Greenforge v3 | Skills Book — Greenforged Edition |
| **Versão** | 3.0 | 1.0 (com 6 ações de diagnóstico aplicadas) |
| **Data** | 2026-07-29 | 2026-07-27 (ações até 2026-08-05) |
| **Objetivo central** | Framework genérico reutilizável para qualquer gênero | Sistema completo de produção com foco em qualidade editorial e código compartilhado |
| **Arquivo de entrada** | `LEIA-ME-PRIMEIRO.md` + `CONFIG.md` | `inicializador.txt` |
| **Total de arquivos** | ~87 arquivos / 584 KB | Não especificado (mais leve em docs, mais pesado em código Python) |

---

## Agentes (Pipeline)

| Agente | `skills_book_1` (v3) | `skills_book_2` (v1.0+) |
|---|---|---|
| **Orquestrador** | ✅ | ✅ |
| **Escritor** | ✅ | ✅ |
| **Atomizador** | ✅ | ✅ |
| **Validador MARCH** | ✅ (cego) | ✅ (cego) |
| **Validador Continuidade** | ✅ (cego) | ✅ (cego) |
| **Editor** | ✅ (opcional) | ✅ (opcional) |
| **Consolidador** | ✅ | ✅ |
| **Controle da Obra** | ❌ Não existe | ✅ **NOVO** — agente separado, espelho do filesystem |
| **Revisor Cego Editorial** | ❌ Não existe | ✅ **NOVO** — checker cego de forma editorial (estrutura, clareza, ritmo) |

---

## Gêneros Suportados

| Gênero | `skills_book_1` (v3) | `skills_book_2` (v1.0+) |
|---|---|---|
| **Podbook/Mentor** | ✅ `generos_completos/podbook_mentor/` | ⚠️ LEGACY — `GENERO_PODBOOK_LEGACY.md` (ainda funciona, não evoluído) |
| **Ficção Literária** | ✅ `generos_completos/ficcao_literaria/` | ✅ `GENERO_ROMANCE.md` |
| **Técnico/Manual** | ✅ `generos_completos/tecnico_manual/` | ✅ `GENERO_TECNICO.md` (reescrito v2.0, agnóstico) |
| **Não-Ficção** | ❌ Não existe como perfil próprio | ✅ `GENERO_NAO_FICCAO.md` (reescrito v2.0, agnóstico) |
| **Memórias** | ❌ | ✅ `GENERO_MEMORIAS.md` |
| **Thriller** | ❌ | ✅ **NOVO** `GENERO_THRILLER.md` (177 linhas, 5 arquetipos) |
| **Cookbook** | ❌ | ✅ **NOVO** `GENERO_COOKBOOK.md` (183 linhas, também para livros prescritivos) |
| **Acadêmico** | ❌ | ✅ **NOVO** `GENERO_ACADEMICO.md` (196 linhas, 5 arquetipos) |
| **Personalizado** | ✅ (template de 11 seções) | ✅ `GENERO_PERSONALIZADO.md` |
| **Total de gêneros** | 3 + template | 10 (incluindo LEGACY e personalizado) |

---

## Infraestrutura Técnica

| Recurso | `skills_book_1` (v3) | `skills_book_2` (v1.0+) |
|---|---|---|
| **Código compartilhado (utils/)** | ❌ Não existe | ✅ Pasta `utils/` com 3 arquivos Python |
| **`constantes.py`** | ❌ | ✅ 133 constantes — elimina hardcoded nas skills |
| **`checksum.py`** | ❌ (usa `sha256sum \| cut -c1-8` manual) | ✅ 587 linhas, 14 funções, CLI, detecção de drift |
| **`vigia_integridade.py`** | ❌ | ✅ Script de vigilância de integridade |
| **Salvamento atômico** | ✅ (`os.replace`) | ✅ (`.tmp → rename`) |
| **Checksum round-trip** | ✅ (SHA256, 8 chars) | ✅ (com versão e detecção de drift) |
| **Isolamento por worktree** | ✅ (pasta por cena) | ✅ (pasta por capítulo/cena) |
| **Retomada de checkpoint** | ✅ | ✅ (exata, retoma EXATAMENTE onde parou) |

---

## Validação e Qualidade

| Critério | `skills_book_1` (v3) | `skills_book_2` (v1.0+) |
|---|---|---|
| **Travas MARCH** | ✅ 1 CONTRADITO = REPROVADO, <80% CONFIRMADO = REPROVADO | ✅ Mesmas regras |
| **Travas Continuidade** | ✅ 1 CONTRADITO = REPROVADO | ✅ Mesmas regras |
| **Max retries por cena** | 3 (depois: flag para humano) | 3 (depois: flag para humano) |
| **Cegueira dos validadores** | ✅ Absoluta | ✅ Absoluta |
| **Revisão editorial cega** | ❌ Não existe | ✅ 3 categorias, 18 tipos de problemas, 3 gravidades |
| **Nivelamento editorial** | ❌ Não existe | ✅ **OBRIGATÓRIO** — 4 perguntas de múltipla escolha (estilo de abertura, densidade, analogias, voz) |
| **Perfil editorial persistido** | ❌ | ✅ Persiste em Bible + Estado |
| **Cenas de calibração** | ✅ 8 cenas (3 perfis) | ❌ Não há no pacote base |
| **Auditoria automatizada** | ✅ 10 testes (AUTO_AUDITORIA) | ❌ Não documentado |

---

## Estrutura de Documentação

| Documento | `skills_book_1` (v3) | `skills_book_2` (v1.0+) |
|---|---|---|
| **README.md** | ✅ (195 linhas) | ✅ (175 linhas) |
| **CHANGELOG** | ✅ `CHANGELOG_V3.md` (detalhado) | ❌ Sem changelog dedicado |
| **Guia de uso** | ✅ `GUIA_DE_USO.md` (3 cenários + troubleshooting) | ❌ Substituído pelo `inicializador.txt` |
| **Fluxo completo** | ✅ `FLUXO_COMPLETO_PIPELINE.md` | ✅ `exemplos/FLUXO_COMPLETO_LIVRO.md` |
| **Regras do pipeline** | ✅ `REGRAS_GREENFORGE_PIPELINE.md` | Embutidas no README (Regras de Ouro) |
| **CONFIG.md** | ✅ (template a preencher) | ❌ Não existe |
| **Esquema de pasta** | ❌ | ✅ `esquema/ESTRUTURA_PROJETO_LIVRO.md` |
| **Bible viva** | ✅ Templates genéricos + 3 exemplos | ✅ Template + exemplo |
| **Estado da obra** | ✅ Template | ✅ Template |

---

## Leis / Regras de Ouro

| # | `skills_book_1` (v3) — 6 Leis Duras | `skills_book_2` (v1.0+) — 8 Regras de Ouro |
|---|---|---|
| 1 | Cena por cena, sempre | Orquestrador NÃO escreve, NÃO valida. Só COORDENA |
| 2 | Validação dupla cega, sempre | Cada agente recebe SÓ o insumo necessário |
| 3 | Atualização atômica, sempre | Validação MARCH + Continuidade SÃO OBRIGATÓRIAS |
| 4 | Checksum e round-trip, sempre | CEGUEIRA ABSOLUTA dos validadores |
| 5 | Isolamento por worktree, sempre | MAX 3 RETRIES por cena |
| 6 | Zero material de marketing, sempre | CHECKSUM ROUND-TRIP |
| 7 | — | SALVAMENTO ATÔMICO |
| 8 | — | BIBLE + ESTADO = CHECKPOINTS ÚNICOS |

---

## Resumo Executivo

| | `skills_book_1` (v3) | `skills_book_2` (v1.0+) |
|---|---|---|
| **Ponto forte** | Documentação rica, cenas de calibração, auditoria automatizada, parametrização total | Mais agentes, mais gêneros, código Python robusto, nivelamento editorial, revisor cego |
| **Ponto fraco** | Sem utilitários Python, sem nivelamento editorial, apenas 3 gêneros | Sem cenas de calibração no pacote base, sem CONFIG.md, sem changelog detalhado |
| **Melhor para** | Quem quer um pacote completo, bem documentado, pronto para usar sem código | Quem quer robustez técnica, mais gêneros e controle editorial fino |
| **Posicionamento** | Pipeline reutilizável e genérico — entrega a estrutura | Sistema de escrita com mais guardrails e ferramentas — entrega a experiência |
