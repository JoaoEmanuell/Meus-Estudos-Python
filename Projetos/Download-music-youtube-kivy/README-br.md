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

Normalmente os módulos estarão no diretório **lib64**.

## source_api

No diretório source_api, você deve criar uma pasta chamada "external_modules".

Dentro de **lib64** copie as pastas : 

1. certifi
2. charset_normalizer
3. idna
4. requests
5. urllib3

E cole elas dentro da pasta *external_modules* que você acabou de criar.

**Todas essas pastas estão dentro da pasta lib64 que foi criada quando o ambiente virtual foi criado e quando as dependências foram instaladas**
