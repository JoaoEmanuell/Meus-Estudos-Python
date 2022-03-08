from source import RepositoryInterface
from typing import Type

class User:
    def __init__(self, repository : Type[RepositoryInterface]) -> None:
        self.__repository = repository
        
    def save_data(self, data : any) -> None:
        self.__repository.insert(data)

    def remove(self, data : any) -> None:
        self.__repository.remove(data)

class MysqlRepository(RepositoryInterface):
    def insert(self, data : any) -> None:
        print(f"Insert '{data}' into mysql")
    
    def remove(self, data : any) -> None:
        print(f"Remove '{data}' from mysql")

class MongoRepository(RepositoryInterface):
    def insert(self, data : any) -> None:
        print(f"Insert '{data}' into mongo")
    
    def remove(self, data : any) -> None:
        print(f"Remove '{data}' from mongo")

if __name__ == '__main__':
    mysql = MysqlRepository()
    mongo = MongoRepository()

    user = User(mysql)
    user.save_data(15)
    user.remove(15)

    user_2 = User(mongo)
    user_2.save_data(15)
    user_2.remove(15)