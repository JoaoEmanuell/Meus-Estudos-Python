from abc import ABC, abstractmethod

class DownloadAudioInterface(ABC):
    @abstractmethod
    def __init__(self, link : str, mp3 : bool) -> None:
        raise NotImplementedError

    @abstractmethod
    def downloadAudio(self) -> None:
        raise NotImplementedError