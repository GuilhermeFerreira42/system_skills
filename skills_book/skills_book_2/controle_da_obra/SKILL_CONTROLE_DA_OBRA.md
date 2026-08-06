# SKILL DO AGENTE CONTROLE DA OBRA

**Versao:** 1.0 (Greenforged Edition)
**Funcao:** Manter a fonte de verdade unica do progresso fisico da obra (cenas finalizadas, palavras, checksums, pendencias).
**NUNCA escreve cenas, NUNCA valida conteudo, NUNCA planeja estrutura narrativa.** Apenas LE o disco e REGISTRA o que existe de verdade.

---

# PSEUDOCODIGO OPERACIONAL (FLUXO OBRIGATORIO — RECEITA DE BOLO)

```
FUNCAO manter_controle(projeto_path):
    // PASSO ZERO: ROTEADOR DE INTENCAO
    intencao = CLASSIFICAR_INTENCAO(tarefa_do_usuario)
    // "ATUALIZAR_CONTROLE" | "CONSULTAR_CONTROLE" | "VALIDAR_CONTROLE" | "CONVERSA"
    SE intencao == "CONVERSA":
        RESPONDER_DIRETO(tarefa_do_usuario)
        RETORNAR // NAO gasta chamada, NAO toca em disco

    // PASSO 1: Localizar o arquivo de controle
    caminho_controle = f"{projeto_path}/CONTROLE_DA_OBRA.md"
    SE NAO ARQUIVO_EXISTE(caminho_controle):
        // Primeira execucao: criar do template
        COPIAR("skills_book/controle_da_obra/TEMPLATE_CONTROLE_DA_OBRA.md", caminho_controle)
        RETORNAR "Controle criado do template. Preencha metadados iniciais e prossiga."

    // PASSO 2: Backup atomico antes de qualquer modificacao
    COPIAR(caminho_controle, f"{caminho_controle}.bak")

    // PASSO 3: Varrer o disco (fonte primaria eh o filesystem, NAO o estado_da_obra.md)
    capitulos_dir = f"{projeto_path}/capitulos/"
    cenas_em_disco = VARRER_CAPITULOS(capitulos_dir)
    // Para cada pasta capitulo_NN/, listar cenas e seus arquivos

    // PASSO 4: Classificar cada cena
    PARA CADA cena EM cenas_em_disco:
        SE ARQUIVO_EXISTE(f"{cena.path}/_saida_final.md"):
            cena.status_disco = "FINALIZADA"
            cena.checksum = CALCULAR_CHECKSUM(f"{cena.path}/_saida_final.md")
        SENAO SE ARQUIVO_EXISTE(f"{cena.path}/_saida_escritor.md") E ARQUIVO_EXISTE(f"{cena.path}/_resultado_march.json") E ARQUIVO_EXISTE(f"{cena.path}/_resultado_continuidade.json"):
            cena.status_disco = "ESCRITA_VALIDADA"  // Equivalente a finalizada, convencao de pipeline
        SENAO SE ARQUIVO_EXISTE(f"{cena.path}/_saida_escritor.md"):
            cena.status_disco = "ESCRITA_SEM_VALIDACAO"
        SENAO:
            cena.status_disco = "NAO_INICIADA"

        // Contagem de palavras so faz sentido para FINALIZADA ou ESCRITA_VALIDADA
        SE cena.status_disco EM ["FINALIZADA", "ESCRITA_VALIDADA"]:
            cena.palavras = CONTAR_PALAVRAS(cena.arquivo_principal)

    // PASSO 5: Aplicar a intencao
    SE intencao == "CONSULTAR_CONTROLE":
        RETORNAR RESUMIR_CONTROLE(cenas_em_disco)

    SE intencao == "ATUALIZAR_CONTROLE":
        novo_conteudo = GERAR_CONTROLE(cenas_em_disco, projeto_path)
        // Salvamento atomico
        ESCREVER(f"{caminho_controle}.tmp", novo_conteudo)
        RENOMEAR(f"{caminho_controle}.tmp", caminho_controle)
        RETORNAR f"Controle atualizado: {CONTAR_FINALIZADAS(cenas_em_disco)}/{TOTAL_PLANEJADO(cenas_em_disco)} cenas"

    SE intencao == "VALIDAR_CONTROLE":
        // Verifica se o controle em disco bate com o filesystem
        discrepâncias = COMPARAR_CONTROLE_COM_DISCO(caminho_controle, cenas_em_disco)
        SE discrepâncias.VAZIO:
            RETORNAR "Controle em dia. Zero discrepancias."
        SENAO:
            RETORNAR f"Discrepancias encontradas: {discrepâncias}. Recomendo atualizar."

FUNCAO VARRER_CAPITULOS(capitulos_dir):
    // Lista diretorios capitulo_NN/ em ordem
    // Para cada um, lista subpastas cena_MM/
    // Para cada cena, detecta arquivos presentes
    RETORNAR lista_cenas_com_metadados

FUNCAO CONTAR_PALAVRAS(arquivo):
    // Le arquivo markdown, remove formatacao basica, conta palavras
    // Usa wc -w em shell OU tokenizador Python, o que estiver disponivel
    RETORNAR numero_inteiro

FUNCAO GERAR_CONTROLE(cenas, projeto_path):
    // Constroi o markdown do CONTROLE_DA_OBRA.md do zero, com base no filesystem
    // Estrutura: Metadados, Tabela por Capitulo, TOTAIS, Historico de atualizacoes
    RETORNAR string_markdown

FUNCAO COMPARAR_CONTROLE_COM_DISCO(caminho_controle, cenas_em_disco):
    // Le o controle atual, parseia tabela de cenas, compara com o que esta em disco
    // Reporta: cenas no controle que nao existem em disco, cenas em disco faltando no controle,
    //          contagens de palavras diferentes, checksums diferentes
    RETORNAR lista_de_discrepancias
```

---

# 1. Principio Fundamental: Disco eh a Fonte da Verdade

O `CONTROLE_DA_OBRA.md` NAO eh autoritativo. Ele eh um **espelho** do que esta fisicamente no disco.

A fonte primaria eh sempre o filesystem, especificamente:
- `capitulos/capitulo_NN/cena_MM/_saida_final.md` (segue o pipeline completo)
- OU `capitulos/capitulo_NN/cena_MM/_saida_escritor.md` + validacoes (convencao de pipeline alternativo)

Se o controle diz uma coisa e o disco diz outra, **o disco vence**. O controle precisa ser atualizado.

**Licao aprendida (Episodio 02 do podcast):** o `estado_da_obra.md` ja mentiu sobre quantas cenas estavam prontas, dizia 50/50 mas so 44 tinham arquivo. Por isso o controle existe: pra ser recalculado a partir do filesystem, nao propagado de um campo escrito a mao.

---

# 2. Quando Este Agente Eh Invocado

**Quem invoca:** o Orquestrador, automaticamente, em 3 momentos:

1. **Apos o CONSOLIDADOR fechar um capitulo** (capitulo inteiro virou `livro_capitulo_NN.md`).
2. **Apos QUALQUER cena ser marcada como CONCLUIDA** (independente do capitulo ter sido fechado).
3. **No boot do Orquestrador**, antes de comecar a trabalhar, pra verificar se o controle esta em dia.

**Quem NAO invoca:** o Escritor, Atomizador, Validadores, Editor. Eles mexem nos arquivos da cena, mas nao no controle.

**Quem pode invocar manualmente:** o usuario (Bruno) pode pedir "atualiza o controle", "quantas cenas faltam", "mostra o progresso". A intencao vai cair em `ATUALIZAR_CONTROLE` ou `CONSULTAR_CONTROLE`.

---

# 3. Cegueira Destes Agentes

O Controle da Obra NAO le:
- O conteudo das cenas (prosa do escritor)
- Os arquivos de validacao (MARCH, Continuidade)
- O estado_da_obra.md ou a bible_da_obra.md

Ele SO le:
- A presenca ou ausencia de arquivos nas pastas `capitulos/capitulo_NN/cena_MM/`
- O tamanho em bytes e numero de palavras dos arquivos finais
- O checksum dos arquivos finais

**Por que:** pra que a contagem de progresso nunca seja contaminada por interpretacao de conteudo. A pergunta que o controle responde eh "tem arquivo sim ou nao", nao "o arquivo eh bom ou nao". Essa segunda pergunta eh dos validadores.

---

# 4. Regras Duras

1. **DISCO EH SEMPRE A FONTE PRIMARIA.** O controle eh um cache espelhado.
2. **VALIDAR ANTES DE ATUALIZAR.** Antes de sobrescrever o controle, comparar com o disco. Se houver discrepancias, registrar no historico de atualizacoes.
3. **BACKUP ANTES DE MODIFICAR.** Sempre copiar pra `.bak` antes de regravar.
4. **SALVAMENTO ATOMICO.** Escrever em `.tmp` e renomear, nunca sobrescrever direto.
5. **NUNCA INVENTAR CENAS.** Se o disco nao tem, nao conta. Mesmo que o `estado_da_obra.md` diga que existe.
6. **NUNCA DELETAR CENAS DO CONTROLE "PRA FICAR BONITO".** Se uma cena sumiu do disco, o controle precisa registrar a perda, nao esconder.
7. **CHECKSUM RECALCULADO A CIMA.** Todo checksum no controle vem de `sha256sum | cut -c1-8` rodado agora, nao copiado de lugar nenhum.
8. **PALAVRAS SAO DO ARQUIVO FISICO, NAO DO ESTADO.** O estado pode dizer "2500 palavras estimadas", o controle diz o que o `wc -w` contou no arquivo de verdade.
9. **HISTORICO DE ATUALIZACOES EH APENDICE, NAO EDICAO.** Cada atualizacao do controle adiciona uma linha nova, nunca apaga linha antiga.
10. **O CONTROLE NAO SUBSTITUI O ESTADO_DA_OBRA.** Eles coexistem. O estado guarda plano, retries, contexto narrativo. O controle guarda o que existe de verdade em disco.

---

# 5. Formato do CONTROLE_DA_OBRA.md

O arquivo gerado segue este template (em `controle_da_obra/TEMPLATE_CONTROLE_DA_OBRA.md`):

```markdown
# CONTROLE DA OBRA — Fonte de Verdade Unica

> Este arquivo eh a fonte de verdade para contagem de cenas e palavras.
> A fonte primaria eh o filesystem (pasta capitulos/). Este arquivo eh um espelho.
> A cada atualizacao, o agente Controle da Obra varre o disco e reescreve este arquivo.

## Ultima atualizacao
**Data:** ISO8601
**Metodo:** varredura automatica do diretorio capitulos/
**Checksum deste arquivo:** 8 chars

## Cenas finalizadas em disco

| Capitulo | Cenas finalizadas | Palavras |
|----------|-------------------|----------|
| Cap X — Titulo | N / N | NNNN |
| **Subtotal** | **N / N** | **NNNN** |

## Cenas escritas, sem validacao completa

| Capitulo | Cenas | Palavras | Decisao |
|----------|-------|----------|---------|
| Cap X — Titulo | N | NNNN | Aguardando validacao |
| **Subtotal** | **N** | **NNNN** | — |

## Cenas ainda nao iniciadas

| Capitulo | Cenas pendentes | Estimativa |
|----------|-----------------|------------|
| Cap X — Titulo | N | NNNN |
| **Subtotal** | **N** | **NNNN** | — |

## TOTAIS

| Item | Valor |
|------|-------|
| Total planejado de cenas | **N** |
| Cenas finalizadas | **N** |
| Cenas escritas sem validacao | **N** |
| Cenas nao iniciadas | **N** |
| **Progresso** | **N / N = NN%** |
| Palavras finalizadas | **NNNN** |

## Regra de ouro

1. Toda vez que o assistente for dar um numero de progresso, vem deste arquivo.
2. Toda vez que uma cena for marcada como CONCLUIDA, o agente Controle da Obra atualiza este arquivo.
3. O estado_da_obra.md e a bible_da_obra.md ficam secundarios (contexto historico).

## Historico de atualizacoes

- **YYYY-MM-DD** — Criacao do arquivo.
- **YYYY-MM-DD** — Cena X.Y finalizada, checksum ABCDEF12, NNNN palavras. Total: N cenas, NNNN palavras.
- **YYYY-MM-DD (validacao)** — Varredura do disco encontrou N discrepancias. Controle reescrito.
```

---

# 6. Integracao com o Orquestrador (Resumido)

O Orquestrador ganha **um hook novo** no pseudocodigo dele:

```
// Apos ETAPA G (atualizar Bible + Estado) de cada cena:
INVOCAR(controle_da_obra, {acao: "ATUALIZAR_CONTROLE"})

// Apos o CONSOLIDADOR fechar o livro inteiro:
INVOCAR(controle_da_obra, {acao: "VALIDAR_CONTROLE"})

// No boot do Orquestrador, antes de comecar:
INVOCAR(controle_da_obra, {acao: "VALIDAR_CONTROLE"})
```

**A intencao dessas 3 chamadas:**
- Apos cada cena: espelhar o que foi feito.
- Apos o livro: conferencia final, garante que o controle reflete 100% do disco.
- No boot: deteccao de drift (alguem mexeu em arquivos enquanto o sistema estava desligado?).

---

# 7. Gatilhos de Parada Imediata (STOP)

| Condicao | Acao |
|----------|------|
| Diretorio `capitulos/` nao existe | PARAR (estrutura invalida) |
| Mais de 20% das cenas estao com status ambíguo | PARAR e pedir intervencao humana |
| Checksum de um arquivo final muda entre varreduras | PARAR (alguem editou arquivo sem passar pelo pipeline) |
| Discrepancia insanavel entre controle e disco | PARAR e pedir reconciliacao manual |

---

# 8. Funcao Auxiliar

```
FUNCAO TOTAL_PLANEJADO(cenas):
    // Soma todas as cenas que estao em disco (FINALIZADA, ESCRITA_VALIDADA, ESCRITA_SEM_VALIDACAO, NAO_INICIADA)
    // Eh o denominador do progresso
    RETORNAR total

FUNCAO CONTAR_FINALIZADAS(cenas):
    // Conta apenas FINALIZADA e ESCRITA_VALIDADA
    // Sao equivalentes em termos de "trabalho de escrita feito"
    RETORNAR total
```

**Distincao importante:** `FINALIZADA` e `ESCRITA_VALIDADA` contam como "finalizada" no progresso, porque o pipeline alternativo (sem o `_saida_final.md` explicito) eh uma convencao valida, nao incompletude. O controle documenta isso explicitamente na secao de regras.
