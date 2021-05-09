"""
7 - Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade.
Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""

class bichinho():
    def __init__(self, nome, fome = 10, saude = 100, idade = 1):
        self.nome = nome

        self.fome = fome

        self.saude = saude

        self.idade = idade


    def status(self):
        print (f"O nome do bichinho é {self.nome}\nA fome de {self.nome} está em {self.fome}%\nA saúde de {self.nome} está em {self.saude}%\nA idade de {self.nome} é {self.idade} anos")
        
        bichinho.novo_humor()
        
        return (f"O nome do bichinho é {self.nome}\nA fome de {self.nome} está em {self.fome}%\nA saúde de {self.nome} está em {self.saude}%\nA idade de {self.nome} é {self.idade} anos")
    
    def alterar_nome(self):
        self.nome = str(input("Qual o novo nome do bichinho? "))
        
        print (f"O novo nome do bichinho é {self.nome}")
        
        bichinho.novo_humor()
        
        return (f"O novo nome do bichinho é {self.nome}")
    
    def alterar_fome(self):
        self.fome = abs(int(input(f"Qual a nova porcentagem de fome de {self.nome}? ")))
        
        print (f"A fome de {self.nome} está em {self.fome}%")
        
        bichinho.novo_humor()
        
        return (f"A fome de {self.nome} está em {self.fome}%")
    
    def alterar_saude(self):
        self.saude = abs(int(input(f"Qual a nova porcentagem de saude de {self.nome}? ")))
        
        print (f"A saúde de {self.nome} está em {self.saude}%")
        
        bichinho.novo_humor()
        
        return (f"A saúde de {self.nome} está em {self.saude}%")
    
    def alterar_idade(self):
        self.idade = abs(int(input(f"Qual a nova idade de {self.nome}? ")))
        
        print (f"A idade de {self.nome} é {self.idade} anos")
        
        bichinho.novo_humor()
        
        return (f"A idade de {self.nome} é {self.idade} anos")

    def novo_humor(self):
        if self.fome > 75 or self.saude < 25:
            self.humor = print(f'{self.nome} está Irritado')
        
        elif self.fome > 50 or self.saude < 50:
            self.humor = print(f'{self.nome} está Triste')
        
        elif self.fome > 25 or self.saude < 75:
            self.humor = print(f'{self.nome} está Feliz')
        
        else:
            self.humor = print(f'{self.nome} está Muito feliz')

bichinho = bichinho("Midas")

bichinho.alterar_idade()