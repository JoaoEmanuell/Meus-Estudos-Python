from source import interface
import os
def main():
    clear()
    tela = interface.TelaPython()
    tela.Iniciar()
    clear()  

def clear():
    os.system('clear')

if __name__ == '__main__':
    main()