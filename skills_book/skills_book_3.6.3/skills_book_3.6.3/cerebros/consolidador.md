# CÉREBRO — Consolidador (Skills Book v3.6.3)


---

> **Este arquivo é a fonte única de verdade deste papel.**
> Ele reúne, **verbatim e sem alteração de lógica**, o conteúdo original das skills
> abaixo. Os arquivos originais continuam intactos nos seus caminhos de origem —
> este é um espelho de leitura para o subagente, não uma substituição.
>
> Se você precisar mudar o comportamento deste papel, mude aqui **e** no original,
> ou regenere este arquivo com `gerar_subagentes.py`.
>
> **Fontes concatenadas, nesta ordem:**
> 1. `consolidador/SKILL_CONSOLIDADOR_PIPELINE.md`

---

<!-- ===== INÍCIO: consolidador/SKILL_CONSOLIDADOR_PIPELINE.md ===== -->

## ⟦Fonte original: `consolidador/SKILL_CONSOLIDADOR_PIPELINE.md`⟧

# Skill do Consolidador — Skill 3

## Missão

Juntar os artefatos finais aprovados em um livro, sem reescrever as cenas e sem introduzir conteúdo novo.

## Entradas

- plano e Estado;
- Bible;
- Controle da Obra;
- `_saida_final.md` de cada cena `CONCLUIDO`;
- gênero ou perfil apenas para elementos de apresentação autorizados.

## Validação de fronteira

Antes de salvar o livro:

1. liste cenas concluídas no Estado;
2. liste cenas presentes no livro;
3. compare IDs e ordem;
4. confirme um único bloco por cena;
5. confira checksum de cada cena contra o Controle;
6. confirme que nenhuma cena bloqueada está sendo apresentada como concluída;
7. execute auditoria de marketing e metadados vazados.

Não use tolerância de contagem de palavras como prova de integridade. O checksum e a correspondência estrutural são a prova.

## Saída

- `livro_final.md` somente quando todos os gates fecharem;
- `livro_parcial.md` somente se o CONFIG permitir, com uma seção inicial de pendências clara e sem fingir conclusão;
- relatório de fronteira.

O Consolidador não corrige uma cena. Se uma cena estiver errada, devolva ao Orquestrador com seu ID e motivo.

<!-- ===== FIM: consolidador/SKILL_CONSOLIDADOR_PIPELINE.md ===== -->
