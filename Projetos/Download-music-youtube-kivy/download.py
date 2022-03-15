# Global imports

from re import findall

# Local imports

from source_download.downloadPlaylist import DownloadPlaylist
from source_download.downloadVideo import DownloadVideo
from source_download.downloadEssential import DownloadEssential
from source_download.message import Message

class DownloadVerfiy():

    def VerifyUrl(url):
        verfiy_url = findall('^(https\:\/\/)', str(url))
        verfiy_domain_full = findall('^(https:\/\/www.youtube.com\/)', str(url))
        verfiy_domain_short = findall('^(https:\/\/youtu.be\/)', str(url))
        verify_track = findall('^(https:\/\/www\.youtube\.com\/watch\?)', str(url))
        if (len(verfiy_url) != 0 or len(verfiy_domain_full) != 0 or len(verfiy_domain_short) != 0 or len(verify_track) != 0):
            return True
        else:
            return False

    def VerifyPlaylist(url):
        verfiy_url = findall('(playlist\?list=)', str(url))
        if len(verfiy_url) != 0 :
            return True
        else :
            return False
    
    def main(link, mp3):
        link = str(link)
        print("Iniciando o download")
        if DownloadVerfiy.VerifyUrl(link):
            DownloadEssential().createDirectory('Música')
            if DownloadVerfiy.VerifyPlaylist(link):
                print("Verificado playlist, iniciando o download da playlist")
                DownloadPlaylist(link, mp3)
            else :
                print("Verificado vídeo, iniciando o download do vídeo")
                DownloadVideo(link, mp3)
        else:
            Message.set_output("Erro, url invalida!")