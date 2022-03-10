# Menu

- [Menu](#menu)
- [Inicio](#inicio)
- [Adapter](#adapter)
  - [Como implementar](#como-implementar)
    - [Interface](#interface)
    - [Adapter](#adapter-1)
    - [Exemplo](#exemplo)

# Inicio

Desing Patterns são padrões de desenho de softwares que servem para resolver problemas comuns dentro de um determinado contexto 

# Adapter

O Adapter serve para fazer adaptações de dados, entre um sistema antigo e um novo [ou um framework antigo e um framework novo].

## Como implementar

Primeiramente entenda o contexto, você irá adaptar de uma classe antiga [que usa um formato x] para uma classe nova [que usa um formato y].

### Interface

    from abc import ABC, abstractmethod

    class AdapterCodeInterface(ABC) :
        @abstractmethod
        def handle(self, message : dict) -> None:
            pass

### Adapter

Crie uma classe chamada de Adapter, no *init* dela ela deve receber um paramentro chamado *process* que é uma instancia de uma classe que implementa a interface [AdapterCodeInterface].

    from .interfaces import AdapterCodeInterface
    from typing import Type

    class Adapter:
        def __init__(self, process : Type[AdapterCodeInterface]) -> None:
            self.__process  = process

Ela deve ter um método chamado de *handle* ele será o metódo conversor, no nosso caso ele vai receber um paramentro chamado de *request* que é um *dict* no formato antigo.

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

Por fim ele irá chamar o método *handle* da classe que implementa a interface [AdapterCodeInterface] passando o paramentro *message* que é um *dict* no formato novo.

    self.__process.handle(message)

### Exemplo

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