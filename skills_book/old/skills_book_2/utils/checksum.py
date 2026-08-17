# -*- coding: utf-8 -*-
"""
utils/checksum.py
==================

Calculo de checksum com deteccao de drift de versao do algoritmo.

Este modulo existe pra resolver 3 problemas que a gente tinha antes:

1. **Calculo manual e propenso a erro.** A gente rodava `sha256sum | cut -c1-8`
   no terminal, e dava pra errar (typo no hash, esquecimento de calcular de novo,
   inconsistencia entre agentes). Agora tem uma funcao unica `calcular_checksum`.

2. **Falta de deteccao de drift de versao.** Se o algoritmo de checksum mudar no
   futuro (ex: de SHA256 truncado em 8 chars pra SHA3-256 truncado em 12 chars),
   os hashes antigos vao parecer "diferentes do arquivo atual" mesmo quando o
   arquivo NAO mudou. A funcao `calcular_checksum_etiquetado` retorna o hash
   COM a versao do algoritmo grudada, tipo `v1.0:a1b2c3d4`. A funcao `verificar_checksum`
   compara corretamente entre hashes de versoes diferentes.

3. **Falta de teste de integridade automatizado.** Antes da gente modificar a
   skill, a gente precisa de uma "baseline" (foto) dos hashes de todos os
   arquivos. Depois da modificacao, a gente roda `verificar` e descobre se
   algum arquivo que nao devia ter mudado mudou. Isso transforma o teste
   "funciona igual?" em produto com saida binaria (OK ou lista de violacoes).

**Como usar:**

```python
from utils.checksum import calcular_checksum, calcular_checksum_etiquetado, verificar_checksum

# Calcular hash de um arquivo
hash_simples = calcular_checksum("/proj/bible/bible_da_obra.md")
# Retorna: "a1b2c3d4" (8 chars)

# Calcular hash COM etiqueta de versao (recomendado pra gravacao)
hash_etiquetado = calcular_checksum_etiquetado("/proj/bible/bible_da_obra.md")
# Retorna: "v1.0:a1b2c3d4"

# Verificar se um arquivo ainda tem o hash esperado
integro = verificar_checksum("/proj/bible/bible_da_obra.md", "v1.0:a1b2c3d4")
# Retorna: True (mesma versao, mesmo hash) ou False (mudou OU drift de versao)

# Criar baseline de uma pasta inteira
from utils.checksum import criar_baseline
baseline = criar_baseline("/proj/skills_book", excluir_pastas=[".git", "__pycache__"])
# Retorna: dict {caminho_relativo: hash_etiquetado}

# Verificar baseline contra estado atual
from utils.checksum import comparar_com_baseline
violacoes = comparar_com_baseline("/proj/skills_book", baseline)
# Retorna: lista de violacoes (arquivos alterados, adicionados, removidos)
```

**Como usar via CLI (sem importar Python):**

```bash
# Calcular checksum de um arquivo
python3 utils/checksum.py calcular skills_book/orquestrador/SKILL_ORQUESTRADOR_LIVRO.md

# Criar baseline de uma pasta (salva em .checksums.json)
python3 utils/checksum.py baseline skills_book/ -o .checksums.json

# Verificar baseline contra estado atual
python3 utils/checksum.py verificar skills_book/ --baseline .checksums.json
```

**Versao do algoritmo:** 1.0
**Baseado em:** utils/constantes.py (importa CHECKSUM_ALGORITMO, CHECKSUM_TAMANHO, etc)
**Acao do diagnostico do Episodio 02:** Acao 3 (Criar utils/checksum.py com checksum puro e deteccao de drift)
"""

import hashlib
import json
import os
import sys
from pathlib import Path

# Importa constantes centralizadas. Se este arquivo for executado diretamente
# (sem ser importado como modulo), ajusta o path pra encontrar utils/constantes.py.
try:
    from utils.constantes import (
        CHECKSUM_ALGORITMO,
        CHECKSUM_TAMANHO,
        CHECKSUM_VERSAO_ALGORITMO,
        CHECKSUM_SEPARADOR,
        CHECKSUM_TAMANHO_DEFAULT,
        FORMATO_HASH_ETIQUETADO,
        PASTA_UTILS,
        EXTENSAO_BAK,
        EXTENSAO_TMP,
    )
except ImportError:
    # Fallback: importa direto do diretorio utils/
    _dir_atual = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, _dir_atual)
    from constantes import (
        CHECKSUM_ALGORITMO,
        CHECKSUM_TAMANHO,
        CHECKSUM_VERSAO_ALGORITMO,
        CHECKSUM_SEPARADOR,
        CHECKSUM_TAMANHO_DEFAULT,
        FORMATO_HASH_ETIQUETADO,
        PASTA_UTILS,
        EXTENSAO_BAK,
        EXTENSAO_TMP,
    )


# ============================================================================
# 1. CALCULO BASICO DE CHECKSUM
# ============================================================================

def calcular_hash_bytes(conteudo_bytes, algoritmo=CHECKSUM_ALGORITMO):
    """Calcula o hash completo (sem truncar) do conteudo binario.

    Args:
        conteudo_bytes: bytes do arquivo
        algoritmo: nome do algoritmo hash (padrao sha256)

    Returns:
        String hex completa do hash (ex: 'a1b2c3d4e5f6...' pra SHA256)
    """
    h = hashlib.new(algoritmo)
    h.update(conteudo_bytes)
    return h.hexdigest()


def truncar_hash(hash_completo, tamanho=CHECKSUM_TAMANHO):
    """Trunca um hash completo em N caracteres.

    Args:
        hash_completo: hash hex completo (ex: 'a1b2c3d4e5f6...')
        tamanho: quantos caracteres manter (padrao 8)

    Returns:
        String hex truncada (ex: 'a1b2c3d4')
    """
    return hash_completo[:tamanho]


def calcular_checksum(caminho_arquivo, tamanho=CHECKSUM_TAMANHO):
    """Calcula o checksum truncado de um arquivo.

    Esta eh a funcao basica. Use `calcular_checksum_etiquetado` para gravacao
    persistente, porque ela inclui a versao do algoritmo e detecta drift.

    Args:
        caminho_arquivo: caminho absoluto ou relativo do arquivo
        tamanho: quantos caracteres do hash manter (padrao CHECKSUM_TAMANHO = 8)

    Returns:
        String com o hash truncado (ex: 'a1b2c3d4')

    Raises:
        FileNotFoundError: se o arquivo nao existir
        PermissionError: se nao tiver permissao de leitura
    """
    with open(caminho_arquivo, "rb") as f:
        conteudo = f.read()
    hash_completo = calcular_hash_bytes(conteudo)
    return truncar_hash(hash_completo, tamanho)


# ============================================================================
# 2. CHECKSUM ETIQUETADO (com deteccao de drift de versao)
# ============================================================================

def formatar_hash_etiquetado(hash_truncado, versao=CHECKSUM_VERSAO_ALGORITMO):
    """Formata um hash truncado com etiqueta de versao do algoritmo.

    Args:
        hash_truncado: hash ja truncado (ex: 'a1b2c3d4')
        versao: versao do algoritmo (padrao CHECKSUM_VERSAO_ALGORITMO = '1.0')

    Returns:
        String no formato 'v{versao}:{hash}' (ex: 'v1.0:a1b2c3d4')
    """
    return FORMATO_HASH_ETIQUETADO.format(versao=versao, hash=hash_truncado)


def parsear_hash_etiquetado(hash_etiquetado):
    """Separa um hash etiquetado em (versao, hash_truncado).

    Args:
        hash_etiquetado: string no formato 'v{versao}:{hash}'

    Returns:
        Tupla (versao, hash_truncado). Se nao tiver etiqueta, retorna
        (None, hash_truncado) e sinaliza drift de versao.

    Note:
        A etiqueta eh 'v' + versao (ex: 'v1.0'). A funcao retorna a versao
        SEM o 'v' (ex: '1.0') pra facilitar comparacao com CHECKSUM_VERSAO_ALGORITMO.
    """
    if CHECKSUM_SEPARADOR in hash_etiquetado:
        partes = hash_etiquetado.split(CHECKSUM_SEPARADOR, 1)
        # A primeira parte deve comecar com 'v'
        if partes[0].startswith("v"):
            # Strippa o 'v' inicial pra retornar so o numero da versao
            versao = partes[0][1:]  # remove o primeiro caractere ('v')
            return versao, partes[1]
    return None, hash_etiquetado


def calcular_checksum_etiquetado(caminho_arquivo, tamanho=CHECKSUM_TAMANHO, versao=CHECKSUM_VERSAO_ALGORITMO):
    """Calcula o checksum etiquetado de um arquivo (com versao do algoritmo).

    Este eh o formato RECOMENDADO para gravacao persistente (no Estado da Obra,
    no Controle da Obra, em metadados), porque ele permite detectar drift de
    versao do algoritmo.

    Args:
        caminho_arquivo: caminho do arquivo
        tamanho: quantos chars do hash manter (padrao 8)
        versao: versao do algoritmo (padrao '1.0')

    Returns:
        String no formato 'v1.0:a1b2c3d4'
    """
    hash_truncado = calcular_checksum(caminho_arquivo, tamanho)
    return formatar_hash_etiquetado(hash_truncado, versao)


# ============================================================================
# 3. VERIFICACAO (com deteccao automatica de drift)
# ============================================================================

def verificar_checksum(caminho_arquivo, hash_esperado, tamanho=CHECKSUM_TAMANHO):
    """Verifica se o arquivo tem o checksum esperado.

    Detecta automaticamente drift de versao:
    - Se `hash_esperado` tem etiqueta de versao, verifica se a versao atual
      do algoritmo eh a mesma. Se for diferente, retorna False e indica drift.
    - Se `hash_esperado` NAO tem etiqueta (formato antigo), assume versao 1.0
      por compatibilidade, mas registra isso como "drift potencial".

    Args:
        caminho_arquivo: caminho do arquivo a verificar
        hash_esperado: hash esperado (pode ser 'a1b2c3d4' ou 'v1.0:a1b2c3d4')
        tamanho: quantos chars do hash calcular (padrao 8)

    Returns:
        True se o arquivo tem o hash esperado
        False caso contrario (arquivo mudou OU drift de versao)
    """
    versao_esperada, hash_esperado_puro = parsear_hash_etiquetado(hash_esperado)

    # Se a versao esperada eh diferente da versao atual do algoritmo, drift!
    if versao_esperada is not None and versao_esperada != CHECKSUM_VERSAO_ALGORITMO:
        return False  # drift de versao detectado

    # Calcula o hash atual do arquivo (com a versao atual do algoritmo)
    hash_atual = calcular_checksum(caminho_arquivo, tamanho)

    # Compara
    return hash_atual == hash_esperado_puro


def verificar_drift_versao(hash_esperado):
    """Verifica se o hash esperado tem drift de versao (foi calculado com
    uma versao diferente do algoritmo).

    Args:
        hash_esperado: hash no formato simples ou etiquetado

    Returns:
        Tupla (tem_drift, versao_esperada, versao_atual):
            tem_drift: True se as versoes diferem
            versao_esperada: versao do algoritmo usada no hash (ou None se sem etiqueta)
            versao_atual: versao atual do algoritmo
    """
    versao_esperada, _ = parsear_hash_etiquetado(hash_esperado)

    if versao_esperada is None:
        # Sem etiqueta: assume versao 1.0 (drift potencial)
        return True, None, CHECKSUM_VERSAO_ALGORITMO

    tem_drift = versao_esperada != CHECKSUM_VERSAO_ALGORITMO
    return tem_drift, versao_esperada, CHECKSUM_VERSAO_ALGORITMO


# ============================================================================
# 4. BASELINE (foto de uma pasta inteira)
# ============================================================================

# Diretorias que devem ser ignoradas ao criar baseline (nao sao codigo da skill)
DIRETORIOS_IGNORADOS = [
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".tox",
    ".venv",
    "venv",
    "env",
    ".env",
    "node_modules",
    "dist",
    "build",
    "out",
    ".next",
    ".parcel-cache",
    ".cache",
    ".ruff_cache",
    ".svelte-kit",
    ".turbo",
    ".vite",
    ".nox",
    ".arena",
    ".output",
    "target",
]

# Extensoes que devem ser ignoradas (binarios, temporarios, etc)
EXTENSOES_IGNORADAS = [
    ".pyc",
    ".pyo",
    ".egg-info",
    ".DS_Store",
    "Thumbs.db",
    ".log",
    ".tmp",
    ".bak",
    ".swp",
    ".swo",
]


def deve_ignorar(caminho_relativo, dir_base):
    """Verifica se um arquivo deve ser ignorado na baseline.

    Args:
        caminho_relativo: caminho relativo ao dir_base (ex: 'utils/constantes.py')
        dir_base: diretorio base da varredura

    Returns:
        True se o arquivo deve ser ignorado
    """
    partes = Path(caminho_relativo).parts
    nome_arquivo = Path(caminho_relativo).name

    # Ignora diretorios da lista
    for parte in partes:
        if parte in DIRETORIOS_IGNORADOS:
            return True

    # Ignora extensoes da lista
    for ext in EXTENSOES_IGNORADAS:
        if nome_arquivo.endswith(ext):
            return True

    return False


def criar_baseline(dir_base, extensoes_validas=None):
    """Cria uma baseline (foto) de todos os arquivos de uma pasta.

    Args:
        dir_base: diretorio base pra varrer (ex: '/proj/skills_book')
        extensoes_validas: lista de extensoes a incluir (None = todas que nao sao ignoradas)

    Returns:
        Dict {caminho_relativo: hash_etiquetado}
        Ex: {'utils/constantes.py': 'v1.0:a1b2c3d4', 'orquestrador/SKILL_ORQUESTRADOR_LIVRO.md': 'v1.0:e5f6a7b8'}
    """
    baseline = {}
    dir_base_path = Path(dir_base)

    if not dir_base_path.exists():
        raise FileNotFoundError(f"Diretorio base nao encontrado: {dir_base}")

    for arquivo_path in sorted(dir_base_path.rglob("*")):
        if not arquivo_path.is_file():
            continue

        caminho_relativo = str(arquivo_path.relative_to(dir_base_path))

        if deve_ignorar(caminho_relativo, dir_base):
            continue

        if extensoes_validas is not None:
            if not any(arquivo_path.suffix == ext for ext in extensoes_validas):
                continue

        try:
            hash_etiquetado = calcular_checksum_etiquetado(str(arquivo_path))
            baseline[caminho_relativo] = hash_etiquetado
        except (PermissionError, FileNotFoundError):
            # Ignora arquivos que nao conseguiu ler (race condition, etc)
            continue

    return baseline


def comparar_com_baseline(dir_base, baseline, extensoes_validas=None):
    """Compara o estado atual de uma pasta com uma baseline.

    Args:
        dir_base: diretorio base (mesmo usado em criar_baseline)
        baseline: dict retornado por criar_baseline
        extensoes_validas: lista de extensoes a verificar (None = todas)

    Returns:
        Lista de violacoes. Cada violacao eh um dict com:
            - tipo: 'arquivo_alterado' | 'arquivo_adicionado' | 'arquivo_removido' | 'drift_versao'
            - caminho: caminho relativo do arquivo
            - hash_esperado: hash da baseline (se aplicavel)
            - hash_atual: hash calculado agora (se aplicavel)
            - mensagem: descricao legivel da violacao
    """
    violacoes = []
    baseline_atual = criar_baseline(dir_base, extensoes_validas=extensoes_validas)

    # Detecta alteracoes e remocoes
    for caminho, hash_esperado in baseline.items():
        if caminho not in baseline_atual:
            violacoes.append({
                "tipo": "arquivo_removido",
                "caminho": caminho,
                "hash_esperado": hash_esperado,
                "hash_atual": None,
                "mensagem": f"Arquivo removido: {caminho} (era {hash_esperado})"
            })
            continue

        hash_atual = baseline_atual[caminho]

        # Detecta drift de versao
        tem_drift, versao_esperada, _ = verificar_drift_versao(hash_esperado)
        if tem_drift:
            violacoes.append({
                "tipo": "drift_versao",
                "caminho": caminho,
                "hash_esperado": hash_esperado,
                "hash_atual": hash_atual,
                "mensagem": f"Drift de versao detectado em {caminho}: esperado {versao_esperada}, atual {CHECKSUM_VERSAO_ALGORITMO}"
            })
            continue

        # Compara hashes (parseando a etiqueta de versao)
        _, hash_esperado_puro = parsear_hash_etiquetado(hash_esperado)
        _, hash_atual_puro = parsear_hash_etiquetado(hash_atual)

        if hash_esperado_puro != hash_atual_puro:
            violacoes.append({
                "tipo": "arquivo_alterado",
                "caminho": caminho,
                "hash_esperado": hash_esperado,
                "hash_atual": hash_atual,
                "mensagem": f"Arquivo alterado: {caminho} (esperado {hash_esperado}, atual {hash_atual})"
            })

    # Detecta adicoes
    for caminho in baseline_atual:
        if caminho not in baseline:
            violacoes.append({
                "tipo": "arquivo_adicionado",
                "caminho": caminho,
                "hash_esperado": None,
                "hash_atual": baseline_atual[caminho],
                "mensagem": f"Arquivo adicionado: {caminho} (hash {baseline_atual[caminho]})"
            })

    return violacoes


# ============================================================================
# 5. PERSISTENCIA DE BASELINE (JSON)
# ============================================================================

def salvar_baseline(baseline, caminho_arquivo):
    """Salva uma baseline em arquivo JSON.

    Args:
        baseline: dict retornado por criar_baseline
        caminho_arquivo: onde salvar (ex: '.checksums.json')
    """
    payload = {
        "versao_algoritmo": CHECKSUM_VERSAO_ALGORITMO,
        "algoritmo": CHECKSUM_ALGORITMO,
        "tamanho_hash": CHECKSUM_TAMANHO,
        "total_arquivos": len(baseline),
        "checksums": baseline,
    }
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def carregar_baseline(caminho_arquivo):
    """Carrega uma baseline de arquivo JSON.

    Args:
        caminho_arquivo: arquivo JSON criado por salvar_baseline

    Returns:
        Tupla (metadata, baseline):
            metadata: dict com versao_algoritmo, algoritmo, tamanho_hash, total_arquivos
            baseline: dict {caminho_relativo: hash_etiquetado}
    """
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        payload = json.load(f)

    metadata = {
        "versao_algoritmo": payload.get("versao_algoritmo"),
        "algoritmo": payload.get("algoritmo"),
        "tamanho_hash": payload.get("tamanho_hash"),
        "total_arquivos": payload.get("total_arquivos"),
    }
    baseline = payload.get("checksums", {})
    return metadata, baseline


# ============================================================================
# 6. CLI (Command Line Interface)
# ============================================================================

def main():
    """Entry point do CLI."""
    if len(sys.argv) < 2:
        print("Uso: python3 utils/checksum.py {calcular|baseline|verificar} [args...]")
        print("")
        print("Comandos:")
        print("  calcular <arquivo>              Calcula o checksum etiquetado de um arquivo")
        print("  baseline <pasta> -o <saida>     Cria baseline de uma pasta e salva em JSON")
        print("  verificar <pasta> --baseline <arquivo>  Compara pasta com baseline")
        print("")
        print("Constantes atuais:")
        print(f"  Algoritmo: {CHECKSUM_ALGORITMO}")
        print(f"  Tamanho do hash: {CHECKSUM_TAMANHO}")
        print(f"  Versao do algoritmo: {CHECKSUM_VERSAO_ALGORITMO}")
        sys.exit(0)

    comando = sys.argv[1]

    if comando == "calcular":
        if len(sys.argv) < 3:
            print("Erro: informe o arquivo a calcular")
            print("Uso: python3 utils/checksum.py calcular <arquivo>")
            sys.exit(1)
        arquivo = sys.argv[2]
        try:
            hash_etiquetado = calcular_checksum_etiquetado(arquivo)
            print(f"{arquivo}: {hash_etiquetado}")
        except FileNotFoundError:
            print(f"Erro: arquivo nao encontrado: {arquivo}")
            sys.exit(1)

    elif comando == "baseline":
        if len(sys.argv) < 4 or sys.argv[3] != "-o":
            print("Erro: uso correto: python3 utils/checksum.py baseline <pasta> -o <saida.json>")
            sys.exit(1)
        pasta = sys.argv[2]
        saida = sys.argv[4]
        print(f"Criando baseline de {pasta}...")
        baseline = criar_baseline(pasta)
        salvar_baseline(baseline, saida)
        print(f"Baseline salva em {saida} ({len(baseline)} arquivos)")

    elif comando == "verificar":
        if len(sys.argv) < 5 or sys.argv[3] != "--baseline":
            print("Erro: uso correto: python3 utils/checksum.py verificar <pasta> --baseline <arquivo.json>")
            sys.exit(1)
        pasta = sys.argv[2]
        baseline_path = sys.argv[4]
        print(f"Carregando baseline de {baseline_path}...")
        metadata, baseline = carregar_baseline(baseline_path)
        print(f"Baseline: algoritmo={metadata['algoritmo']}, versao={metadata['versao_algoritmo']}, arquivos={metadata['total_arquivos']}")
        print(f"Verificando {pasta} contra baseline...")
        violacoes = comparar_com_baseline(pasta, baseline)
        if not violacoes:
            print(f"OK: nenhum arquivo foi alterado. {len(baseline)} arquivos integrais.")
            sys.exit(0)
        else:
            print(f"FALHA: {len(violacoes)} violacao(oes) detectada(s):")
            for v in violacoes:
                print(f"  [{v['tipo']}] {v['mensagem']}")
            sys.exit(1)

    else:
        print(f"Erro: comando desconhecido '{comando}'")
        print("Comandos validos: calcular, baseline, verificar")
        sys.exit(1)


if __name__ == "__main__":
    main()
