from abc import ABC, abstractmethod

class BirdFlyInterface(ABC) : 
    @abstractmethod
    def eat(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def fly(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def sing(self) -> None:
        raise NotImplementedError

class BirdNotFlyInterface(ABC) : 
    @abstractmethod
    def eat(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def sing(self) -> None:
        raise NotImplementedError