from abc import ABC, abstractmethod

class DownloadInterface(ABC):
    @abstractmethod
    def __init__(self, link : str, mp3 : bool) -> None:
        raise NotImplementedError

    @abstractmethod
    def download(self) -> None:
        raise NotImplementedError