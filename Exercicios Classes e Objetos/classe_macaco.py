"""8 - Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""
    
class macaco():
    def __init__(self, nome, estomago = 'banana'):
        self.nome = nome
        self.estomago = [estomago]
    
    def comer(self):
        while True:
            comida = str(input(f"O que o {self.nome} ira comer? "))
            self.estomago.append(comida)
            print(f'Sucesso, o {self.nome} comeu {comida}')
            fim = str(input("Sair? ")).upper()
            if fim[0] == 'S':
                break
        
    def ver_estomago(self):
        if len(self.estomago) == 0:
            print(f'O estomago de {self.nome} está vazio')
        else:
            print (f'O estomago de {self.nome} tem: ')
            for i in self.estomago:
                print(f'{i},',end=' ')

    def digerir(self):
        print('Digerindo os alimentos:')
        for i in self.estomago:
            print(f'Digerindo {i}')
            self.estomago.remove(i)

mamaco = macaco('Simba')

mamaco.comer()

mamaco.ver_estomago()