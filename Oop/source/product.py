from .interface import ProductInterface

class Product (ProductInterface) :
    def __init__(self, name : str, value : float) -> None:
        self.__name = name
        self.__value = value

    def get_product_infos(self) -> str:
        return f"Product : {self.__name} || Value : R$ {self.__value:.2f}"
