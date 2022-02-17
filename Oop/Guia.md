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
- [Solid](#solid)
  - [SRP](#srp)
  
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

# Solid

Solid é um acrônimo dos cinco primeiros princípios da programção orientada a objetos, eles são :

    Single Responsibility Principle (SRP)
    Open/Closed Principle (OCP)
    Liskov Substitution Principle (LSP)
    Interface Segregation Principle (ISP)
    Dependency Inversion Principle (DIP)

## SRP

O SRP (Principio de responsabilidade unica) definie que um método deve ter uma unica responsabilidade, isso é, ele deve realizar apenas um trabalho *um exemplo que pode ser aplicado é o de uma função gigantesca que pode ser quebrada em varias outras funções cada uma com uma responsabilidade única*

    class CadastralSystem:
    def register(self, name : str, age : int) -> None:
        if self.__verify_data(name, age):
            self.__save_user(name, age)
        else :
            self.__indicate_error()

    def __verify_data(self, name : str, age : int) -> bool:
        if isinstance(name, str) and isinstance(age, int) : return True # Isinstance é uma função que retornar True caso o tipo do valor seja igual ao tipo passado como parametro, senão ela retorna False.

No caso acima a função de registro está cuidando apenas do registro, quem faz a validação são outras funções.