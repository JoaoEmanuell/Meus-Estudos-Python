from api.license import RequestLicense

class repos_information_control():
    def set_items(self):
        self.row = self.repos_name.list_repos_names.currentRow()
        create_date = repos_information_control.format_date(self.repos[self.row]['created_at'])
        updated_date = repos_information_control.format_date(self.repos[self.row]["updated_at"])
        pushed_date = repos_information_control.format_date(self.repos[self.row]["pushed_at"])
        link_template = '<a href="%s">%s</a>'
        self.repos_information.repo_name.setText(link_template % (self.repos[self.row]["html_url"], self.repos[self.row]["name"]))
        self.repos_information.repo_full_name.setText(self.repos[self.row]["full_name"])
        self.repos_information.repo_description.setText(self.repos[self.row]["description"])
        self.repos_information.repo_created_at.setText(f'Data de criação : {create_date}')
        self.repos_information.repo_updated_at.setText(f'Data de atualização : {updated_date}')
        self.repos_information.repo_pushed_at.setText(f'Ultimo push : {pushed_date}')
        self.repos_information.repo_clone_url.setText(link_template % (f'git clone {self.repos[self.row]["clone_url"]}', 'Clone o repositório'))
        self.repos_information.repo_size.setText(f'Tamanho : {self.repos[self.row]["size"]}')
        self.repos_information.repo_language.setText(f'Linguagem principal : {self.repos[self.row]["language"]}')
        try : 
            license_url = RequestLicense(self.repos[self.row]).get_license()
            self.repos_information.repo_license_name.setText(link_template % (license_url, f'Licença : {self.repos[self.row]["license"]["name"]}'))
        except :
            self.repos_information.repo_license_name.setText(f'Licença : Não encontrada!')
        
    def format_date(date):
        day = date[8:10]
        month = date[5:7]
        year = date[0:4]
        return f'{day}/{month}/{year}'