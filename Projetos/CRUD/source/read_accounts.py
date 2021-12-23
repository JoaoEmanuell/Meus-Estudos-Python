import mysql.connector
from mysql.connector import connection

class read_accounts():
    def __init__(self, host, user, password, database) -> None:
        self.connection = self.create_connection(host, user, password, database)
        
    def create_connection(self,host, user, password, database):
        return mysql.connector.connect(host=host,user=user,password=password, database=database)

    def close_connection(self):
        return self.connection.close()

    def list_accounts(self):
        cursor = self.connection.cursor()
        sql = "SELECT NAME, PASS FROM TEST WHERE NAME != 'root'"
        cursor.execute(sql)
        row = cursor.fetchall()
        return row

    def update_user_name(self, old_name, new_name):
        cursor = self.connection.cursor()
        for account in self.list_accounts():
            if new_name in account: return False
        if new_name != '' and new_name != 'root':
            sql = f"UPDATE TEST SET NAME = '{new_name}' WHERE NAME = '{old_name}'"
            cursor.execute(sql)
            self.connection.commit()
            return True
        else:
            print("Nome de usuario invalido!")