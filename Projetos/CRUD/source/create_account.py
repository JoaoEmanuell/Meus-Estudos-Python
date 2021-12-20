import mysql.connector
from mysql.connector import connection

class createAccount():
    def __init__(self, host, user, password, database) -> None:
        self.connection = self.create_connection(host, user, password, database)
        
    def create_connection(self,host, user, password, database):
        return mysql.connector.connect(host=host,user=user,password=password, database=database)

    def close_connection(self):
        return self.connection.close()

    def create_account(self, name, password):
        if self.verfiy_if_account_exists(name):
            return False
        else :
            cursor = self.connection.cursor()
            sql = f"INSERT INTO TEST (NAME, PASS) VALUES ('{name}', '{password}')"
            cursor.execute(sql)
            cursor.close()
            self.connection.commit()
            return True
            
    def verfiy_if_account_exists(self, name):
        cursor = self.connection.cursor()
        sql = f"SELECT NAME FROM TEST WHERE NAME = '{name}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if type(row) == tuple: return True
        else: True