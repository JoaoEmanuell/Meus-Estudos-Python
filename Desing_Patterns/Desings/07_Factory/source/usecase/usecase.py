from ..interfaces import DatabaseInterface
from typing import Type, Union

class UseCase:

    def __init__(self, repository : Type[DatabaseInterface]) -> None:
        self.__repository = repository

    def do_something(self, data : bool = True) -> Union[dict, None]:
        if data :
            repository_response = self.__repository.select_one()
            return repository_response

        return None