"""8 - Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""
    
class macaco():
    def __init__(self, nome, estomago = 'banana'):
        self.nome = nome
        self.estomago = [estomago]
    
    def comer(self):
        comida = str(input(f"O que o {self.nome} ira comer? "))
        self.estomago.append(comida)
        print(f'Sucesso, o {self.nome} comeu {comida}')
        
    def ver_estomago(self):
        atual = self.estomago
        print (f'O estomago de {self.nome} tem: ')
        for i in atual:
            print(f'{i}')


mamaco = macaco('Simba')

mamaco.ver_estomago()