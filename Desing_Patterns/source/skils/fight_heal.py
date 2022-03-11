from .interfaces import SkillInterface

class UseHeal(SkillInterface):
    def __init__(self, level : int = 1) -> None:
        self.__level = level

    def behavior(self) -> None:
        print("Heal yourself")

    def level_atribute(self) -> None:
        print(f"Heal level : {self.__level}")