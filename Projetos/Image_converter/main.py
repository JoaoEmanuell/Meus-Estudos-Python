# Imports
from PyQt5 import uic, QtWidgets
from pathlib import Path

class window():
    def __init__(self):
        self.app = QtWidgets.QApplication([])

        # Forms

        self.form = self.load_ui('interface.ui')

        # Buttons

        self.form.select_images_button.clicked.connect(self.open_images)
        self.form.convert_images_button.clicked.connect(self.convert_images)

        # Execute
        self.form.show()
        self.app.exec()

    def load_ui(self, ui_file):
        """Loads the desired interface, every interface is a .ui file

        Args:
            ui_file ([ui]): [.ui file name]

        Returns:
            [ui]: [Interface loaded]
        """
        path = Path().absolute()
        return uic.loadUi(f'{path}/{ui_file}')

    def open_images(self):
        filter = "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        self.files = QtWidgets.QFileDialog.getOpenFileNames(filter=filter)[0]
        self.set_images_in_list()

    def convert_images(self):
        print("Convert")

    def set_images_in_list(self):
        for image in self.files:
            self.form.image_name_list.addItem(image)

if __name__ == '__main__':
    window()