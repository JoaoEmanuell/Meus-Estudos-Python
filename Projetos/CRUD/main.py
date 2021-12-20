# Imports
from PyQt5 import uic, QtWidgets
from pathlib import Path
from os.path import join

class window():
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.form = self.load_ui('login.ui')
        self.form.show()
        self.app.exec()

    def load_ui(self, ui_file):
        path = join(Path().absolute(), 'interfaces/')
        return uic.loadUi(f'{path}{ui_file}')

window()