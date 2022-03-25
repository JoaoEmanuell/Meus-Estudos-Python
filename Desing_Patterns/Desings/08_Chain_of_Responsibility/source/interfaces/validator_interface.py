from abc import ABC, abstractmethod

class ValidatorInterface(ABC) :
    @abstractmethod
    def validate(self, food : str) -> bool :
        raise NotImplementedError

    @abstractmethod
    def action(self) -> None :
        raise NotImplementedError