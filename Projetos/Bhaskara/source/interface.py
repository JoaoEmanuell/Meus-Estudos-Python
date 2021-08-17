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
        [sg.Output(key="delt-alert", visible=False, size=(20,0))]
        ]
        self.janela = sg.Window('EQUAÇÃO DO SEGUNDO GRAU').layout(layout)

    def Start(self):
        while True:
            self.button, self.values = self.janela.Read()
            self.a = float(self.values['A'])
            self.b = float(self.values['B'])
            self.c = float(self.values['C'])
            screen.ClearElements(self.janela)
            rot = roots.roots(self.a, self.b, self.c)
            if rot[2] < 0:
                self.janela.FindElement('delt-alert').update(visible=True)
                screen.Write(self.janela, 'delt-alert', 'Delta negativo, portanto as raizes são indetermiandas!')
            screen.WriteElements(self.janela, rot)
            
    def Clear(window, key):
        window.FindElement(key).Update('')

    def ClearElements(window):
        window.FindElement('delt').Update('')
        window.FindElement('x1').Update('')
        window.FindElement('x2').Update('')

    def Write(window, key, text):
        window.FindElement(key).Update(text)

    def WriteElements(window, rot):
        window.FindElement('x1').Update(rot[0])
        window.FindElement('x2').Update(rot[1])
        window.FindElement('delt').Update(rot[2])