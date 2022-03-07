from abc import ABC, abstractmethod

class ShapesInterface(ABC) : 
    @abstractmethod
    def get_perimeter(self) -> float :
        raise NotImplementedError

    def get_area(self) -> float :
        raise NotImplementedError