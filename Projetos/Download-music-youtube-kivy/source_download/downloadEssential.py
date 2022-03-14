from os.path import exists
import os
from kivy.utils import platform
from json import loads
from getpass import getuser

class DownloadEssential():
    def VerifyIfFileNotExists(self):
        if self.convert:
            filename = self.stream.default_filename.replace('.mp4', '')
            return not(exists(f"{self.path}{filename}.mp3"))
        else:
            filename = self.stream.default_filename
            return not(exists(f"{self.path}{filename}"))

    def ConvertToMp3(self):
        filename = self.stream.default_filename.replace('.mp4', '')
        os.rename(f"{self.path}{filename}.mp4", f"{self.path}{filename}.mp3")
        print(f"'{self.video.title}' convertido para mp3")

    def _get_download_path(self) -> str:
        with open('./source_download/paths.json', 'r') as file:
            if platform != 'android' :
                paths = loads(file.read())
                try :
                    return paths[platform] % getuser()
                except KeyError:
                    raise "Plataforma invalida"
            return '/storage/emulated/0/'
