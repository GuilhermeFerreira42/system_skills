# SKILL DO CONSOLIDADOR DE LIVRO

**Versao:** 1.0
**Funcao:** Juntar todos os capitulos/cenas aprovados em um livro final coeso (Markdown + opcional EPUB/PDF).

---

# PSEUDOCODIGO OPERACIONAL

```
// Importacao das constantes centralizadas (ver utils/constantes.py)
DE utils.constantes IMPORTAR (
    SAIDA_EDITOR_ARQ,
    SAIDA_ESCRITOR_ARQ,
    SAIDA_FINAL_ARQ,
    METADADOS_CENA_ARQ,
    PASTA_CAPITULOS,
    STATUS_CENA_CONCLUIDO,
    CAPITULO_PREFIXO_PASTA,
    CAPITULO_NUMERO_DIGITOS
)

FUNCAO consolidar_livro(plano, estado, output_path):
    // 1. Ler todos os capitulos/cenas CONCLUIDOS em ordem
    cenas_ordenadas = ORDENAR_POR_ORDEM_NARRATIVA(plano.cenas)
    // filtro: so status == STATUS_CENA_CONCLUIDO

    partes = []

    PARA CADA cena EM cenas_ordenadas:
        worktree = f"{PASTA_CAPITULOS}/{CAPITULO_PREFIXO_PASTA}{str(cena.capitulo).zfill(CAPITULO_NUMERO_DIGITOS)}/"

        // Ler saida final (editor se houver, senao escritor)
        SE ARQUIVO_EXISTE(f"{worktree}/{SAIDA_EDITOR_ARQ}"):
            prosa = LER(f"{worktree}/{SAIDA_EDITOR_ARQ}")
        SENAO:
            prosa = LER(f"{worktree}/{SAIDA_ESCRITOR_ARQ}")

        metadados = LER(f"{worktree}/{METADADOS_CENA_ARQ}")

        // Extrair so a prosa (remover metadados do final do arquivo)
        prosa_limpa = EXTRAIR_PROSA(prosa)

        // Adicionar marcadores de capitulo/cena se necessario
        SE cena.eh_primeira_do_capitulo:
            partes.ADICIONAR(f"# Capitulo {cena.capitulo}: {cena.titulo_capitulo}\n")

        // Opcional: marcador de cena (###) se genero usa
        SE genero.usar_marcador_cena:
            partes.ADICIONAR(f"### {cena.titulo}\n")

        partes.ADICIONAR(prosa_limpa)
        partes.ADICIONAR("\n\n---\n\n")  // Separador de cena

    // 2. Juntar tudo
    livro_completo = JUNTAR(partes)

    // 3. Adicionar front matter (metadados do livro)
    front_matter = GERAR_FRONT_MATTER(estado, plano)
    livro_final = front_matter + "\n\n" + livro_completo

    // 4. Salvar Markdown final
    SALVAR(output_path, livro_final)

    // 5. Opcional: Gerar EPUB
    SE estado.gerar_epub:
        GERAR_EPUB(livro_final, f"{output_path}.epub", estado.metadados_epub)

    // 6. Opcional: Gerar PDF
    SE estado.gerar_pdf:
        GERAR_PDF(livro_final, f"{output_path}.pdf")

    RETORNAR {"status": "CONCLUIDO", "arquivo_md": output_path, "arquivo_epub": ..., "arquivo_pdf": ...}
```

---

# 1. Entrada

- `plano`: Plano de cenas do `estado_da_obra.md` (so as CONCLUIDAS)
- `estado`: Estado da obra completo
- `output_path`: `"livro_final.md"`

---

# 2. Ordenacao Narrativa

O plano ja define a ordem. O consolidador so segue:
1. Capitulo 1 -> Cena 1, 2, 3...
2. Capitulo 2 -> Cena 1, 2...
...

---

# 3. Front Matter (YAML no topo do MD)

```yaml
---
title: "[TITULO DO LIVRO]"
subtitle: "[SUBTITULO]"
author: "[AUTOR]"
genre: "[GENERO]"
subgenre: "[SUBGENERO]"
language: "pt-BR"
created: "2026-07-27"
version: "1.0"
word_count: 87432
chapter_count: 12
scene_count: 47
status: "CONCLUIDO"
foco_usuario: "[Foco original do usuario]"
bible_version: "v4.1"
validacao_march: "TODAS_APROVADAS"
validacao_continuidade: "TODAS_APROVADAS"
---
```

---

# 4. Estrutura do Markdown Final

```markdown
---
title: "O Homem Sabotado"
subtitle: "Como o mundo moderno destroi a masculinidade e como recuperar o controle"
author: "Usuario + IA"
genre: "Nao-Ficcao"
subgenre: "Ciencia Popular / Saude Masculina"
language: "pt-BR"
created: "2026-07-27"
version: "1.0"
word_count: 87432
chapter_count: 12
scene_count: 47
status: "CONCLUIDO"
foco_usuario: "Foque nos estudos sobre plasticos e na solucao pratica. Evite jargao medico excessivo."
bible_version: "v4.1"
validacao_march: "TODAS_APROVADAS"
validacao_continuidade: "TODAS_APROVADAS"
---

# Prefacio

[Prosa do prefacio se houver]

---

# Capitulo 1: O Inimigo Invisivel

### Cena 1: O Despertar

[Prosa da cena 1...]

---

### Cena 2: A Descoberta

[Prosa da cena 2...]

---

# Capitulo 2: O Plastico em Nos

### Cena 1: A Cozinha

[Prosa...]

...

# Epilogo

[Prosa...]

---

## Agradecimentos

## Referencias / Bibliografia

## Sobre o Autor
```

---

# 5. Geracao EPUB (Opcional)

Usar biblioteca padrão (ex: `pandoc`, `ebooklib`, `calibre`).
Incluir:
- Capa (gerada ou placeholder)
- Indice (TOC) automatico baseado em `# Capitulo` / `### Cena`
- Metadados do front matter
- CSS basico para leitura agradavel

---

# 6. Geracao PDF (Opcional)

Via `pandoc` + LaTeX ou `weasyprint`.
Opcoes: margens, fonte, tamanho, numeracao de paginas.

---

# 7. Validacao de Fronteira (OBRIGATORIA)

Antes de salvar, o Consolidador DEVE verificar:

```python
def validar_fronteira(livro_final, plano, estado):
    // 1. Contar palavras total vs soma das cenas
    total_cenas = sum(c.palavras for c in estado.cenas_concluidas)
    total_livro = contar_palavras(livro_final)
    // Tolerancia 5% (front matter, separadores, titulos)
    assert abs(total_livro - total_cenas) / total_cenas < 0.05
    
    // 2. Todas as cenas CONCLUIDAS estao presentes
    cenas_no_livro = extrair_cenas_do_md(livro_final)
    assert set(cenas_no_livro) == set(estado.cenas_concluidas.ids)
    
    // 3. Ordem narrativa preservada
    assert ordem(cenas_no_livro) == ordem(plano.cenas_concluidas)
    
    // 4. Nenhuma cena PENDENTE/REPROVADA inclusa
    assert all(c.status == "CONCLUIDO" for c in cenas_incluidas)
    
    // 5. Checksums das cenas conferem
    PARA CADA cena EM cenas_incluidas:
        prosa_original = LER(f"{PASTA_CAPITULOS}/{CAPITULO_PREFIXO_PASTA}{str(cena.cap).zfill(CAPITULO_NUMERO_DIGITOS)}/{SAIDA_FINAL_ARQ}")
        prosa_no_livro = EXTRAIR_CENA(livro_final, cena.id)
        assert CALCULAR_CHECKSUM(prosa_original) == CALCULAR_CHECKSUM(prosa_no_livro)
```

SE qualquer validacao falhar -> PARAR("Validacao de fronteira falhou. Livro nao gerado.")

---

# 8. Regra de Ouro

**O Consolidador NAO edita prosa.** So junta, formata, valida integridade.
Se algo esta errado -> volta para o Orquestrador -> Escritor/Editor.