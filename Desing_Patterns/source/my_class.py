class SaySomething:
    def __init__(self, message : str) -> None:
        self.__message = message

    def say(self) -> None:
        print(self.__message)

    def change_message(self, new_message : str) -> None :
        self.__message = new_message
