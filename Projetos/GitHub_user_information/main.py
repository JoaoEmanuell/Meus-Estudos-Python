from PyQt5 import uic, QtWidgets
from pathlib import Path
from os.path import join
from source.api import user

class Window():
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication([])

        # Forms

        self.form_init = self.load_ui('user_name_information')

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
        username = self.form_init.lineEdit.text().strip()
        self.user = user.RequestUser(username).get_user()
        if self.user.get('message') == 'Not Found':
            QtWidgets.QMessageBox.about(self.form_init, 'Error', 'User not found')
        else:
            print(self.user)

if __name__ == '__main__':
    Window()