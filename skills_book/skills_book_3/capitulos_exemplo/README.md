# capitulos_exemplo — Pasta para Calibração por Gênero

**Versão:** 3.0
**Aplicação:** os capítulos de calibração ficam DENTRO de cada perfil de gênero em `generos_completos/[perfil]/capitulos_calibracao/`. Esta pasta é para calibrações genéricas ou transversais.

---

## O que tem aqui (por padrão)

Esta pasta começa **vazia**. Ela existe para calibrações que não se encaixam em um gênero específico — por exemplo, se o usuário quiser criar uma "calibração de como o Editor deve polir frases longas em qualquer gênero".

---

## Como usar (se for preenchida no futuro)

Se você criar uma calibração aqui, siga o mesmo padrão dos gêneros:

```
capitulos_exemplo/
└── [nome_da_calibracao]/
    ├── cena_01/
    │   ├── _saida_escritor.md
    │   ├── _resultado_march.json
    │   └── _resultado_continuidade.json
    └── ...
```

---

## Calibrações por gênero

Para calibrações específicas de cada gênero (recomendado), use:

`generos_completos/[perfil]/capitulos_calibracao/`

Exemplos:
- `generos_completos/podbook_mentor/capitulos_calibracao/capitulo_01/cena_01/_saida_escritor.md`
- `generos_completos/ficcao_literaria/capitulos_calibracao/capitulo_01/cena_01/_saida_escritor.md`

Essas calibrações são mais úteis porque mostram à IA produtora como o pipeline funciona NO CONTEXTO de cada gênero.
