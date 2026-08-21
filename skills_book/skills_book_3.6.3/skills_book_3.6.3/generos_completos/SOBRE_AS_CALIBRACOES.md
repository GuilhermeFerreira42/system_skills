# Sobre as cenas de calibração (v3.6.3)

As pastas `generos_completos/*/capitulos_calibracao/` **não foram trazidas** da v3.6.2.

## Por quê

Aquelas 40 amostras foram produzidas sob as regras da 3.6.2. Rodando o próprio
`utils/lint_conviccao.py` da skill sobre elas, **todas reprovam** — média 6.83, com o
Vetor 6 apontando "cena sem fechamento próprio" (regra que passou a valer na v3.6.1).

Distribuir como *referência de calibração* um exemplo que o gate da própria skill rejeita
é pior do que não distribuir: o Escritor calibraria a voz por um padrão reprovado.

## O que continua aqui

Os perfis de gênero seguem completos — `GENERO.md`, `BIBLE_EXEMPLO.md` e `README.md` de
cada perfil. É deles que sai o contrato de forma.

## Se você quiser recalibrar

1. Copie uma pasta `capitulos_calibracao/` da 3.6.2 ao lado, para consulta.
2. Rode `python3 utils/lint_conviccao.py <cena>/_saida_escritor.md` e veja o que reprova.
3. Reescreva a cena até passar, e só então promova a nova amostra a calibração da 3.6.3.

`capitulos_exemplo/README.md` ainda descreve a convenção de onde as calibrações moram —
a convenção continua válida, só não há amostras empacotadas nesta versão.
