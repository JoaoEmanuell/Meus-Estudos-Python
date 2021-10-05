import PySimpleGUI as sg
from download import DownloadVerfiy

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
            try:
                self.button, self.values = self.janela.Read()
                self.clear('output')
                self.link = self.values['link']
                DownloadVerfiy(self.link)
            except:
                print("Algo deu errado, portanto o download não pode ser concluido, por favor tente inserir uma nova url!")
    
    def clear(self, key):
        self.janela.FindElement(key).Update('')

    def write(self, key, text):
        self.janela.FindElement(key).Update(text)

tela = Interface()
tela.start()