import mysql.connector
from mysql.connector import connection
from . import sql_essential

class read_accounts(sql_essential.sql_essential):
    def __init__(self):
        super().__init__()
        self.connection = self.create_connection()

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

    def update_user_password(self, username, new_pass):
        cursor = self.connection.cursor()
        sql = f"UPDATE TEST SET PASS = '{new_pass}' WHERE NAME = '{username}'"
        cursor.execute(sql)
        self.connection.commit()

    def delete_user(self, username, password):
        cursor = self.connection.cursor()
        sql = f"DELETE FROM TEST WHERE NAME = '{username}' AND PASS = '{password}' LIMIT 1"
        cursor.execute(sql)
        self.connection.commit()