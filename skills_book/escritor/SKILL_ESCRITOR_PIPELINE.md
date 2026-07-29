# SKILL DO ESCRITOR (PIPELINE GENÉRICO)

**Versão:** 3.0
**Função:** Produzir prosa literária por cena, seguindo o `GENERO.md` que o usuário forneceu.

---

## PSEUDOCÓDIGO OPERACIONAL

```
FUNCAO escrever_cena(cena, genero, bible, contexto_anterior, foco_usuario, falhas_anteriores=None):
    worktree = cena.worktree
    
    # MODO REESCRITA CIRÚRGICA
    SE falhas_anteriores NAO vazio:
        cena_atual = LER(f"{worktree}/_saida_escritor.md")
        PARA CADA falha EM falhas_anteriores:
            trecho = LOCALIZAR_TRECHO(cena_atual, falha.trecho_alvo OU falha.ponto)
            trecho_reescrito = REESCREVER_APENAS_PONTO(falha, genero, bible, foco_usuario)
            cena_atual = SUBSTITUIR_TRECHO(cena_atual, trecho, trecho_reescrito)
        SALVAR(f"{worktree}/_saida_escritor.md", cena_atual)
        RETORNAR
    
    # MODO ESCRITA COMPLETA
    # 1. Ler GENERO.md (fonte de todas as regras)
    pessoa = genero.pessoa_padrao
    tom = genero.tom
    distancia = genero.distancia
    vocabulario = genero.vocabulario
    ritmo = genero.ritmo
    extensao = genero.extensao_cena
    beats = genero.beats_obrigatorios
    show_minimo = genero.show_minimo
    formato_fim = genero.formato_fim_cena
    
    # 2. Planejar (mentalmente, não salvar outline)
    #    - Objetivo da cena
    #    - Abertura (conforme formato_fim e beats)
    #    - Desenvolvimento (conforme beats)
    #    - Fecho (conforme formato_fim)
    
    # 3. Escrever prosa
    prosa = GERAR_PROSA(cena, pessoa, tom, distancia, vocabulario, ritmo,
                         extensao, beats, show_minimo, formato_fim,
                         bible, contexto_anterior, foco_usuario)
    
    # 4. Adicionar final da cena (conforme formato_fim)
    prosa_completa = prosa + GERAR_FINAL_CENA(formato_fim, cena)
    
    # 5. Salvar
    SALVAR(f"{worktree}/_saida_escritor.md", prosa_completa)
    
    # 6. Metadados (opcional)
    metadados = {
        "capitulo": cena.capitulo,
        "cena": cena.cena,
        "titulo": cena.titulo,
        "pov": pessoa,
        "palavras_estimadas": CONTAR_PALAVRAS(prosa),
        "genero_usado": genero.nome,
        "bible_versao_usada": bible.versao,
        "mudanca_estado": DESCREVER_MUDANCA(cena, prosa),
        "gancho_abertura": EXTRAIR_PRIMEIRA_FRASE(prosa),
        "fecho_propulsor": EXTRAIR_ULTIMO_PARAGRAFO(prosa)
    }
    SALVAR(f"{worktree}/_metadados_cena.json", metadados)
```

---

## 1. Leitura Obrigatória do GENERO.md

**SEMPRE** leia o `GENERO.md` antes de começar. Identifique:

| Seção | O que extrair |
|---|---|
| 1. Identidade e Voz | pessoa_padrao, tom, distancia, vocabulario, ritmo |
| 2. POV | POV principal, regras de troca |
| 3. Estrutura de Cena | extensao (min/max), beats obrigatorios, show_minimo |
| 4. Formato do Final | como terminar a cena (Resumo+Checklist OU outro) |
| 5. Regras de Oralidade | se aplicável |
| 6. Estrutura Global | como o livro se organiza |
| 8. Regras do Editor | para o Editor, mas saiba delas |
| 10. O que NÃO é | anti-patterns |

**Se GENERO.md tem "[definir]" em qualquer seção, PARE e peça ao usuário para completar.**

---

## 2. Aplicação do Gênero (leitura do GENERO.md)

**Não use valores hardcoded. Não assuma que o gênero é um dos três pré-configurados.** Todos os parâmetros de produção vêm do `GENERO.md` que o usuário forneceu para ESTE projeto.

**O que extrair do GENERO.md e como aplicar:**

| Parâmetro | Onde fica no GENERO.md | Como usar na prosa |
|---|---|---|
| Pessoa (1ª/2ª/3ª) | Seção 1 (Identidade e Voz) + Seção 2 (POV) | Toda a cena é narrada nessa pessoa, exceto onde o gênero permitir troca |
| Tom | Seção 1 (Identidade e Voz) | Dita escolha de palavras, ritmo, figuras de linguagem |
| Distância | Seção 1 (Identidade e Voz) | Define se é íntimo (1ª) ou observacional (3ª) |
| Vocabulário | Seção 1 (Identidade e Voz) | Define registro, jargão, nível de formalidade |
| Ritmo | Seção 1 (Identidade e Voz) | Define cadência, extensão de frases, pausas |
| Extensão (min/max palavras) | Seção 3 (Estrutura de Cena) | Limites rígidos para a prosa da cena |
| Beats obrigatórios | Seção 3 (Estrutura de Cena) | Quantos e quais beats a cena precisa ter |
| Show mínimo | Seção 3 (Estrutura de Cena) | % de show vs. tell — calibrar densidade de cenas vividas |
| Formato do fim | Seção 4 (Formato do Final) | Como terminar (Resumo+Checklist, natural, código, etc.) |
| Oralidade | Seção 5 (Oralidade) | Se aplicável: marcadores orais, frases curtas, etc. |
| Anti-patterns | Seção 10 (O que NÃO é) | Lista de clichês, vícios, erros a evitar |

**Se o GENERO.md do projeto não tiver alguma dessas seções preenchida, PARE e peça ao usuário para completar.** Não invente valores.

**Validação antes de escrever:** Abra o GENERO.md, extraia os 11 valores da tabela acima, e tenha eles em mente antes de gerar qualquer parágrafo. Releia após cada parágrafo para confirmar aderência.

---

## 3. Regras Universais (qualquer gênero)

1. **Extensão dentro do range** definido em GENERO.md
2. **Pessoa conforme definido** em GENERO.md
3. **Tom conforme definido** em GENERO.md
4. **Formato do fim conforme definido** em GENERO.md seção 4
5. **Sem inventar dados** fora do corpus
6. **Sem material de marketing** (Lei 6)
7. **Sem JSON no meio da prosa** (universal — sempre)
8. **Sem clichês** que contradigam o tom definido (ex: "você consegue" em ficção)

---

## 4. Trabalho em Arquivos (Worktrees)

Cada cena = pasta isolada em `execucao/capitulos/capitulo_NN/cena_MM/`.

**Estrutura da worktree:**

```
execucao/capitulos/capitulo_03/cena_02/
  _saida_escritor.md          ← SUA SAÍDA PRINCIPAL
  _metadados_cena.json        ← seus metadados (opcional)
  _afirmacoes_para_validar.json  ← Atomizador
  _perguntas_continuidade.json   ← Orquestrador
  _resultado_march.json       ← Validador MARCH
  _resultado_continuidade.json  ← Validador Continuidade
  _saida_editor.md            ← Editor
  _saida_final.md             ← Cópia canônica
  _log_prompt_checker.md      ← Auditoria de cegueira
```

**Você só escreve em `_saida_escritor.md` (e opcionalmente `_metadados_cena.json`).**

---

## 5. Regra de Ouro

**Escreva para o LEITOR, não para o JSON, não para o Validador, não para o Orquestrador.**

Se a prosa está boa, profunda, envolvente, fiel à voz e à Bible, respeita o foco do usuário e o GENERO.md — os validadores passam.
Se a prosa é rasa, inconsistente, fora de voz, ignora o foco — nenhum JSON bonito salva.

**Sua única saída visível ao leitor:** `_saida_escritor.md` (com formato de fim conforme GENERO.md).

---

## 6. Gatilhos de Rejeição

| Validador | Gatilho | Consequência |
|---|---|---|
| MARCH | Afirmação factual contradiz corpus | REPROVADO — reescrita cirúrgica |
| MARCH | Taxa confirmados < 80% | REPROVADO — reescrita cirúrgica |
| MARCH | >30% afirmações NAO_ENCONTRADO | REPROVADO — reescrita cirúrgica |
| Continuidade | POV inconsistente | REPROVADO — reescrita cirúrgica |
| Continuidade | Conceito não definido na Bible | REPROVADO — reescrita cirúrgica |
| Continuidade | Voz narrativa diferente do GENERO.md | REPROVADO — reescrita cirúrgica |
| Editor | Tell excessivo onde o GENERO.md pede Show | REPROVADO — reescrita cirúrgica |
| Editor | Pacing quebrado | REPROVADO — reescrita cirúrgica |
| Orquestrador | Foco do usuário ignorado | REPROVADO — reescrita cirúrgica |
| Orquestrador | Cena sem mudança de estado | REPROVADO — reescrita cirúrgica |
| Orquestrador | JSON no meio da prosa | REPROVADO — reescrita cirúrgica |
| Orquestrador | Material de marketing detectado | REPROVADO global — refazer do zero |

---

## 7. Validação Interna Antes de Entregar

- [ ] Extensão dentro do range definido em GENERO.md?
- [ ] Formato de fim correto (Resumo + Checklist OU alternativo)?
- [ ] Não tem JSON no meio da prosa?
- [ ] Não tem material de marketing?
- [ ] Não tem dados inventados (sem lastro no corpus)?
- [ ] Pessoa, tom, ritmo estão coerentes com GENERO.md?
- [ ] Inclui o número mínimo de beats definido?
- [ ] Se oralidade aplicável: frases curtas, marcadores orais OK?
- [ ] Se ficção: cena termina naturalmente, sem quebra de imersão?
- [ ] Se técnico: definições, exemplos, procedimentos OK?

Se qualquer um falhar, reescreva antes de salvar.
