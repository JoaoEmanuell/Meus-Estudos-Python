# Global imports

from re import findall
from typing import Type

# Local imports

from source_download.downloadEssential import DownloadEssential
from source_download.interfaces import DownloadInterface, DownloadPlaylistInterface
from source_download.message import Message

class DownloadVerfiy():

    def VerifyUrl(url : str) -> bool:
        verfiy_url = findall('^(https\:\/\/)', str(url))
        verfiy_domain_full = findall('^(https:\/\/www.youtube.com\/)', str(url))
        verfiy_domain_short = findall('^(https:\/\/youtu.be\/)', str(url))
        verify_track = findall('^(https:\/\/www\.youtube\.com\/watch\?)', str(url))
        if (len(verfiy_url) != 0 or len(verfiy_domain_full) != 0 or len(verfiy_domain_short) != 0 or len(verify_track) != 0):
            return True
        else:
            return False

    def VerifyPlaylist(url : str) -> bool:
        verfiy_url = findall('(playlist\?list=)', str(url))
        if len(verfiy_url) != 0 :
            return True
        else :
            return False
    
    def main(link : str, mp3 : bool, video : Type[DownloadInterface], playlist : Type[DownloadPlaylistInterface]) -> None:
        link = str(link)
        print("Iniciando o download")
        if DownloadVerfiy.VerifyUrl(link):
            DownloadEssential().createDirectory('Música')
            if DownloadVerfiy.VerifyPlaylist(link):
                print("Verificado playlist, iniciando o download da playlist")
                playlist(link, mp3).download_playlist(video)
            else :
                print("Verificado vídeo, iniciando o download do vídeo")
                if mp3:
                    video(link, mp3).downloadAudio()
                else :
                    video(link, mp3).downloadVideo()
        else:
            Message.set_output("Erro, url invalida!")