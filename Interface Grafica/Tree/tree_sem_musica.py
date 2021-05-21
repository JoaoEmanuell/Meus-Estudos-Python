#Como eu não conseguia resolver os bugs, decidi criar 2 arquivos, esse arquivo abre e no final toca o beep assim com o primeiro, sem lofi

from time import sleep
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Tree
from audioplayer import AudioPlayer

def tempo(t, janela, chave):
    """[Serve para contar o tempo que você irar passar]

    Args:
        t ([int]): [Minutos que o progama ira contar]
        janela ([str]): [Janela que a interface está executando]
        chave ([str]): [chave para modifcar o elemento e subistituir ele]
    """
    minutos = int(t)
    segundos = 59
    while True:
        janela.FindElement(chave).Update('')
        texto = '{:02d}:{:02d}'.format(minutos, segundos)
        if minutos < 0:
            break
        elif segundos == 59:
            minutos -= 1
            segundos -= 1
        elif segundos == 0:
            segundos = 59
        else:
            segundos -= 1
        print(texto, end = "\r")
        sleep(1)
    try:
        AudioPlayer("./Interface Grafica/Tree/tree_lofi/beeps1.mp3").play(False, True) #toca o som dos beeps ao fim do progama
    except FileNotFoundError:
        print("Arquivo de audio não encontrado")

class interface():
    """[Classe responsavel pela interface grafica]
    """    
    def __init__(self):
        """[init, cria o layout]
        """        
        layout = [
            [sg.Text("Minutos: ") ,sg.Input(size = '2', key = "Tempo")],
            [sg.Button("Iniciar")],
            [sg.Output(key = "saida", size = ('150', '5'))]
        ]
        
        self.janela = sg.Window('Tree').layout(layout)
    def iniciar(self):
        """[Recolhe as informações da tela e chama a função tempo]
        """        
        while True:
            self.button, self.values = self.janela.Read()
            minutos = self.values["Tempo"]
            tempo(minutos, self.janela, 'saida')


tela = interface()

tela.iniciar()