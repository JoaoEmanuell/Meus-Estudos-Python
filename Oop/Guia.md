- [Classe](#classe)
  - [Definição](#definição)
  - [Declarando uma classe](#declarando-uma-classe)
  - [Atributos](#atributos)
  - [Métodos](#métodos)
    - [Declarando um método](#declarando-um-método)
  - [Métodos especiais](#métodos-especiais)
    - [Construtor](#construtor)
  - [Instanciando uma classe](#instanciando-uma-classe)
  - [Métodos e atributos privados](#métodos-e-atributos-privados)
  - [Getters e Setters](#getters-e-setters)
  - [Variaveis de classe](#variaveis-de-classe)
  - [Métodos de classe](#métodos-de-classe)
  - [Métodos estáticos](#métodos-estáticos)
  - [Associações de classes](#associações-de-classes)
    - [Definindo o tipo do paramentro](#definindo-o-tipo-do-paramentro)
    - [Exemplo :](#exemplo-)
  - [Injeção de dependência](#injeção-de-dependência)
  - [Associação bilateral](#associação-bilateral)
- [Solid](#solid)
  - [SRP](#srp)
  - [OCP](#ocp)
  
# Classe

## Definição

A classe é uma descrição que abstrai um conjunto de objetos com características comuns.

## Declarando uma classe

Para declarar uma classe faça o seguinte : 

    class NomeDaClasse:
        . . .

    class RemoteControll:

Nesse caso eu não coloquei os paranteses, eles são opcionais.

## Atributos

Atributos são valores da classe que podem ser compartilhados entre a classe, eles são definidos dentro da propia classe, dentro de métodos ou dentro da propia classe *sendo esse segundo caso mais incomum* o mais comum é eles serem definidos no [método construtor](#construtor).

    self.atributo = valor

    self.room = room

## Métodos

### Declarando um método

Para declarar um método faça da seguinte forma :

    def nome_metodo(self, parametros : tipo_paramentro) -> tipo_retorno:
        . . .

    def chose_channel(self, channel : int) -> None:
        . . .

## Métodos especiais

Na classe existe métodos especiais chamados de métodos [dunder](https://www.geeksforgeeks.org/dunder-magic-methods-python/), esses métodos são padrões das classes e podem ser reescritos.

### Construtor

O método construtor é chamado de __ init __ toda vez que a classe é instanciada ele é chamado, ele deve retornar None.

    def __init__(self, parametros : tipo) -> None:
        . . .

## Instanciando uma classe

Para instanciar uma classe é só atribuir ela a uma variavel, automaticamente a variavel passa a ser um objeto da classe.

    objeto = NomeDaClasse()

    controll = RemoteControll("Samsung", "Living Room")

Assim sendo para acessar os métodos é só passar o objeto.nome_metodo(parametros) e para acessar os atributos é só objeto.atributo.

    controll.chose_channel(1)
    controll.room

## Métodos e atributos privados

Um método privado é um método que não pode ser acessado fora da classe, ele é definido como __ nome_metodo.

    def __add(self, num_1 : float, num_2 : float) -> float:
        return (num_1 + num_2)

Para acessar ele é só colocar self.__nome_metodo(parametros), no caso ele só pode ser acessado dentro da classe.

    self.__add(num_1, num_2)

No caso do atributo é a mesma regra :

    self.__atributo = valor

Para acessar é da mesma forma:

    print(self.__cpf)

Valendo a regra de que só pode ser acessado dentro da classe

## Getters e Setters

Getters e Setters são funções que facilitam a leitura do código na parte de manipulação dos atributos, eles são definidos como  get_nome_atributo e set_nome_atributo.

    def get_state(self) -> bool:
        return self.__state

    def set_state(self, state : bool) -> None:
        self.__state = state

## Variaveis de classe

Variaveis de classe são variaveis globais dentro da classe, ou seja todo objeto irá herdar elas, mas ao mesmo tempo se a variavel for reatribuida todos os objetos irão receber o novo valor dela, mesmo se eles já tiverem sido declarados, para acessar ou alterar a variavel dentro do contexto da classe coloque o self *nesse caso ela só será alterada para o objeto*, fora dela é só colocar o nome da classe e o nome da variavel.

    class MyClass:

        variavel = 'valor'

    # Alterando

    # Esse altera de forma global, todos os objetos irão receber esse valor.
    MyClass.variavel = 'novo valor'

    obj = MyClass()

    # Esse altera de forma local, no contexto do objeto, somente esse objeto irá receber a alteração de valor

    obj.variavel = 'novo valor'

## Métodos de classe

Métodos de classe são métodos decorados com o *classmethod* basicamente uma alteração feita em uma variavel de classe irá alterar todos os objetos, isso pois decoramos com o classmethod, quando utilizamos ele não podemos utilzar o self mas sim o *cls* pois o *cls* se refere diretamente a nossa classe.

    @classmethod
    def change_static(cls, static : str) -> None:
        cls.static = static 

Utilzar o *cls* seria a mesma coisa de fazer : 

    @classmethod
    def change_static(cls, static : str) -> None:
        MyClass.static = static

## Métodos estáticos

O método estatico é utilzado principalmente quando você não quer declarar a classe, uma vez que ele não depende das dependencias dela, dessa forma, ele pode ser utilizado em qualquer lugar mesmo sendo um método da classe.

O método estático não recebe *self* ou *cls*

Para criar um método estatico é só decorar uma função com o decorador *staticmethod*

    @staticmethod
    def error_500() -> None:
        print("Internal server error")

Ele pode tanto ser acessado por um *objeto* que instancia a *classe*, quanto por ele por si só [sem instanicar a *classe*] :

    obj = MyClass()
    obj.error_500()

    MyClass.error_500()
    MyClass().error_500()

    # Ambos retornam o mesmo resultado.

## Associações de classes

Associações de *classes* são quando as *classes* interagem entre si por uso de métodos de outras ou tipos, assim sendo se o tipo de um *paramentro* de uma função de uma *classe* for uma outra *classe* ele será automaticamente associado a essa *classe*, podendo chamar os métodos da mesma.

### Definindo o tipo do paramentro

Para definir o tipo do paramentro como sendo de uma classe importamos de typing o *Type* e utilizamos o *Type[classe]* para definir o tipo do paramentro.

    from typing import Type

    def turn_on_light(self, light_switch : Type[LightSwitch]) -> None:
        . . .

### Exemplo : 

    from typing import Type

    class LightSwitch:
        def __init__(self, room : str) -> None:
            self.__room = room

        def light_up(self) -> None:
            print(f"The light in the {self.__room} is on")

    class Person:
        def turn_on_light(self, light_switch : Type[LightSwitch]) -> None:
            light_switch.light_up()

Nesse método temos a função de ligar a luz, note que o paramentro *light_switch* é uma *classe* no caso o tipo de *classe* é do tipo *LightSwitch*, dessa forma ao passar o interruptor de luz como paramentro ele será automaticamente associado a *classe Person*, dessa forma esse paramentro poderá utilzar todos os métodos de *LightSwitch*.

    if __name__ == '__main__':
        Jhon = Person()
        light_switch_room = LightSwitch("room")
        
A variavel *light_switch_room* é uma um objeto da classe *LightSwitch*, ou seja, ela contem todos os métodos da classe *LightSwitch*.

    Jhon.turn_on_light(light_switch_room)
        
A pessoa liga a luz pela função dela [da classe pessoa], ao passamos a variavel *light_switch_room* como paramentro, ela será automaticamente associada a classe Person, dessa forma poderemos utilzar todos os métodos da classe *LightSwitch* chamando : *nome_paramentro.função()*.

## Injeção de dependência

Injeção de dependência é quando uma *classe* depende de outra *classe* para funcionar, sendo assim se algo da *classe a* for mudado a *classe b* que depende dela irá parar de funcionar.

Exemplo : 

    from typing import Type

    class House:
        def __init__(self) -> None:
            self.__address = 'Aurora Avenue 1'

Primeiramamente criamos a *classe House* que por sua vez não depende de ninguem.

    class Person:
        def __init__(self, name : str, place : Type[House]) -> None:
            self.__name = name
            self.__place = place

Após isso criamos a *classe Person*, o *init* de Person é 100% depedente de *House*, ou seja, se a *classe House* sofrer uma alteração a *classe Person* pode não funcionar mais e todo o código deve ser reescrito para se adequar as mudanças.

## Associação bilateral

Associação bilateral é quando duas classes dependem uma da outra para existir.

Exemplo : 

    class House:
        def __init__(self) -> None:
            self.__address = '123 Fake Street'
            self.__owner = None

        def turn_on_lights(self) -> None:
            print('Turning on lights in the house')

        def get_address(self) -> str:
            return self.__address

        def get_owner(self) -> any:
            return self.__owner

        def set_owner(self, owner : any) -> None:
            self.__owner = owner

A classe house está associada a um objeto chamado *owner*.

    class Person:
        def __init__(self, name : str) -> None:
            self.__name = name
            self.__place = None

        def enter_the_place(self) -> None:
            self.__place.turn_on_lights()

        def introduce_place(self) -> None:
            address = self.__place.get_address()
            print(f'Hi, my name is {self.__name} and I live in {address}')

        def set_place(self, place : any) -> None:
            self.__place = place

Já a classe *Person* está associada a um objeto chamado de place, assim sendo quando a função *enter_the_place* for chamada ela irá executar o método *turn_on_lights* de *house*.

    house = House()
    person = Person('Jhon')
    house.set_owner(person)
    person.set_place(house)

Acima dizemos que a casa pertence a pessoa e que a pessoa vive na casa.

    person.enter_the_place()
    person.introduce_place()

Quando chamamos o método get_owner da classe *House* ele retorna o objeto *person* que é o dono da casa.

    owner = house.get_owner()

Sendo assim podemos acessar métodos dele como : *owner.introduce_place()* e *owner.enter_the_place()*, assim gerando uma associação bilateral.

****
# Solid

Solid é um acrônimo dos cinco primeiros princípios da programção orientada a objetos, eles são :

    Single Responsibility Principle (SRP)
    Open/Closed Principle (OCP)
    Liskov Substitution Principle (LSP)
    Interface Segregation Principle (ISP)
    Dependency Inversion Principle (DIP)

## SRP

O SRP (Principio de responsabilidade unica) define que um método deve ter uma unica responsabilidade, isso é, ele deve realizar apenas um trabalho *um exemplo que pode ser aplicado é o de uma função gigantesca que pode ser quebrada em varias outras funções cada uma com uma responsabilidade única*

    class CadastralSystem:
    def register(self, name : str, age : int) -> None:
        if self.__verify_data(name, age):
            self.__save_user(name, age)
        else :
            self.__indicate_error()

    def __verify_data(self, name : str, age : int) -> bool:
        if isinstance(name, str) and isinstance(age, int) : return True # Isinstance é uma função que retornar True caso o tipo do valor seja igual ao tipo passado como parametro, senão ela retorna False.

No caso acima a função de registro está cuidando apenas do registro, quem faz a validação são outras funções.

## OCP

O OCP (Principio de abertura/fechamento) define que uma classe deve ser aberta para extensão e fechada para modificação, isso é, uma classe deve ser reutilizada e não modificada.

Um exemplo que pode ser dado é de um circo.

    class Circus:
        def introduce(self, presenter : int) -> None:
            if presenter == 1 :
                Clow().introduce_show()

            elif presenter == 2 :
        . . .

A forma demonstrada acima é inficiente, pois para cada um dos apresentadores, um novo *if* deve ser realizado, fazendo assim o código ficar grande, e não é uma boa prática, uma forma de reduzir isso seria se *presenter* fosse sempre uma instancia de uma classe qualquer que tivesse o metodo de *introduce_show*.

Dessa forma seria só criar uma classe qualquer que possua o método *introduce_show* e passar a mesma como paramentro.

    class Circus:
        def introduce(self, presenter : any) -> None:
            presenter.introduce_show()

Dessa forma se uma classe tiver esse método e for passada como paramentro automaticamente ele será chamado, dessa forma a *classe* será uma extensão da classe *Circus*.

    class Juggler:

        def introduce_show(self) -> None:
            print("Juggler introduce your show")

    if __name__ == '__main__':
        circus = Circus()
        juggler = Juggler()
        circus.introduce(juggler)

Observe agora que não estamos precisando de milhares de *ifs* para verificar cada estado, precisamos apensar de uma classe que possua o método *introduce_show* e passar como paramentro a classe propia classe.

Dessa forma milhares de classes podem ser criadas, desde que contenham o método desejado, assim quando ela for passada como paramentro esse método será chamado.

    class Clown:

        def introduce_show(self) -> None:
            print("Clown introduce your show")

    class Tamer:
    
        def introduce_show(self) -> None:
            print("Tamer introduce your show")

Dessa forma as classes criadas seriam uma extensão de *Circus*, sendo assim *Circus* está fechada para modificação mais aberta para extensão [desde que as classes extensoras possuam o método desejado].