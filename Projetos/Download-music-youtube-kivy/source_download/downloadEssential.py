from os.path import exists
import os
from kivy.utils import platform
from json import loads
from getpass import getuser
from pathlib import Path

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
        if platform != 'android' :
            paths = {
                        "win" : r"C:\Users\%s\Desktop\Música\\",
                        "linux" : "/home/%s/Música/"
                    }
            try :
                return paths[platform] % getuser()
            except KeyError:
                raise "Plataforma invalida"
        return '/storage/emulated/0/Musicas/'
