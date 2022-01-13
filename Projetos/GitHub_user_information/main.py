from PyQt5 import uic, QtWidgets
from pathlib import Path
from os.path import join
from source.layouts_controls import user_name_informations_control, user_information_control

class Window():
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication([])

        # Forms

        self.form_init = self.load_ui('user_name_information')
        self.user_informations = self.load_ui('user_informations')

        # Buttons

        # Form init

        self.form_init.pushButton.clicked.connect(self.get_user_information)

        # Exec

        self.form_init.show()
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

    def get_user_information(self) -> None:
        """Gets the user information from GitHub API

        Returns:
            None
        """
        user_name_informations_control.user_name_informations_control.get_user_information(self)

    def show_user_informations(self) -> None:
        """Shows the user information

        Returns:
            None
        """
        user_information_control.user_information_control.show_user_information(self)

if __name__ == '__main__':
    Window()