from typing import Type
class House:
    def __init__(self) -> None:
        self.__address = 'Aurora Avenue 1'

    def turn_on_lights(self) -> None:
        print('Turning on lights in the house')

    def get_address(self) -> str:
        return self.__address

class Person:
    def __init__(self, name : str, place : Type[House]) -> None:
        self.__name = name
        self.__place = place

    def enter_the_place(self) -> None:
        self.__place.turn_on_lights()

    def introduce_place(self) -> None:
        address = self.__place.get_address()
        print(f'Hi, my name is {self.__name} and I live in {address}')
        
if __name__ == '__main__':
    house = House()
    ana = Person('Ana', house)
    
    ana.introduce_place()
    ana.enter_the_place()