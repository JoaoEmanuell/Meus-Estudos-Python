from pytube import YouTube
import sys
from . import downloadEssential

class DownloadVideo():
    def __init__(self, link) -> None:
        self.video = YouTube(link)
        self.download()

    def download(self):
        self.stream = self.video.streams.get_audio_only()
        self.path = sys.path[0]
        if downloadEssential.DownloadEssential.VerifyIfFileNotExists(self):
            print(f"Baixando '{self.video.title}'")
            self.stream.download(output_path=f'{self.path}/Musicas/')
            print(f"Vídeo '{self.video.title}' baixado")
            downloadEssential.DownloadEssential.ConvertToMp3(self)
        else :
            print(f"Vídeo '{self.video.title}' já foi baixado!")