class CadastralSystem:
    def register(self, name : str, age : int) -> None:
        if self.__verify_data(name, age):
            self.__save_user(name, age)
        else :
            self.__indicate_error()

    def __verify_data(self, name : str, age : int) -> bool:
        if isinstance(name, str) and isinstance(age, int) : return True # Isinstance is a function that returns True if the object is of the specified type
        return False

    def __save_user(self, name : str, age : int) -> None:
        print(f"Save, Name : {name}, Age : {age}")

    def __indicate_error(self) -> None:
        print("Error, Invalid Input")

if __name__ == '__main__':
    user = CadastralSystem()
    user.register("John", 20)