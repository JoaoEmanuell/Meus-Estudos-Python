class DatabaseConnection:
    def __init__(self) -> None:
        self.__database = 'MongoDB'
        self._con = '//localhost:27017'
        self.user = 'root'

    def get_database(self) -> None:
        print(self.__database)

    def _testing_connection(self) -> None:
        print(self._con)

class Repository(DatabaseConnection):
    def __init__(self) -> None:
        super().__init__()

if __name__ == '__main__':
    python = Repository()
    python.get_database()
    python._testing_connection()