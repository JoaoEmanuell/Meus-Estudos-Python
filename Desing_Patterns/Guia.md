# Menu

- [Menu](#menu)
- [Inicio](#inicio)
- [Adapter](#adapter)
  - [Como implementar](#como-implementar)
    - [Interface](#interface)
    - [Adapter](#adapter-1)
    - [Exemplo](#exemplo)
- [Strategy](#strategy)
  - [Como implementar](#como-implementar-1)
    - [Interface](#interface-1)
    - [Implementação](#implementação)
    - [Strategy](#strategy-1)
- [Singleton](#singleton)
  - [Como implementar](#como-implementar-2)
    - [Classe](#classe)
    - [Singleton](#singleton-1)
    - [Implementação](#implementação-1)

# Inicio

Design Patterns são padrões de desenho de softwares que servem para resolver problemas comuns dentro de um determinado contexto 

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

Crie uma classe chamada de Adapter, no *init* dela ela deve receber um parâmetro chamado *process* que é uma instancia de uma classe que implementa a interface [AdapterCodeInterface].

    from .interfaces import AdapterCodeInterface
    from typing import Type

    class Adapter:
        def __init__(self, process : Type[AdapterCodeInterface]) -> None:
            self.__process  = process

Ela deve ter um método chamado de *handle* ele será o método conversor, no nosso caso ele vai receber um parâmetro chamado de *request* que é um *dict* no formato antigo.

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

Por fim ele irá chamar o método *handle* da classe que implementa a interface [AdapterCodeInterface] passando o parâmetro *message* que é um *dict* no formato novo.

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

# Strategy

O Strategy basicamente trabalha no conceito de inversão de dependência, ou seja, quando uma classe requerer um método de outra classe, ela deve trabalhar utilizando *interfaces* ao invés de utilizar a classe de forma direta.

## Como implementar

Analise o seu caso especifico e crie as *interfaces* que irão trabalhar, dessa forma a *injeção de dependência* pode ser evitada.

### Interface

    from abc import ABC, abstractmethod

    class SkillInterface(ABC):
        @abstractmethod
        def behavior(self) -> None:
            raise NotImplementedError

        @abstractmethod
        def level_atribute(self) -> None:
            raise NotImplementedError

### Implementação 

    from .interfaces import SkillInterface

    class UseBow(SkillInterface):
        def __init__(self, level : int = 1) -> None:
            self.__level = level

        def behavior(self) -> None:
            print("Shoot Arrows")

        def level_atribute(self) -> None:
            print(f"Bow usage level : {self.__level}")

### Strategy

    from .skills import SkillInterface
    from typing import Type

Classe que irá depender das interfaces.

    class Warrior:
        def __init__(self, skill : Type[SkillInterface]) -> None:
            self.__skill = skill

Observe que o tipo de skill é uma interface, dessa forma o warrior não precisa saber qual é a class que será passada, ele só precisa saber que essa classe implemente a interface.

        def action(self) -> None:
            self.__skill.behavior()

        def atributes(self) -> None:
            self.__skill.level_atribute()

Arquivo principal

    from source import Warrior, UseBow

    archer = Warrior(UseBow(6))
    archer.action()
    archer.atributes()

# Singleton

O Singleton diz que uma classe criada deve ser instanciada uma única vez de forma global, sendo assim você não irá criar diversos objetos alocados em lugares diferentes na memória.

## Como implementar

Primeiramente crie um arquivo com a classe desejada :

### Classe

    class SaySomething:
        def __init__(self, message : str) -> None:
            self.__message = message

        def say(self) -> None:
            print(self.__message)

        def change_message(self, new_message : str) -> None :
            self.__message = new_message

### Singleton

Em seguida um arquivo chamado *singleton* que irá instanciar a classe.

    from .my_class import SaySomething

    message = SaySomething("Hello World")

Dessa forma ao invés de importamos a classe de forma direta, iremos importar o singleton.

### Implementação

init.py

    from .singleton import message

element1.py

    from source import message

    element1 = message
    element1.say()
    element1.change_message("Element 1")

element2.py

    from source import message

    element2 = message
    element2.say()

main.py

    from element1 import element1
    from element2 import element2

Uma coisa interessante a se notar é que se importamos o *element1* primeiro, o valor de *message* será alterado no *element2*, isso pode causar algumas dores de cabeça indesejadas, então tome cuidado.
