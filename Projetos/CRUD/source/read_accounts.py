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