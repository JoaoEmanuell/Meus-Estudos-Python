from PyQt5.QtWidgets import QMainWindow

class ReposNameControl():
    def __init__(self, layout : QMainWindow, repositories : dict) -> None:
        self.layout = layout
        self.repositories = repositories

    def set_repos_in_list(self):

        self.layout.list_repos_names.clear()

        for repo in self.repositories:
            
            self.layout.list_repos_names.addItem(repo['name'])
