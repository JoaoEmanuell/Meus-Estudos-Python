import interface
import os
def main():
    clear()
    tela = interface.TelaPython()
    tela.Iniciar()  

def clear():
    os.system('clear')

if __name__ == '__main__':
    main()