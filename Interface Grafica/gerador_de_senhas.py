#Imports
import PySimpleGUI as sg
from random import randint

#Interface
class interface():
    def __init__(self):
        layout = [
            [sg.Text("GERADOR DE SENHAS", justification = 'center')],
            [sg.Text("Tamanho"), sg.Input(size = (20,0), key = 'Tam')],
            [sg.Checkbox("Letras minusculas", key = 'Min')],
            [sg.Checkbox("Numeros", key = 'Nums')],
            [sg.Checkbox("Caracteres especiais (#$?!)", key = 'Esp')],
            [sg.Button("Gerar senha")],
            [sg.Output(size = (50, 5), key = 'saida')]
        ]

        self.janela = sg.Window('GERADOR DE SENHAS').layout(layout)
        
    def Iniciar(self):
        interface.listas(self)
        while True:
            self.button, self.values = self.janela.Read()
            self.tamanho = self.values['Tam']
            self.minusculas = self.values['Min']
            self.numeros = self.values['Nums']
            self.especiais = self.values['Esp']
            '''print(int(self.tamanho))
            print(self.minusculas)
            print(self.numeros)
            print(self.especiais)'''
            interface.geração(self)
            
#Gerador
    def listas(self):
        self.Minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.Maisculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.Numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.Especiais = ['?', ';', ',', '.', '!', '{', '}', '(', ')', '/', '*', '-', '+']
    
    def geração(self):
        limite = int(self.tamanho)
        l = 0
        if self.minusculas and self.numeros and self.especiais == True:
            while l != limite:
                lista = randint(1 , 4)
                if lista == 1:
                    car = self.Maisculas[randint(0, 25)]
                elif lista == 2:
                    car = self.Minusculas[randint(0, 25)]
                elif lista == 3:
                    car = self.Numeros[randint(0, 9)]
                elif lista == 4:
                    car = self.Especiais[randint(0, 12)]
                else:
                    car = car = self.Maisculas[randint(0, 25)]
                print(f"{car}", end='')
                l += 1
        elif self.minusculas == True:
            if self.minusculas == True:
                while l != limite:
                    lista = randint(1, 1)
                    if lista == 0:
                        car = self.Maisculas[randint(0, 25)]
                    elif lista == 1:
                        car = self.Minusculas[randint(0, 25)]
                    else:
                        car = car = self.Maisculas[randint(0, 25)]
                    print(f"{car}", end='')
                    l += 1
            elif self.minusculas and self.numeros == True:
                while l != limite:
                    lista = randint(1 , 3)
                    if lista == 1:
                        car = self.Maisculas[randint(0, 25)]
                    elif lista == 2:
                        car = self.Minusculas[randint(0, 25)]
                    elif lista == 3:
                        car = self.Numeros[randint(0, 9)]
                    else:
                        car = car = self.Maisculas[randint(0, 25)]
                    print(f"{car}", end='')
                    l += 1
            elif self.minusculas and self.especiais == True:
                while l != limite:
                    lista = randint(1 , 2)
                    if lista == 1:
                        car = self.Maisculas[randint(0, 25)]
                    elif lista == 2:
                        car = self.Minusculas[randint(0, 25)]
                    else:
                        car = car = self.Maisculas[randint(0, 25)]
                    print(f"{car}", end='')
                    l += 1
#Progama

tela = interface()
tela.Iniciar()
tela.geração()