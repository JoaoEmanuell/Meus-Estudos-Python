from PyQt5 import uic
from pathlib import Path
from os.path import join
from PyQt5.QtWidgets import QMainWindow

class Essential():
    def load_ui(self, ui_file) -> QMainWindow :
        """Loads the desired interface, every interface is a .ui file

        Args:
            ui_file ([ui]): [.ui file name]

        Returns:
            [ui]: [Interface loaded]
        """
        path = join(Path().absolute(), './layouts/')
        return uic.loadUi(f'{path}{ui_file}.ui')

    def get_style_sheet(self) -> str:
        """Gets the style sheet"""

        return open(join(Path().absolute(), './style.qss'), 'r').read()