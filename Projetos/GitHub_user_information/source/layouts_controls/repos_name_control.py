class repos_name_control():
    def set_repos_in_list(self):
        self.repos_name.list_repos_names.clear()
        for repo in self.repos:
            self.repos_name.list_repos_names.addItem(repo['name'])

    def show_repo_info(self):
        self.repos_name.close()
        self.repos_information.show()
            
    def menu_back(self):
        self.repos_name.close()
        self.user_informations.show()