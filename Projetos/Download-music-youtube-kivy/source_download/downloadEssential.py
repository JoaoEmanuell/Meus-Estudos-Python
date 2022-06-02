# Global imports

from os.path import exists, isdir, join
from os import mkdir, remove, rename
from kivy.utils import platform
from getpass import getuser
from typing import Type
from time import sleep

# Local imports

from pytube.streams import Stream
from source_api import ApiControll
from .message import Message
from .download import Download

class DownloadEssential():
    def VerifyIfFileNotExists(self, convert : bool, file : Type[Stream], path : str) -> bool:
        if convert:
            filename = str(file.default_filename).replace('.mp4', '')
            return not(exists(f"{path}Música/{filename}.mp3"))
        else:
            filename = file.default_filename
            return not(exists(f"{path}Música/{filename}"))

    def ConvertToMp3(self, file_path : str, file_name : str) -> None :

        rename(file_path, file_path.replace('.mp4', '.mp3'))

        file_path = file_path.replace('.mp4', '.mp3')

        api_controll = ApiControll()

        # Upload file

        print("Upload file")

        Message.set_output('Enviando a música para a api...')

        response = api_controll.upload(file_path)

        hash = response['hash']

        Message.set_output('Conversão iniciada!')

        Message.set_progressbar(0, 100)

        print(f'Hash : {hash}')

        sleep(2)

        while True :

            sleep(2)

            response = api_controll.get_status(hash)

            print(f"Status : {response}")

            if response['status'] :
                break
            
            try :

                Message.set_progressbar(response['total'], response['current'])

            except KeyError :
                pass

        # Download File

        converted = api_controll.get_file(hash)

        print(f'Converted : {converted}')

        Message.set_output('Removendo arquivo antigo')

        remove(file_path)

        download = Download()

        Message.set_output('Download do arquivo convertido iniciado!')

        file = download.download(converted['audio'])

        # Save File

        Message.set_output('Salvando novo arquivo')

        path = f'{self._get_download_path()}Música/'

        download.save_file(name=file_name, dir=path, content=file)

    def _get_download_path(self) -> str:
        paths = {
                    "win" : r"C:\Users\%s\Desktop\\",
                    "linux" : "/home/%s/",
                    "android" : "/storage/emulated/0/"
                }
        try :
            if platform != 'android' :
                return paths[platform] % getuser()
            return paths[platform]
        except KeyError:
            raise "Plataforma invalida"

    def createDirectory(self, name : str) -> None:
        path = self._get_download_path()
        print(f'Path : {path}')
        if not(isdir(f'{path}/{name}')):
            path = join(path, name)
            mkdir(path)