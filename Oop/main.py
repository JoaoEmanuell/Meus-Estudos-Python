from source import ShapesInterface
from typing import Type

class GroundSquare(ShapesInterface) : 
    def __init__(self, shape : int = 10) -> None:
        self.shape = shape
        super().__init__()

    def get_area(self) -> int:
        return self.shape ** 2

    def get_perimeter(self) -> int:
        return 4 * self.shape

class GroundRectangle(ShapesInterface) : 
    def __init__(self, width : int = 10, height : int = 10) -> None:
        self.width = width
        self.height = height
        super().__init__()

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return (self.width * 2) + (self.height * 2)

class Enginer:
    def __init__(self, name : str = "Jhon") -> None:
        self.name = name

    def measure_perimeter(self, ground : Type[ShapesInterface]) -> float:
        return ground.get_perimeter()

    def measure_area(self, ground : Type[ShapesInterface]) -> float:
        return ground.get_area()


if __name__ == '__main__':
    square = GroundSquare()
    print(square.get_area())
    print(square.get_perimeter())

    rectangle = GroundRectangle()
    print(rectangle.get_area())
    print(rectangle.get_perimeter())

    enginer = Enginer()
    print(enginer.measure_perimeter(square))
    print(enginer.measure_perimeter(rectangle))
    print(enginer.measure_area(square))
    print(enginer.measure_area(rectangle))