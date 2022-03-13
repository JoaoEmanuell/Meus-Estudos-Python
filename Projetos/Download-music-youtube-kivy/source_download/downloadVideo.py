from pytube import YouTube
from pytube.cli import on_progress
from . import downloadEssential
from .interfaces import DownloadInterface
import ssl, main
ssl._create_default_https_context = ssl._create_unverified_context

class DownloadVideo(DownloadInterface):
    def __init__(self, link : str, mp3 : bool) -> None:
        self.video = YouTube(link, on_progress_callback=on_progress)
        self.convert = mp3
        main.Tela.progressbar(100, 0)
        self.download()

    def download(self):
        if self.convert:
            main.Tela.output(f'Iniciando o download da música :\n{self.video.title}\nAguarde um pouco!')
            self.stream = self.video.streams.get_audio_only()
        else:
            main.Tela.output(f'Iniciando o download do vídeo :\n{self.video.title}\nAguarde um pouco!')
            self.stream = self.video.streams.get_highest_resolution()
        # self.path = '/storage/emulated/0/'
        self.path = downloadEssential.DownloadEssential()._get_download_path()
        if downloadEssential.DownloadEssential.VerifyIfFileNotExists(self):
            if self.convert:
                main.Tela.output(f'Download da música:\n{self.video.title}\nIniciado')
            else:
                main.Tela.output(f'Download do vídeo:\n{self.video.title}\nIniciado')
            self.stream.download(output_path=f'{self.path}/Músicas/')
            if self.convert:
                downloadEssential.DownloadEssential.ConvertToMp3(self)
                main.Tela.output(f"Música:\n{self.video.title} baixado e convertido para MP3")
                main.Tela.progressbar(100, 100)
            else:
                main.Tela.output(f"Vídeo:\n{self.video.title} baixado")
                main.Tela.progressbar(100, 100)
        else :
            if self.convert:
                main.Tela.output(f"Música: \n{self.video.title}\n já foi baixado!")
            else:
                main.Tela.output(f"Vídeo: \n{self.video.title}\n já foi baixado!")