#Imports
import PySimpleGUI as sg

#Interface
class interface():
    def __init__(self):
        layout = [
            [sg.Text("GERADOR DE SENHAS", justification = 'center')],
            [sg.Text("Tamanho"), sg.Input(size = (20,0))],
            [sg.Checkbox("Letras minusculas", key = 'Letras minusculas')],
            [sg.Checkbox("Numeros")],
            [sg.Checkbox("Caracteres especiais (#$?!)")],
            [sg.Button("Gerar senha")],
            [sg.Output(size = (50, 5))]
        ]

        self.janela = sg.Window('Teste').layout(layout)
        
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
#Gerador

#Progama

tela = interface()

tela.Iniciar()