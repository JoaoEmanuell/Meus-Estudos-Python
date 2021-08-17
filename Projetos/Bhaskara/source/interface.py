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
        [sg.Text('X"'), sg.Output(key="x2", size=(20,0))]
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
            screen.Write(self.janela, 'x1', rot[0])
            screen.Write(self.janela, 'x2', rot[1])
            screen.Write(self.janela, 'delt', rot[2])
            
    def Clear(window, key):
        window.FindElement(key).Update('')

    def ClearElements(window):
        window.FindElement('delt').Update('')
        window.FindElement('x1').Update('')
        window.FindElement('x2').Update('')

    def Write(window, key, text):
        window.FindElement(key).Update(text)
