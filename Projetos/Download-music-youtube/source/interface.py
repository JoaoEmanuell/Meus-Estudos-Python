import PySimpleGUI as sg
from . import download

class Interface():
    def __init__(self) -> None:
        layout = [
            [sg.Text('Link da Música ou playlist', key='playlist')],
            [sg.Input(key = 'link', size=(80, 20))],
            [sg.Button('Baixar Música')],
            [sg.Output(size = (80, 5), key='output')]
        ]
    
        self.janela = sg.Window('MUSIC-DOWNLOAD').layout(layout)

    def start(self):
        while True:
            try:
                self.event, self.values = self.janela.Read()
                self.clear('output')
                self.link = self.values['link']
                if self.event == 'Baixar Música':
                    download.DownloadVerfiy(self.link)
            except Exception:
                print(f"Algo deu errado, portanto o download não pode ser concluido, por favor tente inserir uma nova url!\n {Exception}")
                if self.event == sg.WIN_CLOSED:
                    break
    
    def clear(self, key):
        self.janela.FindElement(key).Update('')

    def write(self, key, text):
        self.janela.FindElement(key).Update(text)