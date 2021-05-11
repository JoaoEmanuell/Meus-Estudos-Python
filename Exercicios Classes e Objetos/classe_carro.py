"""[ 11 - Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

a - Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
b - O consumo é especificado no construtor e o nível de combustível inicial é 0.
c - Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
d - Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e - Forneça um método adicionarGasolina( ), para abastecer o tanque.]
"""

class carro():    
    def __init__(self, consumo = 10, combustível = 0):
        """[summary]

        Args:
            consumo (int, optional): [consumo de gasolina por litro]. Defaults to 10.
            combustível (float, optional): [quantidade total de gasolina do carro]. Defaults to 0.
        """        
        self.consumo = consumo
        self.combustivel = combustível
    
    def andar(self):
        """[pergunta quantos km devem ser andados, depois divide a distancia pecorrida pelo total de consumo do carro e subtrai isso do combustivel, se o combustivel for inferior a 0, o combustivel recebe 0, escreva "A gasolina acabou", chame a função obterGasolina e retorne Falso, senão escreva "O carro andou {distancia} km, e consumiu {consumo} litros de combustivel" e retorne o consumo]

        Returns:
            [float]: [retorna o consumo de gasolina]
        """        
        distancia = float(input("Deseja andar quantos km? "))
        consumo = distancia / self.consumo
        self.combustivel -= consumo
        if self.combustivel < 0:
            self.combustivel = 0
            print("A gasolina acabou")
            carro.obterGasolina(self)
            return False
        else:
            print(f"O carro andou {distancia} km, e consumiu {consumo} litros de combustivel")
            return consumo
    
    def obterGasolina(self):
        """[mostra o nivel de gasolina]

        Returns:
            [float]: [retorna o total de combustivel do carro]
        """        
        print(f"O nivel de gasolina é {self.combustivel} litros")
        return self.combustivel
    
    def adicionarGasolina(self):
        """[serve para adicionar gasolina ao carro, pergunta quantos litros serão colocados, o self.combustivel += quantidade, escreve "sucesso..." retorna o numero de litros adicionados]
        """           
        gasolina = float(input("Quantos litros de gasolina serão colocados? "))
        self.combustivel += gasolina
        print(f"Sucesso, adicionado {gasolina} litros de gasolina no carro")
        return(gasolina)

carrinho = carro(combustível = 100)

carrinho.andar()

carrinho.obterGasolina()

carrinho.adicionarGasolina()

carrinho.obterGasolina()