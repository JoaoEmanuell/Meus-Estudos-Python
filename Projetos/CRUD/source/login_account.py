import mysql.connector
from mysql.connector import connection

class Login():
    def __init__(self, host, user, password, database) -> None:
        self.connection = self.create_connection(host, user, password, database)
    def create_connection(self,host, user, password, database):
        return mysql.connector.connect(host=host,user=user,password=password, database=database)

    def close_connection(self):
        return self.connection.close()

    def login_account(self, name, password):
        cursor = self.connection.cursor()
        sql = f"SELECT NAME, PASS FROM TEST WHERE NAME = '{name}' AND PASS = '{password}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        return row