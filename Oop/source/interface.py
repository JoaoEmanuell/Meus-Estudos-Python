from abc import ABC, abstractmethod

class ProductInterface(ABC) :
    @abstractmethod
    def get_product_infos(self) -> str:
        raise NotImplementedError()
