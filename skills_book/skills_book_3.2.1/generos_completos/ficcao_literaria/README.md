# ficcao_literaria — Perfil de Gênero Completo

**Versão:** 1.0
**Aplicação:** este é o perfil de gênero para romances, contos, narrativas literárias com personagens e arcos.

---

## Quando usar este gênero

Use este perfil quando:
- A obra é ficção (romance, conto, novela)
- Tem personagens fictícios com arcos narrativos
- A narrativa é construída por POV, conflitos, revelações
- O público é leitor de ficção literária, não aluno de curso
- A prosa é literária, com subtexto, sensorialidade, ritmo próprio

**Exemplos de livros que se encaixam:**
- Romance contemporâneo ("A Casa do Cais", exemplo deste perfil)
- Romance histórico
- Ficção científica
- Fantasy
- Thriller/Literatura policial
- Conto literário (para coletâneas)
- Graphic novel com prosa

---

## O que tem aqui

- `GENERO.md` — Arquivo principal do gênero (preenchido)
- `BIBLE_EXEMPLO.md` — Bible exemplo com "A Casa do Cais" (romance genérico)
- `capitulos_calibracao/capitulo_01/` — Cap 1 exemplo, 1 cena (calibração mínima; Ficção não precisa de muitas)

---

## Como usar

1. Copie `GENERO.md` para `execucao/GENERO.md` do seu projeto
2. Use `BIBLE_EXEMPLO.md` como referência de estrutura para criar a Bible do SEU livro
3. Olhe `capitulos_calibracao/capitulo_01/` para calibrar tom, formato e sensorialidade
4. Configure o `CONFIG.md` com título, corpus (se houver — para Ficção pura, pode ser vazio), foco
5. Passe para a IA produtora

---

## Particularidades deste gênero

**Atomizador:** pode produzir array vazio se a obra for Ficção pura sem corpus factual.

**Validador MARCH:** pode ser pulado ou rodar mas retornar "sem afirmações extraídas" se a obra for Ficção pura.

**Validador de Continuidade:** OBRIGATÓRIO, com categorias adaptadas:
- PERSONAGEM_ACAO (personagem age de forma coerente)
- PERSONAGEM_ESTADO (estado emocional/localização coerente)
- FIO_NARRATIVO_SETUP/PAYOFF (arcos de personagem)
- TIMELINE_CRONOLOGIA
- VOZ_NARRATIVA (POV consistente)

**Editor:** Foco em Show (70%), subtexto, ancoragem sensorial. NUNCA adiciona didatismo.

**Formato do fim da cena:** SEM resumo, sem checklist, sem "próxima cena" como heading. A cena termina narrativamente.

---

## Calibração disponível

O `capitulos_calibracao/capitulo_01/` contém **1 cena** de exemplo, mostrando como a prosa literária termina — sem Resumo, sem Checklist, sem heading visível. Serve para a IA produtora entender o formato.

