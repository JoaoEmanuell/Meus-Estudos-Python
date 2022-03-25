from source.validators import MeatValidator, BananaValidator, NutValidator

class Validate :
    def __init__(self) -> None :
        self.__validators = [
            BananaValidator(),
            NutValidator(),
            MeatValidator()
        ]

    def process(self, food : str) -> None :
        for validator in self.__validators :
            if validator.validate(food) :
                return validator.action()
        print("Indefinite food")

if __name__ == '__main__' :
    validate = Validate()
    validate.process("banana")
    validate.process("nut")
    validate.process("meat")
    validate.process("apple")