# Guia de uso — Skill 3

## 1. Criar um projeto

```bash
cp -r skill3 meu_livro
cd meu_livro
cp CONFIG.md execucao/CONFIG.md
```

Coloque as fontes em `execucao/corpus/` e preencha o título, público e foco do usuário.

## 2. Iniciar o boot

O Orquestrador pergunta quatro preferências:

1. forma de abertura;
2. densidade de explicação;
3. uso de analogias e exemplos;
4. voz do autor.

Responda A, B ou C. Se já houver um perfil salvo, ele será preservado até que o usuário peça um novo nivelamento.

## 3. Produzir uma cena

O ciclo é:

```text
Escritor → Editor → Candidato → Atomizador/Continuidade →
MARCH/Continuidade → Revisor Cego → Vigia → Checkpoint
```

O escritor nunca precisa calcular métricas de ritmo. O revisor decide se a prosa respira de modo natural.

## 4. Auditar uma cena localmente

A partir da raiz da Skill 3:

```bash
python3 utils/checksum.py calcular caminho/para/_saida_candidato.md
python3 utils/vigia_integridade.py caminho/para/a/cena
```

O segundo comando retorna exit 0 somente quando a linhagem e os arquivos obrigatórios fecham.

## 5. Reconciliar o projeto

```bash
python3 utils/reconciliar_controle.py caminho/para/o/projeto
```

A reconciliação não corrige arquivos. Ela produz um relatório de divergências e orienta a transição para `REVALIDACAO_NECESSARIA`.

## 6. Interpretar falhas

| Status | Significado | Ação |
|---|---|---|
| `REPROVADO_MARCH` | Fato sem lastro ou contradito | reescrita cirúrgica e revalidação |
| `REPROVADO_CONTINUIDADE` | Quebra da Bible/Estado | corrigir a cena e revalidar |
| `REPROVADO_REVISOR` | Problema holístico de comunicação | revisão cirúrgica |
| `MODIFICADO_MANUALMENTE` | Bytes mudaram fora do pipeline | preservar, revalidar |
| `BLOQUEADA_REVISAO_HUMANA` | Três retries sem aprovação | intervenção humana |
| `CONCLUIDO` | Pacote físico fechado | avançar |

## 7. O que não fazer

Não copie resultados de uma tentativa anterior para uma nova versão. Não rode o Vigia para aprovar estilo. Não use o checksum como motivo para apagar uma edição humana. Não declare livro concluído com cenas bloqueadas.


==========================================
Conteúdo de LEIA-ME-PRIMEIRO.md (caminho: skills_book_3/LEIA-ME-PRIMEIRO.md) [enc: utf-8]:

==========================================
Conteúdo de LEIA-ME-PRIMEIRO.md (caminho: skills_book_3/LEIA-ME-PRIMEIRO.md) [enc: utf-8]: