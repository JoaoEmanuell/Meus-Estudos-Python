"""
    This module contains the Message class.
"""

from kivy.app import App
from kivy.clock import mainthread

class Message:
    """
        This class send message to interface in main thread.
    """    
    @mainthread
    def set_output(text : str):
        App.get_running_app().root.ids.output.text = str(text)

    @mainthread
    def set_progressbar(max : int = 100, percent : int = 0):
        App.get_running_app().root.ids.progressbar.max = int(max)
        App.get_running_app().root.ids.progressbar.value = int(percent)