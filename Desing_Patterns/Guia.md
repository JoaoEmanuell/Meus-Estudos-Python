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
- [Decorator](#decorator)
  - [Como implementar](#como-implementar-3)
    - [Decorator](#decorator-1)
- [Observer](#observer)
  - [Como implementar](#como-implementar-4)
    - [Interface](#interface-2)
    - [Observer](#observer-1)
    - [Implementação](#implementação-2)
- [Facade](#facade)
  - [Como implementar](#como-implementar-5)
    - [Delete](#delete)
    - [Insert](#insert)
    - [Facade](#facade-1)
    - [Lei de Demeter](#lei-de-demeter)
- [Factory](#factory)
  - [Como implementar](#como-implementar-6)
    - [Interfaces](#interfaces)
    - [Database](#database)
    - [Caso de uso](#caso-de-uso)
    - [Factory](#factory-1)
- [Chain of Responsibility](#chain-of-responsibility)
  - [Como implementar](#como-implementar-7)
    - [Interfaces](#interfaces-1)
    - [Validators](#validators)
    - [Chain of Responsibility](#chain-of-responsibility-1)
  - [Observações](#observações)
- [Command](#command)
  - [Como implementar](#como-implementar-8)
    - [Interfaces](#interfaces-2)
    - [ButtonCommand](#buttoncommand)
    - [Receptor](#receptor)
    - [Button](#button)
    - [Command](#command-1)

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

# Decorator

Decorator é um design pattern que permite adicionar funcionalidades a uma função já existente.

[Nesse arquivo](https://github.com/JoaoEmanuell/Meus-Estudos-Python/blob/master/Aulas%20txt/Decorators.txt) temos uma demonstração de implementação do decorator utilizando uma classe ao invés de uma função.

## Como implementar

Diferente de outras linguagens, para implementar o decorator no python é bem simples, você só vai precisar criar uma função que receba outra função e fazer um processamento dentro de outra função e retornar essa outra função [confuso]

### Decorator


    from typing import Callable # Callable vai servir para dizer que o objeto passado tem que ser do tipo clamável, isso é uma função ou uma classe.

    def decorator(function : Callable) -> None:

Colocamos *args e **kwargs para evitar um bug de argumentos, pois se estamos trabalhando com uma *classe* e a *função* receber um *self*, ela iria da erro pois não tem argumentos.

        def wrapper(*args, **kwargs):

Wrapper é como normalmente é chamada a função superior que faz o processamento.

            print("Hello World")
            function(*args, **kwargs)

No final ela deve chamar a função e passar o *args e *kwargs* para ela.

        return wrapper

    class MyClass:
        @decorator
        def method(self, number : int) -> None:
            print(f"My method {number}")

    cl = MyClass()

# Observer

Observer é um *design pattern* que serve para que uma classe possa notificar outras classes por meio de um método.

## Como implementar

Para implementar crie uma interface com o método *update*, e uma classe que implemente essa interface.

### Interface

    from abc import ABC, abstractmethod

    class ObserverInterface(ABC):
        @abstractmethod
        def update(self, message : str) -> None:
            raise NotImplementedError

### Observer

    from .interfaces import ObserverInterface

    class Person(ObserverInterface):
        def __init__(self, name : str) -> None:
            self.__name = name
            self.__awake = False

        def update(self) -> None:
            print(f"{self.__name} Awake")
            self.__awake = True

### Implementação

    # Imports

    from .interfaces import ObserverInterface
    from typing import Type

    class Alarm:

Class que irá utilizar o *observer*.

        def __init__(self) -> None:
            self.__beep = False

persons será uma lista com pessoas que são do tipo *ObserverInterface*.

            self.__persons = []

        def add_person(self, person : Type[ObserverInterface]) -> None:
            self.__persons.append(person)

        def play(self) -> None:
            self.__beep = True
            for person in self.__persons:
                person.update()

Aqui estamos notificando as pessoas pelo método *update*, como elas implementam a interface, elas tem esse método.

            self.__persons = []

Por fim limpamos a lista de pessoas.

    from source import Alarm, Person

    emanuel = Person("Emanuel")
    john = Person("John")
    rebeca = Person("Rebeca")

Criamos as pessoas

    alarm = Alarm()

    alarm.add_person(emanuel)
    alarm.add_person(john)
    alarm.add_person(rebeca)

Adicionamos as pessoas

    alarm.play()

Notificamos as pessoas.

# Facade

O Facade [fachada em português] é um design pattern que serve para simplificar as interações, ao invés de você interagir com cada objeto de uma classe, quando for fazer algo, você irá atribuir esses objetos a uma classe de fachada que irá fazer a interação.

## Como implementar

Primeiramente iremos ter classes que fazem todo o trabalho de interação com o banco de dados.

### Delete

    class Delete :

        def delete_single_element(self) -> None :
            print('Delete a single register')

### Insert

    class Insert :

        def insert_single_element(self) -> None :
            print('Insert a single register')

        def insert_many_elements(self) -> None :
            print('Insert a list of registers')

### Facade

    from .delete import Delete
    from .insert import Insert

    class Repository:
        def __init__(self) -> None :
            self.__delete = Delete()
            self.__insert = Insert()

        def insert_one(self) -> None :
            return self.__insert.insert_single_element()

        def insert_many(self) -> None :
            return self.__insert.insert_many_elements()

        def delete_one(self) -> None :
            return self.__delete.delete_single_element()

Observe que a classe acima agrega as outras classes e simplifica os seus usos.

### Lei de Demeter

A Lei de Demeter diz que uma classe só deve interagir com objetos que estão sendo passados para ela ou que ela instanciou no inicio, isso é basicamente semelhante ao principio da inversão de dependência.

Portanto a *facade* só deve interagir com objetos que estão sendo passados para ela ou que ela instanciou no inicio.

# Factory

Factory é um design pattern que serve para criar objetos de forma dinâmica [como uma fabrica].

## Como implementar

A implementação dele depende de várias outras classes independentes, tudo que ele irá é unir elas e retornar um único resultado, ele simplifica alterações futuras.

### Interfaces

    from abc import ABC, abstractmethod

    class DatabaseInterface(ABC) :
        @abstractmethod
        def select_one(self) -> dict :
            raise NotImplementedError

### Database

    from ..interfaces import DatabaseInterface

    class MysqlRepository(DatabaseInterface) :
        def select_one(self) -> dict:
            return {
                'success' : True,
                'data' : 'Hello World!'
            }

### Caso de uso

    from ..interfaces import DatabaseInterface
    from typing import Type, Union

    class UseCase:

        def __init__(self, repository : Type[DatabaseInterface]) -> None:

Utilizando *Type* estamos evitando a injeção de dependência.

            self.__repository = repository

        def do_something(self, data : bool = True) -> Union[dict, None]:

Union serve para dizer que tem duas respostas possíveis

            if data :
                repository_response = self.__repository.select_one()
                return repository_response

            return None

### Factory

    from ..usecase import UseCase
    from ..databases import MysqlRepository

    class MysqlFactory :
        @staticmethod
        def create() -> UseCase :
            return UseCase(MysqlRepository())

@staticmethod diz que o método é estático, então não é necessário instanciar a classe para utilizar o método.

Create irá retornar uma instancia de UseCase, passando uma instancia de MysqlRepository como parâmetro, caso no futuro tenhamos que trocar o repositório, basta alterar a classe que está sendo passada como parâmetro.

No nosso arquivo main iremos criar o UseCase por meio do MysqlFactory.

    from source import MysqlFactory

    usecase = MysqlFactory.create()

Após isso vamos utilizar os métodos de UseCase : 

    response = usecase.do_something()
    print(response)

Desta forma a modificação a longo prazo fica muito mais simples.

# Chain of Responsibility

Chain of Responsibility trabalha no conceito de responsabilidades únicas, sendo um Design Pattern extremamente útil quando se tem muitas verificações há serem realizadas.

## Como implementar

Para implementar ele você irá precisar de sub-classes [pode haver milhares delas] e uma única classe que irá ser responsável por chamar a ação da sub-classe caso o valor corresponda a um validador dela.

### Interfaces

    from abc import ABC, abstractmethod

    class ValidatorInterface(ABC) :
        @abstractmethod
        def validate(self, food : str) -> bool :
            raise NotImplementedError

        @abstractmethod
        def action(self) -> None :
            raise NotImplementedError

### Validators

    from ..interfaces import ValidatorInterface

    class NutValidator(ValidatorInterface) :
        def validate(self, food: str) -> bool:
            if food == "nut" :
                return True
            return False

        def action(self) -> None:
            print("The squirrel eats the nut")

    from ..interfaces import ValidatorInterface

    class BananaValidator(ValidatorInterface) :

        def validate(self, food : str) -> bool :
            if food == 'banana' :
                return True
            return False

        def action(self) -> None:
            print("The monkey eats the banana")

Perceba que em ambos os validadores temos uma verificação que irá retornar um *bool*.

### Chain of Responsibility

    from source.validators import MeatValidator, BananaValidator, NutValidator

    class Validate :
        def __init__(self) -> None :

Adicionaremos as classes de validadores a uma lista, como elas seguem a implementação da interface, todas elas tem os métodos *validate* e *action*.

    self.__validators = [
        BananaValidator(),
        NutValidator(),
        MeatValidator()
    ]

Agora iremos verificar se o valor passado corresponde a alguma das classes, por meio de um *for*, caso o *validate* dela retorne verdadeiro então poderemos chamar o método *action* dela.

    def process(self, food : str) -> None :
        for validator in self.__validators :
            if validator.validate(food) :
                return validator.action()
        print("Indefinite food")

O *print* final serve caso não corresponda há nenhuma, se o *for* não for quebrado ele irá ser executado.

## Observações

Ao invés de criar a lista com todos as instancias já feitas, podemos criar uma função que irá adicionar os *validators* a lista.

    from typing import List 

A importação acima irá servir para indicar o tipo da lista (int, float, interface, etc).

    from source.validators import MeatValidator, BananaValidator, NutValidator
    from source.interfaces import ValidatorInterface

    class Validate :
        def __init__(self) -> None :

Especificaremos que o tipo da lista vai ser de ValidatorInterface.

    self.__validators : List[ValidatorInterface] = []

Especificamos o tipo da lista do parâmetro.

    def add_validators(self, validators : List[ValidatorInterface]) -> None :

Faremos um for e verificaremos se é uma instancia da interface, caso não seja iremos exibir um *TypeErro*, caso esse erro não ocorra iremos adicionar ele a lista.

        for validator in validators :
            if not isinstance(validator(), ValidatorInterface) :
                raise TypeError(f"Invalid validator type {validator}")
            self.__validators.append(validator())

    if __name__ == '__main__' :
        validate = Validate()
        validate.add_validators([BananaValidator, NutValidator, MeatValidator])

Caso prefira adicionar ele diretamente em *self.__validators* você pode utilizar o *List* :

    def __init__(self) -> None :
        self.__validators : List[ValidatorInterface] = [
            BananaValidator(), 
            NutValidator(), 
            MeatValidator()
        ]

# Command

Command é um Design pattern extremamente útil quando se tem um contexto de mensagens.

## Como implementar

A implementação dele depende primeiramente de um elemento que irá enviar a mensagem para outro elemento que irá formatar a mensagem e enviar, para um receptor.

### Interfaces

Interface do Command :

    from abc import ABC, abstractmethod

    class CommandInterface(ABC) :
        
        @abstractmethod
        def execute(self) -> None :
            raise NotImplementedError

    from abc import ABC, abstractmethod

Interface do receptor :

    class ReceptorInterface(ABC) :

        @abstractmethod
        def process_information(self, information : any) -> None :
            raise NotImplementedError

### ButtonCommand 

    from typing import Type
    from .interfaces import CommandInterface, ReceptorInterface

    class ButtonCommand(CommandInterface) :
        def __init__(self, receptor : Type[ReceptorInterface], information : any) -> None:
            self.__receptor = receptor
            self.__information = self.__format_information(information)

Perceba que ele formata a mensagem, para que ela seja enviada para o receptor.

        def __format_information(self, information : any) -> any :
            return information

        def execute(self) -> None:
            self.__receptor.process_information(self.__information)

### Receptor

    from .commands.interfaces import ReceptorInterface

    class Receptor(ReceptorInterface) :
        def process_information(self, information : any) -> None :
            print('Receptor : send information to back-end!')
            print(information)

### Button

    from typing import Type
    from .commands.interfaces import CommandInterface

    class Button :
        def __init__(self) -> None:
            self.__command = None

        def set_command(self, command : Type[CommandInterface]) -> None:
            self.__command = command

        def action(self) -> None :
            if self.__command :
                self.__command.execute()

Caso exista um *command* execute ele.


### Command

    from source import Button, Receptor
    from source.commands import ButtonCommand

    receptor = Receptor()
    button = Button()

Iremos setar o *command* no *button*, para isso iremos passar o receptor e um dicionario com uma mensagem.

    button.set_command(ButtonCommand(receptor, {
        'Hello' : 'World'
    }))

Após isso iremos chamar o método *action* que irá executar toda a ação necessária para que a mensagem seja enviada ao back-end.

    button.action()