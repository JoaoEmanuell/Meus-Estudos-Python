from pytube import Playlist
from . import downloadVideo
import ssl, main
ssl._create_default_https_context = ssl._create_unverified_context

class DownloadPlaylist():
    def __init__(self, playlistLink : list, convertToMp3  : bool = True) -> None:
        self.playlist = Playlist(playlistLink)
        self.CONVERT = convertToMp3
        DownloadPlaylist.downloadVideos(self)

    def downloadVideos(self):
        main.Tela.output(f"Download da playlist iniciado!")
        for v in self.playlist:
            downloadVideo.DownloadVideo(v, self.CONVERT)
        main.Tela.output("Download da Playlist concluido!")