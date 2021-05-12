"""[13 - Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.]
"""

class funcionario:
    def __init__(self, nome, salario = 1000.00):
        """[init]

        Args:
            nome ([str]): [Nome do funcionario]
            salario (float, optional): [salario do funcionario]. Defaults to 1000.00.
        """        
        self.nome = nome
        self.salario = salario
        
    def nome_funcionario(self):
        """[escreve f"O nome do funcionario é {self.nome}", retorna self.nome]
        """        
        print(f"O nome do funcionario é {self.nome}")
        return(self.nome)
    
    def salario_funcionario(self):
        """[escreve f"O salario do funcionario é {self.salario} reais", retorna self.salario]
        """        
        print(f"O salario do funcionario é {self.salario} reais")
        return(self.salario)
    
fun = funcionario('Apolo')

fun.nome_funcionario()

fun.salario_funcionario()