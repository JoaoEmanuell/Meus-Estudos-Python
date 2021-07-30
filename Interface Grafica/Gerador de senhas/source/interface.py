#Imports
import PySimpleGUI as sg
from .generate import generate

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
        generate.listas(self)
        while True:
            self.button, self.values = self.janela.Read()
            self.tamanho = self.values['Tam']
            self.minusculas = self.values['Min']
            self.numeros = self.values['Nums']
            self.especiais = self.values['Esp']
            self.maisculas = self.values['Max']
            interface.limpar(self.janela, 'saida') # limpa o output toda vez que um novo é chamado, vem antes da geração para limpar toda vez
            generate.geração(self) #gera os valores

    def limpar(janela, chave):
        janela.FindElement(chave).Update('')