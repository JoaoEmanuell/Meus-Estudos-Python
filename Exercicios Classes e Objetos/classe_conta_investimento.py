"""[12 - Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.]
"""

class conta_investimento:
    def __init__(self, saldo = 1000, juros = 10):
        """[init]

        Args:
            saldo (float, optional): [Saldo da conta]. Defaults to 1000.
            juros (float, optional): [Juros da conta]. Defaults to 10.
        """        
        self.saldo = saldo
        self.juros = juros
    
    def adicionarJuros(self):
        """[adiciona juros ao saldo da conta]

        Returns:
            [floa]: [retorna saldo com o juros]
        """        
        self.saldo += (self.saldo / 100) * self.juros
        print(self.saldo)
        return (self.saldo)
        
class poupança(conta_investimento):
    pass

conta = poupança()

for v in range(0, 5):
    conta.adicionarJuros()