# Imports

# Global imports

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget
from PySide2.QtCore import QFile
from pathlib import Path
from os.path import join
from typing import Type

class Window(QMainWindow):
    def __init__(self) -> None :
        self.app = QApplication([])

        self.main_form = self.load_ui("main.ui")

        self.main_form.show()

        self.app.exec_()

    def load_ui(self, ui_file : str) -> Type[QWidget] :
        path = Path().absolute()
        ui_file = QFile(f'{join(path, "layouts/")}{ui_file}')
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        ui = loader.load(ui_file)
        return ui

if __name__ == '__main__' :
    window = Window()