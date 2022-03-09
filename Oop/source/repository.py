from .insert import Insert
from .select import Select

class Repository :
    def __init__(self) -> None :
        self.__insert = Insert()
        self.__select = Select()

    def select_by_id(self) -> None:
        self.__select.select_one()