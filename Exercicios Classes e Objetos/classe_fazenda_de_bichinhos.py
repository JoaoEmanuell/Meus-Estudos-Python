"""17 - [Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.]
"""
from random import randint

class bichinho():
    """[Classe bixinho, essa classe possui 6 metodos e um __init__]
    """    
    def __init__(self, nome, fome = randint(1, 100), saude = randint(1, 100), idade = randint(1, 5), humor = 100):
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
        self.brincarr = humor

    def status(self):
        """[Descreve o status do bichinho]

        Returns:
            [str]: [Retorna o estado do bichinho]
        """        
        print (f"O nome do bichinho é {self.nome}\nA fome de {self.nome} está em {self.fome}%\nA saúde de {self.nome} está em {self.saude}%\nA idade de {self.nome} é {self.idade} anos")
        
        bichinho.novo_humor(self)
        
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
        if self.fome > 75 or self.saude < 25 or self.brincarr < 2:
            self.humor = print(f'{self.nome} está Irritado')
        
        elif self.fome > 50 or self.saude < 50 or self.brincarr < 5:
            self.humor = print(f'{self.nome} está Triste')
        
        elif self.fome > 25 or self.saude < 75 or self.brincarr < 10:
            self.humor = print(f'{self.nome} está Feliz')
        
        else:
            self.humor = print(f'{self.nome} está Muito feliz')

    def brincar(self):
        """[Serve para informar quanto tempo você deseja brincar com o bichinho]
        """        
        tempo = abs(float(input(f"Por quanto minutos deseja brincar com {self.nome}? ")))
        self.brincarr = tempo
        return self.brincarr

class bichinho2(bichinho):
    pass
class bichinho3(bichinho):
    pass

Midas = bichinho("Midas")
Miriel = bichinho2("Miriel")
Asriel = bichinho3("Asriel")

Midas.status()
Miriel.status()
Asriel.status()