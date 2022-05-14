# Imports

# Global imports

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from pathlib import Path
from os.path import join
from typing import Type

# Local imports

from ..interfaces import MainWindowInterface
from ..generate_window import GenerateWindow

class MainWindow(MainWindowInterface):
    def __init__(self) -> None :
        self.__app = QApplication([])

        # Main form

        self.__main_form = self.load_ui("main.ui")
        self.__main_form.generate_button.clicked.connect(self.__main_generate_button_clicked)
        self.__main_form.scan_button.clicked.connect(self.__scan_button_clicked)

        # Generate form

        self.__generate_form = self.load_ui("generate_qr_code.ui")
        self.__generate_form.pushButton.clicked.connect(self.__generate_form_generate_button_clicked)

        self.__main_form.show()

        self.__app.exec_()

    def load_ui(self, ui_file : str) -> Type[QWidget] :
        path = Path().absolute()
        ui_file = QFile(f'{join(path, "layouts/")}{ui_file}')
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        ui = loader.load(ui_file)
        return ui

    def __main_generate_button_clicked(self) -> None :

        self.__generate_form.show()

        self.__main_form.close()

    def __generate_form_generate_button_clicked(self) -> None :
        win = GenerateWindow()

        win.generate_button_clicked()

    def __scan_button_clicked(self) -> None :
        pass