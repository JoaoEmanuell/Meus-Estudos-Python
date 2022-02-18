class Store:
    tariff = 2
    def __init__(self, address : str) -> None:
        self.__address = address

    def show_address(self) -> None:
        print(self.__address)

    @classmethod
    def sell(cls, product : str, amount : int) -> int:
        return cls.tariff * amount

    @classmethod
    def set_tariff(cls, tariff : int) -> None:
        cls.tariff = tariff

if __name__ == '__main__':
    my_store_1 = Store('Rua 1')
    my_store_2 = Store('Rua 2')
    print(my_store_1.sell('Coca-Cola', 2))
    my_store_2.set_tariff(3)
    print(my_store_1.sell('Coca-Cola', 2))