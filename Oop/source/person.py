class Person:
    def __init__(self, name : str) -> None:
        self.__name = name
        self.__place = None

    def introduce_yourself(self) -> None:
        print(f'Hi, my name is {self.__name}')

    def enter_the_place(self) -> None:
        self.__place.turn_on_lights()

    def introduce_place(self) -> None:
        address = self.__place.get_address()
        print(f'Hi, my name is {self.__name} and I live in {address}')

    def set_place(self, place : any) -> None:
        self.__place = place

    def get_place(self) -> any:
        return self.__place