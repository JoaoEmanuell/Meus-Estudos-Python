# Imports

# Global imports

## Qt imports

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QLabel
from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QPixmap

from pathlib import Path
from os.path import join
from typing import Type
from PIL import Image

# Local imports

from ..interfaces import MainWindowInterface
from ..generate_window import GenerateWindow
from ..scan_window import ScanWindow

class MainWindow(MainWindowInterface):
    def __init__(self) -> None :
        self.__app = QApplication([])

        # Main form

        self.__main_form = self.load_ui("main.ui")
        self.__main_form.generate_button.clicked.connect(self.__main_generate_button_clicked)
        self.__main_form.scan_button.clicked.connect(self.__main_scan_button_clicked)

        # Generate form

        self.__generate_form = self.load_ui("generate_qr_code.ui")
        self.__generate_form.generate_qr_code.clicked.connect(self.__generate_form_generate_button_clicked)
        self.__generate_form.pushButton.clicked.connect(self.__generate_form_save_button_clicked)

        # Scan form

        self.__scan_form = self.load_ui("scan_qr_code.ui")
        self.__scan_form.select_button.clicked.connect(self.__scan_form_scan_button_clicked)

        # Menus

        # Generate form

        self.__generate_form.action_return.triggered.connect(self.__menu_generate_form_return_clicked)

        # Scan form

        self.__scan_form.action_return.triggered.connect(self.__menu_scan_form_return_clicked)

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

        generate_window = GenerateWindow(url)

        del url # Delete variable to free memory

        image = generate_window.generate_qrcode()

        tmp_path = join(Path().absolute(), '.tmp', 'tmp.png')

        generate_window.save_image(image, tmp_path)

        image_label : QLabel = self.__generate_form.image_label
        image_label.setPixmap(QPixmap(tmp_path))

        del image, generate_window, tmp_path # Delete variable to free memory

        self.__generate_form.image_layout.addWidget(image_label, alignment=Qt.AlignCenter) # Add image to layout and center it

        image_label.adjustSize()

        del image_label

        QMessageBox.information(self.__generate_form, "Success", "QR code generated")

    def __generate_form_save_button_clicked(self) -> None :
        path = str(QFileDialog.getSaveFileName(
            filter='Images (*.png)', # Filter for file types
        )[0])

        generate_window = GenerateWindow('')

        tmp_path = join(Path().absolute(), '.tmp', 'tmp.png')

        with Image.open(tmp_path) as image :

            try : 

                generate_window.save_image(image, path)

            except ValueError :
            
                QMessageBox.warning(self.__generate_form, "Error", "Invalid file extension")

            except FileNotFoundError :

                QMessageBox.warning(self.__generate_form, "Error", "File not found")

            else :

                QMessageBox.information(self.__generate_form, "Success", "QR code saved")

    def __main_scan_button_clicked(self) -> None :
        self.__main_form.close()

        self.__scan_form.show()

    def __scan_form_scan_button_clicked(self) -> None :
        path = str(QFileDialog.getOpenFileName(
            filter='Images (*.png)', # Filter for file types
        )[0])

        qr_codes = ScanWindow.extract_qr(path)

        del path

        qr_text = ''

        for qr in qr_codes :
            qr_text += f'{str(qr)}\n'

        del qr_codes

        self.__scan_form.result_label.setText(qr_text)

        del qr_text

    def __menu_generate_form_return_clicked(self) -> None :
        self.__generate_form.close()

        self.__main_form.show()

    def __menu_scan_form_return_clicked(self) -> None :
        self.__scan_form.close()

        self.__main_form.show()