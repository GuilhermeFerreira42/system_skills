# Fluxo completo da Skill 3

## Visão geral

```text
BOOT
  → nivelamento editorial
  → Bible + Estado + mapa do corpus
  → planejar cenas

PARA CADA CENA
  → worktree isolada
  → Escritor
  → Editor ou cópia controlada
  → artefato candidato
  → Atomizador + perguntas de Continuidade
  → MARCH e Continuidade cegos
  → Revisor Cego holístico
  → candidato aprovado
  → cópia final + checksum
  → Vigia físico
  → Bible + Estado + Controle atômicos

FIM
  → reconciliação final
  → validação de fronteira
  → auditoria de marketing
  → livro final ou relatório bloqueado
```

## Fase 0 — Boot

1. Leia `CONFIG.md`, o corpus e os checkpoints existentes.
2. Execute o nivelamento editorial; guarde as respostas e a fonte (`usuario`, `padrao_confirmado` ou `perfil_existente`).
3. Gere ou atualize a Bible com o contrato de voz qualitativo, conceitos, fontes, personagens, fios e mapa de módulos.
4. Gere ou atualize o Estado e o Controle da Obra atomically.
5. Faça reconciliação inicial. Drift encontrado é sinalizado, nunca apagado.

## Fase 1 — Preparar uma cena

Crie:

```text
execucao/capitulos/capitulo_NN/cena_MM/
```

Salve o status `ESCREVENDO` antes da invocação do Escritor. Os artefatos esperados são:

```text
_saida_escritor.md
_metadados_cena.json
_saida_editor.md                 # quando Editor está ativado
_saida_candidato.md              # última mutação antes das validações
_afirmacoes_para_validar.json
_perguntas_validador.json
_perguntas_continuidade.json
_resultado_march.json
_resultado_continuidade.json
_resultado_revisor_cego.json
_saida_final.md
_manifesto_integridade.json
_log_prompt_checker.md
_log_prompt_continuidade.md
_log_vigia.md
```

## Fase 2 — Escritor

O Escritor recebe o objetivo da cena, o contexto anterior, a Bible relevante, o perfil editorial e o foco do usuário.

Ele escreve prosa. Não calcula ritmo, não gera JSON de validação, não lê resultados de validadores e não tenta satisfazer contadores estéticos.

## Fase 3 — Editor e candidato

O Editor é a última etapa que pode alterar a prosa antes da validação. Ele pode melhorar clareza, voz, transições, ancoragem e ritmo natural, mas não pode inventar fatos, trocar o objetivo da cena ou apagar uma restrição da Bible.

Se o Editor estiver desligado, copie `_saida_escritor.md` para `_saida_candidato.md` sem alteração.

Calcule o checksum do candidato. Esse checksum acompanha os pacotes de perguntas e os resultados, sem revelar a prosa aos validadores cegos.

## Fase 4 — Perguntas e validação

O Orquestrador lê o candidato e cria:

- Atomizador: afirmações factuais + perguntas MARCH.
- Continuidade: perguntas sobre voz, conceitos, cronologia, fios e objetivo.

MARCH recebe apenas seu pacote de perguntas, o corpus permitido e o identificador de linhagem. Continuidade recebe apenas suas perguntas, Bible, Estado e identificador de linhagem. Nenhum dos dois recebe o texto.

MARCH e Continuidade podem rodar em paralelo. O Orquestrador recalcula os agregados do MARCH a partir de `resultados[]`; não confia no resumo devolvido pelo agente.

## Fase 5 — Revisor Cego Editorial

O Revisor recebe apenas `_saida_candidato.md` e uma rubrica qualitativa. Ele verifica:

- entendimento na primeira leitura;
- coerência da progressão;
- variação natural de densidade;
- respiros e transições;
- voz e tom;
- abertura, desenvolvimento e fecho;
- ausência de metadados, marketing e clichês incompatíveis.

Ele não mede palavras, não conta frases e não usa thresholds estéticos. Ele pode aprovar ou devolver uma orientação cirúrgica.

## Fase 6 — Reprovação e retry

Qualquer alteração no Escritor, Editor ou candidato invalida os resultados derivados daquela versão.

```text
falha factual/coerência/clareza
  → registrar status e motivo
  → retry += 1
  → Escritor recebe feedback cirúrgico
  → Editor
  → novo candidato
  → Atomizador + perguntas
  → MARCH + Continuidade + Revisor
```

Não pule diretamente para o checksum de uma versão nova.

Após três retries sem aprovação:

```text
BLOQUEADA_REVISAO_HUMANA
```

A obra pode continuar produzindo outras cenas, mas a consolidação final não pode ser declarada concluída.

## Fase 7 — Fechamento físico

Somente depois de todos os validadores aprovarem:

1. Copie o candidato para `_saida_final.md` atomicamente.
2. Calcule o checksum do candidato e do final.
3. Escreva `_manifesto_integridade.json` com `status_fisico: FECHAMENTO_EM_VERIFICACAO` e `vigia: PENDENTE`.
4. Execute `utils/vigia_integridade.py`.
5. Se o Vigia retornar exit 0, atualize o manifesto para `status_fisico: APROVADO` e `vigia: APROVADO` atomically.
6. Atualize Bible, Estado e Controle da Obra atomically.
7. Registre `CONCLUIDO` e a próxima cena.
8. Faça round-trip: releia o arquivo final e compare o checksum.

O Vigia não julga literatura. Ele apenas verifica que os arquivos e as linhagens fecham.

## Fase 8 — Drift manual

No boot ou antes de avançar, compare os checksums registrados com o disco.

Se houver divergência:

```text
MODIFICADO_MANUALMENTE
REVALIDACAO_NECESSARIA
```

Preserve a edição humana. Não reescreva automaticamente e não apague o histórico.

## Fase 9 — Consolidação

O Consolidador inclui apenas cenas com pacote fechado. Ele verifica:

- ordem das cenas;
- presença de todas as cenas concluídas;
- ausência de duplicatas;
- correspondência dos checksums;
- ausência de material de marketing;
- inexistência de cenas bloqueadas quando o status final for `CONCLUIDO`.

Se alguma cena estiver pendente, gere `livro_parcial.md` com aviso explícito ou pare a consolidação, conforme o CONFIG.

