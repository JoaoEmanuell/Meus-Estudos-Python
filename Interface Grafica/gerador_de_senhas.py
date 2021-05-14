#Imports
import PySimpleGUI as sg
from random import randint

#Interface
class interface():
    def __init__(self):
        layout = [
            [sg.Text("GERADOR DE SENHAS", justification = 'center')],
            [sg.Text("Tamanho"), sg.Input(size = (20,0), key = 'Tam')],
            [sg.Checkbox("Letras maisculas", key = 'Max')],
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
            self.maisculas = self.values['Max']
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
#bloco com todas as opções marcadas
        limite = int(self.tamanho)
        if self.minusculas and self.numeros and self.especiais and self.maisculas == True:
            interface.aleatorio_4(self.Maisculas, self.Minusculas, self.Numeros, self.Especiais, limite)
#bloco das letras maisculas
        elif self.maisculas == True:
            #sub bloco letras minusculas
            if self.maisculas and self.minusculas == True:
                if self.maisculas and self.minusculas and self.numeros == True:
                    interface.aleatorio_3(self.Maisculas, self.Minusculas, self.Numeros, limite)
                elif self.maisculas and self.minusculas and self.especiais == True:
                    interface.aleatorio_3(self.Especiais, self.Maisculas, self.Minusculas, limite)
                else:
                    interface.aleatorio_2(self.Maisculas, self.Minusculas, limite)
            #sub bloco numeros
            elif self.maisculas and self.numeros == True:
                if self.maisculas and self.especiais and self.numeros == True:
                    interface.aleatorio_3(self.Especiais, self.Maisculas, self.Numeros, limite)
                else:
                    interface.aleatorio_2(self.Maisculas, self.Numeros, limite)
            elif self.maisculas and self.especiais == True:
                interface.aleatorio_2(self.Maisculas, self.Especiais, limite)
            else:
                interface.aleatorio_1(self.Maisculas, limite)
#bloco das letras minusculas
        elif self.minusculas == True:
            #sub bloco numeros
            if self.minusculas and self.numeros == True:
                if self.minusculas and self.numeros and self.especiais == True:
                    interface.aleatorio_3(self.Minusculas, self.Numeros, self.Especiais, limite)
                else:
                    interface.aleatorio_2(self.Minusculas, self.Numeros, limite)
            #sub bloco especiais
            elif self.minusculas and self.especiais == True:
                interface.aleatorio_2(self.Minusculas, self.Especiais, limite)
            else:
                interface.aleatorio_1(self.Minusculas, limite)
#bloco dos numeros
        elif self.numeros == True:
            if self.numeros and self.especiais == True:
                interface.aleatorio_2(self.Numeros, self.Especiais, limite)
            else:
                interface.aleatorio_1(self.Numeros, limite)
#bloco dos especiais
        else:
            interface.aleatorio_1(self.Especiais, limite)
#Função de aleatoridade
    def aleatorio_1(lista, limite):
        l = 0
        while l != limite:
                car = lista[randint(0, (len(lista) - 1))]
                print(f"{car}", end='')
                l += 1
    
    def aleatorio_2(lista1, lista2, limite):
        l = 0
        while l != limite:
            lista = randint(1 , 2)
            if lista == 1:
                car = lista1[randint(0, (len(lista1) - 1))]
            elif lista == 2:
                car = lista2[randint(0, (len(lista2) - 1))]
            print(f"{car}", end='')
            l += 1

    def aleatorio_3(lista1, lista2, lista3, limite):
        l = 0
        while l != limite:
            lista = randint(1 , 3)
            if lista == 1:
                car = lista1[randint(0, (len(lista1) - 1))]
            elif lista == 2:
                car = lista2[randint(0, (len(lista2) - 1))]
            elif lista == 3:
                car = lista3[randint(0, (len(lista3) - 1))]
            print(f"{car}", end='')
            l += 1
    
    def aleatorio_4(lista1, lista2, lista3, lista4, limite):
        l = 0
        while l != limite:
            lista = randint(1 , 4)
            if lista == 1:
                car = lista1[randint(0, (len(lista1) - 1))]
            elif lista == 2:
                car = lista2[randint(0, (len(lista2) - 1))]
            elif lista == 3:
                car = lista3[randint(0, (len(lista3) - 1))]
            elif lista == 4:
                car = lista4[randint(0, (len(lista4) - 1))]
            print(f"{car}", end='')
            l += 1    
#Progama

tela = interface()
tela.Iniciar()
tela.geração()