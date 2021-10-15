from pytube import YouTube
import pathlib
from . import downloadEssential
from threading import Thread

class DownloadVideo():
    def __init__(self, link) -> None:
        self.video = YouTube(link)
        Thread(target=self.download).start()

    def download(self):
        print("Download iniciado!")
        self.stream = self.video.streams.get_audio_only()
        self.path = pathlib.Path().absolute()
        if downloadEssential.DownloadEssential.VerifyIfFileNotExists(self):
            print(f"Baixando '{self.video.title}'")
            self.stream.download(output_path=f'{self.path}/Musicas/')
            print(f"Vídeo '{self.video.title}' baixado")
            downloadEssential.DownloadEssential.ConvertToMp3(self)
        else :
            print(f"Vídeo '{self.video.title}' já foi baixado!")