"""
[9 - Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
a. Possua uma classe chamada Ponto, com os atributos x e y.
b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
c. Possua uma função para imprimir os valores da classe Ponto
d. Possua uma função para encontrar o centro de um Retângulo.
e. Você deve criar alguns objetos da classe Retangulo.
f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
h. O valor do centro do objeto deve ser mostrado na tela.
i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

No caso eu não irei fazer as e, f, g, h e i, uma vez que eu não entendi o que é para fazer.
"""

class ponto:
    def __init__(self, x = 10, y = 10):
        """[init]

        Args:
            x (int, optional): [valor x]. Defaults to 10.
            y (int, optional): [valor y]. Defaults to 10.
        """        
        self.x = x
        self.y = y
        
    def escrever(self):
        """[escreve os valores de x e y]

        Returns:
            [type]: [retorna x e y]
        """        
        print (f'x = {self.x}')
        print (f'y = {self.y}')
        return (f'x = {self.x}\ny = {self.y}')

class retangulo:
    def __init__(self, largura = 10, altura = 10):
        """[init]

        Args:
            largura (int, optional): [largura]. Defaults to 10.
            altura (int, optional): [altura]. Defaults to 10.
        """        
        self.largura = largura
        self.altura = altura
        
    def centro(self):
        """[calcula o centro do retangulo]

        Returns:
            [float]: [retorna o centro do triangulo]
        """        
        center = (self.largura + self.altura) / 2
        print(f'O centro do retangulo é {center}')
        return (center)

ponto = ponto(10, 10)

retangulo = retangulo(10, 10)
