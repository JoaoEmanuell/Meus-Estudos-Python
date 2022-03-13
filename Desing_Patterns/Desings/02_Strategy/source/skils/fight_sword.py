from .interfaces import SkillInterface

class UseSword(SkillInterface):
    def __init__(self, level : int = 1) -> None:
        self.__level = level

    def behavior(self) -> None:
        print("Fight with sword")

    def level_atribute(self) -> None:
        print(f"Sword usage level : {self.__level}")