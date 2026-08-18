# CHANGELOG v3.6 — Refatoração: Arquitetura Híbrida + Fidelidade à Fonte (2026-08-18)

**Base:** v3.5.2 (arquitetura híbrida Lint + Ressonância)
**Decisões aplicadas:** sessão de calibração de 18/08/2026 (17 itens avaliados com revisão externa)

---

## Decisões estruturais da sessão

A sessão partiu de duas constatações:

1. **A IA não chega ao nível desejado sem um capítulo de referência** — regras delimitam (espaço negativo); o exemplo calibra a voz (espaço positivo). Mantido o princípio: referência = VOZ, corpus = CORPO.
2. **Métricas não capturam alma** — e, quando viram gate, empurram a IA para otimizar o score em vez de escrever bem. Por isso o lint deixou de ser juiz de conteúdo e virou guardião de estrutura.

Adicionalmente, o usuário revelou uma camada externa que muda o cálculo de risco: **existe um segundo script que percorre o livro inserindo as fontes, e haverá revisão humana especializada antes da publicação.** A atribuição de fontes e a cautela médica deixam de ser responsabilidade da prosa.

---

## O que mudou na v3.6

### `utils/lint_conviccao.py` — reescrito

| Vetor | v3.5.2 | v3.6 |
|---|---|---|
| F1 (fonte visível) | infração eliminatória | **removida** — citar fonte é permitido (fidelidade) |
| F2 (disclaimer) | infração eliminatória | **removida** — ressalva específica permitida quando há risco |
| F3 (hedge) | teto de 2 por cena | **removido** — hedge livre, especialmente em alegação contestada |
| F5 (quantificador vago) | infração | **removida** — vago permitido quando a fonte não tem número |
| F6 (ação burocrática) | bloqueio duro | **mantida** — única família que permanece como bloqueio |
| Vetor 1 (notação) | exige LaTeX em 100% dos capítulos | **afrouxado** — nota 10 com notação presente + ≥3 percentuais, sem exigência por capítulo |
| Vetor 2 (cientistas) | lista `CIENTISTAS_PADRAO` hardcoded (Carrel, Batmanghelidj, Agre...) | **genérico** — detecção de nome próprio (título+nome ou sobrenome duplo) + `--nomes` por projeto |
| Vetor 4 (listas) | nota 10 exigia 6+ listas | **afrouxado** — nota 10 com ≥2 listas bem usadas; sem teto de 5 (fiel à fonte) |
| Correções | apontavam a regex disparada | **orientadas à causa** (opção 2) — o feedback diz o problema de fundo, não o padrão |

### `utils/gerar_pontos_de_acao.py` — novo

Gera `PONTOS_DE_ACAO.md`: manifesto externo dos **Chamados Táteis** (fechamentos imperativos com verbo + medida + critério). Checklist de prioridade para a revisão humana especializada — o revisor não relê a obra inteira, vai direto nos pontos onde o leitor é instruído a agir com o corpo. Não altera o livro.

### `generos_completos/nao_ficcao_pratica/GENERO.md`

- **§1:** "PROIBIDO disclaimers" → "EVITE ressalva genérica de rodapé; **PERMITIDO** ressalva específica e pertinente quando a alegação envolve risco real (dosagem, condição clínica, substituição de tratamento), mantendo a forma da fonte".
- **§8:** teto de 5 itens em listas → **fiel à fonte** (se a fonte lista 10, mantém 10); única limitação: categórica, nunca tutorial.

### `escritor/DNA_REVELACAO_RESPEITOSA.md`

- **§10 reescrito:** apenas **F6 (ação burocrática)** permanece como bloqueio duro; F1, F2, F3, F4, F5 viram **direção preferencial** (permitidas quando a fonte/risco pedem); F7 (metáfora descartável) mantida como regra de obra.
- **§11:** tabela de exemplos **reescrita com exemplos fictícios genéricos** (método de estudo, material de construção, leitura diária) — removeu os exemplos específicos do corpus da água (úlcera/Batmanghelidj) que contaminavam um arquivo global.

### `revisor_cego_editorial/RUBRICA_QUALITATIVA_V3.md`

- **§3.9:** reprova apenas ressalva **genérica de rodapé** sem função; aprova ressalva **específica e pertinente** quando há risco real.

### `orquestrador/SKILL_ORQUESTRADOR_PIPELINE.md`

- Correção do lint **orientada à causa** (opção 2 da sessão): o feedback diz "reescreva resolvendo a causa — assuma a descoberta, transforme a ação em gesto físico", não "troque a palavra X".
- Novo passo final: **gerar `PONTOS_DE_ACAO.md`** via `utils/gerar_pontos_de_acao.py`.

### Mantido (sem alteração)

- Piso de densidade 800–1500 (não-ficção) — restaurado na v3.5.2, mantido.
- 5 Movimentos Retóricos na Bible (Arquitetura Retórica) — mantido.
- Separação referência = VOZ / corpus = CORPO — mantido.
- Vetor 6 (fechamento de 30s) + F6 — mantido.
- `FINGERPRINT_ESTILO_DEPRECATED_v1.md` — mantido como registro histórico (substituído pela Assinatura Estilística qualitativa na Bible).

---

## Validação executada na v3.6

- `python3 utils/lint_conviccao.py uploads/LIVRO_FINAL.md --metafora aquário` → **10/10 nos seis vetores, APROVADO, exit 0** (com o lint reescrito).
- `python3 utils/gerar_pontos_de_acao.py uploads/LIVRO_FINAL.md` → **5 Chamados Táteis** detectados (cenas 2, 3, 5, 7, 9), com a medida citada e o fechamento final marcado com "· critério".

---

## Notas

- O lint v3.6 é **genérico**: pode rodar em qualquer obra de qualquer tema sem lista de cientistas fixa. Para obras com elenco próprio, use `--nomes "Personagem1,Personagem2"`.
- A fidelidade à fonte tornou-se o princípio transversal: o texto reproduz o conteúdo como a fonte apresenta; fontes e ressalvas formais vivem no Aparato e no script externo de atribuição.
