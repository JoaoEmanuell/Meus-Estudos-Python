from abc import ABC, abstractmethod

class ReceptorInterface(ABC) :

    @abstractmethod
    def process_information(self, information : any) -> None :
        raise NotImplementedError