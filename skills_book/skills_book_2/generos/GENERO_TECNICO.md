# GENERO: TECNICO (Manual, How-To, Documentação, Procedimento, Receita Estruturada, Guia de Campo)

**Versao:** 2.0 (Greenforged Edition - Agnóstico de domínio)
**Tipo:** TECNICO
**Estrutura:** Módulos → Tópicos → Passos (hierarquia clara, referência rápida)

**Mudanças da v1.0 pra v2.0:**
- Removido viés implícito pra tech/software (autenticação, database, API, deploy).
- Adicionados subgêneros de domínio físico, artesanal, agrícola, culinário, automotivo, manutenção, jurídico-administrativo.
- Mantidos os 4 arquétipos clássicos (Tutorial Progressivo, Referência por Tópico, Cookbook, Documentação de API), agora interpretados de forma ampla.
- Adicionado arquétipo novo: "Guia de Campo / Manual Portátil" (uso offline, índice lateral, busca por sintoma).
- Estrutura de "passo" generalizada: não é só código, é qualquer instrução executável.

---

## Voz Narrativa

- **pessoa:**
  - `2a_imperativa` (você faça isto) — padrão em tutoriais
  - `3a_instrutiva` (o usuário faz isto / o operador deve...) — manual corporativo
  - `1a_oficial` (eu, o autor, recomendo) — manual assinado, prefácio do especialista
- **tempo_verbal:**
  - `presente` (instruções atemporais) — padrão, "Conecte o cabo vermelho no terminal positivo"
  - `imperativo` (faça isto, não faça aquilo) — listas numeradas
  - `passado` (em caso de troubleshooting: "se o led estava apagado, isso indica...")
- **distancia:**
  - `instrutora`, `direta`, `sem_ambiguidades` — padrão
  - `didatica` (explica o "porquê" antes do "como") — manuais educacionais
  - `consultiva` (resposta a perguntas, não narrativa) — FAQs, base de conhecimento
- **tom:** varia por subgênero. Lista sugerida (escolha 3-4 adjetivos):
  - Software/Digital: `profissional`, `claro`, `escaneável`, `técnico-preciso`
  - Manutenção/Reparo: `objetivo`, `seguro`, `preventivo`, `metódico`
  - Culinária/Craft: `acolhedor`, `preciso`, `didático`, `encorajador`
  - Jurídico/Administrativo: `formal`, `cuidadoso`, `exaustivo`, `técnico-rigoroso`
  - Agrícola/Campo: `prático`, `sazonal`, `observacional`, `tradicional-moderno`
- **vocabulario:**
  - `tecnico_preciso` (termo definido no primeiro uso) — padrão
  - `padrao_industria` (nomenclatura oficial)
  - `cotidiano` (linguagem do dia-a-dia) — manuais domésticos
  - `cientifico` (papers, terminologia acadêmica) — manuais médicos, científicos
- **ritmo:**
  - `linear`, `modular`, `referenciavel` (não narrativo) — padrão
  - `passo_a_passo` (1, 2, 3, ...) — procedimento
  - `diagnostico_tratamento` (sintoma → causa → solução) — troubleshooting

## POV

- **padrao:** `autor_tecnico` (voz única da documentação) ou `equipe_tecnica` (manual assinado por um coletivo)
- **multi_pov:** `false` — exceto em guias de campo com "voz do especialista" + "voz do nativo/local"

## Estrutura de "Cena" (Unidade = Tópico/Procedimento)

Em técnico, "cena" = **um procedimento completo** ou **um tópico autocontido**. Não há personagem nem arcos emocionais. Há **problema → pré-requisitos → passos → resultado → troubleshooting**.

- **min_palavras:** 200 (cenas muito curtas viram listas, não cenas)
- **max_palavras:** 1500 (acima disso, dividir em sub-procedimentos)
- **beats_obrigatorios:** `["objetivo_claro", "pre_requisitos", "passos_numerados", "resultado_esperado", "troubleshooting_comum", "proximos_passos"]`
- **show_minimo:** 30% (capturas de tela, outputs, diagramas, exemplos de código, configs, fotos passo-a-passo)
- **gancho_tipos:**
  - `problema_resolvido` ("Você não consegue conectar? Faça isto.")
  - `meta_atingida` ("Em 5 minutos você terá X funcionando.")
  - `erro_evitado` ("Não faça X — vai quebrar Y.")
- **fecho_tipos:**
  - `verificacao_sucesso` ("Se você viu a luz verde, deu certo.")
  - `link_relacionado` ("Veja também: capítulo N, seção M.")
  - `exercicio_pratica` ("Tente você mesmo com o dataset de exemplo.")

## Estrutura de Capítulo (Módulo)

- **topicos_por_modulo:** 4-10
- **ordem:** `dependencias_primeiro` (fundamentos → avançado)
- **recap_final:** `true` (resumo + checklist + links)

## Estrutura Global (5 Arquétipos)

### Opção A: Tutorial Progressivo (Aprenda Fazendo)
1. Introdução & Setup
2. Primeiro Sucesso (hello world, primeira receita, primeiro reparo)
3. Conceitos Fundamentais (1 por capítulo)
4. Casos de Uso Comuns
5. Padrões Avançados
6. Produção / Boas Práticas
7. Troubleshooting & FAQ
8. Apêndice / Referência Rápida

**Exemplos:** tutorial de React, curso de panificação, manual de manutenção de ar-condicionado, guia de primeiros socorros.

### Opção B: Referência por Tópico (Manual de Consulta)
- Capítulos = Áreas funcionais (Autenticação, Database, API, Deploy, Monitoramento, **OU** Motor, Freios, Suspensão, Elétrica)
- Cada tópico autocontido
- Cross-references pesados
- Índice remissivo no final

**Exemplos:** documentação oficial de linguagem de programação, manual de reparo automotivo, manual de políticas de RH, código de obras.

### Opção C: Cookbook / Receitas (Solução de Problemas)
- Capítulos = Categorias de problema
- Cada "cena" = Uma receita completa: Problema → Solução → Explicação → Variações
- **Não confundir com Cookbook culinário** — "cookbook" aqui é o padrão de organização por receitas, aplicável a qualquer domínio (receitas de SQL, receitas de culinária, receitas de manutenção).

### Opção D: Documentação de API / Especificação Técnica
- Referência completa (endpoints, params, responses, códigos erro)
- Guias de início rápido
- Exemplos em multi-linguagens
- Changelog / Migração
- **Quando usar:** documentação de software, especificação de produto físico, norma técnica regulatória, padrão de indústria.

### Opção E: Guia de Campo / Manual Portátil — NOVO
- Pensado para uso **offline**, em campo, com uma mão só
- Índice lateral/sumário de sintomas no início
- Páginas robustas (resistentes a água, suor, frio)
- Linguagem telegráfica, escaneável em 5 segundos
- Foco em "o que fazer AGORA" não em "por que"
- Troubleshooting é a parte central (mais que os procedimentos)
- **Exemplos:** manual de primeiros socorros de emergência, guia de mecânico de corrida, manual de trilha, código de conduta de imprensa.

## Bible Requisitos

A Bible de técnico carrega o **conhecimento de domínio** que sustenta a obra. A profundidade varia por subgênero:

- **conceitos_chave:** `true` (glossário técnico, siglas, termos canônicos) — sempre
- **versoes_suportadas:** `true` (versão mínima, depreciações, roadmap) — software, norma
- **dependencias:** `true` (versões exatas, compatibilidade) — software
- **ambientes:** `true` (OS, runtime, container, cloud, **OU** clima, terreno, equipamento) — sempre que houver variação
- **exemplos_canonicos:** `true` (projetos referência, repos oficiais, peças-modelo) — sempre
- **erros_comuns:** `true` (lista de erros, causa, solução) — sempre, é o coração do troubleshooting
- **checklists_verificacao:** `true` (pre-deploy, pos-migracao, security audit, **OU** pré-viagem, pós-procedimento) — sempre
- **faq_vivo:** `true` (atualizado com suporte, perguntas frequentes) — manual de produto
- **changelog:** `true` (releases, breaking changes, **OU** revisões, errata) — software ou norma
- **seguranca:** `true` (cuidado com danos materiais, pessoais, jurídicos) — manual físico
- **glossario_visual:** `true` (ícones, símbolos, chamadas de atenção tipo ⚠️, 🔥, ℹ️) — manual de campo

## Validações Extras (Editor)

- **exige_editor:** `true` (technical writer / dev advocate / especialista de domínio review)
- **regras_editor:** (varia por subgênero)
  - **Todos os subgêneros:**
    - `precisao_tecnica` (comando/instrução funciona, versão correta, procedimento testado)
    - `completude` (não pula passos "óbvios")
    - `testabilidade` (leitor pode verificar se funcionou, com critério de sucesso claro)
    - `escaneabilidade` (headers, code blocks, bold, lists, tables, ícones)
    - `consistencia_terminologica` (mesmo termo = mesma coisa sempre)
  - **Software, API:**
    - `atualidade` (versões, links não quebrados, depreciações marcadas)
  - **Manual físico, manutenção, culinária:**
    - `seguranca` (não ensina anti-patterns perigosos, não esquece de EPI, não esquece de tempo de cozimento)
    - `materiais_necessarios` (lista explícita antes de começar)
    - `tempo_estimado` (quanto tempo leva, pra usuário se programar)
  - **Jurídico, regulatório:**
    - `precisao_juridica` (cita a norma exata, não parafraseia)
    - `atualidade_legal` (avisa sobre mudanças recentes)
  - **Guia de campo:**
    - `portabilidade` (informação crítica em uma frase)
    - `resiliência` (funciona com suor, água, frio)

## Foco Padrão do Usuário

Por subgênero:

**Software/Digital:**
> "Cada procedimento deve ser testável. Se o leitor seguir os passos e não funcionar, o documento falhou. Inclua output esperado. Marque versões. Avise sobre breaking changes."

**Manutenção/Reparo:**
> "Segurança em primeiro lugar. Liste ferramentas e peças antes de começar. Estimativa de tempo. O que fazer se der errado (não só o caminho feliz)."

**Culinária/Craft:**
> "Ingredientes com quantidades exatas. Tempo de preparo vs tempo de cozimento. Indicação de ponto ('massa lisa, brilhante, soltando do fundo'). Substituições possíveis."

**Jurídico/Administrativo:**
> "Citar a base legal exata. Diferenciar o que é obrigatório do que é recomendável. Onde achar o formulário. Prazo. Consequência de não fazer."

**Guia de campo:**
> "O leitor tem uma mão só, está com sol na cara, e precisa achar a resposta em 5 segundos. Frases curtas, ícones universais, decisão clara."

## Template para Usuário Criar Subgênero Personalizado

```
# GENERO: TECNICO_[SEU_SUBGENERO]

Base: TECNICO (v2.0)

Alteracoes:
- arquétipo_principal: TUTORIAL_PROGRESSIVO | REFERENCIA_TOPICO | COOKBOOK_RECEITAS | DOCUMENTACAO_API | GUIA_CAMPO
- pessoa: 2a_imperativa | 3a_instrutiva | 1a_oficial
- tom: [seus adjetivos]
- vocabulario: tecnico_preciso | padrao_industria | cotidiano | cientifico
- exige_editor: true/false
- bible_extra: [requisitos específicos: normas, segurança, glossary visual, changelog]
- regras_editor_extras: [suas regras específicas deste subgênero]
```
