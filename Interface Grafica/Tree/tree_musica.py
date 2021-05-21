#Como eu não conseguia resolver os bugs, decidi criar 2 arquivos, esse arquivo abre e toca o lofi e tem o bug do lofi tocar infinitamente indepedente do tempo :/

from time import sleep
import PySimpleGUI as sg
from audioplayer import AudioPlayer
from PySimpleGUI.PySimpleGUI import Tree
from threading import Thread 

def tempo(t, janela, chave):
    """[Serve para contar o tempo que você irar passar]

    Args:
        t ([int]): [Minutos que o progama ira contar]
        janela ([str]): [Janela que a interface está executando]
        chave ([str]): [chave para modifcar o elemento e subistituir ele]
    """
    try:
        minutos = abs(int(t))
    except ValueError:
        print("Descupe, o numero de minutos informados está invalido, sera considerado 1 minuto")
        sleep(3)
        minutos = 1
    finally:
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
def musica():
    """[Função que toca a musica]
    """
    try:   
        AudioPlayer("./Interface Grafica/Tree/tree_lofi/lofi.mp3").play(True, True)
    except FileNotFoundError:
        print("A musica não pode ser reproduzida, pois ouve um erro")

def main():
    """[main, executa ambas as funções em pararelo, infelizmente a função musica não para quando o progama termina de contar o tempo]
    """
    try:
        t1 = Thread(target = tempo)
        t2 = Thread(target = musica)
        t1.start()
        t2.start()
    except TypeError:
        print("Erro de tipo na hora de chamar a função")

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
        """[Recolhe as informações da tela, chama a função main e a função tempo]
        """        
        while True:
            self.button, self.values = self.janela.Read()
            minutos = self.values["Tempo"]
            if __name__ == "__main__":
                main()
            tempo(minutos, self.janela, 'saida')

tela = interface()

tela.iniciar()
