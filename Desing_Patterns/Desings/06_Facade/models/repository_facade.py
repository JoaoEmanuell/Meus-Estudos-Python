from .delete import Delete
from .insert import Insert
from .select import Select

class Repository:
    def __init__(self) -> None :
        self.__delete = Delete()
        self.__insert = Insert()
        self.__select = Select()

    def select_one(self) -> None :
        return self.__select.select_single_element()

    def select_many(self) -> None :
        return self.__select.select_many_elements()

    def insert_one(self) -> None :
        return self.__insert.insert_single_element()

    def insert_many(self) -> None :
        return self.__insert.insert_many_elements()

    def delete_one(self) -> None :
        return self.__delete.delete_single_element()