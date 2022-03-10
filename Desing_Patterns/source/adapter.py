from .interfaces import AdapterCodeInterface
from typing import Type

class Adapter (AdapterCodeInterface):
    def __init__(self, process : Type[AdapterCodeInterface]) -> None :
        self.__process  = process

    def handle(self, request : dict) -> None :
        message = {
            "method" : request["HTTP_method"],
            "header" : {
                "token" : request["HTTP_header"][0][1],
                "origin" : request["HTTP_header"][1][1]
            },
            "body" : {
                "name" : request["HTTP_body"][0][1],
                "message" : request["HTTP_body"][1][1]
            }
        }
        self.__process.handle(message)