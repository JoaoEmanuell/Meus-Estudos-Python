from .interfaces import ObserverInterface
from typing import Type

class Alarm:
    def __init__(self) -> None:
        self.__beep = False
        self.__persons = []

    def add_person(self, person : Type[ObserverInterface]) -> None:
        self.__persons.append(person)

    def get_beep(self) -> bool:
        return self.__beep

    def play(self) -> None:
        self.__beep = True
        for person in self.__persons:
            person.update()
        self.__persons = []
