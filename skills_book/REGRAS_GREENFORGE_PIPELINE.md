# REGRAS GREENFORGE PARA PIPELINE GENÉRICO — As 6 Leis Duras

**Versão:** 3.0
**Aplicação:** OBRIGATÓRIA. Qualquer violação reprova a cena ou o livro inteiro.

---

## 🚨 LEITURA OBRIGATÓRIA ANTES DE PRODUZIR QUALQUER CENA

Estas são as 6 leis que sustentam todo o pipeline. Se você quebrá-las, o livro não presta. Não importa se a prosa está bonita, se o tom está certo, se o usuário gostou. As leis estão acima de tudo. Estão acima do gênero, acima do usuário, acima de você. São as regras que separam este pipeline de qualquer tentativa de "fazer tudo de uma vez".

---

## Lei 1 — CENA POR CENA, SEMPRE

**Uma cena = uma unidade de produção isolada.** Nunca produza duas cenas em uma mesma chamada. Nunca produza o livro inteiro em uma mesma chamada. O loop de produção é:

```
PARA CADA cena EM plano.cenas:
    Executar loop completo (Escritor → Atomizador → MARCH → Continuidade → Editor → Atomicidade)
    Confirmar CONCLUÍDA antes de avançar
```

**Consequência da violação:** livro monolítico, sem granularidade, sem validação, sem rastreabilidade. É o que produz o "livro ruim" que o usuário comparou.

**Por que existe:** cérebro de modelo de linguagem tem janela limitada. Sem isolamento por cena, em torno da 20ª-30ª cena, a coerência cai, a prosa se repete, fatos se contradizem. Cena por cena mantém o padrão de qualidade constante.

---

## Lei 2 — VALIDAÇÃO DUPLA CEGA, SEMPRE

**Toda cena passa por dois validadores, ambos cegos para a prosa do Escritor:**

- **Validador MARCH** recebe só: perguntas extraídas pelo Atomizador + corpus bruto. Nunca vê `_saida_escritor.md`. Verifica se cada afirmação factual está no corpus.
- **Validador de Continuidade** recebe só: perguntas de continuidade extraídas pelo Orquestrador + Bible da Obra + Estado da Obra (cenas anteriores). Nunca vê `_saida_escritor.md`. Verifica se a cena é coerente com a história, personagens, conceitos, timeline, voz.

**Cegueira é inviolável.** Antes de invocar o Validador MARCH, o Orquestrador salva o prompt que será enviado em `_log_prompt_checker.md`. Depois, o Orquestrador verifica se esse log **NÃO contém** conteúdo de `_saida_escritor.md`. Se contiver, **REPROVADO por violação de cegueira**.

**Travas duras do Validador MARCH:**
- 1+ afirmação `CONTRADITO` → status geral = REPROVADO
- Taxa de `CONFIRMADO` < 80% → REPROVADO
- Taxa de `NAO_ENCONTRADO` > 30% → REPROVADO

**Travas duras do Validador de Continuidade:**
- 1+ verificação `CONTRADITO` → status geral = REPROVADO
- (NAO_ENCONTRADO é aceitável, é informação nova legítima)

**Consequência da violação:** livro com afirmações inventadas, com contradições internas, sem lastro no corpus. É o segundo problema mais grave (atrás de violar a Lei 3).

**Por que existe:** sem validação cega, o sistema autoaprovava o que produzia. A cegueira força o sistema a provar cada afirmação contra uma fonte externa (corpus) ou interna (Bible/Estado).

---

## Lei 3 — ATUALIZAÇÃO ATÔMICA, SEMPRE

**Bible da Obra e Estado da Obra são checkpoints únicos.** São atualizados **atomicamente** após cada cena aprovada.

**Procedimento de salvamento atômico:**

```python
def salvar_atomico(caminho_arquivo, conteudo):
    temp_path = caminho_arquivo + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(conteudo)
    os.replace(temp_path, caminho_arquivo)  # rename atômico
```

**Quando atualizar:**
- Bible: após cada cena CONCLUÍDA, com novos conceitos introduzidos, threads abertos/resolvidos, mudança de estado documentada.
- Estado: após cada cena CONCLUÍDA, com status da cena, validações (MARCH/Cont), checksum, retries, próxima cena.

**Consequência da violação:** estado corrompido, bible inconsistente, impossível retomar do ponto exato se o processo cair no meio.

**Por que existe:** atomicidade garante que ou o arquivo é escrito inteiro, ou fica intacto. Crash no meio do write = arquivo original preservado.

---

## Lei 4 — CHECKSUM E ROUND-TRIP, SEMPRE

**Toda cena CONCLUÍDA tem um checksum SHA256 (8 primeiros caracteres) e um tamanho em bytes registrados no Estado.**

**Procedimento de checksum:**

```python
import hashlib
def calcular_checksum(caminho_arquivo):
    with open(caminho_arquivo, "rb") as f:
        conteudo = f.read()
    return hashlib.sha256(conteudo).hexdigest()[:8]
```

**Round-trip check:** após anotar o checksum no Estado, o Orquestrador **reabre o arquivo do disco**, recalcula o checksum, e compara. Se for diferente do valor registrado, a cena é marcada como **INCONSISTENTE** e o sistema para.

**Consequência da violação:** cena "aprovada" pode ter sido sobrescrita, corrompida, ou simplesmente não existir mais. O checksum é a **única prova física** de que a cena é o que diz ser.

**Por que existe:** sem checksum, não há como detectar corrupção silenciosa. O sistema precisa de uma âncora física que prove que o conteúdo em disco é o que foi aprovado.

---

## Lei 5 — ISOLAMENTO POR WORKTREE, SEMPRE

**Cada cena = pasta isolada:**

```
execucao/capitulos/capitulo_NN/cena_MM/
  _saida_escritor.md
  _afirmacoes_para_validar.json
  _perguntas_continuidade.json
  _resultado_march.json
  _resultado_continuidade.json
  _saida_editor.md
  _saida_final.md
  _log_prompt_checker.md
```

**Nada vaza entre worktrees.** O Validador MARCH da cena 2.3 não pode ver a prosa da cena 2.2. O Validador de Continuidade da cena 5.1 não pode ver `_saida_escritor.md` da cena 4.7.

**Consequência da violação:** cenas contaminadas, validações enviesadas, impossível refazer uma cena sem estragar as outras.

**Por que existe:** worktree é o "cinto de segurança" do sistema. Permite refazer uma cena localmente, sem afetar o resto. Permite auditar cada cena isoladamente.

---

## Lei 6 — ZERO MATERIAL DE MARKETING NO LIVRO, SEMPRE

**O livro é didático. Não é página de venda.**

**PROIBIDO no livro final:**
- Preços de outros cursos, serviços ou produtos
- CTAs de venda ("clique aqui", "garanta sua vaga", "acesse o link")
- Ofertas com prazo ("última chance", "última abertura")
- Cupons de desconto para outros produtos
- Links para landing pages de venda
- Frases como "não perca tempo", "inscreva-se", "matricule-se"
- Qualquer texto que tente converter o leitor em cliente pagante

**PERMITIDO no livro final:**
- Menções a ferramentas, marcas, plataformas
- Nomes de cupons quando são **parte do método** (não são venda)
- Indicação de que existe uma comunidade, fórum, ou grupo (fato do método)
- Indicação de que existem outros livros ou cursos como recurso de aprofundamento (referência, não CTA)

**Consequência da violação:** o livro vira material de marketing disfarçado. O leitor percebe, sente-se manipulado, abandona.

**Por que existe:** o usuário pediu um LIVRO, não uma página de vendas. Livro informa, ensina, conta história. Página de vendas empurra decisão de compra. São produtos diferentes. O pipeline produz livros.

---

## 🔒 CONSEQUÊNCIA GLOBAL

Qualquer violação destas 6 leis reprova:
- A cena específica (se a violação é local)
- O livro inteiro (se a violação é sistêmica)

Não há "quase seguiu". Não há "foi um detalhe". Cada lei é ou respeitada ou violada. Se violada, a saída é reescrever, revalidar, refazer. Não é "passar com ressalva".

---

## 🧪 COMO SE AUTO-AUDITAR

Antes de marcar o livro como CONCLUÍDO, o Orquestrador confere:

1. **Cada cena tem 7 arquivos?** (conforme Lei 5)
2. **Cada cena tem `_resultado_march.json` e `_resultado_continuidade.json` com `status_geral: APROVADO`?** (Lei 2)
3. **Cada cena tem `_log_prompt_checker.md` que NÃO contém conteúdo de `_saida_escritor.md`?** (Lei 2)
4. **Cada cena tem checksum e round-trip OK no Estado?** (Lei 4)
5. **Bible e Estado foram atualizados após cada cena, atomicamente?** (Lei 3)
6. **Auto-auditoria da Lei 6 retorna sem matches?** (ver `regras_negocio/AUTO_AUDITORIA_PIPELINE.md`)

Se qualquer um falha, o livro **não está pronto**.
