from source import Mon

class Daughter(Mon):
    def __init__(self) -> None:
        super().__init__()

    def play(self, game : str) -> None :
        print(f'I am playing {game}')
        
class GrandDaughter(Daughter):
    def __init__(self) -> None:
        super().__init__()


if __name__ == '__main__':
    daughter = Daughter()
    daughter.play('Chess')
    grand_daughter = GrandDaughter()
    grand_daughter.play('Chess')
    print(daughter.address)