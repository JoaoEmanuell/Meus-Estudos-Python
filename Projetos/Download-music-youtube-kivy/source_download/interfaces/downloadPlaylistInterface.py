from abc import ABC, abstractmethod

class DownloadPlaylistInterface(ABC):
    @abstractmethod
    def __init__(self, link : str, mp3 : bool) -> None:
        raise NotImplementedError

    @abstractmethod
    def download_playlist(self) -> None:
        raise NotImplementedError