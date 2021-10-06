from pytube import YouTube
import sys
from . import downloadEssential

class DownloadVideo():
    def __init__(self, link) -> None:
        self.video = YouTube(link)
        self.download()

    def download(self):
        if downloadEssential.DownloadEssential.VerifyIfFileNotExists(self, "Musicas"):
            source = sys.path[0]
            print(f"Baixando '{self.video.title}'")
            self.stream = self.video.streams.get_audio_only()
            self.stream.download(output_path=f'{source}/Musicas/')
            print(f"Vídeo '{self.video.title}' baixado")
            downloadEssential.DownloadEssential.ConvertToMp3(self)
        else :
            print(f"Vídeo '{self.video.title}' já foi baixado!")