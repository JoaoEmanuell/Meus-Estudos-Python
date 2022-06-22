# Global imports

from re import findall
from typing import Type

# Local imports

from source_download.downloadEssential import DownloadEssential
from source_download.interfaces import DownloadEssentialInterface, DownloadPlaylistInterface
from source_download.message import Message

class DownloadVerify():

    def VerifyUrl(url : str) -> bool:
        verify_url = findall('^(https\:\/\/)', str(url))
        verify_domain_full = findall('^(https:\/\/www.youtube.com\/)', str(url))
        verify_domain_short = findall('^(https:\/\/youtu.be\/)', str(url))
        verify_track = findall('^(https:\/\/www\.youtube\.com\/watch\?)', str(url))
        if (len(verify_url) != 0 or len(verify_domain_full) != 0 or len(verify_domain_short) != 0 or len(verify_track) != 0):
            return True
        else:
            return False

    def VerifyPlaylist(url : str) -> bool:
        verify_url = findall('(playlist\?list=)', str(url))
        if len(verify_url) != 0 :
            return True
        else :
            return False
    
    def main(link : str, mp3 : bool, video : Type[DownloadEssentialInterface], playlist : Type[DownloadPlaylistInterface]) -> None:
        link = str(link)
        print("Iniciando o download")
        try :
            if DownloadVerify.VerifyUrl(link):
                DownloadEssential().createDirectory('Música')
                if DownloadVerify.VerifyPlaylist(link):
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

        except Exception as Ex :
            Message.set_output("YouTube quebrou o app :/")
            print(f'ERROR : {Ex.with_traceback()}')