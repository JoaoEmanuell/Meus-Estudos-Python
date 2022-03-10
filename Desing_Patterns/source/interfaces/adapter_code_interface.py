from abc import ABC, abstractmethod

class AdapterCodeInterface(ABC) :
    @abstractmethod
    def handle(self, message : dict) -> None:
        raise NotImplementedError