'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class pessoa():
    def __init__(self, nome=str, idade=int, peso=float, altura=float):
        """[__init__]

        Args:
            nome ([str]): [Nome]
            idade ([int]): [Idade]
            peso ([float]): [Peso]
            altura ([float]): [Altura]
        """
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):       
        self.idade += int(input("Deseja envelhecer quantos anos? "))
        if self.idade < 21:
            self.altura += 0.5
        return (f"A nova idade de {self.nome} é {self.idade}")
    
    def engordar(self):
        self.peso += float(input("Deseja engordar quantos kg? "))
        return (f"O novo peso de {self.nome} é {self.peso} kg")

    def emagrecer(self):
        self.peso -= float(input("Deseja emagrecer quantos kg? "))
        return (f"O novo peso de {self.nome} é {self.peso} kg")
    
    def creser(self):
        altura = float(input("Deseja aumentar a altura em quantos cm? "))
        if len(str(altura)) == 4:
            self.altura += altura / 100
        elif len(str(altura)) == 3:
            self.altura += altura / 100
        return (f"A nova altura de {self.nome} é {self.altura}")
    
p1 = pessoa("João", 15, 47.0, 1.67)