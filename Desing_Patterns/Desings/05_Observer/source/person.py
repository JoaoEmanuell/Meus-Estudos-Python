from .interfaces import ObserverInterface

class Person(ObserverInterface):
    def __init__(self, name : str) -> None:
        self.__name = name
        self.__awake = False

    def get_awake(self) -> bool:
        return self.__awake

    def update(self) -> None:
        print(f"{self.__name} Awake")
        self.__awake = True