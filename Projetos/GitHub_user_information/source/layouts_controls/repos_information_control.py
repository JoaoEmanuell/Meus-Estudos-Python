class repos_information_control():
    def set_items(self):
        row = self.repos_name.list_repos_names.currentRow()
        url_template = '<a href="{}">{}</a>'
        self.repos_information.repo_name.setText(f'<a href="{self.repos[row]["html_url"]}">{self.repos[row]["name"]}</a>')
        self.repos_information.repo_full_name.setText(self.repos[row]["full_name"])
        self.repos_information.repo_description.setText(self.repos[row]["description"])

    def menu_back(self):
        self.repos_information.close()
        self.repos_name.show()