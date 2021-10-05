from pytube import YouTube
import os, sys, re
class DownloadVideo():
    def __init__(self, link) -> None:
        if DownloadVideo.VerifyUrl(link):
            self.video = YouTube(link)
            DownloadVideo.createDirectory("Musicas")
            self.download()
            self.source = sys.path[0]
            self.ConvertToMp3()
        else:
            print("Erro, url invalida!")
    
    def download(self):
        source = sys.path[0]
        print(f"Baixando '{self.video.title}'")
        stream = self.video.streams.get_audio_only()
        stream.download(output_path=f'{source}/Musicas')
        print(f"Vídeo '{self.video.title}' baixado")


    def ConvertToMp3(self):
        filename = self.video.title.replace("|", '').replace(".", '')
        os.rename(f"{self.source}/Musicas/{filename}.mp4", f"{self.source}/Musicas/{filename}.mp3")
        print(f"'{self.video.title}' convertido para mp3")

    def createDirectory(name):
        path = sys.path[0]
        if not(os.path.isdir(f'{path}/{name}')):
            path = os.path.join(sys.path[0], name)
            os.mkdir(path)

    def VerifyUrl(url):
        verfiy_url = re.findall('^(https://)', url)
        verfiy_domain_full = re.findall('^(https://www.youtube.com/)', url)
        verfiy_domain_short = re.findall('^(https://youtu.be/)', url)
        if (len(verfiy_url) != 0 or len(verfiy_domain_full) != 0 or len(verfiy_domain_short) != 0):
            return True
        else:
            return False