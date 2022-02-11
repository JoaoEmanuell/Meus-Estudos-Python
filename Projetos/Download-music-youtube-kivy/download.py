import os, main
from re import findall
from threading import Thread
from source_download import downloadVideo, downloadPlaylist
from shutil import move

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
    
    def createDirectory(name):
        path = '/storage/emulated/0/'
        if not(os.path.isdir(f'{path}/{name}')):
            path = os.path.join(path, name)
            os.mkdir(path)
    
    def main(link, mp3):
        link = str(link)
        print("Iniciando o download")
        if DownloadVerfiy.VerifyUrl(link):
            DownloadVerfiy.createDirectory('Musicas')
            if DownloadVerfiy.VerifyPlaylist(link):
                print("Verificado vídeo, iniciando o download do vídeo")
                downloadPlaylist.DownloadPlaylist(link, mp3)
            else :
                print("Verificado playlist, iniciando o download da playlist")
                downloadVideo.DownloadVideo(link, mp3)
        else:
            main.Tela.output("Erro, url invalida!")