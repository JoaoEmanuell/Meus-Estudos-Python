from json.decoder import JSONDecoder
import mysql.connector
from pathlib import Path
from os.path import join

class sql_essential():
    def __init__(self) -> None:
        self.json = self.sql_connection_read_json()
        self.connection = self.create_connection()
        
    def create_connection(self): return mysql.connector.connect(host=self.json["host"], user=self.json["user"], password=self.json["password"], database=self.json["database"])
    
    def close_connection(self): return self.connection.close()

    def sql_connection_read_json(self):
        path = join(Path().absolute(), 'source/')
        with open(f'{path}sql_configs.json', 'r') as f: return JSONDecoder().decode(f.read())