import PySimpleGUI as sg
from download import DownloadVideo

class Interface():
    def __init__(self) -> None:
        layout = [
            [sg.Text('Link da Música', key='playlist')],
            [sg.Input(key = 'link', size=(80, 20))],
            [sg.Button('Baixar Música')],
            [sg.Output(size = (80, 5), key='output')]
        ]
    
        self.janela = sg.Window('MUSIC-DOWNLOAD').layout(layout)

    def start(self):
        while True:
            self.clear('output')
            self.button, self.values = self.janela.Read()
            self.link = self.values['link']
            DownloadVideo(self.link)
    
    def clear(self, key):
        self.janela.FindElement(key).Update('')

    def write(self, key, text):
        self.janela.FindElement(key).Update(text)

tela = Interface()
tela.start()