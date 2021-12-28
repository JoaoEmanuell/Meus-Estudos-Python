# Imports
from PyQt5 import uic, QtWidgets, QtCore
from pathlib import Path

class window():
    def __init__(self):
        self.app = QtWidgets.QApplication([])

        # Forms

        self.form = self.load_ui('interface.ui')

        # Buttons

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

if __name__ == '__main__':
    window()