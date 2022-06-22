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

To do this, just run *setup.py* if it hasn't run before, it will move the directories, thus preventing bugs from occurring.