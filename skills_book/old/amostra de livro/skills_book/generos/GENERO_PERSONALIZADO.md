# GENERO: PERSONALIZADO (Template para o Usuario Criar o Seu)

**Versao:** 1.0
**Tipo:** PERSONALIZADO
**Uso:** Copie este arquivo, renomeie para `GENERO_MEU_GENERO.md`, preencha e salve em `generos/`.

---

## Instrucoes

1. Copie este arquivo
2. Renomeie para `GENERO_[SEU_NOME].md` (ex: `GENERO_THRILLER_PSICOLOGICO.md`)
3. Preencha **TODOS** os campos abaixo
4. Salve na pasta `generos/` do projeto
5. O Orquestrador carregara automaticamente quando voce disser o nome do genero

---

## Configuracao do Genero

### Identidade
- **nome_exibicao:** "[Nome amigavel, ex: Thriller Psicologico]"
- **base:** "ROMANCE | NAO_FICCAO | MEMOIR | TECNICO" (qual base herda)
- **descricao_curta:** "Uma frase descrevendo o genero"

### Voz Narrativa
- **pessoa:** "1a | 2a | 3a_limitada | 3a_onisciente | 3a_multipla | 3a_autoral | 3a_instrutiva"
- **tempo_verbal:** "passado | presente | misto_controlado"
- **distancia:** "intima | proxima | media | ampla | cinematografica | mentor | instrutor_ao_lado"
- **tom:** ["adjetivo1", "adjetivo2", "adjetivo3"] (ex: ["tenso", "claustrofobico", "analitico"])
- **vocabulario:** "simples | medio | rico | tecnico | construido | pessoal | acessivel"
- **ritmo:** "lento | variado | rapido | acelerado | modular | ondulatorio | linear"

### POV (Point of View)
- **padrao:** (mesmo valor de pessoa acima, ou especifico: "1a_dual_temporalidade")
- **multi_pov:** true/false
- **regras_troca:** "so_na_quebra_de_cena | cada_capitulo_1_pov | marcado_explicitamente | NA"

### Estrutura de Cena (Unidade Basica)
- **min_palavras:** [numero]
- **max_palavras:** [numero]
- **beats_obrigatorios:** ["beat1", "beat2", "beat3"] (ex: ["gancho", "objetivo", "obstaculo", "desenvolvimento", "climax", "mudanca", "fecho"])
- **show_minimo:** [porcentagem 0-100]
- **gancho_tipos:** ["tipo1", "tipo2"] (ex: ["pergunta_provocativa", "imagem_forte", "acao_em_andamento"])
- **fecho_tipos:** ["tipo1", "tipo2"] (ex: ["ponte_proximo", "revelacao_parcial", "cliffhanger"])

### Estrutura de Capitulo
- **unidades_por_capitulo:** [min]-[max] (cenas por capitulo, ou secoes conceituais)
- **arco_capitulo:** "descricao do arco tipico de um capitulo"
- **recap_final:** true/false

### Estrutura Global (Arquitetura do Livro)
- **arquetipo:** "TRES_ATOS | JORNADA_HEROI | KISHOTENKETSU | PROBLEMA_SOLUCAO | GRANDE_IDEIA | BIOGRAFIA | INVESTIGATIVO | CURSO_PROGRESSIVO | COOKBOOK | TEMATICO | CRONOLOGICO | FRAGMENTADO"
- **capitulos_estimados:** [min]-[max]
- **partes_atos:** true/false (se tem divisao em Partes/Atos explicitas)

### Bible Requisitos (O que a Bible DEVE conter para este genero)
- **personagens_detalhados:** true/false
- **worldbuilding_profundo:** true/false
- **cronologia_rigida:** true/false
- **sistema_magia_regras:** true/false
- **conceitos_chave:** true/false
- **estudos_citados:** true/false
- **protocolos_praticos:** true/false
- **glossario_tecnico:** true/false
- **ambiente_referencia:** true/false
- **locais_detalhados:** true/false
- **fios_narrativos:** true/false
- **versao_oficial_vs_verdade:** true/false
- **etica_privacidade:** true/false
- **erros_comuns:** true/false
- **checklists_verificacao:** true/false

### Validacoes Extras (Editor)
- **exige_editor:** true/false
- **regras_editor:** ["regra1", "regra2", "regra3"] (ex: ["voice_consistency", "pacing", "show_dont_tell", "dialogo_natural", "ancoragem_sensorial", "gancho_abertura_fecho", "arco_emocional_pov", "clareza_conceitual", "densidade_evidencia", "aplicabilidade", "precisao_tecnica", "reprodutibilidade", "verdade_emocional", "especificidade_sensorial", "dual_temporalidade_clara"])

### Foco Padrao do Usuario (Sugestao para o Orquestrador perguntar)
> "Exemplo de instrucao tipica para este genero: 'Foque em X. Evite Y. Priorize Z.'"

---

## Exemplo Preenchido: THRILLER PSICOLOGICO

```markdown
# GENERO: THRILLER_PSICOLOGICO

# Identidade
nome_exibicao: "Thriller Psicologico"
base: "ROMANCE"
descricao_curta: "Suspense centrado na mente do protagonista, paranoia, unreliable narrator, tensao interna > acao externa"

# Voz Narrativa
pessoa: "3a_limitada"
tempo_verbal: "presente"
distancia: "claustrofobica"
tom: ["tenso", "paranoico", "analitico", "visceral"]
vocabulario: "medio"
ritmo: "acelerado_com_pausas_respiratorias"

# POV
padrao: "3a_limitada"
multi_pov: true
regras_troca: "cada_capitulo_1_pov_marcado_explicitamente"

# Estrutura de Cena
min_palavras: 1500
max_palavras: 4000
beats_obrigatorios: ["gancho_paranoide", "objetivo_sobrevivencia", "ameaca_interna_externa", "escalada_tensao", "revelacao_parcial", "fecho_cliffhanger"]
show_minimo: 75
gancho_tipos: ["pensamento_intrusivo", "som_ambiguo", "lacre_de_memoria", "percepcao_distorcida"]
fecho_tipos: ["nova_ameaca", "duvida_sobre_realidade", "contagem_regressiva"]

# Estrutura de Capitulo
unidades_por_capitulo: 2-3
arco_capitulo: "Tensao sobe -> Pico -> Queda falsa -> Nova ameaca"
recap_final: false

# Estrutura Global
arquetipo: "TRES_ATOS_COM_TWIST_MEIO"
capitulos_estimados: 18-24
partes_atos: true

# Bible Requisitos
personagens_detalhados: true
worldbuilding_profundo: false
cronologia_rigida: true
sistema_magia_regras: false
conceitos_chave: true
estudos_citados: false
protocolos_praticos: false
glossario_tecnico: false
ambiente_referencia: false
locais_detalhados: true
fios_narrativos: true
versao_oficial_vs_verdade: true
etica_privacidade: false
erros_comuns: false
checklists_verificacao: false

# Validacoes Extras
exige_editor: true
regras_editor: ["voice_consistency", "pacing", "show_dont_tell", "ancoragem_sensorial", "gancho_abertura_fecho", "arco_emocional_pov", "verdade_emocional", "especificidade_sensorial", "dual_temporalidade_clara"]

# Foco Padrao
foco_padrao: "Foque na experiencia subjetiva do protagonista. O leitor deve duvidar do que e real. Tensao interna > acao externa. Unreliable narrator controlado."
```