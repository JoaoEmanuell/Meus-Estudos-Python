from ..interfaces import ValidatorInterface

class MeatValidator(ValidatorInterface) :
    def validate(self, food: str) -> bool:
        if food == "meat" :
            return True
        return False

    def action(self) -> None:
        print("The lion eats the meat")