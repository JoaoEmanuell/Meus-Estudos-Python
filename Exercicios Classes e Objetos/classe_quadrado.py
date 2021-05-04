'''
2 - Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class quadrado():
    """[Classe quadrado]

        Def:
        
        __init__ ([inicial]): [Def inicial]

        tamanho ([tamanho]): [Def que pergunta um tamanho]

        escrever ([escrever]): [Def que escreve na tela]
    """
    def __init__(self, lado):
        """[summary]

        Args:
            lado ([type]): [Recebe o lado do quadrado]
        """
        self.lado = lado
    
    def tamanho(self):
        """[summary]
        
        Args:
            l ([int]): [Pergunta qual sera o novo lado do quadrado]
        """
        l = int(input("Qual é o novo tamanho do lado do quadrado? "))
        self.lado = l
           
    def escrever(self):
        """[summary]

        Returns:
            [int]: [Retorna o total do tamanho dos lados do quadrado vezes 4]
        """
        print(f'O tamanho de cada lado do quadrado é {self.lado}')
        return print(f"A area total do quadrado é {self.lado * 4}")

p1 = quadrado(150)

p1.escrever()