# Global imports

from os.path import exists, isdir, join
from os import rename, mkdir
from kivy.utils import platform
from getpass import getuser
from typing import Type

# Local imports

from pytube.streams import Stream
from pytube import YouTube

class DownloadEssential():
    def VerifyIfFileNotExists(self, convert : bool, file : Type[Stream], path : str) -> bool:
        if convert:
            filename = str(file.default_filename).replace('.mp4', '')
            return not(exists(f"{path}Música/{filename}.mp3"))
        else:
            filename = file.default_filename
            return not(exists(f"{path}Música/{filename}"))

    def ConvertToMp3(self, file : Type[Stream], video : Type[YouTube], path : str) -> None:
        filename = str(file.default_filename).replace('.mp4', '')
        rename(f"{path}Música/{filename}.mp4", f"{path}Música/{filename}.mp3")
        print(f"'{video.title}' convertido para mp3")

    def _get_download_path(self) -> str:
        paths = {
                    "win" : r"C:\Users\%s\Desktop\\",
                    "linux" : "/home/%s/",
                    "android" : "/storage/emulated/0/"
                }
        try :
            return paths[platform] % getuser()
        except KeyError:
            raise "Plataforma invalida"

    def createDirectory(self, name : str) -> None:
        path = self._get_download_path()
        print(f'Path : {path}')
        if not(isdir(f'{path}/{name}')):
            path = join(path, name)
            mkdir(path)