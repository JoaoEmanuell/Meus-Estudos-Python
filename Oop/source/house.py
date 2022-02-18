class House:
    def __init__(self) -> None:
        self.__address = '123 Fake Street'
        self.__owner = None

    def turn_on_lights(self) -> None:
        print('Turning on lights in the house')

    def get_address(self) -> str:
        return self.__address

    def get_owner(self) -> any:
        return self.__owner

    def set_owner(self, owner : any) -> None:
        self.__owner = owner