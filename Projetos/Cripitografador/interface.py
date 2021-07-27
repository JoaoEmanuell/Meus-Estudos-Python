import PySimpleGUI as sg
import cript
import descpt

class TelaPython():
    def __init__(self):
        layout = [
            [sg.Radio('CRIPTOGRAFAR', 'select', key='cript'), sg.Radio('DESCRIPTOGRAFAR', 'select', key='descript')],
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
            self.cript = self.values['cript']
            self.descript = self.values['descript']
            TelaPython.limpar(self.janela, 'output')
            if (self.cript):
                print(progam.callCript(self.entrada))
            elif (self.descript):
                print(progam.callDescript(self.entrada))
            else:
                print('Por favor, marque uma opção válida!')

    def limpar(janela, chave):
        janela.FindElement(chave).Update('')

class progam():
    def callCript(text):
        return(cript.criptografador(text))
    def callDescript(text):
        return(descpt.descriptografador(text))