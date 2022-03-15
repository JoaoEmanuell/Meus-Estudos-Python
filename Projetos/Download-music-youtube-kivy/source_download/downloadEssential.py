from os.path import exists, isdir, join
from os import rename, mkdir
from kivy.utils import platform
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
        rename(f"{self.path}Música/{filename}.mp4", f"{self.path}Música/{filename}.mp3")
        print(f"'{self.video.title}' convertido para mp3")

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

    def createDirectory(self, name : str):
        path = DownloadEssential()._get_download_path()
        print(f'Path : {path}')
        if not(isdir(f'{path}/{name}')):
            path = join(path, name)
            mkdir(path)