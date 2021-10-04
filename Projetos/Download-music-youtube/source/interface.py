import PySimpleGUI as sg

class Interface():
    def __init__(self) -> None:
        layout = [
            [sg.Radio('CRIPTOGRAFAR', 'select', key='encrypt', default=True), sg.Radio('DESCRIPTOGRAFAR', 'select', key='decrypt')],
            [sg.Text('Texto de entrada')],
            [sg.Input(key = 'entrada', size=(80, 20))],
            [sg.Button('REALIZAR OPERAÇÃO')],
            [sg.Text('Saida')],
            [sg.Output(size = (80, 10), key='output')]
        ]
    
        self.janela = sg.Window('MUSIC-DOWNLOAD').layout(layout)

    def start(self):
        while True:
            self.button, self.values = self.janela.Read()
            self.entrada = self.values['entrada']
            self.encrypt = self.values['encrypt']
            self.decrypt = self.values['decrypt']
            Interface.clear(self.janela, 'output')
    
    def clear(janela, chave):
        janela.FindElement(chave).Update('')

tela = Interface()
tela.start()