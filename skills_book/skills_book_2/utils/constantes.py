# -*- coding: utf-8 -*-
"""
utils/constantes.py
===================

Constantes centralizadas da skill `skills_book`.

Este arquivo existe pra eliminar a duplicacao de strings hardcoded que apareceva
em 19 arquivos da skill (152 ocorrenoes de nomes de arquivo, caminhos de pasta,
status, chaves JSON, etc). Quando a gente precisar renomear um arquivo, mudar um
caminho, ou ajustar um status, a gente muda AQUI e todas as skills que importam
estas constantes sao atualizadas de uma vez.

**REGRA DE OURO:** nenhum agente da skill (orquestrador, escritor, atomizador,
validador_march, validador_continuidade, editor, consolidador, controle_da_obra)
hardcoda nome de arquivo, caminho, ou chave de negocio. Todos importam deste
arquivo.

**Convencoes de nomenclatura:**
- Pastas e arquivos do projeto: CAIXA_ALTA_COM_UNDERSCORE
- Caminhos completos (com pasta): CAIXA_ALTA_COM_UNDERSCORE
- Status e enums: CAIXA_ALTA_COM_UNDERSCORE
- Chaves JSON: snake_case (igual ao que aparece no JSON)
- Sufixo `_DIR` = pasta
- Sufixo `_ARQ` ou `_PATH` = arquivo
- Sufixo `_STATUS` = valor de status
- Sufixo `_CHAVE` = chave de dicionario JSON

**Versao:** 1.0
**Data:** 2026-08-05
**Acao do diagnostico do Episodio 02:** Acao 5 (Criar utils/constantes.py)
"""

# ============================================================================
# 1. ESTRUTURA DE PASTAS DO PROJETO DE LIVRO
# ============================================================================
# Estas constantes definem a estrutura canonica de pastas que todo projeto de
# livro criado pela skill deve seguir.

PASTA_RAIZ_NOME = ""  # raiz do projeto, usada como prefixo
PASTA_CORPUS = "corpus"
CORPUS_README_ARQ = "README.md"  # indice do corpus modular (dentro de PASTA_CORPUS)
CORPUS_NOVO_ARQ = "corpus_novo.md"  # corpus monolitico (raiz do projeto)
PASTA_BIBLE = "bible"
PASTA_ESTADO = "estado"
PASTA_CAPITULOS = "capitulos"
PASTA_GENEROS = "generos"
PASTA_UTILS = "utils"
PASTA_CONTROLE_DA_OBRA = "controle_da_obra"
PASTA_OUTPUT = "output"  # saida final do livro (livro_final.md, .epub, .pdf)
PASTA_BACKUP = ".bak"  # sufixo de backup (usado para gerar .bak em arquivos criticos)
PASTA_RASCUNHOS = "rascunhos"  # rascunhos intermediarios por cena/capitulo


# ============================================================================
# 2. ARQUIVOS GLOBAIS DO PROJETO (fora de capitulos/)
# ============================================================================
# Arquivos de controle e contexto que existem na raiz do projeto.

BIBLE_DA_OBRA_ARQ = "bible_da_obra.md"
ESTADO_DA_OBRA_ARQ = "estado_da_obra.md"
CONTROLE_DA_OBRA_ARQ = "CONTROLE_DA_OBRA.md"
LIVRO_FINAL_ARQ = "livro_final.md"
LIVRO_FINAL_EPUB_ARQ = "livro_final.epub"
LIVRO_FINAL_PDF_ARQ = "livro_final.pdf"
LIVRO_COMPLETO_ARQ = "livro_completo.md"

# Backups canonicos
BIBLE_DA_OBRA_BAK_SUFIXO = ".bak"  # gera bible_da_obra.md.bak
ESTADO_DA_OBRA_BAK_SUFIXO = ".bak"  # gera estado_da_obra.md.bak
CONTROLE_DA_OBRA_BAK_SUFIXO = ".bak"  # gera CONTROLE_DA_OBRA.md.bak


# ============================================================================
# 3. ARQUIVOS DO WORKTREE DE CENA (dentro de capitulos/capitulo_NN/cena_MM/)
# ============================================================================
# Estes sao os arquivos que cada agente produz ou consome dentro do worktree
# isolado de uma cena. O padrao eh: arquivo comeca com "_" pra ficar visivel
# em listagens de diretorio.

# --- Saidas principais (cada agente produz 1 destes) ---
SAIDA_ESCRITOR_ARQ = "_saida_escritor.md"          # prosa bruta do Escritor
SAIDA_EDITOR_ARQ = "_saida_editor.md"              # prosa polida do Editor (opcional)
SAIDA_FINAL_ARQ = "_saida_final.md"                # copia canonica da saida final (editor ou escritor)

# --- Metadados por agente ---
METADADOS_CENA_ARQ = "_metadados_cena.json"        # metadados da cena produzida pelo Escritor
TRABALHO_ESCRITOR_ARQ = "_trabalho_escritor.json"  # log de trabalho do Escritor (reescrita cirurgica etc)

# --- Entregas de agentes de validacao ---
AFIRMACOES_PARA_VALIDAR_ARQ = "_afirmacoes_para_validar.json"  # saida do Atomizador
PERGUNTAS_VALIDADOR_ARQ = "_perguntas_validador.json"          # saida secundaria do Atomizador
PERGUNTAS_CONTINUIDADE_ARQ = "_perguntas_continuidade.json"    # perguntas de continuidade (geradas pelo Orquestrador)
RESULTADO_MARCH_ARQ = "_resultado_march.json"                  # saida do Validador MARCH
RESULTADO_CONTINUIDADE_ARQ = "_resultado_continuidade.json"    # saida do Validador Continuidade
RESULTADO_REVISOR_CEGO_ARQ = "_resultado_revisor_cego.json"    # saida do Revisor Cego Editorial (Acao 4)
LOG_PROMPT_CHECKER_ARQ = "_log_prompt_checker.md"              # auditoria do prompt do Validador

# --- Entregas do Editor ---
METADADOS_EDITOR_ARQ = "_metadados_editor.json"  # metadados da edicao (opcional)

# --- Livros consolidados por capitulo (gerados pelo Consolidador) ---
LIVRO_CAPITULO_PREFIXO = "livro_capitulo_"  # gera livro_capitulo_NN.md
LIVRO_CAPITULO_EXTENSAO = ".md"


# ============================================================================
# 4. PADROES DE NOMENCLATURA DE CAPITULOS E CENAS
# ============================================================================
# Como nomear pastas e arquivos de capitulo/cena no filesystem.

CAPITULO_PREFIXO_PASTA = "capitulo_"  # gera capitulo_01, capitulo_02, ...
CAPITULO_NUMERO_DIGITOS = 2           # zero-padded: 01, 02, ..., 12, 13
CENA_PREFIXO_PASTA = "cena_"          # gera cena_01, cena_02, ...
CENA_NUMERO_DIGITOS = 2               # zero-padded: 01, 02, ...

# Funcao utilitaria pra formatar caminho
def formatar_pasta_capitulo(numero):
    """Retorna 'capitulo_NN' com zero-padding."""
    return f"{CAPITULO_PREFIXO_PASTA}{str(numero).zfill(CAPITULO_NUMERO_DIGITOS)}"


def formatar_pasta_cena(numero):
    """Retorna 'cena_NN' com zero-padding."""
    return f"{CENA_PREFIXO_PASTA}{str(numero).zfill(CENA_NUMERO_DIGITOS)}"


def formatar_livro_capitulo(numero):
    """Retorna 'livro_capitulo_NN.md'."""
    return f"{LIVRO_CAPITULO_PREFIXO}{str(numero).zfill(CAPITULO_NUMERO_DIGITOS)}{LIVRO_CAPITULO_EXTENSAO}"


# ============================================================================
# 5. VALORES DE STATUS DE CENA
# ============================================================================
# Status possiveis de uma cena no estado_da_obra.md.

STATUS_CENA_PENDENTE = "PENDENTE"
STATUS_CENA_ESCREVENDO = "ESCREVENDO"
STATUS_CENA_REVISAO_MARCH = "REVISAO_MARCH"
STATUS_CENA_REVISAO_CONT = "REVISAO_CONT"
STATUS_CENA_CONCLUIDO = "CONCLUIDO"
STATUS_CENA_REPROVADO = "REPROVADO"
STATUS_CENA_REPROVADO_MARCH = "REPROVADO_MARCH"
STATUS_CENA_REPROVADO_CONTINUIDADE = "REPROVADO_CONTINUIDADE"
STATUS_CENA_REPROVADO_REVISOR = "REPROVADO_REVISOR"  # novo: Acao 4 (Revisor Cego reprovou)
STATUS_CENA_INCONSISTENTE = "INCONSISTENTE"

STATUS_CENA_VALIDOS = [
    STATUS_CENA_PENDENTE,
    STATUS_CENA_ESCREVENDO,
    STATUS_CENA_REVISAO_MARCH,
    STATUS_CENA_REVISAO_CONT,
    STATUS_CENA_CONCLUIDO,
    STATUS_CENA_REPROVADO,
    STATUS_CENA_REPROVADO_MARCH,
    STATUS_CENA_REPROVADO_CONTINUIDADE,
    STATUS_CENA_REPROVADO_REVISOR,
    STATUS_CENA_INCONSISTENTE,
]

# Status agregados da obra
STATUS_OBRA_EM_ANDAMENTO = "EM_ANDAMENTO"
STATUS_OBRA_CONCLUIDO = "CONCLUIDO"
STATUS_OBRA_INTERROMPIDO = "INTERROMPIDO"

# Status do agente Controle da Obra
STATUS_DESCO_FINALIZADA = "FINALIZADA"
STATUS_DESCO_ESCRITA_VALIDADA = "ESCRITA_VALIDADA"
STATUS_DESCO_ESCRITA_SEM_VALIDACAO = "ESCRITA_SEM_VALIDACAO"
STATUS_DESCO_NAO_INICIADA = "NAO_INICIADA"


# ============================================================================
# 6. VALORES DE VALIDACAO (MARCH e Continuidade)
# ============================================================================
# Status possiveis nas validacoes.

VALIDACAO_APROVADO = "APROVADO"
VALIDACAO_REPROVADO = "REPROVADO"
VALIDACAO_PENDENTE = "PENDENTE"

# Status das afirmacoes no MARCH
MARCH_CONFIRMADO = "CONFIRMADO"
MARCH_CONTRADITO = "CONTRADITO"
MARCH_NAO_ENCONTRADO = "NAO_ENCONTRADO"
MARCH_PARCIAL = "PARCIAL"  # confirmacao parcial, ainda conta como problematico

# Thresholds do MARCH (recalculados pelo orquestrador, NAO confia no agregado)
MARCH_TAXA_CONFIRMACAO_MINIMA = 0.80  # 80% das afirmacoes devem ser CONFIRMADO
MARCH_TAXA_NAO_ENCONTRADO_MAXIMA = 0.30  # maximo 30% de NAO_ENCONTRADO
MARCH_TOLERANCIA_CONTRADITO = 0  # ZERO tolerancia para CONTRADITO


# ============================================================================
# 7. CHAVES DO JSON DE AFIRMACOES (Atomizador)
# ============================================================================

CHAVE_AFIRMACOES_ID = "id"
CHAVE_AFIRMACOES_TEXTO = "texto"
CHAVE_AFIRMACOES_CATEGORIA = "categoria"
CHAVE_AFIRMACOES_CONTEXTO = "contexto"
CHAVE_AFIRMACOES_CAPITULO = "capitulo"
CHAVE_AFIRMACOES_CENA = "cena"

CATEGORIAS_AFIRMACAO_VALIDAS = [
    "fato_historico",
    "dado_numerico",
    "citacao_literal",
    "conceito_tecnico",
    "referencia_pessoa",
    "evento_cronologico",
    "localizacao_geografica",
    "relacao_pessoal",
    "regra_negocio",
    "procedimento",
]


# ============================================================================
# 8. CHAVES DO JSON DE RESULTADO MARCH
# ============================================================================

CHAVE_MARCH_RESULTADOS = "resultados"
CHAVE_MARCH_STATUS_GERAL = "status_geral"
CHAVE_MARCH_TAXA_CONFIRMADOS = "taxa_confirmados"
CHAVE_MARCH_AFIRMACAO_ID = "afirmacao_id"
CHAVE_MARCH_AFIRMACAO_TEXTO = "afirmacao_texto"
CHAVE_MARCH_STATUS = "status"
CHAVE_MARCH_EVIDENCIA = "evidencia"
CHAVE_MARCH_TRECHO_CORPUS = "trecho_corpus"
CHAVE_MARCH_JUSTIFICATIVA = "justificativa"


# ============================================================================
# 9. CHAVES DO JSON DE RESULTADO CONTINUIDADE
# ============================================================================

CHAVE_CONT_STATUS_GERAL = "status_geral"
CHAVE_CONT_ERROS = "erros"
CHAVE_CONT_TIPO_ERRO = "tipo_erro"
CHAVE_CONT_DESCRICAO = "descricao"
CHAVE_CONT_GRAVIDADE = "gravidade"
CHAVE_CONT_SUGESTAO = "sugestao"

TIPOS_ERRO_CONTINUIDADE_VALIDOS = [
    "personagem_inconsistente",
    "localizacao_errada",
    "timeline_quebrada",
    "conceito_mal_usado",
    "regra_violada",
    "voz_narrativa_diferente",
    "pov_inconsistente",
    "fio_narrativo_abandonado",
    "informacao_contradita",
]


# ============================================================================
# 10. CHAVES DO JSON DE METADADOS DO EDITOR
# ============================================================================

CHAVE_EDITOR_TIPO_EDICAO = "tipo_edicao"
CHAVE_EDITOR_ALTERACOES = "alteracoes"
CHAVE_EDITOR_PALAVRAS_ORIGINAIS = "palavras_originais"
CHAVE_EDITOR_PALAVRAS_FINAIS = "palavras_finais"
CHAVE_EDITOR_OBSERVACOES = "observacoes"
CHAVE_EDITOR_CHECKSUM_ORIGINAL = "checksum_original"
CHAVE_EDITOR_CHECKSUM_FINAL = "checksum_final"

TIPOS_EDICAO_VALIDOS = [
    "polimento_leve",       # troca de palavras, sem mexer em estrutura
    "reescrita_estrutural", # reescreve paragrafos inteiros
    "reescrita_completa",   # reescreve a cena inteira mantendo o sentido
]


# ============================================================================
# 10.5. REVISOR CEGO EDITORIAL (Acao 4)
# ============================================================================
# Constantes do agente Revisor Cego Editorial. Ele produz 3 categorias de
# problemas e classifica por gravidade.

REVISAO_PROBLEMAS_ESTRUTURA = "estrutura"     # tem forma de cena?
REVISAO_PROBLEMAS_CLAREZA = "clareza"         # texto se entende?
REVISAO_PROBLEMAS_RITMO = "ritmo"             # texto "respira" bem?

REVISAO_GRAVIDADE_BAIXA = "BAIXA"             # polemique, toleravel
REVISAO_GRAVIDADE_MEDIA = "MEDIA"             # prejudica experiencia
REVISAO_GRAVIDADE_ALTA = "ALTA"               # bloqueia compreensao

REVISAO_LIMITE_PROBLEMAS_ALTO = 1             # 1+ ALTO = REPROVADO
REVISAO_LIMITE_PROBLEMAS_MEDIO = 3            # 3+ MEDIOS = REPROVADO

REVISAO_GRAVIDADES_VALIDAS = [
    REVISAO_GRAVIDADE_BAIXA,
    REVISAO_GRAVIDADE_MEDIA,
    REVISAO_GRAVIDADE_ALTA,
]

# Tipos de problemas detectados em cada categoria
REVISAO_TIPOS_ESTRUTURA = [
    "abertura_fraca",              # cliche, acordando, descrevendo tempo
    "objetivo_pov_ausente",        # leitor sai sem saber o que o personagem quer
    "obstaculo_ausente",           # cena morna, nada impede
    "mudanca_estado_ausente",      # nada muda entre inicio e fim
    "fecho_resolutivo",            # resolve tudo, "e foram felizes"
    "fecho_resumo",                # resume demais em vez de abrir loop
    "proporcao_inadequada",        # muito curta ou muito longa
]

REVISAO_TIPOS_CLAREZA = [
    "ambiguidade",                 # sujeito ambiguo, "ele ligou para ele"
    "termo_sem_antecedente",       # pronome sem referente claro
    "jump_logico",                 # mudanca de cenario/tempo sem marcador
    "tell_excessivo",              # "ele estava com raiva" sem show
    "duplicidade",                 # mesma informacao repetida
]

REVISAO_TIPOS_RITMO = [
    "variacao_baixa",              # todas as frases do mesmo comprimento
    "ausencia_dialogo",            # cena sem nenhum dialogo (pode ser intencional)
    "dialogo_exclusivo",           # 100% dialogo sem acao narrativa
    "parede_texto",                # paragrafo com mais de 8 linhas
    "frase_longa_excessiva",       # frase com mais de 60 palavras
    "lista_explicativa",           # "primeiro, isso. segundo, aquilo." enumeração seca
    "seq_frases_curtas",           # 3+ frases seguidas com <8 palavras (texto martelado) — ALTA
    "sem_paragrafo_denso",         # menos de 70% de paragrafos densos (>=40 palavras)
    "abertura_responde_cedo",      # pergunta da abertura respondida no 1o/2o paragrafo — ALTA
    "fecho_teaser",                # ultima frase e imperativo seco/teaser sem eco reflexivo
    "fecho_repetido",              # fecho identico ou muleta repetida entre cenas — ALTA
    "ritmo_uniforme",              # desvio-padrao de paragrafo <40 ou falta de contraste
]

REVISAO_TIPOS_VOZ = [
    "abertura_nao_imersiva",       # abre com definicao/estatistica fria em vez de cena/pergunta
    "analogia_sem_3_movimentos",   # analogia sem mapeamento explicito em 3 movimentos
    "detalhe_redondo",             # numero arredondado em vez de assinatura exata
    "critica_conspiratoria",       # acusa lucro/ocultacao/patente — ALTA
    "abertura_mentira",            # 'Mentira.' como recurso de abertura — ALTA
    "fecho_sem_eco",               # ultima frase nao ressoa com a abertura
    "voz_imperativa",              # voz professoral imperativa dominante
]

REVISAO_TIPOS_PROBLEMAS_VALIDOS = (
    REVISAO_TIPOS_ESTRUTURA
    + REVISAO_TIPOS_CLAREZA
    + REVISAO_TIPOS_RITMO
    + REVISAO_TIPOS_VOZ
)

# Criterios padrao de aceitacao (podem ser sobrescritos por GENERO_*.md)
REVISAO_CRITERIOS_PADRAO = {
    "min_palavras": 500,            # abaixo disso, cena suspeita
    "max_palavras": 6000,           # acima disso, cena muito longa
    "max_frase_palavras": 60,       # frases acima disso sao excessivas
    "max_paragrafo_linhas": 8,      # paragrafos acima disso sao paredes
    "min_variacao_frases": 0.3,     # desvio padrao relativo do comprimento
    "max_tell_ratio": 0.6,          # ate 60% de tell e toleravel por cena
}


# ============================================================================
# 11. GENEROS BASE SUPORTADOS
# ============================================================================
# Lista dos generos que a skill oferece como base.

GENERO_ROMANCE = "ROMANCE"
GENERO_NAO_FICCAO = "NAO_FICCAO"
GENERO_MEMORIAS = "MEMORIAS"
GENERO_TECNICO = "TECNICO"
GENERO_PERSONALIZADO = "PERSONALIZADO"
GENERO_THRILLER = "THRILLER"          # v1.0 (Acao 2 do Episodio 02)
GENERO_COOKBOOK = "COOKBOOK"          # v1.0 (Acao 2 do Episodio 02)
GENERO_ACADEMICO = "ACADEMICO"        # v1.0 (Acao 2 do Episodio 02)
GENERO_PODBOOK_LEGACY = "PODBOOK_LEGACY"  # Genero legacy herdado de NAO_FICCAO v1.0, modelo especifico do projeto de Ecommerce ja produzido. NAO deve ser usado em novos livros.

# Alias deprecated: mantido por retrocompatibilidade. O nome canônico é
# GENERO_PODBOOK_LEGACY. Projetos antigos que referenciam "PODBOOK_BRUNO"
# continuam funcionando porque ambas as constantes resolvem pro mesmo valor.
GENERO_PODBOOK_BRUNO = "PODBOOK_LEGACY"  # DEPRECATED: use GENERO_PODBOOK_LEGACY

GENEROS_BASE_VALIDOS = [
    GENERO_ROMANCE,
    GENERO_NAO_FICCAO,
    GENERO_MEMORIAS,
    GENERO_TECNICO,
    GENERO_THRILLER,
    GENERO_COOKBOOK,
    GENERO_ACADEMICO,
    GENERO_PERSONALIZADO,
]

# Genero legacy listado separadamente: nao entra em GENEROS_BASE_VALIDOS
# porque nao deve aparecer como opcao na escolha inicial. Só eh carregado
# se o usuario explicitamente pedir o genero legacy pelo nome canonico
# (PODBOOK_LEGACY) ou pelo alias (PODBOOK_BRUNO).
GENEROS_LEGACY_VALIDOS = [
    GENERO_PODBOOK_LEGACY,
    GENERO_PODBOOK_BRUNO,  # alias
]


# ============================================================================
# 12. METADADOS DO CHECKSUM
# ============================================================================
# Configuracao do calculo de checksum.

CHECKSUM_ALGORITMO = "sha256"
CHECKSUM_TAMANHO = 8  # primeiros 8 caracteres do hash
CHECKSUM_VERSAO_ALGORITMO = "1.0"  # usado pra detectar drift de versao
CHECKSUM_SEPARADOR = ":"  # separador entre checksum e nome do arquivo (formato sha256sum)
CHECKSUM_TAMANHO_DEFAULT = 8  # alias de CHECKSUM_TAMANHO, usado como default em funcoes
FORMATO_HASH_ETIQUETADO = "v{versao}:{hash}"  # formato do hash com etiqueta de versao
FORMATO_BASELINE_JSON = {
    "versao_algoritmo": str,
    "algoritmo": str,
    "tamanho_hash": int,
    "total_arquivos": int,
    "checksums": dict,
}


# ============================================================================
# 13. LIMITES E GATES DA SKILL
# ============================================================================

MAX_RETRIES_POR_CENA = 3  # teto de tentativas de reescrita cirurgica
MAX_CHAMADAS_POR_PROJETO = 200  # limite soft de chamadas de API
TAXA_DISFLUENCIA_MINIMA_PODCAST = 0.30  # 30% das falas devem ter disfluencia

# Alocacao dinamica de cenas por densidade do corpus (Acao da discussao de 2026-08-06)
# O Orquestrador mede o tamanho do modulo de corpus por capitulo e decide quantas
# cenas ele merece. Quanto mais denso o material, mais cenas (ate 4). Quanto mais
# direto, menos cenas (ate 1). Os thresholds e numeros sao configuraveis aqui.
CONFIGURACAO_ALOCACAO_CENAS = {
    # Thresholds de densidade, medidos em palavras-por-subtopico
    # (onde "subtopico" = quebra logica do material: header, topico, conceito distinto)
    "direto_palavras_por_subtopico_max": 3000,   # abaixo disso = direto
    "medio_palavras_por_subtopico_max": 6000,   # entre direto e medio = medio
    # acima de medio_palavras_por_subtopico_max = denso

    # Quantidade de cenas recomendada por densidade
    "direto_cenas_recomendadas": 1,
    "medio_cenas_recomendadas": 2,
    "denso_cenas_recomendadas": 4,

    # Limites maximos e minimos (tetos de seguranca, mesmo que a heuristica erre)
    "cenas_minimo_absoluto": 1,    # nenhum capitulo pode ter 0 cenas
    "cenas_maximo_absoluto": 6,    # nenhum capitulo pode ter mais que 6 (anti-monstro)
}

# Padroes de cenas por arquetipo de genero (sobreposicao opcional acima da densidade)
# Se o genero definir cenas_fixas_por_capitulo, a alocacao usa esse numero
# em vez do calculado por densidade. Util pra livros com cadencia rigida
# (ex: Cookbook com 5 receitas por capitulo, Academia com 3 secoes por cap).
CONFIGURACAO_CENAS_POR_ARQUETIPO = {
    "TRES_ATOS": 4,                  # romance classico: setup, complic, turno, resolucao
    "JORNADA_HEROI": 5,             # epico: 12 estagios divididos em 5 cenas
    "PROBLEMA_SOLUCAO": 3,          # nao-ficcao: problema, causa, solucao (default)
    "GRANDE_IDEIA": 3,              # ciencia popular: paradigma, insight, implicacao
    "BIOGRAFIA": 4,                 # biografia: 4 atos da vida
    "INVESTIGATIVO": 3,             # jornalismo: 3 camadas de investigacao
    "SABEDORIA_ACUMULADA": 2,       # filosofia: 2 angulos (premissa, reflexao)
    "TUTORIAL_PROGRESSIVO": 3,      # tecnico: 3 niveis (basico, intermediario, avancado)
    "REFERENCIA_TOPICO": 1,         # tecnico: 1 topico por secao
    "COOKBOOK_RECEITAS": 1,         # cookbook: 1 receita = 1 cena
    "GUIA_CAMPO": 1,                # guia de campo: 1 procedimento/sintoma = 1 cena
    "DOCUMENTACAO_API": 1,          # doc tecnica: 1 endpoint = 1 cena
    "TEMATICO": 3,                  # memoir: 3 memorias por capitulo
    "CRONOLOGICO": 2,               # memoir: 2 eventos por capitulo
    "FRAGMENTADO": 5,               # memoir experimental: 5 vignettes
    "MONOGRAFIA": 4,                # academia: 4 argumentos centrais
    "LIVRO_TEXTO": 3,              # academia: 3 conceitos por capitulo
    "PAPER_DERIVADO": 2,            # academia: 2 papers por capitulo
    "TRATADO_TECNICO": 1,          # academia: 1 topico enciclopedico
    "ENSAIO_HUMANITIES": 2,         # academia: 2 angulos de argumento
    "MISTERIO_DETETIVE": 4,         # thriller: crime, pistas, red herring, resolucao
    "PSICOLOGICO": 3,              # thriller: setup, rachadura, confronto
    "ESPIONAGEM": 3,               # thriller: missao, complicacao, confronto
    "TERROR": 4,                    # thriller: evento catalisador, escalada, confronto, ambiguidade
    "INGREDIENTE_ESTRELA": 4,      # cookbook: 4 tecnicas por ingrediente
    "TECNICA": 4,                   # cookbook: 4 receitas por tecnica
    "REFEICAO_OCASIAO": 3,         # cookbook: entrada, principal, sobremesa
    "SAZONAL": 3,                   # cookbook: 3 receitas por estacao
    "COZINHA_CULTURA": 4,           # cookbook: entrada, principal, acompanhamento, sobremesa
}

# Default usado quando o arquetipo nao esta mapeado acima
CONFIGURACAO_CENAS_POR_ARQUETIPO_DEFAULT = 3


# ============================================================================
# 14. EXTENSOES DE ARQUIVO POR TIPO
# ============================================================================

EXTENSAO_MD = ".md"
EXTENSAO_JSON = ".json"
EXTENSAO_EPUB = ".epub"
EXTENSAO_PDF = ".pdf"
EXTENSAO_TXT = ".txt"
EXTENSAO_BAK = ".bak"
EXTENSAO_TMP = ".tmp"


# ============================================================================
# 15. MENSAGENS PADRAO DE ERRO
# ============================================================================
# Mensagens canonicas que aparecem em logs e relatorios.

ERRO_ARQUIVO_NAO_ENCONTRADO = "Arquivo nao encontrado"
ERRO_CHECKSUM_INCONSISTENTE = "CHECKSUM INCONSISTENTE: o arquivo no disco nao corresponde ao que foi registrado no estado. A cena precisa ser revista."
ERRO_CEGUEIRA_VIOLADA_MARCH = "VIOLACAO: prompt do Validador MARCH continha a saida do Escritor. Cegueira violada."
ERRO_RETRIES_EXCEDIDOS = "Excedeu 3 tentativas de reescrita cirurgica"
ERRO_GENERO_NAO_ENCONTRADO = "Genero nao encontrado. Verifique o nome ou crie um personalizado."
ERRO_CORPUS_NAO_ENCONTRADO = "Corpus nao encontrado no caminho especificado."
ERRO_PIPELINE_INCOMPLETO = "Pipeline incompleto. Arquivos do worktree estao faltando."


# ============================================================================
# 16. FUNCOES UTILITARIAS DE CAMINHO
# ============================================================================
# Helpers que operam sobre as constantes acima.

def caminho_raiz(projeto_path):
    """Retorna o caminho raiz do projeto."""
    return projeto_path


def caminho_capitulos(projeto_path):
    """Retorna o caminho completo da pasta capitulos/."""
    return f"{projeto_path}/{PASTA_CAPITULOS}"


def caminho_capitulo(projeto_path, numero_capitulo):
    """Retorna o caminho completo de um capitulo especifico."""
    return f"{caminho_capitulos(projeto_path)}/{formatar_pasta_capitulo(numero_capitulo)}"


def caminho_cena(projeto_path, numero_capitulo, numero_cena):
    """Retorna o caminho completo de uma cena especifica."""
    return f"{caminho_capitulo(projeto_path, numero_capitulo)}/{formatar_pasta_cena(numero_cena)}"


def caminho_arquivo_cena(projeto_path, numero_capitulo, numero_cena, nome_arquivo):
    """Retorna o caminho completo de um arquivo dentro do worktree de uma cena."""
    return f"{caminho_cena(projeto_path, numero_capitulo, numero_cena)}/{nome_arquivo}"


def caminho_bible(projeto_path):
    """Retorna o caminho completo do arquivo bible_da_obra.md."""
    return f"{projeto_path}/{PASTA_BIBLE}/{BIBLE_DA_OBRA_ARQ}"


def caminho_estado(projeto_path):
    """Retorna o caminho completo do arquivo estado_da_obra.md."""
    return f"{projeto_path}/{PASTA_ESTADO}/{ESTADO_DA_OBRA_ARQ}"


def caminho_controle(projeto_path):
    """Retorna o caminho completo do arquivo CONTROLE_DA_OBRA.md."""
    return f"{projeto_path}/{CONTROLE_DA_OBRA_ARQ}"


def caminho_livro_capitulo(projeto_path, numero_capitulo):
    """Retorna o caminho completo do livro_capitulo_NN.md."""
    return f"{projeto_path}/{PASTA_CAPITULOS}/{formatar_livro_capitulo(numero_capitulo)}"


def caminho_livro_final(projeto_path):
    """Retorna o caminho completo do livro_final.md."""
    return f"{projeto_path}/{LIVRO_FINAL_ARQ}"


def caminho_backup(caminho_original):
    """Retorna o caminho do backup de um arquivo (sufixo .bak)."""
    return f"{caminho_original}.bak"


def caminho_tmp(caminho_original):
    """Retorna o caminho temporario de um arquivo (sufixo .tmp) pra salvamento atomico."""
    return f"{caminho_original}.tmp"


# ============================================================================
# 17. MAPA DE ISOLAMENTO (Acao 5 / Eixo 2 do Episodio 03)
# ============================================================================
# Define quais arquivos cada acao pode tocar, pra suportar paralelismo seguro.
# Usado quando a gente for implementar o trabalho paralelo entre agentes.

AGENTES_DA_SKILL = [
    "orquestrador",
    "escritor",
    "atomizador",
    "validador_march",
    "validador_continuidade",
    "editor",
    "consolidador",
    "controle_da_obra",
    "revisor_cego_editorial",  # novo ator da Acao 4
]

ACOES_DA_SKILL = [
    "acao_1_controle_da_obra",        # ja feita
    "acao_2_reescrever_generos",      # pendente
    "acao_3_utils_checksum",          # pendente
    "acao_4_revisor_cego_editorial",  # pendente
    "acao_5_utils_constantes",        # esta acao
]


# ============================================================================
# 18. METADADOS DA PROPRIA SKILL
# ============================================================================

SKILL_NOME = "skills_book"
SKILL_VERSAO = "1.1-rc2"
SKILL_EDITING = "Greenforged Edition"
SKILL_DATA_CRIACAO = "2026-07-27"
SKILL_DATA_ULTIMA_REVISAO = "2026-08-08"
# v1.1-rc1 (2026-08-08): correcoes do incidente do teste_04 — bloco RITMO_*
# canonico (secao 21), vigia com baseline correto do Revisor Cego e formato de
# checksum validado, checks de ritmo a prova de inversao, invariante de
# linhagem no loop de reescrita.
# v1.1-rc2 (2026-08-08): medidor de ritmo deterministico (utils/medir_ritmo.py)
# e checagem anti-carimbo no vigia: o Revisor Cego so aprova com o bloco
# metricas_ritmo real do script; aprovacao "por nota" e reprovada.
SKILL_BASEADA_EM = "Skills Podcast 4.0.1 (Greenforged Edition) + Greenforge System"


# ============================================================================
# 19. NIVELAMENTO EDITORIAL (Acao 6 do Episodio 03)
# ============================================================================
# O Nivelamento Editorial captura, via 4 perguntas de multipla escolha, as
# preferencias editoriais do usuario ANTES de comecar qualquer projeto novo.
# Surgiu do diagnostico: a versao antiga da skill produziu um capitulo da Agua
# muito melhor que a versao nova porque a antiga tinha um `foco_usuario` muito
# mais detalhado e especifico. A solucao eh institucionalizar essa captura de
# preferencias na propria skill, em vez de depender de o usuario fornecer
# instrucoes ricas manualmente.
#
# O Orquestrador (Passo 3.2 do BOOT) faz as 4 perguntas no inicio de todo
# projeto novo. As respostas sao salvas no campo `perfil_editorial` da Bible
# (e espelhadas no Estado) e ficam disponiveis pro Escritor em todas as cenas.
#
# Cada eixo tem 3 opcoes (A, B, C) e o sistema aceita resposta unica por eixo.
# Se o usuario nao souber responder, o Orquestrador usa o DEFAULT abaixo
# (4 respostas "A", validadas como o "perfil mais consistente" no diagnostico
# editorial do projeto).
#
# **IMPORTANTE:** o Nivelamento NAO substitui o `foco_usuario` livre. O
# usuario SEMPRE pode adicionar instrucoes extras depois do nivelamento.
# O nivelamento captura o "perfil padrao"; o foco_usuario captura os
# "ajustes finos deste projeto especifico".

# Chaves dos 4 eixos do nivelamento (usadas no JSON do perfil_editorial)
NIVELAMENTO_CHAVE_ABERTURA = "estilo_abertura"
NIVELAMENTO_CHAVE_DENSIDADE = "densidade_livro"
NIVELAMENTO_CHAVE_ANALOGIAS = "densidade_analogias"
NIVELAMENTO_CHAVE_VOZ = "voz_autor"

# Letras das opcoes (padrao multipla escolha A/B/C)
NIVELAMENTO_OPCAO_A = "A"
NIVELAMENTO_OPCAO_B = "B"
NIVELAMENTO_OPCAO_C = "C"
NIVELAMENTO_OPCOES_VALIDAS = [NIVELAMENTO_OPCAO_A, NIVELAMENTO_OPCAO_B, NIVELAMENTO_OPCAO_C]

# --- EIXO 1: ESTILO DE ABERTURA ---
# Como a cena de abertura de cada capitulo deve comecar.
NIVELAMENTO_ABERTURA_OPCOES = {
    NIVELAMENTO_OPCAO_A: "imersao_pergunta_retorica",  # sempre comecar com cena mental + pergunta
    NIVELAMENTO_OPCAO_B: "direto_ao_ponto",            # afirma a tese logo na primeira linha
    NIVELAMENTO_OPCAO_C: "caso_concreto_antes",        # caso real/vinheta antes de explicar
}

# --- EIXO 2: DENSIDADE DO LIVRO ---
# Quantas palavras o livro deve ter no total e por cena.
NIVELAMENTO_DENSIDADE_OPCOES = {
    NIVELAMENTO_OPCAO_A: {
        "nome": "denso",
        "palavras_total_alvo": 250000,
        "palavras_por_cena_min": 800,
        "palavras_por_cena_max": 1500,
    },
    NIVELAMENTO_OPCAO_B: {
        "nome": "medio",
        "palavras_total_alvo": 120000,
        "palavras_por_cena_min": 500,
        "palavras_por_cena_max": 900,
    },
    NIVELAMENTO_OPCAO_C: {
        "nome": "enxuto",
        "palavras_total_alvo": 60000,
        "palavras_por_cena_min": 300,
        "palavras_por_cena_max": 600,
    },
}

# --- EIXO 3: DENSIDADE DE ANALOGIAS ---
# Quantas analogias/metaforas visuais por cena.
NIVELAMENTO_ANALOGIAS_OPCOES = {
    NIVELAMENTO_OPCAO_A: {
        "nome": "alta",
        "analogias_por_cena_min": 1,
        "analogias_por_cena_max": 2,
    },
    NIVELAMENTO_OPCAO_B: {
        "nome": "media",
        "analogias_por_cena_min": 0,
        "analogias_por_cena_max": 1,
    },
    NIVELAMENTO_OPCAO_C: {
        "nome": "baixa",
        "analogias_por_cena_min": 0,
        "analogias_por_cena_max": 0,
    },
}

# --- EIXO 4: VOZ DO AUTOR ---
# Como o narrador se posiciona no texto.
NIVELAMENTO_VOZ_OPCOES = {
    NIVELAMENTO_OPCAO_A: "revelacao_respeitosa",  # cumplice, critica ao sistema, nunca a pessoas (DNA da marca)
    NIVELAMENTO_OPCAO_B: "neutra_engajada",                  # narrador invisivel mas preocupado com clareza
    NIVELAMENTO_OPCAO_C: "academica_distante",               # narrador onisciente, formal, sem opiniao
}

# Default do nivelamento (4 respostas "A", validadas em 2026-08-06 como o
# "perfil editorial consistente" usado como padrao da skill)
# Quando o usuario nao souber responder, o Orquestrador usa estes valores.
NIVELAMENTO_DEFAULT = {
    NIVELAMENTO_CHAVE_ABERTURA: NIVELAMENTO_OPCAO_A,
    NIVELAMENTO_CHAVE_DENSIDADE: NIVELAMENTO_OPCAO_A,
    NIVELAMENTO_CHAVE_ANALOGIAS: NIVELAMENTO_OPCAO_A,
    NIVELAMENTO_CHAVE_VOZ: NIVELAMENTO_OPCAO_A,
}

# Comportamento do nivelamento
NIVELAMENTO_OBRIGATORIO = True  # se True, Orquestrador NAO comeca o projeto sem as 4 respostas
NIVELAMENTO_QUANTOS_EIXOS = 4
NIVELAMENTO_PERGUNTAS_POR_VEZ = 1  # faz 1 pergunta por mensagem, espera resposta, faz a proxima

# Onde o nivelamento eh persistido (decisao: "Bible + espelho no Estado" = redundancia controlada)
NIVELAMENTO_PERSISTIR_BIBLE = True
NIVELAMENTO_PERSISTIR_ESTADO = True

# Caminho do campo na Bible (sob Metadados Gerais)
NIVELAMENTO_BIBLE_CAMPO = "perfil_editorial"
NIVELAMENTO_ESTADO_CAMPO = "perfil_editorial"


# ============================================================================
# 20. VIGIA DA FABRICA (Camada A — integridade e linhagem)
# ============================================================================
LOG_VIGIA_ARQ = "_log_vigia.md"                  # relatorio do vigia por cena
STATUS_CENA_REPROVADO_VIGIA = "REPROVADO_VIGIA"  # vigia reprovou a cena
VIGIA_SCRIPT = "utils/vigia_integridade.py"      # caminho do script (CLI)
CAMPO_INPUT_CHECKSUM = "input_checksum"          # campo de linhagem exigido dos validadores

# Contrato de voz (Revelacao Respeitosa) — quando ativo, o Revisor Cego
# roda desde o capitulo 1 e avalia a categoria "voz".
CONTRATO_VOZ_ATIVADO_GENEROS = ("NAO_FICCAO", "MEMORIAS", "PERSONALIZADO")


# ============================================================================
# 21. CONTRATO DE RITMO — NUMEROS CANONICOS (fonte unica — Acao do diagnostico
# 2026-08-08, incidente do teste_04)
# ============================================================================
# Estes valores sao a UNICA fonte de verdade para o contrato de ritmo
# ("prosa de rio"). Escritor, Editor e Revisor Cego referenciam estes nomes;
# nenhum arquivo de que definha skill deve hardcodar outros numeros para os
# mesmos criterios. A banda 12-22 foi a validada na rubrica do teste externo
# (validacao_teste_01.md); o texto de referencia de excelencia tem media 20.
#
# COMO MEDIR (qualquer agente, inclusive o Revisor Cego):
# - FRASE: trecho terminado por . ! ? ou ... seguido de espaco/quebra.
# - PARAGRAFO: bloco de texto separado por linha em branco.
# - "curtas seguidas": sequencia ininterrupta de frases com menos de
#   RITMO_FRASE_CURTA_PALAVRAS palavras.
# - desvio-padrao do paragrafo: desvio (populacional) do numero de palavras
#   de cada paragrafo da cena.

RITMO_MEDIA_FRASE_MIN = 12            # media de palavras por frase: banda canonica 12-22
RITMO_MEDIA_FRASE_MAX = 22
RITMO_FRASE_CURTA_PALAVRAS = 8        # frase "curta" = menos de 8 palavras
RITMO_MAX_SEQ_FRASES_CURTAS = 2       # nunca 3+ frases curtas consecutivas (climax raro)
RITMO_PARAGRAFO_DENSO_PALAVRAS = 40   # paragrafo "denso" = 40+ palavras
RITMO_PCT_PARAGRAFOS_DENSOS_MIN = 70  # >=70% dos paragrafos devem ser densos
RITMO_DESVIO_PARAGRAFO_MIN = 40       # contraste entre paragrafos (rio, nao monotonia)
RITMO_RESPOSTA_ABERTURA_JANELA = (3, 6)  # a pergunta-gancho deve ser respondida entre o P3 e o P6
RITMO_FECHO_MIN_PALAVRAS = 15         # fecho reflexivo e redondo
RITMO_FECHO_MAX_PALAVRAS = 25
RITMO_PAREDE_PALAVRAS = 100           # PARAGRAFO longo so conta como "parede" se tiver
                                      # mais de 100 palavras E a cena tiver desvio < RITMO_DESVIO_PARAGRAFO_MIN
                                      # (paragrafo longo em cena com contraste NUNCA e parede;
                                      #  o texto-ouro tem paragrafos de ~170 palavras)

# Respiro = paragrafo LEVE de 1 a 3 frases com 8 a 20 palavras cada.
# Respiro NAO e sequencia de frases-pedaco de 1 a 4 palavras — isso e martelada,
# exatamente o que RITMO_MAX_SEQ_FRASES_CURTAS proibe.
