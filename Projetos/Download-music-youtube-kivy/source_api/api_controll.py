from .interfaces import ApiControllInterface
from threading import Thread
from requests import get, post

class ApiControll(ApiControllInterface) :
    def __init__(self) -> None :
        self.__endpoint = 'http://localhost:5000/api/'
        self.private__start_api()

    def private__start_api(self) -> None :
        Thread(target= get, args=(self.__endpoint, )).start()

    def upload(self, file_path : str) -> None :
        pass

    def get_status(self, hash : str) -> None :
        pass

    def get_file(self, hash : str) -> None :
        pass
