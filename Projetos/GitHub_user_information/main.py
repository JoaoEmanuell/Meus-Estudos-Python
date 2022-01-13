from PyQt5 import QtCore, uic, QtWidgets, QtGui
from pathlib import Path
from os.path import join
from requests import get
from source.api import user

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
        self.username = self.form_init.lineEdit.text().strip()
        self.user = user.RequestUser(self.username).get_user()
        if self.user.get('message') == 'Not Found':
            QtWidgets.QMessageBox.about(self.form_init, 'Error', 'User not found')
        else:
            self.form_init.close()
            self.show_user_informations()

    def show_user_informations(self) -> None:
        self.user_informations.show()
        self.user_informations.username.setText(f'<html><head/><body><p><span style = "color : #8b949e">{self.user["login"]}</span></p></body></html>')
        self.user_informations.user_name.setText(f'<html><head/><body><p><span style = "color : #C9D1D9">{self.user["name"]}</span></p></body></html>')
        self.image_set()

    def image_set(self):
        image = QtGui.QImage()
        image.loadFromData(get(self.user['avatar_url']).content)
        self.user_informations.user_profile_photo.setPixmap(QtGui.QPixmap(image).scaled(250, 250))


if __name__ == '__main__':
    Window()