from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from views.user_information_control import user_information_control
from views.user_name_informations_control import user_name_informations_control
from views.repos_name_control import repos_name_control
from views.repos_information_control import repos_information_control
from essential import Essential

class Window(Essential):
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication([])

        # Forms

        self.form_init = self.load_ui('user_name_information')
        self.user_informations = self.load_ui('user_informations')
        self.repos_name = self.load_ui('repos_name')
        self.repos_information = self.load_ui('repos_information')

        # Buttons

        # Form init

        self.form_init.pushButton.clicked.connect(self.get_user_information)

        # User informations

        self.user_informations.button_repos.clicked.connect(self.get_user_repos)

        # Repos name

        self.repos_name.button_repo_select.clicked.connect(self.show_repo_info)

        # Menu

        # Form user information

        self.user_informations.action_return.triggered.connect(self.user_informations_menu_back)

        # Repos name

        self.repos_name.action_return.triggered.connect(self.repos_name_menu_back)

        # Repos information

        self.repos_information.action_return.triggered.connect(self.repos_information_menu_back)
        self.repos_information.action_start_screen.triggered.connect(self.repos_information_menu_start_screen)

        # Exec

        self.form_init.show()
        self.app.setStyleSheet(self.get_style_sheet())
        self.app.exec()

    def get_user_information(self) -> None:
        """Gets the user information from GitHub API

        Returns:
            None
        """
        self.user = user_name_informations_control(self.form_init.lineEdit.text()).get_user_information()
        if type(self.user) == str:
            QMessageBox.about(self.form_init, 'Error', self.user)
        else :
            self.show_user_informations()
            self.form_init.close()

    def show_user_informations(self) -> None:
        """Shows the user information

        Returns:
            None
        """
        user_information_control.show_user_information(self)

    def user_informations_menu_back(self) -> None:
        """Clear cache and closes the user information menu

        Returns:
            None
        """
        user_information_control.get_user_repos.cache_clear(), self.app.closeAllWindows(), self.form_init.show()

    def get_user_repos(self) -> None:
        """Gets the user repositories

        Returns:
            None
        """
        self.repos = user_information_control.get_user_repos(self)

        self.user_informations.close()

        self.repos_name.show()

        repos_name_control.set_repos_in_list(self)

    def repos_name_menu_back(self) -> None:
        """Closes the repos name menu

        Returns:
            None
        """
        self.app.closeAllWindows(), self.user_informations.show()

    def show_repo_info(self) -> None:
        """Shows the repo

        Returns:
            None
        """
        repos_name_control.show_repo_info(self)
        repos_information_control.set_items(self)

    def repos_information_menu_back(self) -> None:
        """Closes the repo information menu

        Returns:
            None
        """
        self.app.closeAllWindows(), self.repos_name.show()

    def repos_information_menu_start_screen(self) -> None:
        """Closes the repo information menu

        Returns:
            None
        """
        user_information_control.get_user_repos.cache_clear(), self.app.closeAllWindows(), self.form_init.show()

if __name__ == '__main__':
    Window()