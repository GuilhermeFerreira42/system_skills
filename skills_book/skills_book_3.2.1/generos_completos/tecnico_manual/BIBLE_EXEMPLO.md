# Bible da Obra: Python para Iniciantes — Do Zero ao Primeiro Projeto (EXEMPLO TECNICO_MANUAL)

## Metadados Gerais
- **Titulo:** Python para Iniciantes — Do Zero ao Primeiro Projeto
- **Subtitulo:** Um manual prático de programação para quem nunca programou
- **Genero:** TECNICO_MANUAL
- **Subgenero:** Tutorial de programação
- **Publico_alvo:** Pessoas sem experiência prévia em programação que querem aprender Python
- **Tom_de_voz:** Objetivo, didático, direto, paciente
- **POV_padrao:** 2ª pessoa ("você") com 3ª autoral ("nós") em explicações conceituais
- **Tempo_verbal:** Presente (instruções) e imperativo (comandos)
- **Distancia_narrativa:** Instrutiva (professor paciente)
- **Vocabulario_nivel:** Técnico com termos introduzidos gradualmente
- **Ritmo_padrao:** Linear, procedural (passo a passo)
- **Extensao_por_cena:** 500-2.000 palavras
- **Formato_do_fim:** Resumo + Checklist
- **Versao_bible:** v1.0

---

## Premissa & Estrutura
- **Logline:** Um iniciante completo aprende Python do zero até construir seu primeiro projeto funcional, sem pular etapas e sem jargon sem explicação.
- **Tema_central:** Programação não é magia, é prática deliberada com conceitos claros
- **Pergunta_tematica:** Como alguém que nunca programou pode aprender Python de forma estruturada, sem desistir no meio?
- **Estrutura_narrativa:** PROBLEMA_SOLUCAO (problema = falta de conhecimento; solução = método sequencial)
- **Numero_estimado_capitulos:** 20
- **Numero_estimado_cenas:** 60
- **Palavras_estimadas_total:** ~60.000

---

## Pré-requisitos (declarados no Capítulo 1)

| Item | Versão | Como verificar |
|------|--------|----------------|
| Python | 3.10+ | `python --version` no terminal |
| Editor de código | VSCode, PyCharm Community, ou similar | Instalado e aberto |
| Sistema operacional | Windows 10+, macOS 11+, ou Linux Ubuntu 20+ | Qualquer um serve |
| Vontade de praticar | 30-60 min/dia por 8 semanas | Compromisso pessoal |

---

## Glossário Técnico (Regras Rígidas)

| Termo | Definição Canônica | Regra Rígida? |
|-------|-------------------|---------------|
| **Variável** | Nome que armazena um valor na memória. | SIM |
| **String** | Sequência de caracteres delimitada por aspas. | SIM |
| **Função** | Bloco de código reutilizável, definido com `def`. | SIM |
| **Lista** | Coleção ordenada e mutável de itens, definida com `[]`. | SIM |
| **Dicionário** | Coleção de pares chave-valor, definida com `{}`. | SIM |
| **Loop for** | Estrutura de repetição que itera sobre uma sequência. | SIM |
| **Loop while** | Estrutura de repetição que executa enquanto condição for verdadeira. | SIM |
| **Condicional if** | Estrutura que executa código se condição for verdadeira. | SIM |
| **Classe** | Modelo para criar objetos, definida com `class`. | SIM |
| **Módulo** | Arquivo Python que pode ser importado. | SIM |
| **Pacote** | Coleção de módulos organizados em diretório com `__init__.py`. | SIM |
| **pip** | Gerenciador de pacotes padrão do Python. | SIM |
| **venv** | Módulo padrão para criar ambientes virtuais isolados. | SIM |

---

## Conceitos-Chave (Marcos de Progressão)

| Marco | Quando | Pré-requisito |
|-------|--------|---------------|
| Instalar Python e rodar primeiro "Hello, World!" | Cap 2 | Python 3.10+ |
| Usar variáveis e tipos básicos | Cap 3 | Cap 2 |
| Ler input do usuário | Cap 4 | Cap 3 |
| Usar condicionais (if/elif/else) | Cap 5 | Cap 4 |
| Usar loops (for/while) | Cap 6 | Cap 5 |
| Criar e chamar funções | Cap 7 | Cap 6 |
| Trabalhar com listas e dicionários | Cap 8-9 | Cap 7 |
| Ler e escrever arquivos | Cap 10 | Cap 9 |
| Tratar erros com try/except | Cap 11 | Cap 10 |
| Usar módulos da biblioteca padrão | Cap 12 | Cap 11 |
| Instalar pacotes com pip | Cap 13 | Cap 12 |
| Criar ambientes virtuais | Cap 14 | Cap 13 |
| Entender classes e objetos | Cap 15-16 | Cap 14 |
| Importar módulos próprios | Cap 17 | Cap 16 |
| Projeto final: agenda de contatos | Cap 18-20 | Cap 17 |

---

## Estrutura dos Capítulos (template)

Cada capítulo segue este template:

1. **Título do capítulo** (reflete o conceito)
2. **Pré-requisitos** (lista do que o leitor deve ter visto antes)
3. **O que você vai aprender** (3-5 bullets)
4. **Conceito principal** (explicação técnica)
5. **Exemplo prático** (código que roda)
6. **Explicação linha por linha** (quando relevante)
7. **Erro comum** (opcional)
8. **Prática** (exercício para o leitor fazer sozinho)
9. **Resolução da prática** (opcional, com spoiler)
10. **Resumo** (recapitulação)
11. **Checklist** (4 itens)
12. **Pré-requisito para o próximo capítulo** (aviso)

---

## Mitos / Erros Comuns a Desconstruir

| Mito/Erro | Verdade | Onde |
|-----------|---------|------|
| "Programação é para gênios" | Não. É prática deliberada. | Cap 1 |
| "Preciso decorar sintaxe" | Não. Você consulta a documentação. | Cap 3 |
| "Python é lento" | Para a maioria dos casos, é rápido o suficiente. | Cap 13 |
| "Se der erro, é porque eu sou burro" | Erros são normais. Ler o erro é parte do aprendizado. | Cap 11 |
| "Preciso entender tudo antes de praticar" | Não. Prática gera perguntas, perguntas geram entendimento. | Cap 1 |

---

## Dependências entre Capítulos

| Cap | Depende de | Próximo desbloqueia |
|-----|-----------|---------------------|
| 1 | Nenhum | 2 |
| 2 | 1 | 3 |
| 3 | 2 | 4, 5 |
| 4 | 3 | 5 |
| 5 | 4 | 6 |
| 6 | 5 | 7 |
| 7 | 6 | 8 |
| 8 | 7 | 9 |
| 9 | 8 | 10 |
| 10 | 9 | 11 |
| 11 | 10 | 12 |
| 12 | 11 | 13 |
| 13 | 12 | 14 |
| 14 | 13 | 15 |
| 15 | 14 | 16 |
| 16 | 15 | 17 |
| 17 | 16 | 18 |
| 18-20 | 17 | Projeto final |

---

## Decisões Editoriais Travadas

| Decisão | Justificativa |
|---------|---------------|
| POV padrão: 2ª pessoa | Instruções diretas, "você faz X" |
| Python 3.10+ como mínimo | Versões anteriores sem features importantes (match-case, etc.) |
| Cada capítulo = 1 conceito principal | Evita sobrecarga cognitiva |
| Código SEMPRE executável | Nada de pseudo-código quebrado |
| Erro comum em cada capítulo | Prepara o leitor para frustrações reais |
| Resumo + Checklist no fim | Reforça o aprendizado e valida pré-requisitos |
| Sem história pessoal do autor | Tom impessoal, técnico |

---

## Fontes do Corpus

Esta obra é baseada em:
- Documentação oficial do Python (https://docs.python.org/3/)
- PEPs relevantes (PEP 8, PEP 20)
- Prática pedagógica de cursos introdutórios de Python
- Padrões da comunidade Python

O corpus inclui tutoriais oficiais, exemplos validados, e referências a bibliotecas padrão. **SEM** material de marketing ou "compre o curso avançado".

---

## Checklist de Integridade
- [x] Pré-requisitos definidos
- [x] Glossário com termos canônicos
- [x] Conceitos-chave com pré-requisitos
- [x] Template de capítulo definido
- [x] Mitos/erros comuns mapeados
- [x] Dependências entre capítulos claras
- [x] Decisões travadas
- [x] Sem material de marketing

