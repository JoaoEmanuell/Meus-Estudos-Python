from abc import ABC, abstractmethod

class AbstractClass(ABC) :
    def __init__(self) -> None:
        self.atribute = 'Hello World'

    def method(self, element : str) -> None:
        print(element)

    @abstractmethod
    def abstract_method(self) -> None:
        pass