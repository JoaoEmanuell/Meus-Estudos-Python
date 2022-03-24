from ..interfaces import ValidatorInterface

class NutValidator(ValidatorInterface) :
    def validate(self, food: str) -> bool:
        if food == "nut" :
            return True
        return False

    def action(self) -> None:
        print("The squirrel eats the nut")