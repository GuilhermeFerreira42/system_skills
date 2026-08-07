### GENERO: PODBOOK_BRUNO (ALIAS DEPRECATED)
**STATUS:** DEPRECATED. Este arquivo existe apenas como alias retrocompatível. O nome canônico deste gênero é `PODBOOK_LEGACY` (constante `GENERO_PODBOOK_LEGACY` em `utils/constantes.py`) e o arquivo de definição ativo é `GENERO_PODBOOK_LEGACY.md`.

**Por que este alias existe:** projetos antigos podem referenciar `PODBOOK_BRUNO` (ou `GENERO_PODBOOK_BRUNO.md`) diretamente. O alias garante que essas referências continuem funcionando sem quebra.

**O que fazer:**
- Para NOVOS livros: use `PODBOOK_LEGACY` (constante) ou `generos/GENERO_PODBOOK_LEGACY.md` (arquivo).
- Para PROJETOS ANTIGOS que já referenciam `PODBOOK_BRUNO`: continue usando, funciona. Mas considere migrar para `PODBOOK_LEGACY` na próxima atualização do estado da obra.
- A constante `GENERO_PODBOOK_BRUNO` em `utils/constantes.py` aponta automaticamente para `PODBOOK_LEGACY` (mesmo valor de string), então não há quebra comportamental.

**Definição completa do gênero:** ver `generos/GENERO_PODBOOK_LEGACY.md`.
