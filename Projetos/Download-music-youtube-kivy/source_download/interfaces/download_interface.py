from abc import ABC, abstractmethod

class DownloadInterface(ABC) :

    @abstractmethod
    def download(self, url : str) -> bytes :
        raise NotImplementedError

    @abstractmethod
    def save_file(self, name : str, path : str, content : bytes) -> None :
        raise NotImplementedError