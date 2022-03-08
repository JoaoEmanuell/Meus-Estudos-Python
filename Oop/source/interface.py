from abc import ABC, abstractmethod

class RepositoryInterface(ABC) :
    @abstractmethod 
    def insert(self, data : any) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove(self, data : any) -> None:
        raise NotImplementedError