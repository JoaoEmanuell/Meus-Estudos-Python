import mysql.connector
from mysql.connector import connection
from . import sql_essential

class Login(sql_essential.sql_essential):
    def __init__(self):
        super().__init__()
        self.connection = self.create_connection()

    def login_account(self, name, password):
        cursor = self.connection.cursor()
        sql = f"SELECT NAME, PASS FROM TEST WHERE NAME = '{name}' AND PASS = '{password}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        return row