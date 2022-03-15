# Global imports

from pytube import YouTube
from pytube.cli import on_progress
import ssl, main
ssl._create_default_https_context = ssl._create_unverified_context

# Local imports

from .downloadEssential import DownloadEssential
from .interfaces import DownloadInterface
from .message import Message

class DownloadVideo(DownloadInterface):
    def __init__(self, link : str, mp3 : bool) -> None:
        self.video = YouTube(link, on_progress_callback=on_progress)
        self.convert = mp3
        Message.set_progressbar(100, 0)
        self.download()

    def download(self):
        if self.convert:
            Message.set_output(f'Iniciando o download da música :\n{self.video.title}\nAguarde um pouco!')
            self.stream = self.video.streams.get_audio_only()
        else:
            Message.set_output(f'Iniciando o download do vídeo :\n{self.video.title}\nAguarde um pouco!')
            self.stream = self.video.streams.get_highest_resolution()
        self.path = DownloadEssential()._get_download_path()
        if DownloadEssential.VerifyIfFileNotExists(self):
            if self.convert:
                Message.set_output(f'Download da música:\n{self.video.title}\nIniciado')
            else:
                Message.set_output(f'Download do vídeo:\n{self.video.title}\nIniciado')
            self.stream.download(output_path=f'{self.path}/Música/')
            if self.convert:
                DownloadEssential.ConvertToMp3(self)
                Message.set_output(f"Música:\n{self.video.title} baixado e convertido para MP3")
                Message.set_progressbar(100, 100)
            else:
                Message.set_output(f"Vídeo:\n{self.video.title} baixado")
                Message.set_progressbar(100, 100)
        else :
            if self.convert:
                Message.set_output(f"Música: \n{self.video.title}\n já foi baixado!")
            else:
                Message.set_output(f"Vídeo: \n{self.video.title}\n já foi baixado!")