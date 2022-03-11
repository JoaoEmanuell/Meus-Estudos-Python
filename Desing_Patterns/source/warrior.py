from .skils import SkillInterface
from typing import Type

class Warrior:
    def __init__(self, skill : Type[SkillInterface]) -> None:
        self.__skill = skill

    def action(self) -> None:
        self.__skill.behavior()

    def atributes(self) -> None:
        self.__skill.level_atribute()