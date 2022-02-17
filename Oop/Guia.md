- [Classe](#classe)
  - [Definição](#definição)
  - [Declarando uma classe](#declarando-uma-classe)
  - [Atributos](#atributos)
  - [Métodos](#métodos)
    - [Declarando um método](#declarando-um-método)
  - [Métodos especiais](#métodos-especiais)
    - [Construtor](#construtor)
  - [Instanciando uma classe](#instanciando-uma-classe)
  
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