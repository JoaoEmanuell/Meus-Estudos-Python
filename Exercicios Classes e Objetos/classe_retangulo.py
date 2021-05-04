'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''

class ret():
    def __init__(self, comprimento, largura):
        """[função de inicialização]

        Args:
            comprimento ([float]): [Comprimento do retangulo]
            largura ([float]): [Comprimento do retangulo]
        """
        self.comprimento = comprimento
        self.largura = largura
        
    def lados(self):
       self.comprimento = float(input("Qual o comprimento? "))
       self.largura = float(input("Qual a largura? "))
       retorno = (print(f"O valor do comprimento é {self.comprimento} e o da largura é {self.largura}\nA area do retangulo é {self.comprimento * self.largura}\nO perimentro do retangulo é igual a {(self.comprimento * 2) + (self.largura * 2)}"))
       return retorno

class casa(ret):
    def __init__(self, comprimento=1, largura=1):
        self.comprimento = comprimento
        self.largura = largura
    
    def lados(self):
       self.comprimento = float(input("Qual o comprimento do lugar? "))
       self.largura = float(input("Qual a largura do lugar? "))
       self.m2 = self.comprimento * self.largura
       retorno = (print(f"Serão necessarios {int(self.m2)} pisos para completar o lugar"))
       return retorno
        
p1 = casa()

p1.lados()