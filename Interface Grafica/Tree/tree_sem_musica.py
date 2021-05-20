#Como eu não conseguia resolver os bugs, decidi criar 2 arquivos, esse arquivo abre e no final toca o beep assim com o primeiro, sem lofi

from time import sleep
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Tree
from audioplayer import AudioPlayer

def tempo(t, janela, chave):
    """[Função para contar o tempo, serve como o nome já diz para contar o tempo que você irar passar]

    Args:
        t ([int]): [Minutos que o contandor passara contando]
    """
    minutos = int(t)
    segundos = 60
    while True:
        janela.FindElement(chave).Update('')
        texto = '{:02d}:{:02d}'.format(minutos, segundos)
        if minutos < 0:
            break
        elif segundos == 60:
            minutos -= 1
            segundos -= 1
        elif segundos == 0:
            segundos = 60
        else:
            segundos -= 1
        print(texto, end = "\r")
        sleep(1)
    AudioPlayer("./Interface Grafica/Tree/tree_lofi/beeps1.mp3").play(False, True)

class interface():
    def __init__(self):
        layout = [
            [sg.Text("Minutos: ") ,sg.Input(size = '2', key = "Tempo")],
            [sg.Button("Iniciar")],
            [sg.Output(key = "saida", size = ('150', '5'))]
        ]
        
        self.janela = sg.Window('Tree').layout(layout)
    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            minutos = self.values["Tempo"]
            tempo(minutos, self.janela, 'saida')


tela = interface()

tela.iniciar()