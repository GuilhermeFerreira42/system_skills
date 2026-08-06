# corpus/ — Pasta de Fontes

**Versão:** 3.0
**Aplicação:** coloque aqui as fontes brutas que serão usadas para produzir o livro. Podem ser transcrições de aulas, documentos técnicos, anotações, rascunhos, ou qualquer material didático.

---

## Formatos aceitos

- `.md` (preferencial — preserva formatação)
- `.txt`
- `.docx` (a IA lê com ferramenta própria)
- `.pdf` (a IA lê com ferramenta própria, se disponível)

## Como organizar

Uma boa prática é nomear os arquivos em ordem lógica, especialmente se for sequência de aulas:

```
corpus/
├── aula_01_introducao.md
├── aula_02_primeiro_conceito.md
├── aula_03_segundo_conceito.md
└── ...
```

Se o corpus for um único documento grande, pode ser um único arquivo:

```
corpus/
└── transcricoes_completas.md
```

## ⚠️ Mistura com material de marketing

Se o corpus tiver mistura de conteúdo didático com material de marketing (páginas de venda, e-mails, CTAs, preços de outros cursos), **separe antes**. O livro só pode usar o conteúdo didático. Lei 6 do Greenforge: zero material de marketing no livro.

Para filtrar, você pode:
1. Ler arquivo por arquivo e remover seções de venda
2. Pedir para a IA separar, revisar, e aí usar só a parte didática
3. Marcar com prefixo `MARKETING_` os arquivos que são só marketing, e a IA vai ignorar

## Quando o corpus é vazio

Se você quer produzir um livro **sem** corpus prévio (ex: ficção inventada do zero), deixe essa pasta vazia. Nesse caso, o Atômicador extrai afirmações do próprio conhecimento do modelo. Mas atenção: a validação MARCH fica limitada (não há corpus para confirmar), e a qualidade do livro depende da consistência interna (validação de Continuidade).

Para ficção sem corpus, a recomendação é criar primeiro um esboço estruturado (Personagens + Arco + Timeline) na Bible, e usar isso como fonte da verdade.
