"""
7 - Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade.
Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""

class bichinho():
    """[Classe bixinho, essa classe possui 6 metodos e um __init__]
    """    
    def __init__(self, nome, fome = 10, saude = 100, idade = 1):
        """[Inicia a classe]

        Args:
            nome ([str]): [Nome do bichinho]
            fome (int, optional): [Porcentagem da fome do bichinho]. Defaults to 10.
            saude (int, optional): [Porcentagem da saude do bichinho]. Defaults to 100.
            idade (int, optional): [Idade do bichinho]. Defaults to 1.
        """  
              
        self.nome = nome

        self.fome = fome

        self.saude = saude

        self.idade = idade


    def status(self):
        """[Descreve o status do bichinho]

        Returns:
            [str]: [Retorna o estado do bichinho]
        """        
        print (f"O nome do bichinho é {self.nome}\nA fome de {self.nome} está em {self.fome}%\nA saúde de {self.nome} está em {self.saude}%\nA idade de {self.nome} é {self.idade} anos")
        
        bichinho.novo_humor()
        
        return (f"O nome do bichinho é {self.nome}\nA fome de {self.nome} está em {self.fome}%\nA saúde de {self.nome} está em {self.saude}%\nA idade de {self.nome} é {self.idade} anos")
    
    def alterar_nome(self):
        """[função para alterar o nome do bichinho]

        Returns:
            [str]: [Retorna o novo nome do bichinho]
        """        
        self.nome = str(input("Qual o novo nome do bichinho? "))
        
        print (f"O novo nome do bichinho é {self.nome}")
        
        bichinho.novo_humor()
        
        return (f"O novo nome do bichinho é {self.nome}")
    
    def alterar_fome(self):
        """[função para alterar a fome do bichinho]

        Returns:
            [str]: [Retorna a porcentagem da fome do bichinho]
        """        
        self.fome = abs(int(input(f"Qual a nova porcentagem de fome de {self.nome}? ")))
        
        print (f"A fome de {self.nome} está em {self.fome}%")
        
        bichinho.novo_humor()
        
        return (f"A fome de {self.nome} está em {self.fome}%")
    
    def alterar_saude(self):
        """[função para alterar a saúde do bichinho]

        Returns:
            [str]: [Retorna a porcentagem da saúde do bichinho]
        """        
        self.saude = abs(int(input(f"Qual a nova porcentagem de saude de {self.nome}? ")))
        
        print (f"A saúde de {self.nome} está em {self.saude}%")
        
        bichinho.novo_humor()
        
        return (f"A saúde de {self.nome} está em {self.saude}%")
    
    def alterar_idade(self):
        """[Função para alterar a idade do bichinho]

        Returns:
            [str]: [Idade do bichinho]
        """        
        self.idade = abs(int(input(f"Qual a nova idade de {self.nome}? ")))
        
        print (f"A idade de {self.nome} é {self.idade} anos")
        
        bichinho.novo_humor()
        
        return (f"A idade de {self.nome} é {self.idade} anos")

    def novo_humor(self):
        """
        [Serve para calcular o humor do bichinho, baseado na sua fome e saúde]
        """        
        if self.fome > 75 or self.saude < 25:
            self.humor = print(f'{self.nome} está Irritado')
        
        elif self.fome > 50 or self.saude < 50:
            self.humor = print(f'{self.nome} está Triste')
        
        elif self.fome > 25 or self.saude < 75:
            self.humor = print(f'{self.nome} está Feliz')
        
        else:
            self.humor = print(f'{self.nome} está Muito feliz')

bichinho = bichinho("Midas")

bichinho.status()