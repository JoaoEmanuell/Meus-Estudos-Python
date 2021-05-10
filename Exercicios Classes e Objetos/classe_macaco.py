"""8 - Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""
    
class macaco():
    """[classe que modela um macaco]
    """    
    def __init__(self, nome, estomago = 'banana'):
        """[init]

        Args:
            nome ([str]): [Nome do macaco]
            estomago (str, optional): [estomago do macaco, por padrão o macaco vem com uma banana dentro do estomago]. Defaults to 'banana'.
        """        
        self.nome = nome
        self.estomago = [estomago]
    
    def comer(self):
        """[serve para dar um alimento para o macaco, pergunte qual o alimento que o macaco ira comer, adicione ao estomago, escreva que foi um Sucesso, pergunte se o usuario quer sair.]
        """        
        while True:
            comida = str(input(f"O que o {self.nome} ira comer? "))
            self.estomago.append(comida)
            print(f'Sucesso, o {self.nome} comeu {comida}')
            fim = str(input("Sair? ")).upper()
            if fim[0] == 'S':
                break
        
    def ver_estomago(self):
        """[serve para verificar o estomago do macaco, caso o len do estomago seja 0, escreva que o estomago está vazio, senão, escreva, para cada item no estomago, escreva o item e separe por ,]
        """        
        if len(self.estomago) == 0:
            print(f'O estomago de {self.nome} está vazio')
        else:
            print (f'O estomago de {self.nome} tem: ')
            for i in self.estomago:
                print(f'{i},',end=' ')

    def digerir(self):
        """[serve para digerir os alimentos guardados no estomago, escreva, para cada item em estomago, escreva "digerindo" {item} e remova do estomago o item.]
        """        
        print('Digerindo os alimentos:')
        for i in self.estomago:
            print(f'Digerindo {i}')
            self.estomago.remove(i)

class macaco1(macaco):
    """[classe que herda as mesmas caracteristicas da classe macaco]

    Args:
        macaco ([class]): [classe macaco]
    """    
    pass

mamaco = macaco('Simba')

mamaco1 = macaco1('Julio')

mamaco1.comer()

mamaco.ver_estomago()

mamaco1.ver_estomago()