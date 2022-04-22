[English](README.md)[Português Brasil](README-br.md)

# App

This app is an android version built using the kivy framework and the pytube library.

It serves to download videos or music from YouTube.

# Starting

## Virtual environment

Windows :
    
    python -m venv .

    .\Scripts\activate.bat

Linux | Mac :

    python3 -m venv .

    source ./bin/activate

## Installing dependencies

    pip install -r requirements.txt

# Configurations

Specific directories need specific settings.

Since kivy on android gives some [many] bugs related to the lack of modules, even though they are installed, it ends up being necessary to add them to the project manually, if they aren't, they can work on windows and linux, but on android are almost certain to fail.

Normally the modules will be in the **lib64** directory.

## source_api

In the source_api directory you must create a folder called "external_modules".

Inside **lib64** copy the folders :

1. certifi
2. charset_normalizer
3. idna
4. requests
5. urllib3

And past them into the *external_modules* folder you just created.

**All these folders are inside the lib64 folder when the virtual environment was created and when the dependencies were installed**
