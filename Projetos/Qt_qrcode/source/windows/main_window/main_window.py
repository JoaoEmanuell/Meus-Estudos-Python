# Imports

# Global imports

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import QFile
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

        self.__app.exec()

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
        url = str(self.__generate_form.lineEdit.text()).strip()

        path = str(QFileDialog.getSaveFileName(
            filter='Images (*.png)', # Filter for file types
        )[0])

        generate_window = GenerateWindow(url)

        del url # Delete variable to free memory

        image = generate_window.generate_qrcode()

        try : 

            generate_window.save_image(image, path)

            del path, image, generate_window

        except ValueError :
            
            QMessageBox.warning(self.__generate_form, "Error", "Invalid file extension")

        else :

            QMessageBox.information(self.__generate_form, "Success", "QR code generated")

    def __scan_button_clicked(self) -> None :
        pass