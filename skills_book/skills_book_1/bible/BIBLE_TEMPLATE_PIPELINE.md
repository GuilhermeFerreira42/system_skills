# TEMPLATE DA BIBLE DA OBRA (PIPELINE GENÉRICO)

**Versão:** 3.0
**Aplicação:** copie para `execucao/bible/bible_da_obra.md` e preencha progressivamente.

**IMPORTANTE:** Este template é **genérico** — funciona para qualquer gênero (Podbook, Ficção, Técnico). As seções marcadas com "[se aplicável]" só são preenchidas se o gênero pedir.

---

# Bible da Obra: [TÍTULO DO LIVRO]

## Metadados Gerais
- **Titulo:** [do CONFIG.md]
- **Subtitulo:** [do CONFIG.md, se houver]
- **Genero:** [nome do gênero, ex: "PODBOOK_MENTOR" | "FICCAO_LITERARIA" | "TECNICO_MANUAL"]
- **Subgenero:** [se aplicável]
- **Publico_alvo:** [do GENERO.md seção 1]
- **Tom_de_voz:** [do GENERO.md seção 1]
- **POV_padrao:** [do GENERO.md seção 1]
- **Tempo_verbal:** [do GENERO.md seção 1]
- **Distancia_narrativa:** [do GENERO.md seção 1]
- **Vocabulario_nivel:** [do GENERO.md seção 1]
- **Ritmo_padrao:** [do GENERO.md seção 1]
- **Extensao_por_cena:** [do GENERO.md seção 3]
- **Formato_do_fim:** [do GENERO.md seção 4]
- **Versao_bible:** v1.0
- **Checksum:** [auto]
- **Ultima_atualizacao:** [ISO 8601]

---

## Premissa & Estrutura
- **Logline:** (uma frase: protagonista + objetivo + obstáculo + stakes)
- **Tema_central:** 
- **Pergunta_tematica:** (o que o livro explora)
- **Estrutura_narrativa:** [do GENERO.md seção 6]
- **Numero_estimado_capitulos:** 
- **Numero_estimado_cenas:** 
- **Palavras_estimadas_total:** 

---

## Trilha Selecionada (Escopo da Obra)

- **Trilha 1:** [Nome — qual módulo do corpus entra no livro]
- **Trilha 2:** [Nome — módulo complementar]
- **Apêndices:** [se houver]

---

## Glossário Técnico (Regras Rígidas do Mundo)

| Termo | Definição Canônica | Tipo | Regra Rígida? |
|-------|-------------------|------|---------------|
| [Termo 1] | [Definição] | Conceito_Técnico | SIM |
| [Termo 2] | [Definição] | Conceito_Técnico | SIM |
| ... | ... | ... | ... |

**Tipos:** `Conceito_Técnico` | `Protocolo` | `Termo_Especial` | `Regra_Sociedade` | `Tecnologia` | `Ferramenta` | `Personagem` | `Local`

**Regra rígida (SIM)** = o termo NÃO pode ser contradito pelo Escritor sem reescrita cirúrgica.

---

## Conceitos-Chave do Método (Marcos)

| Marco | Definição | Onde aparece |
|-------|-----------|--------------|
| [Marco 1] | [Definição] | [Cap X, Cena Y] |
| [Marco 2] | [Definição] | [Cap X, Cena Y] |
| ... | ... | ... |

---

## Cases / Personagens / Elementos Centrais

| Nome | Contexto | Onde aparece | Status na Obra |
|------|----------|--------------|----------------|
| [Nome 1] | [Breve descrição, dados, número] | [Cap X, Cena Y] | REFERÊNCIA PRIMÁRIA |
| [Nome 2] | [Breve descrição] | [Cap X, Cena Y] | REFERÊNCIA SECUNDÁRIA |
| ... | ... | ... | ... |

---

## Personas (Público-Alvo do Leitor)

### Persona Principal
- [Idade, contexto, dor, desejo, frase-tipo]

### Persona Secundária
- [Idade, contexto, dor, desejo]

---

## Cenários / Locais (Universo da Obra)

### Local: [Nome]
- **Tipo:** [Físico | Digital | Marketplace | Ferramenta | Mítico | Histórico]
- **Descrição:** [breve]
- **Regras:** [o que vale nesse local]
- **Relevância:** [por que aparece na obra]

---

## Cronologia (se aplicável)

| Marco Temporal | O que acontece | Onde aparece |
|----------------|----------------|--------------|
| [Marco 1] | [O que acontece] | [Cap X] |
| [Marco 2] | [O que acontece] | [Cap X] |
| ... | ... | ... |

---

## Mitos / Equívocos Comuns (se aplicável)

| Mito | Verdade Apresentada | Onde |
|------|---------------------|------|
| [Mito 1] | [Verdade] | [Cap X, Cena Y] |
| ... | ... | ... |

---

## Fios Narrativos (Estrutura do Livro)

| Fio | Tipo | Introduzido em | Resolvido em | Descrição |
|-----|------|----------------|--------------|-----------|
| [Fio 1] | [Tema Central | Setup | Payoff | Arco | Mistério | Promessa] | [Cap X, Cena Y] | [Cap X, Cena Y] | [Descrição] |
| ... | ... | ... | ... | ... |

**Tipos:** `Tema Central` | `Setup` | `Payoff` | `Tema Recorrente` | `Ameaça` | `Promessa` | `Arco` | `Misterio`

---

## Decisões Editoriais Travadas (NÃO MUDAR SEM APROVAÇÃO)

| Decisão | Origem | Justificativa |
|---------|--------|---------------|
| [Decisão 1] | [Bible vX.Y / GENERO] | [Por que] |
| ... | ... | ... |

---

## Fontes do Corpus (Mapeamento por Capítulo)

| Capítulo | Fonte Principal do Corpus |
|----------|---------------------------|
| Cap 1 | [Caminho do arquivo] |
| Cap 2 | [Caminho do arquivo] |
| ... | ... |

---

## Checklist de Integridade (Preenchido pelo Orquestrador)

- [ ] Conceitos-chave definidos antes de usar (glossário com termos e regras rígidas)
- [ ] Cronologia cobre todos os capítulos planejados (se aplicável)
- [ ] Mitos do mercado listados (se aplicável ao gênero)
- [ ] Cases/personagens referenciados com papel definido
- [ ] Trilhas selecionadas mapeadas
- [ ] Fios narrativos definidos com setup e payoff (se aplicável)
- [ ] Decisões editoriais travadas registradas
- [ ] Versão e data da Bible preenchidos
