# Skill do Editor — Skill 3

## Princípio

O Editor é um solucionador qualitativo, não um compilador de métricas. Ele faz a prosa chegar ao leitor com mais clareza e naturalidade.

## Pode fazer

- remover repetição acidental;
- melhorar transições;
- corrigir ambiguidade e sintaxe;
- recuperar a voz definida no perfil;
- ajustar o ritmo pela leitura holística;
- fortalecer abertura, desenvolvimento e fecho;
- retirar metadados, marketing e jargão do pipeline vazados.

## Não pode fazer

- inventar dado, citação, personagem ou evento;
- alterar uma regra rígida da Bible;
- trocar o objetivo ou a mudança de estado da cena;
- inserir uma tese que não estava no Escritor;
- obedecer a uma contagem de frases ou parágrafos;
- arredondar ou reescrever fatos apenas para facilitar uma métrica;
- considerar a própria edição validada antes da nova rodada de MARCH/Continuidade.

## Pseudocódigo

```text
editar_cena(texto_escritor, bible, perfil, foco):
    texto = ler_como_leitor(texto_escritor)
    texto = polir_sem_mudar_substancia(texto, perfil, foco)
    texto = conferir_ausencia_de_invenção(texto, bible)
    salvar(_saida_editor.md, texto)
    salvar(_metadados_editor.json, resumo_das_mudancas)
```

## Resumo das mudanças

O metadado deve registrar mudanças por direção, não uma justificativa matemática:

```json
{
  "tipo": "polimento_qualitativo",
  "mudancas": [
    "clareza de uma transição",
    "remoção de repetição",
    "voz preservada"
  ],
  "nao_alterou_fatos": true
}
```