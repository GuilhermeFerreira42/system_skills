# Capítulo 1 — Introdução e Instalação
## Cena 2: Instalando Python no seu computador (PÓS-CIRÚRGICA)

---

Este capítulo mostra como instalar Python no seu computador. Vamos cobrir Windows, macOS e Linux. Se você já tem Python instalado, pode pular para a próxima cena.

## O que você vai precisar

Antes de começar, confirme que você tem:

- Um computador com Windows 10 ou superior, macOS 11 ou superior, ou uma distribuição Linux recente
- Acesso de administrador no sistema (para instalar software)
- Conexão com a internet (para baixar o instalador)
- 200 MB de espaço em disco

## Instalando no Windows

Siga estes passos:

1. Acesse o site oficial do Python em `https://www.python.org/downloads/`
2. Clique no botão "Download Python 3.X.X" (a versão mais recente)
3. Quando o download terminar, execute o instalador
4. **IMPORTANTE:** Na primeira tela do instalador, marque a caixa "Add Python to PATH" antes de clicar em "Install Now"
5. Aguarde a instalação terminar
6. Para verificar, abra o Prompt de Comando (cmd) e digite:

```bash
python --version
```

Você deve ver a versão que instalou, por exemplo `Python 3.12.0`.

## Instalando no macOS

A partir do macOS 10.15, o Python 3 vem pré-instalado. Mas a versão do sistema pode estar desatualizada. Para garantir a versão mais recente:

1. Abra o Terminal (Aplicativos > Utilitários > Terminal)
2. Instale o Homebrew (gerenciador de pacotes para macOS) seguindo as instruções em `https://brew.sh/`
3. Com o Homebrew instalado, execute:

```bash
brew install python3
```

4. Verifique a versão:

```bash
python3 --version
```

## Instalando no Linux

Python 3 já vem pré-instalado na maioria das distribuições Linux. Para garantir a versão mais recente:

No Ubuntu, Debian e derivados:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

No Fedora:

```bash
sudo dnf install python3 python3-pip
```

No Arch Linux:

```bash
sudo pacman -S python python-pip
```

Verifique a versão:

```bash
python3 --version
```

## Erro comum: o sistema não reconhece o comando `python`

Se depois de instalar, o terminal retornar `python: command not found` (ou similar), significa que o Python não está no PATH do sistema. No Windows, isso acontece se você esqueceu de marcar "Add Python to PATH" durante a instalação. Reinstale marcando a caixa.

No macOS e Linux, use `python3` em vez de `python` — em alguns sistemas, `python` se refere à versão 2.x.

## Verificando que tudo está pronto

Para ter certeza de que Python está instalado e acessível, abra o terminal e execute:

```bash
python --version
# ou
python3 --version
```

Você deve ver a versão do Python. Se sim, você está pronto para o próximo capítulo.

---

## Resumo

Neste capítulo, você instalou o Python no seu computador. Você aprendeu o procedimento para Windows, macOS e Linux, e viu como verificar se a instalação foi bem-sucedida. No próximo capítulo, você vai escrever e executar seu primeiro programa em Python.

---

## Checklist

Antes de seguir para o próximo capítulo, confirme que você:

- [ ] Python 3.10+ instalado no meu sistema operacional
- [ ] `python --version` (ou `python3 --version`) retorna a versão correta
- [ ] Sei abrir o terminal (cmd no Windows, Terminal no macOS/Linux)
- [ ] Estou pronto para escrever meu primeiro "Olá, mundo!" em Python

