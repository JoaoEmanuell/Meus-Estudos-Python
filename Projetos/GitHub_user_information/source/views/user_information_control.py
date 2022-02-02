from os.path import join
from pathlib import Path
from requests import get
from PyQt5.QtWidgets import QListWidgetItem, QMainWindow
from PyQt5.QtGui import QIcon, QImage, QPixmap
from functools import lru_cache

class UserInformationContro():
    def __init__(self, layout : QMainWindow, user : dict) -> None:
        self.layout = layout
        self.user = user

    def show_user_information(self) -> None:
        self.layout.show()
        self.layout.user_list_informations.clear()
        template_color_center = '<p><span style="color:%s">%s</span></p>'
        self.layout.username.setText(template_color_center % ('#8b949e', self.user['login']))
        self.layout.user_name.setText(template_color_center % ('#C9D1D9', self.user['name']))
        self.layout.user_bio.setText(template_color_center % ('#C9D1D9', self.user['bio']))
        UserInformationContro.set_informations_in_list(self)
        UserInformationContro.set_profile_pic(self)

    def set_profile_pic(self):
        image = QImage()
        image.loadFromData(get(self.user['avatar_url']).content)
        self.layout.user_profile_photo.setPixmap(QPixmap(image).scaled(250, 250))

    def set_informations_in_list(self):
        location_icon = QIcon(join(Path().absolute(), './icons/location_icon.png'))
        followers_icon = QIcon(join(Path().absolute(), './icons/followers_icon.png'))
        followers_item = QListWidgetItem(followers_icon, f"{self.user['followers']} Seguidores | Seguindo {self.user['following']}")
        location_item = QListWidgetItem(location_icon, self.user["location"])
        self.layout.user_list_informations.addItem(followers_item)
        self.layout.user_list_informations.addItem(location_item)
