from .interfaces import SkillInterface

class UseBow(SkillInterface):
    def __init__(self, level : int = 1) -> None:
        self.__level = level

    def behavior(self) -> None:
        print("Shoot Arrows")

    def level_atribute(self) -> None:
        print(f"Bow usage level : {self.__level}")