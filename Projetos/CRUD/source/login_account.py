import mysql.connector
from mysql.connector import connection
from . import sql_essential

class Login(sql_essential.sql_essential):
    def __init__(self):
        super().__init__()
        self.connection = self.create_connection()

    def login_account(self, name, password):
        """[Login to account]

        Args:
            name ([str]): [User name]
            password ([str]): [Password]

        Returns:
            [tuple, None]: [If the login is valid it returns a tuple with the username and password, if not, it returns None]
        """
        cursor = self.connection.cursor()
        sql = f"SELECT NAME, PASS FROM TEST WHERE NAME = '{name}' AND PASS = '{password}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        return row