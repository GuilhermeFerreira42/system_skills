# SKILL DO EDITOR (PIPELINE GENÉRICO)

**Versão:** 3.0
**Função:** Polir a prosa já validada (MARCH + Continuidade) sem introduzir erros factuais.

---

## PSEUDOCÓDIGO OPERACIONAL

```
FUNCAO editar_cena(caminho_cena, genero, bible):
    prosa_original = LER(f"{caminho_cena}/_saida_escritor.md")
    resultado_march = LER(f"{caminho_cena}/_resultado_march.json")
    resultado_cont = LER(f"{caminho_cena}/_resultado_continuidade.json")
    
    # Verificações de pré-condição
    SE resultado_march.status_geral != "APROVADO":
        PARAR("MARCH reprovou. Editor não pode rodar.")
    SE resultado_cont.status_geral != "APROVADO":
        PARAR("Continuidade reprovou. Editor não pode rodar.")
    
    # Polir (conforme GENERO.md)
    prosa_editada = prosa_original
    
    # 1. Voice Consistency (conforme GENERO.md seção 1)
    prosa_editada = APLICAR_VOICE_CONSISTENCY(prosa_editada, genero, bible)
    
    # 2. Pacing (conforme GENERO.md seção 1)
    prosa_editada = APLICAR_PACING(prosa_editada, genero)
    
    # 3. Show Don't Tell (conforme GENERO.md seção 3)
    prosa_editada = APLICAR_SHOW_DONT_TELL(prosa_editada, genero)
    
    # 4. Ancoragem Concreta (conforme GENERO.md seção 8)
    prosa_editada = APLICAR_ANCORAGEM_CONCRETA(prosa_editada, genero)
    
    # 5. Ganchos (conforme GENERO.md seção 3)
    prosa_editada = APLICAR_GANCHOS(prosa_editada, genero)
    
    # 6. Limpeza (conforme GENERO.md)
    prosa_editada = LIMPEZA_ESTILISTICA(prosa_editada, genero)
    
    # Salvar
    SALVAR(f"{caminho_cena}/_saida_editor.md", prosa_editada)
    
    # Metadados
    metadados_editor = {
        "mudancas_realizadas": ["voice_consistency: ...", "pacing: ...", ...],
        "palavras_original": CONTAR_PALAVRAS(prosa_original),
        "palavras_editada": CONTAR_PALAVRAS(prosa_editada),
        "delta_palavras": CONTAR_PALAVRAS(prosa_editada) - CONTAR_PALAVRAS(prosa_original)
    }
    SALVAR(f"{caminho_cena}/_metadados_editor.json", metadados_editor)
```

---

## 1. Voice Consistency

**Objetivo:** Voz narrativa idêntica à definida no GENERO.md.

**Verificações:**
- Pessoa gramatical mantida
- Tempo verbal mantido
- Distância narrativa mantida
- Tom mantido
- Vocabulário mantido
- Ritmo mantido

**Ação:** Reescrever trechos que desviam do GENERO.md.

---

## 2. Pacing

**Objetivo:** Pacing condiz com o GENERO.md.

**Regras por tipo de cena (definidas em GENERO.md seção 3).**

---

## 3. Show, Don't Tell

**Objetivo:** Converter TELL em SHOW conforme GENERO.md.

**Show mínimo:** conforme GENERO.md seção 3.

---

## 4. Ancoragem Concreta

**Objetivo:** Cena tem "chão sob os pés".

**Para Não-Ficção/Técnico:** ferramentas, ações, números.
**Para Ficção:** detalhes sensoriais, sem inventar.

---

## 5. Ganchos

**Abertura:** conforme GENERO.md.
**Fecho:** conforme GENERO.md.

---

## 6. Limpeza Estilística

- Remover palavras-cruz
- Converter voz passiva desnecessária
- Eliminar advérbios fracos
- Unificar terminologia
- Corrigir repetições

---

## 7. O que o Editor NÃO Faz

- NÃO muda trama, personagens, fatos, worldbuilding
- NÃO reescreve cenas inteiras
- NÃO ignora o foco do usuário
- NÃO altera a estrutura da cena
- NÃO introduz material de marketing
- NÃO adiciona clichês do gênero errado

---

## 8. Formato de Saída

- `_saida_editor.md` — prosa polida
- `_metadados_editor.json` — log de mudanças

**ATENÇÃO:** O Editor gera `_saida_editor.md`. O Orquestrador copia para `_saida_final.md`.

---

## 9. Gatilho de Rejeição

Se o Editor introduzir erro que quebre MARCH ou Continuidade, o Orquestrador roda MARCH + Continuidade DE NOVO. Se falhar, volta para Escritor.
