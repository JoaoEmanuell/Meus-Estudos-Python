from ..interfaces import ValidatorInterface

class BananaValidator(ValidatorInterface) :

    def validate(self, food : str) -> bool :
        if food == 'banana' :
            return True
        return False

    def action(self) -> None:
        print("The monkey eats the banana")
