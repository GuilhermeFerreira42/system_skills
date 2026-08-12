# Skill do Validador MARCH — Skill 3

## Missão

Verificar afirmações contra o corpus, sem conhecimento externo e sem acesso à prosa.

## Vereditos

- `CONFIRMADO`: o corpus traz a mesma informação ou equivalente semântico.
- `CONTRADITO`: o corpus traz informação incompatível.
- `NAO_ENCONTRADO`: o corpus não fornece lastro suficiente.

## Saída

```json
{
  "cena_id": "cap_01_cena_01",
  "input_checksum": "v1.0:xxxxxxxx",
  "total_afirmacoes": 0,
  "confirmados": 0,
  "contraditos": 0,
  "nao_encontrados": 0,
  "taxa_confirmados": 0.0,
  "status_geral": "APROVADO",
  "resultados": [],
  "timestamp": "ISO-8601"
}
```

Sempre cite evidência de até 500 caracteres ou use `null` em `NAO_ENCONTRADO`. O Orquestrador recalcula os contadores.

## Travas

- qualquer `CONTRADITO` reprova;
- taxa factual abaixo do limite do projeto reprova;
- ausência de lastro acima do limite factual do projeto reprova.

Essas travas existem para fatos, não para ritmo, comprimento ou estética.



==========================================
Estrutura de pastas:
==========================================
skills_book_3
|-- atomizador
|   |-- BOOT_ATOMIZADOR_PIPELINE.md
|   `-- SKILL_ATOMIZADOR_PIPELINE.md
|-- bible
|   |-- BIBLE_ESQUELETO_VAZIO.md
|   `-- BIBLE_TEMPLATE_PIPELINE.md
|-- capitulos_exemplo
|   `-- README.md
|-- consolidador
|   `-- SKILL_CONSOLIDADOR_PIPELINE.md
|-- controle_da_obra
|   |-- BOOT_CONTROLE_DA_OBRA.md
|   |-- README.md
|   |-- SKILL_CONTROLE_DA_OBRA.md
|   `-- TEMPLATE_CONTROLE_DA_OBRA.md
|-- editor
|   |-- BOOT_EDITOR_PIPELINE.md
|   `-- SKILL_EDITOR_PIPELINE.md
|-- escritor
|   |-- BOOT_ESCRITOR_PIPELINE.md
|   |-- DNA_REVELACAO_RESPEITOSA.md
|   `-- SKILL_ESCRITOR_PIPELINE.md
|-- estado
|   `-- ESTADO_TEMPLATE_PIPELINE.md
|-- execucao
|   |-- bible
|   |   |-- bible_da_obra.md
|   |   `-- README.md
|   |-- capitulos
|   |   `-- README.md
|   |-- controle
|   |   |-- controle_da_obra.json
|   |   `-- README.md
|   |-- estado
|   |   |-- estado_da_obra.md
|   |   `-- README.md
|   |-- CONFIG.md
|   `-- README.md
|-- generos_completos
|   |-- ficcao_literaria
|   |   |-- capitulos_calibracao
|   |   |   `-- capitulo_01
|   |   |       `-- cena_01
|   |   |           |-- _afirmacoes_para_validar.json
|   |   |           |-- _perguntas_continuidade.json
|   |   |           |-- _resultado_continuidade.json
|   |   |           |-- _resultado_march.json
|   |   |           `-- _saida_escritor.md
|   |   |-- BIBLE_EXEMPLO.md
|   |   |-- GENERO.md
|   |   `-- README.md
|   |-- podbook_mentor
|   |   |-- capitulos_calibracao
|   |   |   `-- capitulo_01
|   |   |       |-- cena_01
|   |   |       |   |-- _afirmacoes_para_validar.json
|   |   |       |   |-- _perguntas_continuidade.json
|   |   |       |   |-- _resultado_continuidade.json
|   |   |       |   |-- _resultado_march.json
|   |   |       |   `-- _saida_escritor.md
|   |   |       |-- cena_02
|   |   |       |   |-- _afirmacoes_para_validar.json
|   |   |       |   |-- _perguntas_continuidade.json
|   |   |       |   |-- _resultado_continuidade.json
|   |   |       |   |-- _resultado_march.json
|   |   |       |   `-- _saida_escritor.md
|   |   |       |-- cena_03
|   |   |       |   |-- _afirmacoes_para_validar.json
|   |   |       |   |-- _perguntas_continuidade.json
|   |   |       |   |-- _resultado_continuidade.json
|   |   |       |   |-- _resultado_march.json
|   |   |       |   `-- _saida_escritor.md
|   |   |       |-- cena_04
|   |   |       |   |-- _afirmacoes_para_validar.json
|   |   |       |   |-- _perguntas_continuidade.json
|   |   |       |   |-- _resultado_continuidade.json
|   |   |       |   |-- _resultado_march.json
|   |   |       |   `-- _saida_escritor.md
|   |   |       `-- cena_05
|   |   |           |-- _afirmacoes_para_validar.json
|   |   |           |-- _perguntas_continuidade.json
|   |   |           |-- _resultado_continuidade.json
|   |   |           |-- _resultado_march.json
|   |   |           `-- _saida_escritor.md
|   |   |-- BIBLE_EXEMPLO.md
|   |   |-- GENERO.md
|   |   `-- README.md
|   |-- tecnico_manual
|   |   |-- capitulos_calibracao
|   |   |   `-- capitulo_01
|   |   |       |-- cena_01
|   |   |       |   |-- _afirmacoes_para_validar.json
|   |   |       |   |-- _perguntas_continuidade.json
|   |   |       |   |-- _resultado_continuidade.json
|   |   |       |   |-- _resultado_march.json
|   |   |       |   `-- _saida_escritor.md
|   |   |       `-- cena_02
|   |   |           |-- _afirmacoes_para_validar.json
|   |   |           |-- _perguntas_continuidade.json
|   |   |           |-- _resultado_continuidade.json
|   |   |           |-- _resultado_march.json
|   |   |           `-- _saida_escritor.md
|   |   |-- BIBLE_EXEMPLO.md
|   |   |-- GENERO.md
|   |   `-- README.md
|   `-- README.md
|-- generos_template
|   `-- TEMPLATE_GENERO_VAZIO.md
|-- nivelamento_editorial
|   |-- GUIA_CALIBRACAO_EMPATIA.md
|   |-- PERGUNTAS_NIVELAMENTO.md
|   `-- README.md
|-- orquestrador
|   |-- BOOT_ORQUESTRADOR_PIPELINE.md
|   `-- SKILL_ORQUESTRADOR_PIPELINE.md
|-- regras_negocio
|   |-- AUTO_AUDITORIA_PIPELINE.md
|   `-- CENAS_PROIBIDAS_PIPELINE.md
|-- revisor_cego_editorial
|   |-- BOOT_REVISOR_CEGO_EDITORIAL.md
|   |-- README.md
|   |-- RUBRICA_QUALITATIVA_V3.md
|   `-- SKILL_REVISOR_CEGO_EDITORIAL.md
|-- templates_bible_worktree
|   |-- _afirmacoes_para_validar.template.json
|   |-- _log_prompt_checker.template.md
|   |-- _log_prompt_continuidade.template.md
|   |-- _manifesto_integridade.template.json
|   |-- _perguntas_continuidade.template.json
|   |-- _perguntas_validador.template.json
|   |-- _resultado_continuidade.template.json
|   |-- _resultado_march.template.json
|   |-- _resultado_revisor_cego.template.json
|   `-- _saida_final.template.md
|-- utils
|   |-- atomic.py
|   |-- checksum.py
|   |-- README.md
|   |-- reconciliar_controle.py
|   `-- vigia_integridade.py
|-- validador_continuidade
|   |-- BOOT_VALIDADOR_CONTINUIDADE_PIPELINE.md
|   `-- SKILL_VALIDADOR_CONTINUIDADE_PIPELINE.md
|-- validador_march
|   |-- BOOT_VALIDADOR_MARCH_PIPELINE.md
|   `-- SKILL_VALIDADOR_MARCH_PIPELINE.md
|-- CHANGELOG_V3.md
|-- CONFIG.md
|-- FLUXO_COMPLETO_PIPELINE.md
|-- GUIA_DE_USO.md
|-- LEIA-ME-PRIMEIRO.md
|-- README.md
`-- REGRAS_GREENFORGE_PIPELINE.md