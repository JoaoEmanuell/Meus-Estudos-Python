from .controller import write_in_database
from .adapter import Adapter
from .interfaces import AdapterCodeInterface

def route1(message : dict) -> None:
    process = Adapter(Code())
    process.handle(message)

class Code (AdapterCodeInterface):
    def handle(self, message) -> None: 
        token = message["header"]["token"]

        if token:
            print("Authenticated")
            write_in_database(message['body']['name'], message['body']['message'])