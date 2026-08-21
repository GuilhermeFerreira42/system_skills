# Relatório de Auditoria do Pipeline — Skill 3

- **Projeto:** `/home/user/projeto_restaurado/system_skills/skills_book/skills_book_3.6.2/skills_book_v3.6_FINAL`
- **Executado em:** 2026-08-21T11:48:06.085013+00:00
- **Cenas auditadas:** 1  _(cenas de `capitulos_calibracao/` ignoradas — use `--incluir-calibracao`)_
- **Veredito:** **NAO_CONFORME**

| Severidade | Qtd |
|---|---:|
| BLOQUEIO | 13 |
| ALERTA | 1 |
| INFO | 1 |

## Verificação Python — foi executada?

| Script | Deixa prova em disco? | Situação |
|---|---|---|
| `lint_conviccao.py` | ❌ não (só stdout) | reexecutado por este fiscal em toda cena |
| `vigia_integridade.py` | ✅ `_log_vigia.md` | reexecutado em cópia temporária e comparado |
| `reconciliar_controle.py` | ✅ `reconciliacao_ultima.json` | executado no projeto |

## Achados

### BLOQUEIO (13)

- **[A1.artefato_obrigatorio]** `generos_completos/tecnico_manual/capitulos_calibracao/capitulo_01/cena_01` — artefato ausente: _saida_candidato.md (exigido por vigia_integridade.py)
- **[A1.artefato_obrigatorio]** `generos_completos/tecnico_manual/capitulos_calibracao/capitulo_01/cena_01` — artefato ausente: _saida_final.md (exigido por vigia_integridade.py)
- **[A1.artefato_obrigatorio]** `generos_completos/tecnico_manual/capitulos_calibracao/capitulo_01/cena_01` — artefato ausente: _resultado_revisor_cego.json (exigido por vigia_integridade.py)
- **[A1.artefato_obrigatorio]** `generos_completos/tecnico_manual/capitulos_calibracao/capitulo_01/cena_01` — artefato ausente: _manifesto_integridade.json (exigido por vigia_integridade.py)
- **[A2.artefato_nao_coberto_pelo_vigia]** `generos_completos/tecnico_manual/capitulos_calibracao/capitulo_01/cena_01` — artefato ausente: _log_prompt_checker.md — o vigia NÃO reprova essa ausência (só confere o log se ele existir), então sem este arquivo a cegueira fica NÃO AUDITÁVEL
- **[A2.artefato_nao_coberto_pelo_vigia]** `generos_completos/tecnico_manual/capitulos_calibracao/capitulo_01/cena_01` — artefato ausente: _log_prompt_continuidade.md — o vigia NÃO reprova essa ausência (só confere o log se ele existir), então sem este arquivo a cegueira fica NÃO AUDITÁVEL
- **[B2.lint_reprova]** `generos_completos/tecnico_manual/capitulos_calibracao/capitulo_01/cena_01` — lint_conviccao.py REPROVA o candidato (média 6.83, 0 infração(ões) F6). Problemas: [V6] 1 cena(s) sem fechamento próprio: Cena 1: O que é Python e por que aprender — TODA cena deve concluir com cristalização (GENERO §4). | [V6] última cena sem chamado tátil completo (verbo + medida + critério, sem tarefa burocrática — GENERO §4).
- **[B7.vigia_falha]** `generos_completos/tecnico_manual/capitulos_calibracao/capitulo_01/cena_01` — arquivo ausente: _saida_candidato.md
- **[B7.vigia_falha]** `generos_completos/tecnico_manual/capitulos_calibracao/capitulo_01/cena_01` — arquivo ausente: _saida_final.md
- **[B7.vigia_falha]** `generos_completos/tecnico_manual/capitulos_calibracao/capitulo_01/cena_01` — arquivo ausente: _resultado_revisor_cego.json
- **[B7.vigia_falha]** `generos_completos/tecnico_manual/capitulos_calibracao/capitulo_01/cena_01` — arquivo ausente: _manifesto_integridade.json
- **[B8.vigia_nao_executado]** `generos_completos/tecnico_manual/capitulos_calibracao/capitulo_01/cena_01` — não existe `_log_vigia.md` na cena: o Orquestrador NÃO executou o Vigia (ou não o executou nesta versão). O pipeline exige o Vigia antes de declarar CONCLUIDO.
- **[B12.controle_divergente]** `obra` — cena cap_01_cena_01: arquivo_final_ausente

### ALERTA (1)

- **[B4.lint_sem_prova_de_execucao]** `generos_completos/tecnico_manual/capitulos_calibracao/capitulo_01/cena_01` — não há prova em disco de que o Estágio 1 (lint) foi executado pelo Orquestrador: lint_conviccao.py só escreve em stdout. Recomendação: o Orquestrador deve persistir a saída `--json` em `_log_lint_conviccao.json` na cena. Este fiscal reexecutou o lint para suprir a lacuna.

### INFO (1)

- **[C0.sem_livro]** `obra` — obra consolidada não encontrada; testes §1-§5 da autoauditoria pulados

---

Este fiscal audita **conformidade de processo**, não qualidade literária.
Fluidez é responsabilidade do Escritor, do Editor e do Revisor Cego
(AUTO_AUDITORIA_PIPELINE.md §7). Toda falha aqui é **falha de pacote**.
