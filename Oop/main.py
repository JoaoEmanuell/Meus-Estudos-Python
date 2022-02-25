class PersonA:
    def introduce(self) -> None:
        print("I am a PersonA")

class PersonB(PersonA):
    def introduce(self) -> None:
        print("I am a PersonB")

class PersonC(PersonB):
    def __init__(self) -> None:
        super().__init__()


if __name__ == '__main__':
    PersonA().introduce()
    PersonB().introduce()
    PersonC().introduce()