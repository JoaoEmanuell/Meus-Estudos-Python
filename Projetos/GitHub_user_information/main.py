from PyQt5 import uic, QtWidgets
from pathlib import Path
from os.path import join

class Window():
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication([])

        self.form = self.load_ui('user_name_information')

        self.form.show()

        self.app.exec()

    def load_ui(self, ui_file):
        """Loads the desired interface, every interface is a .ui file

        Args:
            ui_file ([ui]): [.ui file name]

        Returns:
            [ui]: [Interface loaded]
        """
        path = join(Path().absolute(), 'layouts/')
        return uic.loadUi(f'{path}{ui_file}.ui')

if __name__ == '__main__':
    Window()