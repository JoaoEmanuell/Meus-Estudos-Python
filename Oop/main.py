from source import ShoppingCart, Product
from typing import Type

if __name__ == '__main__':
    car = ShoppingCart()
    car.add_product(Product('Coca-Cola', 2.50))
    car.add_product(Product('Pepsi', 1.50))
    car.finalize_purchase()