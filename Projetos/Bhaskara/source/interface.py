#from roots import roots
from . import roots
import PySimpleGUI as sg

class screen():
    def __init__(self) -> None:
        layout = [
        [sg.Text("A"), sg.Input(key="A", size=(20,5))],
        [sg.Text("B"), sg.Input(key="B", size=(20,5))],
        [sg.Text("C"), sg.Input(key="C", size=(20,5))],
        [sg.Button("Calcular")],
        [sg.Text("Δ "), sg.Output(key="delt", size=(20,0))],
        [sg.Text("X'"), sg.Output(key="x1", size=(20,0))], 
        [sg.Text('X"'), sg.Output(key="x2", size=(20,0))],
        [sg.Output(key="delt-alert", visible=False, size=(29,5))]
        ]
        self.janela = sg.Window('EQUAÇÃO DO SEGUNDO GRAU').layout(layout)

    def Start(self):
        while True:
            self.button, self.values = self.janela.Read()
            #self.janela.FindElement('delt-alert').update(visible=False)
            Configs.SetVisibilit(self.janela, 'delt-alert', False)
            Configs.ClearElements(self.janela, 'delt', 'x1', 'x2')
            try:
                self.a = float(self.values['A'])
                self.b = float(self.values['B'])
                self.c = float(self.values['C'])
            except ValueError:
                Configs.SetVisibilit(self.janela, 'delt-alert', True)
                Configs.Write(self.janela, 'delt-alert', 'Valor invalido, tente novamente!')
                Configs.ClearElements(self.janela, 'A', 'B', 'C')
            else:
                rot = roots.roots(self.a, self.b, self.c)
                if rot[2] < 0:
                    Configs.SetVisibilit(self.janela, 'delt-alert', True)
                    Configs.Write(self.janela, 'delt-alert', 'Delta negativo, portanto as raizes são indetermiandas!')
                Configs.WriteElements(self.janela, rot)
class Configs():
    def Clear(window, key):
        window.FindElement(key).Update('')

    def ClearElements(window, key1, key2, key3):
        window.FindElement(key1).Update('')
        window.FindElement(key2).Update('')
        window.FindElement(key3).Update('')

    def Write(window, key, text):
        window.FindElement(key).Update(text)

    def WriteElements(window, rot):
        window.FindElement('x1').Update(rot[0])
        window.FindElement('x2').Update(rot[1])
        window.FindElement('delt').Update(rot[2])

    def SetVisibilit(window, key, vi):
        window.FindElement(key).update(visible=vi)