from PyQt5 import uic, QtWidgets
from pathlib import Path
from os.path import join
from source.layouts_controls import user_name_informations_control, user_information_control, repos_name_control, repos_information_control

class Window():
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

        # Exec

        self.form_init.show()
        self.app.setStyleSheet(self.getStyleSheet())
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

    def user_informations_menu_back(self) -> None:
        """Clear cache and closes the user information menu

        Returns:
            None
        """
        user_information_control.user_information_control.get_user_repos.cache_clear(), self.app.closeAllWindows(), self.form_init.show()

    def get_user_repos(self) -> None:
        """Gets the user repositories

        Returns:
            None
        """
        self.repos = user_information_control.user_information_control.get_user_repos(self)

        self.user_informations.close()

        self.repos_name.show()

        repos_name_control.repos_name_control.set_repos_in_list(self)

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
        repos_name_control.repos_name_control.show_repo_info(self)
        repos_information_control.repos_information_control.set_items(self)

    def repos_information_menu_back(self) -> None:
        """Closes the repo information menu

        Returns:
            None
        """
        self.app.closeAllWindows(), self.repos_name.show()

    def getStyleSheet(self) -> str:
        """Gets the style sheet"""

        return open(join(Path().absolute(), 'style.qss'), 'r').read()

if __name__ == '__main__':
    Window()