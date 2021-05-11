"""[ 11 - Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

a - Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
b - O consumo é especificado no construtor e o nível de combustível inicial é 0.
c - Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
d - Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e - Forneça um método adicionarGasolina( ), para abastecer o tanque.]
"""

class carro():
    def __init__(self, consumo = 10, combustível = 0):
        self.consumo = consumo
        self.combustivel = combustível
    
    def andar(self):
        distancia = float(input("Deseja andar quantos km? "))
        consumo = distancia / self.consumo
        self.combustivel -= consumo
        print(f"O carro andou {distancia} km, e consumiu {consumo} litros de combustivel")
        return consumo
    
    def obterGasolina(self):
        pass
    
    def adicionarGasolina(self):
        pass

carrinho = carro(combustível = 100)

carrinho.andar()