from pytube import YouTube, Playlist
import os, sys
from re import findall
from os.path import exists

class DownloadVerfiy():
    def __init__(self, link) -> None:
        if DownloadVerfiy.VerifyUrl(link):
            if DownloadVerfiy.VerifyPlaylist(link):
                DownloadVerfiy.createDirectory("Musicas")
                DownloadPlaylist(link)
            else :
                DownloadVerfiy.createDirectory("Musica")
                DownloadVideo(link)
        else:
            print("Erro, url invalida!")

    def VerifyUrl(url):
        verfiy_url = findall('^(https://)', url)
        verfiy_domain_full = findall('^(https:\/\/www.youtube.com\/)', url)
        verfiy_domain_short = findall('^(https:\/\/youtu.be\/)', url)
        verify_track = findall('^(https:\/\/www\.youtube\.com\/watch\?)', url)
        if (len(verfiy_url) != 0 or len(verfiy_domain_full) != 0 or len(verfiy_domain_short) != 0 or len(verify_track) != 0):
            return True
        else:
            return False

    def VerifyPlaylist(url):
        verfiy_url = findall('(playlist\?list=)', url)
        if len(verfiy_url) != 0 :
            return True
        else :
            return False
    
    def createDirectory(name):
        path = sys.path[0]
        if not(os.path.isdir(f'{path}/{name}')):
            path = os.path.join(sys.path[0], name)
            os.mkdir(path)
class DownloadVideo():
    def __init__(self, link) -> None:
        self.video = YouTube(link)
        self.download()

    def download(self):
        if DownloadVideo.VerifyIfFileNotExists(self, "Musica"):
            source = sys.path[0]
            print(f"Baixando '{self.video.title}'")
            self.stream = self.video.streams.get_audio_only()
            self.stream.download(output_path=f'{source}/Musica')
            print(f"Vídeo '{self.video.title}' baixado")
            DownloadVideo.ConvertToMp3(self)
        else :
            print(f"Vídeo '{self.video.title}' já foi baixado!")

    def ConvertToMp3(self):
        source = sys.path[0]
        filename = self.stream.default_filename.replace('.mp4', '')
        os.rename(f"{source}/Musica/{filename}.mp4", f"{source}/Musica/{filename}.mp3")
        print(f"'{self.video.title}' convertido para mp3")

    def VerifyIfFileNotExists(self, directoryName):
        source = sys.path[0]
        filename = self.video.title.replace("|", '').replace(".", '').replace("#", '')
        return not(exists(f"{source}/{directoryName}/{filename}.mp3"))

class DownloadPlaylist():
    def __init__(self, playlistLink, convertToMp3=True) -> None:
        self.playlist = Playlist(playlistLink)
        self.CONVERT = convertToMp3
        DownloadPlaylist.downloadVideos(self)

    def downloadVideos(self):
        for v in self.playlist:
            path = sys.path[0]
            self.video = YouTube(v)
            if DownloadVideo.VerifyIfFileNotExists(self, "Musicas"):
                print(f"Baixando '{self.video.title}'")
                stream = self.video.streams.get_audio_only()
                stream.download(output_path=f'{path}/Musicas/')
                print(f"Vídeo '{self.video.title}' baixado")
                if self.CONVERT:
                    self.ConvertToMp3(self.video.title)
                    print(f'Vídeo "{self.video.title}" convertido para mp3')
            else :
                print(f"Vídeo '{self.video.title}' já foi baixado!")
        print("Download da Playlist concluido!")
    
    def ConvertToMp3(self, videoName):
        path = sys.path[0]
        filename = str(videoName).replace("|", '').replace(".", '').replace("#", '')
        os.rename(f"{path}/Musicas/{filename}.mp4", f"{path}/Musicas/{filename}.mp3")