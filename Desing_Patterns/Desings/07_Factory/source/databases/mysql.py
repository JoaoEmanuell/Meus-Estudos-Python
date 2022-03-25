from ..interfaces import DatabaseInterface

class MysqlRepository(DatabaseInterface) :
    def select_one(self) -> dict:
        return {
            'success' : True,
            'data' : 'Hello World!'
        }