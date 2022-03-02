# Global imports
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.clock import mainthread
from kivy.utils import platform
from threading import Thread
import urllib
import urllib.request

# Local imports
import download
from intent import Intent

# Android

try:
    from android.storage import app_storage_path, primary_external_storage_path, secondary_external_storage_path
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.WRITE_EXTERNAL_STORAGE])
except:
    print('Plataforma invalida, permissões do android invalidas!')
finally:
    class Tela(Screen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            # self.verify_message_at_startup()
            self.ids.link.text = Intent(platform).get_intent_text()
        def main(self):
            try :
                urllib.request.urlopen('https://www.youtube.com')
            except urllib.error.URLError:
                self.ids.output.text = 'Sua conexão de internet está indiponivel, por favor tente novamente'
            else:
                self.startDownload()
        def startDownload(self):
            self.ids.output.text = ''
            self.ids.progressbar.value = 0
            try:
                url = str(self.ids.link.text)
                Thread(target=download.DownloadVerfiy.main, args=(url, self.verify_mp3())).start()
                #download.DownloadVerfiy.main(url, self.verify_mp3())
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
        def output(texto):
            App.get_running_app().root.ids.output.text = str(texto)

        @mainthread
        def progressbar(max,percent):
            App.get_running_app().root.ids.progressbar.max = int(max)
            App.get_running_app().root.ids.progressbar.value = int(percent)

    class Main(App):
        def build(self):
            return Tela()

    if __name__ == '__main__':
        Main().run()