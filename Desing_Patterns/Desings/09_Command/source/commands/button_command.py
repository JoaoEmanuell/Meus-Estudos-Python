from typing import Type
from .interfaces import CommandInterface, ReceptorInterface

class ButtonCommand(CommandInterface) :
    def __init__(self, receptor : Type[ReceptorInterface], information : any) -> None:
        self.__receptor = receptor
        self.__information = self.__format_information(information)

    def __format_information(self, information : any) -> any :
        return information

    def execute(self) -> None:
        self.__receptor.process_information(self.__information)
