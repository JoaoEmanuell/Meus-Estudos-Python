from .commands.interfaces import ReceptorInterface

class Receptor(ReceptorInterface) :
    def process_information(self, information : any) -> None :
        print('Receptor : send information to back-end!')
        print(information)