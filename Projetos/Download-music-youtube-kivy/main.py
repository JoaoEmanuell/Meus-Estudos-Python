# Global imports
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.clock import mainthread
from kivy.utils import platform
from threading import Thread
from urllib.error import URLError
from urllib.request import urlopen

# Local imports
import download
from intent import Intent
from source_android import Android
from source_api import ApiControll
import source_download.downloadPlaylist as playlist
import source_download.downloadVideo as video

# Android
class Tela(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.link.text = Intent(platform).get_intent_text()
        ApiControll()

    def main(self):
        try :
            urlopen('https://www.youtube.com')
        except URLError:
            self.ids.output.text = 'Sua conexão de internet está indisponível, por favor tente novamente'
        else:
            self.startDownload()
    def startDownload(self):
        self.ids.output.text = ''
        self.ids.progressbar.value = 0
        try:
            url = str(self.ids.link.text)
            Thread(target=download.DownloadVerify.main, args=(url, self.verify_mp3(), video.DownloadVideo, playlist.DownloadPlaylist)).start()
        except Exception as erro:
            self.ids.output.text = f'Alguma coisa deu errado!\nPor favor insira uma nova url\nTente novamente!\n {erro}'

    def verify_mp3(self):
        mp3 = self.ids.mp3.state
        mp4 = self.ids.mp4.state
        if mp3 == 'down':
            return True
        elif mp4 == 'down' :
            return False
        else :
            return True

    @mainthread
    def progressbar(max,percent):
        App.get_running_app().root.ids.progressbar.max = int(max)
        App.get_running_app().root.ids.progressbar.value = int(percent)

class Main(App):
    def build(self):
        return Tela()

if __name__ == '__main__':
    Android()
    Main().run()