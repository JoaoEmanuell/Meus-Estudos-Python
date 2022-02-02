from PyQt5.QtWidgets import QMessageBox, QApplication
from source.views.user_information_control import UserInformationContro
from source.views.user_name_informations_control import UserNameInformationsControl
from source.views.repos_name_control import ReposNameControl
from source.views.repos_information_control import ReposInformationControl
from essential import Essential
from source.api.repos import RequestRepositories

class Window(Essential):
    def __init__(self) -> None:
        self.app = QApplication([])

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
        self.user = UserNameInformationsControl(self.form_init.lineEdit.text()).get_user_information()
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
        UserInformationContro(self.user_informations, self.user).show_user_information()

    def user_informations_menu_back(self) -> None:
        """Clear cache and closes the user information menu

        Returns:
            None
        """
        RequestRepositories.get_user_repos.cache_clear(), self.app.closeAllWindows(), self.form_init.show()

    def get_user_repos(self) -> None:
        """Gets the user repositories

        Returns:
            None
        """
        self.repos = RequestRepositories(self.user).get_user_repos()

        if type(self.repos) == str:

            QMessageBox.about(self.user_informations, 'Error', self.repos)

        else :

            self.repos_name.show()

            self.user_informations.close()

            self.repos_name.list_repos_names.itemDoubleClicked.connect(self.show_repo_info)

            ReposNameControl(self.repos_name, self.repos).set_repos_in_list()

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
        self.repos_name.close()

        self.repos_information.show()
        
        row = self.repos_name.list_repos_names.currentRow()

        ReposInformationControl(self.repos_information, self.repos, row).set_items()

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
        RequestRepositories.get_user_repos.cache_clear(), self.app.closeAllWindows(), self.form_init.show()

if __name__ == '__main__':
    Window()