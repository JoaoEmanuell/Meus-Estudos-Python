import cript
import descpt
import os
def main():
    while True:
        clear()
        print("Progama de criptografia, você deseja:\n[1]Cripografar um texto\n[2]Descripografar um texto já criptografado\n[3]Sair")
        res = int(input(""))
        if res == 1:
            text = ''
            clear()
            print(cript.criptografador(text))
            break
        elif res == 2:
            text = []
            clear()
            print(descpt.descriptografador(text))
            break
        elif res == 3:
            clear()
            break
        else:
            clear()
            print("Opção invalida! Digite novamente!")

def clear():
    os.system('clear')

if __name__ == '__main__':
    main()