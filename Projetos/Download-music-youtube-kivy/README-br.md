[English](README.md)[Português Brasil](README-br.md)

# App

Esse app é a versão android, construído utilizando o framework kivy e a biblioteca pytube.

Ele serve para baixar vídeos ou músicas do YouTube.

# Iniciando

## Ambiente virtual

Windows :

    python -m venv .

    .\Scripts\activate.bat

Linux | Mac :

    python3 -m venv .

    source ./bin/activate

## Instalando dependências

    pip install -r requirements.txt

# Configurações

Diretórios específicos necessitam de configurações específicas.

Uma vez que o kivy no android da alguns [muitos] bugs relacionados a falta de módulos, mesmos eles estando instalados, acaba sendo necessário adicionar eles ao projeto de forma manual, caso não sejam, eles podem até funcionar no windows e no linux, mas no android é quase certo que irão falhar.

Para isso basta rodar o *setup.py* caso não tenha rodado antes, ele movera os diretórios, assim evitando que bugs ocorram.