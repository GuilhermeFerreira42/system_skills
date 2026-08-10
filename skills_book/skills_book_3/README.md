# Skill 3 — Pipeline Greenforge de Escrita com Fluidez e Integridade

**Versão:** 3.0 — fusão qualitativa + técnica  
**Status:** base operacional em evolução  
**Aplicação:** produção de livros cena a cena, com liberdade literária e rastreabilidade física.

## Propósito

A Skill 3 separa duas responsabilidades que não devem competir:

- **A criação literária** busca sentido, voz, ritmo orgânico, clareza e impacto.
- **A infraestrutura** garante isolamento, validação factual, continuidade, linhagem e recuperação.

O Escritor não calcula desvio-padrão, não conta parágrafos para satisfazer um gate e não escreve para uma métrica. As regras de ritmo são qualitativas. A segurança opera depois, nos agentes e scripts apropriados.

## O que permanece da base limpa

1. Produção cena por cena.
2. Worktree isolada por cena.
3. Bible da Obra como fonte semântica da verdade.
4. Estado da Obra como checkpoint lógico.
5. Validação MARCH e Continuidade em cegueira.
6. Salvamento atômico.
7. Checksum e round-trip.
8. Lei 6: zero material de marketing no livro.

## O que muda na Skill 3

- O gênero deixa de ser um pacote pesado que governa a escrita. Perfis em `generos_completos/` são referências opcionais, não dependências de boot.
- O Orquestrador faz um nivelamento editorial A/B/C e grava um contrato qualitativo na Bible.
- O Editor é a última etapa que pode alterar a prosa antes das validações do artefato candidato.
- O Revisor Cego Editorial avalia fluidez de forma holística. Não há `medir_ritmo.py` nem gate numérico estético.
- O Vigia verifica arquivos, estados, checksums e cegueira. Ele não julga qualidade literária.
- Uma edição manual gera `MODIFICADO_MANUALMENTE` e `REVALIDACAO_NECESSARIA`; nunca dispara uma reescrita automática de toda a cena.
- Após três retries, a cena fica `BLOQUEADA_REVISAO_HUMANA`. O livro só pode ser `CONCLUIDO` quando não houver cenas bloqueadas ou pendentes.

## Componentes

```text
skill3/
├── README.md
├── LEIA-ME-PRIMEIRO.md
├── REGRAS_GREENFORGE_PIPELINE.md
├── FLUXO_COMPLETO_PIPELINE.md
├── CONFIG.md
├── nivelamento_editorial/
├── escritor/
├── editor/
├── atomizador/
├── validador_march/
├── validador_continuidade/
├── revisor_cego_editorial/
├── orquestrador/
├── consolidador/
├── controle_da_obra/
├── utils/
│   ├── checksum.py
│   ├── atomic.py
│   ├── vigia_integridade.py
│   └── reconciliar_controle.py
├── bible/
├── estado/
├── regras_negocio/
├── templates_bible_worktree/
├── generos_completos/       # referências opcionais
├── generos_template/
└── execucao/                # estrutura inicial de um projeto
```

## Fluxo resumido

```text
Boot
  → nivelamento editorial
  → Bible + Estado + mapa do corpus
  → Escritor (prosa)
  → Editor (última mutação)
  → artefato candidato
  → Atomizador + perguntas de Continuidade
  → MARCH + Continuidade cegos
  → Revisor Cego holístico
  → cópia final + checksum
  → Vigia físico
  → atualização atômica de Bible/Estado/Controle
  → consolidação
```

## Autoridade dos registros

| Registro | Autoridade |
|---|---|
| Bible | Semântica da obra: conceitos, personagens, regras, fios e voz |
| Estado | Intenção operacional, plano, status e próximo checkpoint |
| Disco | Bytes realmente existentes e prova física do artefato |
| Controle da Obra | Espelho/reconciliação entre Estado e disco; não substitui a Bible |

## Início rápido

1. Copie `CONFIG.md` para `execucao/CONFIG.md`.
2. Coloque as fontes em `execucao/corpus/`.
3. Inicie o Orquestrador.
4. Responda ao nivelamento editorial ou confirme o perfil padrão.
5. Produza uma cena por vez.
6. Nunca marque uma cena como concluída sem o pacote físico aprovado.

Leia `LEIA-ME-PRIMEIRO.md` para a ordem completa.
