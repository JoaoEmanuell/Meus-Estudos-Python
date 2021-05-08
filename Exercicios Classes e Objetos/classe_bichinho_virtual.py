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
        return (f"O nome do bichinho é {self.nome}A fome de {self.nome} está em {self.fome}%\nA saúde de {self.nome} está em {self.saude}%\nA idade de {self.nome} é {self.idade} anos")
    
    def alterar_nome(self):
        self.nome = str(input("Qual o novo nome do bichinho? "))
        return (f"O novo nome do bichinho é {self.nome}")
    
    def alterar_fome(self):
        self.fome = abs(int(input(f"Qual a nova porcentagem de fome de {self.nome}? ")))
        return (f"A fome de {self.nome} está em {self.fome}%")
    
    def alterar_saude(self):
        self.saude = abs(int(input(f"Qual a nova porcentagem de saude de {self.nome}? ")))
        return (f"A saúde de {self.nome} está em {self.saude}%")
    
    def alterar_idade(self):
        self.idade = abs(int(input(f"Qual a nova idade de {self.nome}? ")))
        return (f"A idade de {self.nome} é {self.idade} anos")
    
    
    

bichinho = bichinho("Midas")

print(bichinho.alterar_idade())