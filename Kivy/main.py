from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Test(App):
    def build(self):
        box = BoxLayout(orientation="vertical")
        button = Button(text="Botão 1")
        label = Label(text="Hello world")
        box.add_widget(label)
        box.add_widget(button)

        box2 = BoxLayout()
        button2 = Button(text="Botão 2")
        label2 = Label(text="Hello world 2")
        box2.add_widget(label2)
        box2.add_widget(button2)
        
        box.add_widget(box2)
        return box

Test().run()