import mysql.connector
from mysql.connector import connection
from . import sql_essential

class createAccount(sql_essential.sql_essential):
    def __init__(self):
        super().__init__()
        self.connection = self.create_connection()

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