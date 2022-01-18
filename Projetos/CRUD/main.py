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

        # Menu

        self.read.actionLogin.triggered.connect(self.show_login)
        
        self.create.actionLogin.triggered.connect(self.show_login)

        # Exec
        self.login.show()
        self.app.exec()

    def load_ui(self, ui_file):
        """Loads the desired interface, every interface is a .ui file

        Args:
            ui_file ([ui]): [.ui file name]

        Returns:
            [ui]: [Interface loaded]
        """
        path = join(Path().absolute(), 'interfaces/')
        return uic.loadUi(f'{path}{ui_file}')

    def show_create_account(self): self.create.show(), self.login.close()

    def show_login(self): self.login.show(), self.create.close(), self.read.close() # Show login and close create, read

    def login_account(self):
        """Enter the account using the username and password, if valid it will run the list_accounts function, otherwise it will return an error dialog box.
        """
        self.name = str(self.login.nameInput.text()).strip()
        self.password = str(self.login.passInput.text()).strip()
        log = login_account.Login()
        user = log.login_account(self.name, self.password)

        # Valid user
        if (type(user)) != tuple:
            QtWidgets.QMessageBox.about(self.login, "Alerta!", "Nome de usuario ou senha invalidos!\nInsira um nome de usuario ou senha validos e tente novamente.")
        else:
            self.list_accounts()

    def create_account(self):
        """Create a new account.
        """
        name = str(self.create.nameInput.text()).lower().strip()
        password = self.create.passInput.text()

        con = create_account.createAccount()
        user = con.create_account(name, password)

        # Valid user
        if user:
            QtWidgets.QMessageBox.about(self.create, "Alerta!", "Conta criada com sucesso!")
            self.login.show()
            self.create.close()
        else :
            QtWidgets.QMessageBox.about(self.create, "Alerta!", "Conta já existente!\nInsira um nome de usuario diferente e tente novamente.")

    def list_accounts(self):
        """Lists the accounts already created and puts the username and password in their respective lists.
        """

        # Clear the lists
        self.read.listNames.clear()
        self.read.listPassword.clear()

        self.read.show()
        self.login.close()
        # Database connection
        con = read_accounts.read_accounts()
        # Original accounts
        self.original_accounts = con.list_accounts()

        # Insert the username and password in their respective lists
        for account in self.original_accounts:
            self.read.listNames.addItem(account[0])
            self.read.listPassword.addItem(account[1])

        # Allows the username and password to be changed. 

        for index in range(self.read.listNames.count()):
            item = self.read.listNames.item(index)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)

        for index in range(self.read.listPassword.count()):
            item = self.read.listPassword.item(index)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)

    def save_user(self):
        """Saves changes made to lists.
        """
        new_names, new_passwords = [], []

        # Add new usernames and passwords to the lists.
        for index in range(self.read.listNames.count()): new_names.append(str(self.read.listNames.item(index).text()).lower().strip())

        for index in range(self.read.listPassword.count()): new_passwords.append(str(self.read.listPassword.item(index).text()).lower().strip())

        account_names = self.original_accounts

        for itens in range(len(new_names)) :
            # Check if the username is different from the original name.
            if account_names[itens][0] != new_names[itens] :
                con = read_accounts.read_accounts()
                user = con.update_user_name(account_names[itens][0], new_names[itens])
                # Save the new information in the variable original_accounts
                self.original_accounts = con.list_accounts()

                if not user:
                    QtWidgets.QMessageBox.about(self.read, "Alerta!", "Nome de usuario já existente!\nInsira um nome de usuario diferente e tente novamente.")
                else :
                    QtWidgets.QMessageBox.about(self.read, "Alerta!", "Nome de usuario alterado com sucesso!")

        for itens in range(len(new_passwords)) :
            # Check if the password is different from the original. 
            if account_names[itens][1] != new_passwords[itens] :
                username = self.read.listNames.item(itens).text()
                con = read_accounts.read_accounts()
                user = con.update_user_password(username, new_passwords[itens])
                if user:
                    # Save the new information in the variable original_accounts
                    self.original_accounts = con.list_accounts()
                    QtWidgets.QMessageBox.about(self.read, "Alerta!", "Senha alterada com sucesso!")
                else :
                    QtWidgets.QMessageBox.about(self.read, "Alerta!", "Alguma senha informada é muito grande, diminua o tamanho da senha e tente novamente!")

    def delete_user(self):
        """Deletes an account."""
        # Salva as alterações nos nomes de usuarios.
        self.save_user()
        row = self.read.listNames.currentRow()
        username = self.read.listNames.item(row).text()
        password = self.read.listPassword.item(row).text()
        self.read.listNames.takeItem(row)
        self.read.listPassword.takeItem(row)
        acc = read_accounts.read_accounts()
        # Delete the account in database.
        acc.delete_user(username, password)
        QtWidgets.QMessageBox.about(self.read, "Alerta!", "Usuario deletado com sucesso!")
        # Save the new information in the variable original_accounts
        self.original_accounts = acc.list_accounts()

if __name__ == '__main__':
    window()