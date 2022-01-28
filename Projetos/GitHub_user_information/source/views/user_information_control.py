from os.path import join
from pathlib import Path
from requests import get
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QIcon, QImage, QPixmap
from functools import lru_cache

class user_information_control():
    def show_user_information(self) -> None:
        self.user_informations.show()
        self.user_informations.user_list_informations.clear()
        template_color_center = '<p><span style="color:%s">%s</span></p>'
        self.user_informations.username.setText(template_color_center % ('#8b949e', self.user['login']))
        self.user_informations.user_name.setText(template_color_center % ('#C9D1D9', self.user['name']))
        self.user_informations.user_bio.setText(template_color_center % ('#C9D1D9', self.user['bio']))
        user_information_control.set_informations_in_list(self)
        user_information_control.image_set(self)

    def image_set(self):
        image = QImage()
        image.loadFromData(get(self.user['avatar_url']).content)
        self.user_informations.user_profile_photo.setPixmap(QPixmap(image).scaled(250, 250))

    def set_informations_in_list(self):
        location_icon = QIcon(join(Path().absolute(), 'icons/location_icon.png'))
        followers_icon = QIcon(join(Path().absolute(), 'icons/followers_icon.png'))
        followers_item = QListWidgetItem(followers_icon, f"{self.user['followers']} Seguidores | Seguindo {self.user['following']}")
        location_item = QListWidgetItem(location_icon, self.user["location"])
        self.user_informations.user_list_informations.addItem(followers_item)
        self.user_informations.user_list_informations.addItem(location_item)
    
    @lru_cache
    def get_user_repos(self) : return get(self.user['repos_url']).json()
