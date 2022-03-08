from .interface import ProductInterface
from typing import Type

class ShoppingCart :
    def __init__(self) -> None :
        self.__product = []

    def add_product(self, product : Type[ProductInterface]) -> None :
        self.__product.append(product)

    def finalize_purchase(self) -> None :
        print("Finalize Purchase")
        for product in self.__product :
            print(product.get_product_infos())

        self.__product = []