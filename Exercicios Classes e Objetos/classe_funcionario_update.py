"""[14 - Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.]
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
    
    def aumentar_salario(self, aumento = 10):
        """[função para aumentar o salario do funcionario]

        Args:
            aumento (int, optional): [Porcentagem de aumento que sera adicionada ao salario]. Defaults to 10.
        """        
        self.salario += (self.salario / 100) * aumento
        print(f"O salario de {self.nome} é {self.salario} reais")
        return(self.salario)
        
fun = funcionario('Apolo')

fun.nome_funcionario()

fun.salario_funcionario()

fun.aumentar_salario()