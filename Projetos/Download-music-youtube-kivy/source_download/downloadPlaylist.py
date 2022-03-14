# Global imports

from pytube import Playlist
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Local imports

from .downloadVideo import DownloadVideo
from .message import Message

class DownloadPlaylist():
    def __init__(self, playlistLink : list, convertToMp3  : bool = True) -> None:
        self.playlist = Playlist(playlistLink)
        self.CONVERT = convertToMp3
        DownloadPlaylist.downloadVideos(self)

    def downloadVideos(self):
        Message.set_output(f"Download da playlist iniciado!")
        for v in self.playlist:
            DownloadVideo(v, self.CONVERT)
        Message.set_output("Download da Playlist concluido!")