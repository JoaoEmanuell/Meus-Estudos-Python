import os, sys
from re import findall
from .source_download import downloadVideo, downloadPlaylist

class DownloadVerfiy():
    def __init__(self, link) -> None:
        if DownloadVerfiy.VerifyUrl(link):
            DownloadVerfiy.createDirectory("Musicas")
            if DownloadVerfiy.VerifyPlaylist(link):
                downloadPlaylist.DownloadPlaylist(link)
            else :
                downloadVideo.DownloadVideo(link)
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