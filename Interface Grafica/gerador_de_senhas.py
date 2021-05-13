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
            [sg.Output(size = (50, 5))]
        ]

        self.janela = sg.Window('Teste').layout(layout)
        
    def Iniciar(self):
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
#Gerador
class Gerador(interface):
    def __init__(self):
        self.Minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.Maisculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.Numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.Especiais = ['?', ';', ',', '.', '!', '{', '}', '(', ')', '/', '*', '-', '+']
    
    def geração(self):
        limite = int(self.numeros)
        
#Progama

tela = interface()

tela.Iniciar()