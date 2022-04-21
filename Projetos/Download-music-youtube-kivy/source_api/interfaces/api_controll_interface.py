from abc import ABC, abstractmethod

class ApiControllInterface :

    @abstractmethod
    def __start_api(self) -> None :
        raise NotImplementedError
    
    @abstractmethod
    def upload(self, file_path : str) -> None :
        raise NotImplementedError

    @abstractmethod
    def get_status(self, hash : str) -> None :
        raise NotImplementedError
    
    @abstractmethod
    def get_file(self, hash : str) -> None :
        raise NotImplementedError