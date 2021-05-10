"""8 - Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""
    
class macaco():
    def __init__(self, nome, estomago = 'banana')
        self.nome = nome
        self.estomago = estomago
    
    def comer(self):
        self.estomago = str(input("O que o macaco ira comer? "))
        print(f'Sucesso, o macaco comeu {self.estomago}')

mamaco = macaco('Simba')