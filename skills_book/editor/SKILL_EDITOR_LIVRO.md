# SKILL DO EDITOR DE LIVRO (SOLVER — OPCIONAL)

**Versao:** 1.0
**Funcao:** Refinar a prosa do escritor para: consistencia de voz, pacing, show-dont-tell, dialogo natural, ancoragem sensorial, ganchos.
**So invocado se** `genero.exige_editor == true`.

---

# PSEUDOCODIGO OPERACIONAL

```
FUNCAO editar_cena(caminho_cena, genero, bible):
    prosa_original = LER(f"{caminho_cena}/_saida_escritor.md")
    metadados = LER(f"{caminho_cena}/_metadados_cena.json")
    resultado_march = LER(f"{caminho_cena}/_resultado_march.json")
    resultado_cont = LER(f"{caminho_cena}/_resultado_continuidade.json")

    // Ja passou MARCH + Continuidade. Agora polir.
    prosa_editada = prosa_original

    // 1. VOICE CONSISTENCY
    prosa_editada = APLICAR_VOICE_CONSISTENCY(prosa_editada, genero, bible, metadados)

    // 2. PACING
    prosa_editada = APLICAR_PACING(prosa_editada, genero, metadados)

    // 3. SHOW DON'T TELL
    prosa_editada = APLICAR_SHOW_DONT_TELL(prosa_editada, genero)

    // 4. DIALOGO NATURAL
    prosa_editada = APLICAR_DIALOGO_NATURAL(prosa_editada, genero, bible)

    // 5. ANCORAGEM SENSORIAL
    prosa_editada = APLICAR_ANCORAGEM_SENSORIAL(prosa_editada, genero)

    // 6. GANCHO ABERTURA + FECHO PROPULSOR
    prosa_editada = APLICAR_GANCHOS(prosa_editada, genero, metadados)

    // 7. LIMPEZA (palavras-cruz, repetições, advérbios fracos, passive voice excessiva)
    prosa_editada = LIMPEZA_ESTILISTICA(prosa_editada, genero)

    // Salvar
    SALVAR(f"{caminho_cena}/_saida_editor.md", prosa_editada)

    // Metadados do editor
    metadados_editor = {
        "mudancas_realizadas": [
            "voice_consistency: ajustado 3 trechos para vocabulario do genero",
            "pacing: acelerado paragrafos 5-7 (acao), desacelerado paragrafo 12 (revelacao)",
            "show_dont_tell: convertido 4 instancias de tell em show",
            "dialogo: removido exposicao disfarçada em 2 falas do Marcus",
            "ancoragem: adicionado cheiro de ozonio e frio no paragrafo de abertura",
            "gancho_abertura: fortalecida primeira frase",
            "fecho_propulsor: adicionado loop para proxima cena"
        ],
        "palavras_original": CONTAR_PALAVRAS(prosa_original),
        "palavras_editada": CONTAR_PALAVRAS(prosa_editada),
        "delta_palavras": CONTAR_PALAVRAS(prosa_editada) - CONTAR_PALAVRAS(prosa_original)
    }
    SALVAR(f"{caminho_cena}/_metadados_editor.json", metadados_editor)
```

---

# 1. Voice Consistency (Consistencia de Voz)

**Objetivo:** Garantir que a voz narrativa seja identica a definida no Genero + Bible, e consistente com capitulos anteriores.

**Verificacoes:**
- Pessoa gramatical (1a/3a) mantida
- Tempo verbal (passado/presente) mantido
- Distancia narrativa (intima/proxima/media/ampla) mantida
- Tom (adjetivos do genero: lirico, cru, ironico, caloroso, clinico, urgente)
- Vocabulario (nivel: simples/medio/rico/tecnico/construido)
- Ritmo de frases (curto/medio/longo, variacao)

**Acao:** Reescrever trechos que desviam. Exemplo:
- Genero diz "vocabulario rico, metaforico" -> trocar "ela ficou com medo" por "o medo gelou-lhe a medula"
- Genero diz "ritmo rapido, frases curtas" -> quebrar frases longas em acao

---

# 2. Pacing (Ritmo)

**Objetivo:** Pacing condiz com o tipo de cena e genero.

**Regras por tipo de cena (do genero):**

| Tipo de Cena | Pacing | Tecnicas |
|--------------|--------|----------|
| Acao/Conflito fisico | Acelerado | Frases curtas, verbos fortes, pouco interior, foco sensorial imediato |
| Revelacao/Climax emocional | Variado (build-up -> explosao -> respiro) | Frases crescentes, depois curtas, depois longo reflexivo |
| Investigacao/Descoberta | Moderado, tensao crescente | Perguntas internas, detalhes tecnicos, dialogo rapido |
| Transicao/Viagem | Mais lento, atmosferico | Descricao sensorial, reflexao, tempo passando |
| Dialogo pesado | Rapido, ping-pong | Falas curtas, subtexto, poucas tags, acao entre falas |

**Acao:** Reestruturar paragrafos, variar comprimento de frases, mover interioridade.

---

# 3. Show, Don't Tell (Mostre, Nao Conte)

**Objetivo:** Converter TELL em SHOW onde o genero exige (minimo definido no genero).

**Padroes TELL -> SHOW:**

| TELL (Fraco) | SHOW (Forte) |
|--------------|--------------|
| "Ela estava com raiva" | "O maxilar travou. As unhas cavaram a palma." |
| "O quarto estava baguncado" | "Roupas no chao. Xicaras com cafe seco na mesa. O cheiro de suor velho." |
| "Ele explicou o plano" | "Ele desenhou no guardanapo. 'Primeiro, o servidor. Depois, o backup.'" |
| "Foi uma viagem longa" | "Tres onibus. Doze horas. As costas doendo no banco de plastico." |
| "Ela se sentiu aliviada" | "O ar voltou aos pulmoes. Os ombros caíram. Pela primeira vez no dia, piscou sem pressa." |

**Regra:** Nao elimine TODO tell. Tell e util para transicoes rapidas, passagem de tempo, info necessaria mas nao dramatizada. Mas em momentos-chave (emocao, revelacao, acao), SHOW e obrigatorio.

---

# 4. Dialogo Natural

**Objetivo:** Dialogos que soam como pessoas reais falando, nao personagens expondo trama.

**Regras:**
- **Subtexto > Texto:** Personagens nao dizem exatamente o que pensam
- **Interruptus:** Cortam uns aos outros, nao respondem direto, mudam de assunto
- **Voz distinta:** Cada personagem tem vocabulario, ritmo, tic verbal proprio (da Bible)
- **Sem exposicao disfarçada:** "Como voce sabe, irmao, nosso pai morreu ha 5 anos" -> REESCREVER
- **Acao entre falas:** Nao so "ele disse / ela disse". Gestos, pausas, olhares, ambiente

**Acao:** Reescrever falas que violam. Manter informacao necessaria mas via subtexto/acao.

---

# 5. Ancoragem Sensorial (Grounding)

**Objetivo:** Toda cena tem "chao sob os pes" — o leitor sabe ONDE, QUANDO, COM QUE CORPO.

**Checklist por cena (primeiros 2-3 paragrafos + mudancas de local):**
- [ ] Onde estamos? (local fisico identificado)
- [ ] Quando? (hora, luz, passagem de tempo desde cena anterior)
- [ ] Quem esta na cena? (nomes + posicao relativa)
- [ ] Pelo menos 2 sentidos ativados (visao + olfato/tato/audicao/paladar/propriocepcao)
- [ ] Corpo do POV sentido (temperatura, tensao, respiracao, batimento, dor, formigamento)

**Acao:** Inserir detalhes sensoriais especificos (nao genericos) onde faltam.

---

# 6. Ganchos (Abertura e Fecho)

**Gancho de Abertura (primeira frase/paragrafo):**
- Deve: levantar pergunta, mostrar imagem forte, iniciar acao, estabelecer voz distinta
- Nao deve: comecar com "Ela acordou", "O sol nasceu", "Era uma vez", descricao de tempo

**Fecho Propulsor (ultimo paragrafo):**
- Deve: abrir loop (pergunta nao respondida, tensao nao resolvida, decisao iminente, revelacao parcial)
- Nao deve: resolver tudo, "e dormiram felizes", "o dia terminou", resumo

**Acao:** Reescrever abertura/fecho se fracos.

---

# 7. Limpeza Estilistica

- Remover palavras-cruz (muito, realmente, basicamente, de fato, na verdade)
- Converter voz passiva desnecessaria em ativa
- Eliminar advérbios fracos em verbos fortes ("caminhou rapidamente" -> "apressou-se")
- Unificar terminologia (Bible terms)
- Corrigir repetições de palavras proximas (janela de 3 paragrafos)

---

# 8. O que o Editor NAO faz

- NAO muda trama, personagens, fatos, worldbuilding (ja validado por MARCH + Continuidade)
- NAO reescreve cenas inteiras (so polimento cirurgico)
- NAO ignora o foco do usuario
- NAO altera metadados da cena (objetivo, mudanca, POV)

---

# 9. Formato de Saida

Arquivo: `{caminho_cena}/_saida_editor.md` (prosa final polida)
Arquivo: `{caminho_cena}/_metadados_editor.json` (log de mudancas)

---

# 10. Gatilho de Rejeicao (Orquestrador -> Reescrita)

Se o Editor introduzir erro que quebre MARCH ou Continuidade (raro, mas possivel):
- Orquestrador roda MARCH + Continuidade DE NOVO apos Editor
- Se falhar -> volta para Escritor (nao para Editor)