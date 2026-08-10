# Changelog — Skill 3

## 3.0 — Fusão qualitativa + técnica

A Skill 3 parte da estrutura limpa do Pipeline Greenforge e incorpora a blindagem física da evolução posterior sem levar métricas estéticas para o contexto do Escritor.

### Decisões principais

- Removidos gates determinísticos de ritmo da produção e da aprovação literária.
- Criado contrato de voz qualitativo, configurado por nivelamento editorial.
- Criado Revisor Cego Editorial holístico, sem script de contagem.
- Editor movido para antes das validações do artefato candidato.
- MARCH e Continuidade passam a validar a última versão mutável.
- Criado manifesto de integridade por cena.
- Criado Vigia físico sem responsabilidade estética.
- Criado Controle da Obra como camada de reconciliação do filesystem.
- Criado estado `MODIFICADO_MANUALMENTE` para edição humana legítima.
- Criado estado `BLOQUEADA_REVISAO_HUMANA` após três retries.
- Consolidadores não podem declarar livro concluído com cenas pendentes.
- Perfis de gênero passaram a ser referências opcionais; o boot gera um perfil editorial dinâmico.

### Não incorporado

- `medir_ritmo.py` como gate.
- Porcentagens de parágrafos densos.
- Desvio-padrão mínimo.
- Proibição matemática de frases curtas.
- Reescrita automática integral causada apenas por divergência de checksum.

### Compatibilidade

Os nomes tradicionais de `_saida_escritor.md`, `_saida_editor.md`, `_saida_final.md`, MARCH e Continuidade são preservados. A Skill 3 adiciona `_saida_candidato.md` e `_manifesto_integridade.json` para separar a última mutação do artefato final fechado.
