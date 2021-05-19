from time import sleep
import PySimpleGUI as sg
from audioplayer import AudioPlayer
from PySimpleGUI.PySimpleGUI import Tree
import threading

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

def musica():   
    AudioPlayer("./Interface Grafica/tree_lofi/lofi.mp3").play(True, True)

def main():
    t1 = threading.Thread(target = tempo)
    t2 = threading.Thread(target = musica)
    t1.start()
    t2.start()

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
            if __name__ == "__main__":
                main()
            tempo(minutos, self.janela, 'saida')
            print("Encerrado")
 
tela = interface()

tela.iniciar()