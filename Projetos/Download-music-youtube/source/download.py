from pytube import YouTube
import os, sys
class DownloadVideo():
    def __init__(self, link) -> None:
        self.link = link
        self.video = YouTube(self.link)
        self.download()
        self.source = sys.path[0]
        self.ConvertToMp3()
    
    def download(self):
        source = sys.path[0]
        print(f"Baixando '{self.video.title}'")
        stream = self.video.streams.get_audio_only()
        stream.download(output_path=source)
        print(f"Vídeo '{self.video.title}' baixado")


    def ConvertToMp3(self):
        filename = self.video.title.replace("|", '').replace(".", '')
        os.rename(f"{self.source}/{filename}.mp4", f"{self.source}/{filename}.mp3")
        print(f"'{self.video.title}' convertido para mp3")