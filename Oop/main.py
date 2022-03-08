from source import BirdFlyInterface, BirdNotFlyInterface

class Canary(BirdFlyInterface) :

    def eat(self) -> None:
        print("Canary is eating")
    
    def fly(self) -> None:
        print("Canary is flying")
    
    def sing(self) -> None:
        print("Canary is singing")
        self.__copulate()

    def __copulate(self) -> None:
        print("Canary is copulating")

class Penguim(BirdNotFlyInterface) :
    def eat(self) -> None:
        print("Penguim is eating")

    def sing(self) -> None:
        print("Penguim is singing")

if __name__ == '__main__':
    canary = Canary()
    canary.fly()
    canary.sing()

    penguim = Penguim()
    penguim.sing()