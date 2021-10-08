from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tarefas(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas :
            self.add_widget(Label(text=tarefa, font_size=30))

class Test(App):
    def build(self):
        return Tarefas(['Fazer compras', 'Ir para a escola', 'Regar as plantas'], orientation='horizontal')

Test().run()