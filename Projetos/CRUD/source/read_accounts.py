import mysql.connector
from mysql.connector import connection
from . import sql_essential

class read_accounts(sql_essential.sql_essential):
    def __init__(self):
        super().__init__()
        self.connection = self.create_connection()

    def list_accounts(self):
        """[Lists accounts stored in the database, does not return the root account.]

        Returns:
            [list]: [Accounts stored in the database.]
        """
        cursor = self.connection.cursor()
        sql = "SELECT NAME, PASS FROM TEST WHERE NAME != 'root'"
        cursor.execute(sql)
        row = cursor.fetchall()
        return row

    def update_user_name(self, old_name, new_name):
        """[Change the username in the database]

        Args:
            old_name ([str]): [Old username, this is the name that is stored in the database]
            new_name ([str]): [New username, this is the name that will become the new name stored in the database.]

        Returns:
            [Bool]: [If the username is not being used it will change and return True, otherwise it will return False]
        """
        for account in self.list_accounts():
            if new_name in account or len(new_name) > 50: return False
        if new_name != '' and new_name != 'root':
            sql = f"UPDATE TEST SET NAME = '{new_name}' WHERE NAME = '{old_name}'"
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            return True

    def update_user_password(self, username, new_pass):
        """[Change the password stored in the database]

        Args:
            username ([str]): [User name]
            new_pass ([str]): [New password]
        """
        if len(new_pass) > 20 : return False
        cursor = self.connection.cursor()
        sql = f"UPDATE TEST SET PASS = '{new_pass}' WHERE NAME = '{username}'"
        cursor.execute(sql)
        self.connection.commit()
        return True

    def delete_user(self, username, password):
        """[Delete the user from the database]

        Args:
            username ([str]): [User name]
            password ([str]): [Password]
        """
        cursor = self.connection.cursor()
        sql = f"DELETE FROM TEST WHERE NAME = '{username}' AND PASS = '{password}' LIMIT 1"
        cursor.execute(sql)
        self.connection.commit()