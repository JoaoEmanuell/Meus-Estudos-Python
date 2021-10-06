from pytube import Playlist
from . import downloadVideo

class DownloadPlaylist():
    def __init__(self, playlistLink, convertToMp3=True) -> None:
        self.playlist = Playlist(playlistLink)
        self.CONVERT = convertToMp3
        DownloadPlaylist.downloadVideos(self)

    def downloadVideos(self):
        for v in self.playlist:
            downloadVideo.DownloadVideo(v)
        print("Download da Playlist concluido!")