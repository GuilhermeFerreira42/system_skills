# AUTO-AUDITORIA (PIPELINE GENÉRICO) — Testes Automáticos

**Versão:** 3.0
**Aplicação:** testes que o Consolidador (e opcionalmente o Orquestrador) executa para garantir que o livro final não viola nenhuma regra.

---

## Teste 1 — Material de Marketing (Lei 6)

```bash
grep -iE "R\$\s+[0-9]{1,}|clique aqui|clique no botão|garanta sua vaga|última chance|última abertura|oferta por tempo limitado|não perca tempo|acesse agora|inscreva-se|matricule-se|promoção imperdível" livro_final.md
```

**Se retornar qualquer linha: REPROVADO.**

---

## Teste 2 — Clichês de Coach (apenas se gênero é Não-Ficção/Técnico)

```bash
# Verificar se o GENERO.md é de Não-Ficção ou Técnico
# O GENERO.md tem um campo **Tipo:** que define isso. Tipos não-ficção:
# PODBOOK, NAO_FICCAO, NAO_FICÇÃO, TECNICO, TÉCNICO, MANUAL, DIDATICO, DIDÁTICO
# (case-insensitive)
grep -iE "^\*\*Tipo:\*\*.*(podbook|não_ficção|nao_ficcao|tecnico|técnico|manual|didatico|didático)" GENERO.md

# Se sim, rodar:
grep -iE "você consegue!|acredite no seu potencial|o segredo é|mude sua vida|saia da zona de conforto|pense rico|vibre alto|lei da atração" livro_final.md
```

**Se retornar: REPROVADO (apenas se gênero é Não-Ficção/Técnico).**

---

## Teste 3 — Estrutura de Gênero Errado

**Se gênero é Não-Ficção ou Técnico:**

```bash
# Verificar se há estrutura de ficção vazada
grep -iE "Aparência:|Ferida nuclear:|Mentira que acredita:|Arco do personagem:|Maneirismos:|head-hopping" livro_final.md
```

**Se retornar: REPROVADO.**

**Se gênero é Ficção:**

```bash
# Verificar se há estrutura didática vazada
grep -iE "## Resumo da cena|## Seu checklist|Checklist Prático|Sua Ação Imediata|Aprenda a aplicar" livro_final.md
```

**Se retornar: REPROVADO.**

---

## Teste 4 — Metadados Vazados

```bash
grep -E '```json|"palavras_estimadas"|"bible_versao"|"pov":|"foco_usuario"|"mudanca_estado"|"objetivo_cena"|"obstaculo_principal"|"beat_emocional"|"genero_usado"' livro_final.md
```

**Se retornar: REPROVADO. Metadados vão em `_metadados_cena.json`, não no texto visível.**

---

## Teste 5 — Frases Longas (heurística)

```bash
awk '{ if (NF > 40) print FILENAME":"NR": "NF" palavras: "$0 }' livro_final.md | head -20
```

**Se retornar muitas linhas (mais de 10% das linhas do livro):** REPROVADO. Reescrever com frases mais curtas.

**NOTA:** Para Ficção, frases longas podem ser aceitáveis em momentos específicos (reflexão, descrição). Use com bom senso.

---

## Teste 6 — POV Inconsistente

```python
# Pseudocódigo para verificar consistência de POV
def verificar_pov(livro_final, genero):
    pessoa_esperada = genero.pessoa_padrao  # "1a", "2a", "3a", etc.
    
    # Heurística: contar pronomes por parágrafo
    paragrafos = extrair_paragrafos(livro_final)
    inconsistencias = []
    for i, paragrafo in enumerate(paragrafos):
        pronomes_1a = count_pronomes_1a(paragrafo)  # eu, meu, minha
        pronomes_2a = count_pronomes_2a(paragrafo)  # você, teu, sua
        pronomes_3a = count_pronomes_3a(paragrafo)  # ele, ela
        
        # Se misturou 1ª e 2ª na mesma frase (heurística simples)
        if pronomes_1a > 0 and pronomes_2a > 0:
            inconsistencias.append(f"Parágrafo {i}: mistura 1ª e 2ª pessoa")
    
    return inconsistencias
```

**Se retornar inconsistências relevantes: REPROVADO.**

---

## Teste 7 — Checksum das Cenas

```python
def verificar_checksums(livro_final, plano, execucao_dir):
    for cena in plano.cenas_concluidas:
        worktree = f"{execucao_dir}/capitulos/capitulo_{cena.capitulo:02d}/cena_{cena.cena:02d}/"
        prosa_original = ler(f"{worktree}/_saida_final.md")
        prosa_no_livro = extrair_cena(livro_final, cena.id)
        
        if calcular_sha256(prosa_original)[:8] != calcular_sha256(prosa_no_livro)[:8]:
            return f"Checksum mismatch na cena {cena.id}"
    
    return None
```

**Se retornar erro: REPROVADO.**

---

## Teste 8 — Contagem de Palavras

```python
def verificar_contagem(livro_final, plano, tolerancia=0.05):
    total_cenas = sum(c.palavras_estimadas for c in plano.cenas_concluidas)
    total_livro = contar_palavras(livro_final)
    
    if abs(total_livro - total_cenas) / total_cenas > tolerancia:
        return f"Contagem inconsistente: livro={total_livro}, cenas={total_cenas}"
    
    return None
```

**Se retornar erro: REPROVADO.**

---

## Teste 9 — Ordem das Cenas

```python
def verificar_ordem(livro_final, plano):
    cenas_no_livro = extrair_cenas_do_md(livro_final)
    ids_no_livro = [c.id for c in cenas_no_livro]
    ids_esperado = [c.id for c in plano.cenas_concluidas]
    
    if ids_no_livro != ids_esperado:
        return f"Ordem divergente. Esperado: {ids_esperado}, Obtido: {ids_no_livro}"
    
    return None
```

**Se retornar erro: REPROVADO.**

---

## Teste 10 — Cenas Pendentes no Livro

```python
def verificar_cenas_concluidas(livro_final, plano):
    ids_no_livro = set(c.id for c in extrair_cenas_do_md(livro_final))
    ids_concluidas = set(c.id for c in plano.cenas_concluidas)
    
    if ids_no_livro != ids_concluidas:
        return f"Cenas divergentes. Faltando: {ids_concluidas - ids_no_livro}"
    
    return None
```

**Se retornar erro: REPROVADO.**

---

## Resumo dos Testes

| # | Teste | Quando rodar | Se falhar |
|---|---|---|---|
| 1 | Material de marketing | Consolidador | REPROVADO, limpar |
| 2 | Clichês de coach | Consolidador (se Não-Ficção) | REPROVADO, reescrever |
| 3 | Estrutura de gênero errado | Consolidador | REPROVADO, reescrever |
| 4 | Metadados vazados | Consolidador | REPROVADO, reescrever |
| 5 | Frases longas | Consolidador | REPROVADO, quebrar |
| 6 | POV inconsistente | Consolidador (manual ou heurístico) | REPROVADO, reescrever |
| 7 | Checksum das cenas | Consolidador | REPROVADO, refazer cena |
| 8 | Contagem de palavras | Consolidador | REPROVADO, investigar |
| 9 | Ordem das cenas | Consolidador | REPROVADO, refazer consolidação |
| 10 | Cenas pendentes no livro | Consolidador | REPROVADO, refazer cena |

**Todos os testes devem passar para o livro ser considerado CONCLUÍDO.**
