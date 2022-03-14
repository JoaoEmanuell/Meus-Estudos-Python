from kivy.app import App
from kivy.clock import mainthread

@mainthread
def set_output(text : str):
    App.get_running_app().root.ids.output.text = str(text)