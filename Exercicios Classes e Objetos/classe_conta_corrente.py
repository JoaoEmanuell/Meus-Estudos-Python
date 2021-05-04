"""
5 - Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""

class conta():
    def __init__(self, num, corren, saldo = (0.0)):
        """[class de conta bancaria, def __init__]

        Args:
            num ([int]): [Numero da conta]
            corren ([str]): [Nome do correntista]
            saldo (tuple, float): [Numero do saldo da conta]. Defaults to (0.0).
        """           
        self.num = num
        self.corren = corren
        self.saldo = saldo
    
    def alterarnome(self):
        self.nome = str(input("Qual o novo nome do correntista? "))
        return (f"O novo nome do correntista é {self.nome}")
    
    def deposito(self):
        self.saldo += float(input("Qual o valor a ser depositado? R$ "))
        return (f"O novo saldo da conta é R$ {self.saldo}")
    
    def saque(self):
        saldo = float(input("Qual o valor a ser sacado? R$ "))
        if (self.saldo < saldo):
            return(f"Desculpe, o valor de saque que você deseja é superior ao seu saldo\n"
                   f"Seu saldo é {self.saldo}")
        else:
            self.saldo -= saldo
            return(f"Saque realizado com sucesso\n"
                   f"Seu novo saldo é {self.saldo} reais")

#codigo principal
p1 = conta(150, 'João', 1000)