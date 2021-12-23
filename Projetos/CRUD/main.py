# Imports
from PyQt5 import uic, QtWidgets, QtCore
from pathlib import Path
from os.path import join
from source import login_account, create_account, read_accounts

class window():
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        # Forms

        self.login = self.load_ui('login.ui')
        self.create = self.load_ui('create_account.ui')
        self.read = self.load_ui('read_accounts.ui')

        # Buttons

        # Login

        self.login.createAccountButton.clicked.connect(self.show_create_account)
        self.login.loginAccountButton.clicked.connect(self.login_account)

        # Create

        self.create.createAccountButton.clicked.connect(self.create_account)

        # List

        self.read.saveButton.clicked.connect(self.save_user)
        self.read.deleteButton.clicked.connect(self.delete_user)

        # Exec
        self.login.show()
        self.app.exec()

    def load_ui(self, ui_file):
        path = join(Path().absolute(), 'interfaces/')
        return uic.loadUi(f'{path}{ui_file}')

    def show_create_account(self):
        self.create.show()
        self.login.close()

    def login_account(self):
        self.name = str(self.login.nameInput.text()).strip()
        self.password = str(self.login.passInput.text()).strip()
        log = login_account.Login('localhost', 'root', 'root', 'TEST')
        user = log.login_account(self.name, self.password)

        if (type(user)) != tuple:
            QtWidgets.QMessageBox.about(self.login, "Alerta!", "Nome de usuario ou senha invalidos!\nInsira um nome de usuario ou senha validos e tente novamente.")
        else:
            self.list_accounts()

    def create_account(self):
        name = str(self.create.nameInput.text()).lower().strip()
        password = self.create.passInput.text()

        con = create_account.createAccount('localhost', 'root', 'root', 'TEST')
        user = con.create_account(name, password)

        if user:
            QtWidgets.QMessageBox.about(self.create, "Alerta!", "Conta criada com sucesso!")
            self.login.show()
            self.create.close()
        else :
            QtWidgets.QMessageBox.about(self.create, "Alerta!", "Conta já existente!\nInsira um nome de usuario diferente e tente novamente.")

    def list_accounts(self):
        self.read.listNames.clear()
        self.read.listPassword.clear()

        self.read.show()
        self.login.close()
        con = read_accounts.read_accounts('localhost', 'root', 'root', 'TEST')
        self.original_accounts = con.list_accounts()

        for account in self.original_accounts:
            self.read.listNames.addItem(account[0])
            self.read.listPassword.addItem(account[1])

        for index in range(self.read.listNames.count()):
            item = self.read.listNames.item(index)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)

        for index in range(self.read.listPassword.count()):
            item = self.read.listPassword.item(index)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)

    def save_user(self):
        new_names, new_passwords = [], []

        for index in range(self.read.listNames.count()): new_names.append(str(self.read.listNames.item(index).text()).lower().strip())

        for index in range(self.read.listPassword.count()): new_passwords.append(self.read.listPassword.item(index).text())

        account_names = self.original_accounts

        for itens in range(len(new_names)) :
            if account_names[itens][0] != new_names[itens] :
                con = read_accounts.read_accounts('localhost', 'root', 'root', 'TEST')
                user = con.update_user_name(account_names[itens][0], new_names[itens])
                self.original_accounts = con.list_accounts()

                if not user:
                    QtWidgets.QMessageBox.about(self.read, "Alerta!", "Nome de usuario já existente!\nInsira um nome de usuario diferente e tente novamente.")
                else :
                    QtWidgets.QMessageBox.about(self.read, "Alerta!", "Nome de usuario alterado com sucesso!")

        for itens in range(len(new_passwords)) :
            if account_names[itens][1] != new_passwords[itens] :
                username = self.read.listNames.item(itens).text()
                con = read_accounts.read_accounts('localhost', 'root', 'root', 'TEST')
                user = con.update_user_password(username, new_passwords[itens])
                self.original_accounts = con.list_accounts()
                QtWidgets.QMessageBox.about(self.read, "Alerta!", "Senha alterada com sucesso!")

    def delete_user(self):
        self.save_user()
        row = self.read.listNames.currentRow()
        username = self.read.listNames.item(row).text()
        password = self.read.listPassword.item(row).text()
        self.read.listNames.takeItem(row)
        self.read.listPassword.takeItem(row)
        acc = read_accounts.read_accounts('localhost', 'root', 'root', 'TEST')
        acc.delete_user(username, password)
        QtWidgets.QMessageBox.about(self.read, "Alerta!", "Usuario deletado com sucesso!")
        self.original_accounts = acc.list_accounts()

if __name__ == '__main__':
    window()