from .controller import write_in_database
from .adapter import Adapter

def route1(message : dict) -> None:
    process = Adapter(Code())
    process.handle(message)

class Code:
    def handle(self, message) : 
        token = message["header"]["token"]

        if token:
            print("Authenticated")
            write_in_database(message['body']['name'], message['body']['message'])