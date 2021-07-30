import PySimpleGUI as sg
from . import encrypt
from . import decrypt

class TelaPython():
    def __init__(self):
        layout = [
            [sg.Radio('CRIPTOGRAFAR', 'select', key='encrypt', default=True), sg.Radio('DESCRIPTOGRAFAR', 'select', key='decrypt')],
            [sg.Text('Texto de entrada')],
            [sg.Input(key = 'entrada', size=(80, 20))],
            [sg.Button('REALIZAR OPERAÇÃO')],
            [sg.Text('Saida')],
            [sg.Output(size = (80, 10), key='output')]
        ]
    
        self.janela = sg.Window('CRIPT').layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            self.entrada = self.values['entrada']
            self.encrypt = self.values['encrypt']
            self.decrypt = self.values['decrypt']
            TelaPython.limpar(self.janela, 'output')
            if (self.encrypt):
                print(progam.callEncrypt(self.entrada))
            elif (self.decrypt):
                print(progam.callDecrypt(self.entrada))

    def limpar(janela, chave):
        janela.FindElement(chave).Update('')

class progam():
    def callEncrypt(text):
        return(encrypt.criptografador(text))
    def callDecrypt(text):
        return(decrypt.descriptografador(text))