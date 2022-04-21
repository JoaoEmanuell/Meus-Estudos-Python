# Global imports

from os.path import exists, isdir, join
from os import mkdir, remove
from kivy.utils import platform
from getpass import getuser
from typing import Type
from time import sleep

# Local imports

from pytube.streams import Stream
from pytube import YouTube
from source_api import ApiControll
from .message import Message

class DownloadEssential():
    def VerifyIfFileNotExists(self, convert : bool, file : Type[Stream], path : str) -> bool:
        if convert:
            filename = str(file.default_filename).replace('.mp4', '')
            return not(exists(f"{path}Música/{filename}.mp3"))
        else:
            filename = file.default_filename
            return not(exists(f"{path}Música/{filename}"))

    def ConvertToMp3(self, file_path : str) -> None:

        api_controll = ApiControll()

        # Upload file

        response = api_controll.upload(file_path)

        hash = response['hash']

        while True :

            sleep(3)

            response = api_controll.get_status(hash)

            if response['status'] :
                break
            
            if response['total'] :
                Message.set_progressbar(response['total'], response['current'])

        # Download File

        remove(file_path)


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