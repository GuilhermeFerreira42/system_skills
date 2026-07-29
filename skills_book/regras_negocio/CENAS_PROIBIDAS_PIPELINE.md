# CENAS PROIBIDAS — Padrões que NÃO Podem Aparecer no Livro (PIPELINE GENÉRICO)

**Versão:** 3.0
**Aplicação:** lista de padrões ruins que o pipeline detecta e elimina, **adaptáveis ao gênero**.

---

## 🚨 Categorias de Padrões Proibidos

### 1. MATERIAL DE MARKETING (Lei 6 — violação grave)

**PROIBIDO em qualquer livro (qualquer gênero):**

| Padrão | Exemplo | Por que é proibido |
|---|---|---|
| Preço de outros cursos/produtos | "R$ 4.999 (última abertura)" | Livro não é página de venda |
| CTA de venda | "clique no botão abaixo para garantir" | Idem |
| "Garanta sua vaga" | "Garanta sua vaga no Viver de Ecommerce" | Idem |
| "Última chance" | "Última chance de se inscrever" | Idem |
| "Última abertura" | "Última abertura da turma" | Idem |
| "Oferta por tempo limitado" | "Oferta acaba meia-noite" | Idem |
| "Não perca tempo" | "Não perca tempo, inscreva-se agora" | Idem |
| "Acesse agora" | "Acesse agora o link abaixo" | Idem |
| "Inscreva-se" | "Inscreva-se no link" | Idem |
| "Matricule-se" | "Matricule-se hoje" | Idem |
| "Promoção imperdível" | "Promoção imperdível por R$ 99" | Idem |
| "Cupom de desconto para outros produtos" | "Use o cupom VIVER10 e ganhe 10% off" | Idem |

**Teste:**
```bash
grep -E "R\$\s+[0-9]|clique aqui|clique no botão|garanta|última chance|última abertura|oferta por tempo limitado|não perca tempo|acesse agora|inscreva-se|matricule-se|promoção imperdível" livro_final.md
```

Se retornar qualquer linha: REPROVADO. Limpar antes de salvar.

---

### 2. CLICHÊS DE COACH MOTIVACIONAL (apenas para gêneros NÃO-FICÇÃO/TÉCNICO)

**PROIBIDO em livros de Não-Ficção/Técnico** (PROIBIDO misturar com tom de mentor pragmático):

| Padrão | Substituir por |
|---|---|
| "Você consegue!" | [Remover ou contextualizar com caso real] |
| "Acredite no seu potencial" | [Remover] |
| "O segredo é" | "O que funciona é" + caso |
| "Mude sua vida" | "Transforme seu negócio" + número |
| "Você merece o melhor" | [Remover] |
| "Abra sua mente" | [Remover] |
| "Saia da zona de conforto" | Exemplo prático: "comece pelo marketplace" |
| "O universo conspira a favor" | [Remover] |
| "Vibre alto" | [Remover] |
| "Energia positiva" | [Remover] |
| "Lei da atração" | [Remover] |
| "Pense rico" | [Remover] |

**Para Ficção:** esses clichês são proibidos se não fazem parte do estilo do autor. Geralmente, ficção os evita naturalmente.

**Teste:** Leia a cena em voz alta. Se soa como post de coach de Instagram genérico, reescreva.

---

### 3. ESTRUTURAS DE GÊNERO ERRADO (vazamento de ficção em não-ficção, ou vice-versa)

**PROIBIDO** misturar convenções de ficção em livros de não-ficção/técnico:

| Padrão | Por que é proibido em Não-Ficção/Técnico |
|---|---|
| "Aparência física: 1.68m, cabelo castanho..." | Livro não é romance, não tem personagens fictícios |
| "Ferida nuclear" | Conceito de ficção, não cabe |
| "Mentira que acredita" | Conceito de psicologia ficcional |
| "Arco do personagem" | Conceito de ficção |
| "Maneirismos" | Idem |
| POV de personagem (1ª do aluno, ex: "Eu, aluno, sinto que...") | Em não-ficção, narrador é o mentor, não o aluno |
| Head-hopping | Conceito de ficção |
| "Voz narrativa onisciente" | Idem |

**PROIBIDO** misturar convenções de não-ficção em livros de ficção:

| Padrão | Por que é proibido em Ficção |
|---|---|
| "Resumo da cena" no fim | Quebra a imersão narrativa |
| "Seu checklist desta cena" | Tom didático, não literário |
| "Próxima cena:" como heading | Estrutura didática, não narrativa |
| "Cases de alunos" como prova | Ficção não usa cases de não-ficção |
| "Como aplicar isso na sua vida" | Quebra a 4ª parede |

**Teste:** O formato do fim da cena (Resumo+Checklist+Próxima) está definido em GENERO.md seção 4. Se a cena não segue o formato do gênero, está errado.

---

### 4. ESTRUTURAS DE METADADOS VAZADAS

**PROIBIDO** visível ao leitor no meio do texto (qualquer gênero):

| Padrão | Por que é proibido |
|---|---|
| ```json | Leitor não vê JSON |
| `"palavras_estimadas":` | Idem |
| `"bible_versao_usada":` | Idem |
| `"pov":` | Idem |
| `"foco_usuario_aplicado":` | Idem |
| `"mudanca_estado":` | Idem |
| `"objetivo_cena":` | Idem |
| `"obstaculo_principal":` | Idem |
| `"beat_emocional":` | Idem |
| Tabelas técnicas de "Metadados" no fim | Idem |

**PERMITIDO apenas:** o formato do fim definido em GENERO.md seção 4.

**Teste:**
```bash
grep -E '```json|"palavras_estimadas"|"bible_versao"|"pov":|"foco_usuario"|"mudanca_estado"|"objetivo_cena"|"obstaculo_principal"|"beat_emocional"' livro_final.md
```

Se retornar: REPROVADO. Esses campos vão em `_metadados_cena.json`, NÃO no texto visível.

---

### 5. MÁ ESCRITA (genérico — qualquer gênero)

**PROIBIDO** (prejudica a leitura, oral ou silenciosa):

| Padrão | Por que é proibido | Substituir por |
|---|---|---|
| Frases com 40+ palavras | Cansa o leitor/ouvinte | Quebrar em 2-3 frases curtas |
| Travessão formal ("—") dentro de frases | Parecer escrito, não falado (se oral) ou literário (se ficção) | Vírgula, ponto, dois pontos |
| Enumeração explicativa ("X, Y, Z. Todos eles...") | Tom professoral | "X. Y. Z. E todos eles..." |
| "Nesta aula veremos" | Forma escrita, não natural | "A gente vai ver aqui" ou "O que a gente vai fazer" |
| "Conforme vimos anteriormente" | Linguagem acadêmica | "Como a gente viu" / "Lembra lá atrás" |
| "É importante salientar" | Linguagem corporativa | Remover, mostrar com caso |
| "Cabe ressaltar" | Idem | Remover |
| "Mediante ao exposto" | Idem | Remover |
| "Destarte" | Idem | Remover |

**Para Ficção:** frases longas podem ser aceitáveis em momentos específicos (reflexão, descrição). Mas prosa explicativa de não-ficção é proibida.

**Teste:** Leia em voz alta. Se travar a respiração, é frase longa demais.

---

### 6. DADOS INVENTADOS (vazamento de validação)

**PROIBIDO** (em qualquer gênero baseado em fatos):

| Padrão inventado | Substituir por |
|---|---|
| "Exatamente 30.000 alunos" (se corpus não confirma) | "Mais de 30 mil alunos" |
| "Em 2018, eu montei [nome fictício de negócio]" (se corpus não cita o ano) | "Lá no começo" |
| "180 bilhões em 2023" (se corpus não cita) | "Mais de cem bilhões" |
| "R$ 2 milhões por mês" (se corpus não confirma) | "Mais de um milhão" |
| "Taxa de conversão de 5%" (se corpus não cita) | "Conversão boa / razoável" |

**Para Ficção:** dados inventados são aceitáveis se fazem parte da história (datas, eventos, locais fictícios).

**Teste:** Se você precisa de um número exato e o corpus não dá, reformule conservadoramente.

---

### 7. POV INCONSISTENTE

**PROIBIDO** (quebra de voz do narrador):

| Padrão | Por que é proibido | Substituir por |
|---|---|---|
| Mistura de 1ª e 2ª pessoa na mesma frase | POV do narrador é fixo | Uma pessoa por frase |
| "Você, quando era iniciante, pensava..." (3ª se referindo ao aluno) | Confuso | "Quando eu comecei, eu pensava..." (1ª) |
| "A gente viu que você precisa" (mistura) | Idem | "Você precisa" (2ª) ou "A gente viu que é preciso" (1ª plural) |
| "O mentor recomenda" (3ª se referindo a si mesmo em Podbook) | Idem | "Eu recomendo" (1ª) |
| Em Ficção, troca de POV sem aviso | Quebra imersão | Usar break de cena explícito |

**Teste:** Leia a cena em voz alta. Se em algum momento você precisa pensar "quem está falando?", reescreva.

---

## Auto-Auditoria Antes de Cada Cena Ser Marcada CONCLUÍDA

```bash
# Padrões de marketing
grep -E "R\$\s+[0-9]|clique aqui|clique no botão|garanta|última chance|última abertura|oferta por tempo limitado|não perca tempo|acesse agora|inscreva-se|matricule-se" livro_final.md

# Clichês de coach (apenas se gênero é Não-Ficção/Técnico)
grep -E "você consegue|acredite no seu potencial|o segredo é|mude sua vida|saia da zona de conforto|pense rico" livro_final.md

# Estrutura de ficção em não-ficção (apenas se gênero é Não-Ficção/Técnico)
grep -E "Aparência:|Ferida nuclear:|Mentira que acredita:|Arco do personagem:|Maneirismos:" livro_final.md

# Estrutura didática em ficção (apenas se gênero é Ficção)
grep -E "## Resumo da cena|## Seu checklist|Sua Ação Imediata|Checklist Prático" livro_final.md

# Metadados vazados
grep -E '```json|"palavras_estimadas"|"bible_versao"|"pov":|"foco_usuario"|"mudanca_estado"|"objetivo_cena"' livro_final.md

# Frases longas (heurística)
awk '{ if (NF > 40) print FILENAME":"NR": "NF" palavras" }' livro_final.md
```

**Se qualquer padrão for detectado, a cena é REPROVADA com reescrita cirúrgica apenas do trecho que falhou.**

---

## Resumo

**No livro, cabem:**
- ✅ Voz do narrador conforme GENERO.md
- ✅ Casos/personagens coerentes com a Bible
- ✅ Números do corpus (com formulação conservadora se incerto)
- ✅ Termos técnicos com analogia (se não-ficção/técnico) ou sem (se ficção)
- ✅ Formato de fim conforme GENERO.md seção 4
- ✅ Mitos/equívocos desconstruídos (se aplicável)
- ✅ Procedimentos práticos (se aplicável)

**No livro, NÃO cabem:**
- ❌ Material de marketing (preços, CTAs, "garanta sua vaga")
- ❌ Clichês de coach motivacional (se não-ficção)
- ❌ Estrutura de ficção em não-ficção (e vice-versa)
- ❌ JSON/metadados vazados no meio do texto
- ❌ Frases de 40+ palavras
- ❌ Dados inventados
- ❌ POV inconsistente

Se você tem dúvida entre "didático" e "marketing", escolha didático. SEMPRE.
