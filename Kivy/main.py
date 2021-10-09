from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout

class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas :
            self.ids.box.add_widget(Tarefa(text=tarefa))

class Tarefa(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Test(App):
    def build(self):
        return Tarefas(['Fazer compras', 'Ir para a escola', 'Regar as plantas', 'Cornelius', 'Legal', 'top'])

Test().run()