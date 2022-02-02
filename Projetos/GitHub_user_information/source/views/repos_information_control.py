from source.api.license import RequestLicense
from PyQt5.QtWidgets import QMainWindow

class ReposInformationControl():
    def __init__(self, layout : QMainWindow, repository_info : dict, row : int) -> None:
        self.layout = layout
        self.repo = repository_info[row]

    def set_items(self):
        create_date = self.format_date(self.repo['created_at'])
        updated_date = self.format_date(self.repo["updated_at"])
        pushed_date = self.format_date(self.repo["pushed_at"])

        link_template = '<a href="%s">%s</a>'

        self.layout.repo_name.setText(link_template % (self.repo["html_url"], self.repo["name"]))
        self.layout.repo_full_name.setText(self.repo["full_name"])
        self.layout.repo_description.setText(self.repo["description"])
        self.layout.repo_created_at.setText(f'Data de criação : {create_date}')
        self.layout.repo_updated_at.setText(f'Data de atualização : {updated_date}')
        self.layout.repo_pushed_at.setText(f'Ultimo push : {pushed_date}')
        self.layout.repo_clone_url.setText(link_template % (f'git clone {self.repo["clone_url"]}', 'Clone o repositório'))
        self.layout.repo_size.setText(f'Tamanho : {self.repo["size"]}')
        self.layout.repo_language.setText(f'Linguagem principal : {self.repo["language"]}')
        
        try : 
            license_url = RequestLicense(self.repo).get_license()
            self.layout.repo_license_name.setText(link_template % (license_url, f'Licença : {self.repo["license"]["name"]}'))
        except :
            self.layout.repo_license_name.setText(f'Licença : Não encontrada!')
        
    def format_date(self, date):
        day = date[8:10]
        month = date[5:7]
        year = date[0:4]
        return f'{day}/{month}/{year}'