from typing import Dict, List
from random import randint
from abc import ABC, abstractmethod

class AlgorithmTemplate(ABC) :

    def insert_data(self, data : List[str]) -> None :
        formatted_data = self.__format_data(data)
        formatted_data_with_id = self.__insert_id(formatted_data)
        self.insert_value_in_doc(formatted_data_with_id)

    def __format_data(self, data : List[str]) -> Dict[str, str] :
        formatted_data = {
            "name" : data[0],
            "last name" : data[1],
            "city" : data[2]
        }
        return formatted_data

    def __insert_id(self, formatted_data : Dict[str, str]) :
        formatted_data["id"] = randint(1, 1000)
        return formatted_data

    @abstractmethod
    def insert_value_in_doc(self, formatted_data_with_id : Dict[str, str]) -> None :
        raise NotImplementedError