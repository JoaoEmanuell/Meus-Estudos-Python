from typing import Type
class Animal:
    def __init__(self, specie : str) -> None:
        self.__specie = specie

    def eat(self) -> None:
        print(f"{self.__specie} is eating")
    
    def sleep(self) -> None:
        print(f"{self.__specie} is sleeping")
    
    def walk(self) -> None:
        print(f"{self.__specie} is walking")

class Penguin(Animal):
    def __init__(self) -> None:
        super().__init__("Penguin")

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__("Cat")

class Person():
    def observer(self, animal : Type[Animal]) -> None:
        animal.walk()

if __name__ == '__main__':
    jhon = Person()
    jhon.observer(Penguin())
    jhon.observer(Cat())