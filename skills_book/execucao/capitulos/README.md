# capitulos/ — Pasta de Cenas Produzidas

**Versão:** 3.0
**Aplicação:** aqui ficam as cenas produzidas durante a execução. Cada cena é uma pasta isolada com 8 arquivos.

---

## Estrutura por cena

```
capitulos/
└── capitulo_NN/
    └── cena_MM/
        ├── _saida_escritor.md              ← Prosa do Escritor (output bruto)
        ├── _afirmacoes_para_validar.json   ← Afirmações factuais extraídas pelo Atomizador
        ├── _perguntas_continuidade.json    ← Perguntas de continuidade extraídas pelo Orquestrador
        ├── _resultado_march.json           ← Resultado da validação MARCH (cego)
        ├── _resultado_continuidade.json    ← Resultado da validação de Continuidade (cego)
        ├── _saida_editor.md                ← Prosa após Editor (polimento, sem mudar substância)
        ├── _saida_final.md                 ← Prosa final, CONGELADA, com checksum
        └── _log_prompt_checker.md          ← Log do prompt enviado ao Validador MARCH (verificação de cegueira)
```

## O que cada arquivo é

- **`_saida_escritor.md`**: prosa bruta produzida pelo Escritor, antes de qualquer validação. Tem os placeholders de afirmações factuais que vão ser validadas.
- **`_afirmacoes_para_validar.json`**: lista de afirmações factuais extraídas pelo Atomizador, no formato `{"id": "F1", "texto": "...", "contexto": "..."}`.
- **`_perguntas_continuidade.json`**: lista de perguntas de continuidade extraídas pelo Orquestrador, no formato `{"id": "C1", "categoria": "personagem", "pergunta": "..."}`.
- **`_resultado_march.json`**: resultado da validação MARCH, no formato `{"validacoes": [{"id": "F1", "status": "CONFIRMADO", "trecho_corpus": "..."}]}`. Status geral APROVADO ou REPROVADO.
- **`_resultado_continuidade.json`**: resultado da validação de Continuidade, no mesmo formato do MARCH. Status geral APROVADO ou REPROVADO.
- **`_saida_editor.md`**: prosa após o Editor fazer polimento (clareza, ritmo, repetição). Não muda substância, só forma.
- **`_saida_final.md`**: prosa CONGELADA que vai para o livro final. Checksum calculado sobre este arquivo.
- **`_log_prompt_checker.md`**: log do prompt enviado ao Validador MARCH. Verificado pelo Orquestrador para garantir que NÃO contém conteúdo de `_saida_escritor.md` (cegueira).

## Status das cenas

Cada cena tem um status registrado no Estado:

- **PENDENTE**: ainda não foi iniciada
- **EM_ANDAMENTO**: está em alguma fase do loop
- **CONCLUÍDA**: aprovada, com checksum e round-trip OK
- **REPROVADO**: falhou validação após 3 retries, marcada como não-pronta
- **PÓS-CIRÚRGICA**: cena REPROVADA que foi refeita com reescrita cirúrgica após as 3 tentativas

## O que vai para o livro final

O Consolidador pega todos os `_saida_final.md` em ordem (capitulo_01/cena_01, capitulo_01/cena_02, ..., capitulo_02/cena_01, ...) e concatena com front matter adaptado ao gênero. Esse é o livro final.
