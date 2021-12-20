# Imports
from PyQt5 import uic, QtWidgets
from pathlib import Path
from os.path import join
from source import login_account

class window():
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        # Forms

        self.login = self.load_ui('login.ui')
        self.create = self.load_ui('create_account.ui')
        self.read = self.load_ui('read_accounts.ui')

        # Buttons

        self.login.createAccountButton.clicked.connect(self.create_account)
        self.login.loginAccountButton.clicked.connect(self.login_account)

        # Exec
        self.login.show()
        self.app.exec()

    def load_ui(self, ui_file):
        path = join(Path().absolute(), 'interfaces/')
        return uic.loadUi(f'{path}{ui_file}')

    def create_account(self):
        self.create.show()
        self.login.close()

    def login_account(self):
        self.name = self.login.nameInput.text()
        self.password = self.login.passInput.text()
        log = login_account.Login('localhost', 'root', 'root', 'TEST')
        user = log.login_account(self.name, self.password)

        if (type(user)) != tuple:
            QtWidgets.QMessageBox.about(self.login, "Alerta!", "Nome de usuario ou senha invalidos!\nInsira um nome de usuario ou senha validos e tente novamente.")
        else:
            self.read.show()
            self.login.close()

if __name__ == '__main__':
    window()