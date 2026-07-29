# generos_completos — Repositório de Gêneros Prontos

**Versão:** 3.0
**Aplicação:** cada subpasta é um perfil de gênero completo, com GENERO.md, BIBLE_EXEMPLO.md, e capítulos de calibração.

---

## Como usar

Quando o usuário quiser produzir um livro, ele escolhe um gênero desta pasta e copia o `GENERO.md` para `execucao/GENERO.md`. O pipeline usa esse gênero para configurar todas as skills.

---

## Gêneros disponíveis (Camada 2 — versão inicial)

| Gênero | Pasta | Para quê serve |
|---|---|---|
| **Podbook de Mentor** | `podbook_mentor/` | Livros baseados em transcrições de aulas, com voz de mentor experiente (ex: Ecommerce do Zero, curso de investimentos, etc.) |
| **Ficção Literária** | `ficcao_literaria/` | Romances, contos, narrativas literárias com personagens e arcos |
| **Técnico Manual** | `tecnico_manual/` | Manuais how-to, documentação técnica, livros didáticos de programação, etc. |

---

## Sobre as cenas de calibração

As cenas em `capitulos_calibracao/` são **exemplos intermediários do pipeline**. Foram geradas até a fase de validação (Escritor → Atomizador → MARCH → Continuidade), e é por isso que:

- ✅ Têm `_saida_escritor.md` (com metadados JSON no fim — isso é o output bruto do Escritor)
- ✅ Têm `_afirmacoes_para_validar.json`, `_perguntas_continuidade.json`
- ✅ Têm `_resultado_march.json`, `_resultado_continuidade.json`
- ❌ **NÃO** têm `_saida_editor.md` (o Editor ainda não rodou)
- ❌ **NÃO** têm `_saida_final.md` (a versão final só existe após o Editor)
- ❌ **NÃO** têm `_log_prompt_checker.md` (esse log é gerado pelo Orquestrador durante a execução, não é parte do exemplo)

**Como usar para entender o tom do gênero:** leia o `_saida_escritor.md` e ignore o bloco `### Metadados da Cena` no fim. O pipeline real remove esse bloco na fase do Editor.

---

## Como adicionar um novo gênero

1. Copie `generos_template/TEMPLATE_GENERO_VAZIO.md` para `generos_completos/[nome_do_genero]/GENERO.md`
2. Preencha TODAS as seções (nenhuma pode ter "[definir]")
3. Crie uma Bible exemplo usando `bible/BIBLE_ESQUELETO_VAZIO.md` como base, salve em `generos_completos/[nome_do_genero]/BIBLE_EXEMPLO.md`
4. Produza 1-2 capítulos de calibração usando a IA produtora nesse gênero
5. Valide que o pipeline funciona
6. Documente o gênero no README desta pasta

---

## Estrutura de cada gênero

```
generos_completos/[perfil]/
├── GENERO.md                              ← Arquivo principal (preenchido)
├── BIBLE_EXEMPLO.md                      ← Bible exemplo preenchida
├── README.md                              ← Notas específicas do gênero
└── capitulos_calibracao/
    └── capitulo_01/
        ├── cena_01/
        │   ├── _saida_escritor.md         ← Prosa do Escritor (com metadados — ignorar)
        │   ├── _afirmacoes_para_validar.json
        │   ├── _resultado_march.json
        │   ├── _resultado_continuidade.json
        │   ├── _perguntas_continuidade.json
        │   └── (sem _saida_editor.md e _saida_final.md — ver acima)
        └── cena_02/
            └── (mesma estrutura)
```

---

## Cobertura dos 3 perfis incluídos

### Podbook de Mentor (Não-Ficção baseada em transcrições)
- Voz: 1ª do mentor como base, 2ª pontual
- Extensão: 1.000-4.000 palavras por cena
- Formato do fim: ## Resumo + ## Seu checklist + **Próxima cena:**
- Validação MARCH obrigatória (fatos do corpus)
- Validação de Continuidade obrigatória (coerência interna)
- Cenas de calibração: 5 (3 do Cap 1 de Ecommerce do Zero + 1 REPROVADA + 1 PÓS-CIRÚRGICA)

### Ficção Literária
- Voz: 3ª limitada ou 1ª do personagem
- Extensão: 1.500-5.000 palavras por cena (sem limite rígido)
- Formato do fim: cena termina naturalmente, sem Resumo/Checklist
- Validação MARCH opcional (só para referências factuais)
- Validação de Continuidade obrigatória (personagens, arcos, timeline)
- Cenas de calibração: 1 (Helena chega à casa da avó, A Casa do Cais)

### Técnico Manual
- Voz: 2ª pessoa "você" ou 3ª autoral
- Extensão: 500-2.000 palavras por cena
- Formato do fim: ## Resumo + checklist de passos
- Validação MARCH obrigatória (fatos técnicos)
- Validação de Continuidade obrigatória (progressão lógica, pré-requisitos)
- Cenas de calibração: 2 (1 REPROVADA sobre criador/ano do Python + 1 APROVADA sobre instalação)
