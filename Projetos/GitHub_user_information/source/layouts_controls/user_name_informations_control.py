from ..api import user
from PyQt5.QtWidgets import QMessageBox

class user_name_informations_control():
    def get_user_information(self) -> None:
        """Gets the user information from GitHub API

        Returns:
            None
        """
        self.username = self.form_init.lineEdit.text().strip()
        self.user = user.RequestUser(self.username).get_user()
        if self.user.get('message') == 'Not Found':
            QMessageBox.about(self.form_init, 'Error', 'User not found')
        else:
            self.form_init.close()
            self.show_user_informations()