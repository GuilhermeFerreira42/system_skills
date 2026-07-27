# GENERO: TECNICO / MANUAL / HOW-TO / DOCUMENTACAO

**Versao:** 1.0
**Tipo:** TECNICO
**Estrutura:** Modulos -> Topicos -> Passos (hierarquia clara, referencia rapida)

---

## Voz Narrativa

- **pessoa:** `2a_imperativa` (voce faca isto) | `3a_instrutiva` (o usuario faz isto)
- **tempo_verbal:** `presente` (instrucoes atemporais)
- **distancia:** `instrutora`, `direta`, `sem_ambiguidades`
- **tom:** `profissional`, `claro`, `encorajador_sem_ser_informal`, `escaneavel`
- **vocabulario:** `tecnico_preciso` (termo definido no primeiro uso) | `padrao_industria`
- **ritmo:** `linear`, `modular`, `referenciavel` (nao narrativo)

## POV

- **padrao:** `autor_tecnico` (voz unica da documentacao)
- **multi_pov:** `false`

## Estrutura de "Cena" (Unidade = Topico/Procedimento)

- **min_palavras:** 200
- **max_palavras:** 1500
- **beats_obrigatorios:** `["objetivo_claro", "pre_requisitos", "passos_numerados", "resultado_esperado", "troubleshooting_comum", "proximos_passos"]`
- **show_minimo:** 30% (capturas de tela, outputs, diagramas, exemplos de codigo, configs)
- **gancho_tipos:** `["problema_resolvido", "meta_atingida", "erro_evitado"]`
- **fecho_tipos:** `["verificacao_sucesso", "link_relacionado", "exercicio_pratica"]`

## Estrutura de Capitulo (Modulo)

- **topicos_por_modulo:** 4-10
- **ordem:** `dependencias_primeiro` (fundamentos -> avancado)
- **recap_final:** `true` (resumo + checklist + links)

## Estrutura Global

### Opcao A: Tutorial Progressivo (Aprenda Fazendo)
1. Introducao & Setup
2. Hello World / Primeiro Sucesso
3. Conceitos Fundamentais (1 por capitulo)
4. Casos de Uso Comuns
5. Padroes Avancados
6. Producao / Boas Praticas
7. Troubleshooting & FAQ
8. Apindice / Referencia Rapida

### Opcao B: Referencia por Topico (Manual de Consulta)
- Capitulos = Areas funcionais (Autenticacao, Database, API, Deploy, Monitoramento)
- Cada topico autocontido
- Cross-references pesados

### Opcao C: Cookbook / Receitas (Solucao de Problemas)
- Capitulos = Categorias de problema
- Cada "cena" = Uma receita completa: Problema -> Solucao -> Explicacao -> Variacoes

### Opcao D: Documentacao de API / SDK
- Referencia completa (endpoints, params, responses, codigos erro)
- Guias de inicio rapido
- Exemplos em multi-linguagens
- Changelog / Migracao

## Bible Requisitos

- **conceitos_chave:** `true` (glossario tecnico, siglas, termos canonicos)
- **versoes_suportadas:** `true` (versao minima, depreciacoes, roadmap)
- **dependencias:** `true` (versoes exatas, compatibilidade)
- **ambientes:** `true` (OS, runtime, container, cloud)
- **exemplos_canonicos:** `true` (projetos referencia, repos oficiais)
- **erros_comuns:** `true` (lista de erros, causa, solucao)
- **checklists_verificacao:** `true` (pre-deploy, pos-migracao, security audit)
- **faq_vivo:** `true` (atualizado com suporte)
- **changelog:** `true`

## Validacoes Extras (Editor)

- **exige_editor:** `true` (tecnico writer / dev advocate review)
- **regras_editor:**
  - `precisao_tecnica` (comando funciona, versao correta)
  - `completude` (nao pula passos "obvios")
  - `testabilidade` (leitor pode verificar se funcionou)
  - `escaneabilidade` (headers, code blocks, bold, lists, tables)
  - `atualidade` (versoes, links nao quebrados, depreciacoes marcadas)
  - `acessibilidade` (alt text, contraste, plain language)
  - `seguranca` (nao ensina anti-patterns perigosos)
  - `consistencia_terminologica` (mesmo termo = mesma coisa sempre)

## Foco Padrao do Usuario

> "Cada procedimento deve ser testavel. Se o leitor seguir os passos e nao funcionar, o documento falhou. Inclua output esperado. Marque versoes. Avise sobre breaking changes."