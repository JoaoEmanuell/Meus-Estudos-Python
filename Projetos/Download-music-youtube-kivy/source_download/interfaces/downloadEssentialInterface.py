from abc import ABC, abstractmethod

class DownloadEssentialInterface(ABC):
    @abstractmethod
    def __init__(self, link : str, mp3 : bool) -> None:
        raise NotImplementedError

    @abstractmethod
    def downloadVideo(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def downloadAudio(self) -> None:
        raise NotImplementedError