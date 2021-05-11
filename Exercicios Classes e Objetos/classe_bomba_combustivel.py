"""
[10 - 
    Faça um programa completo utilizando classes e métodos que:
a - Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
    i   - tipoCombustivel.
    ii  - valorLitro
    iii - quantidadeCombustivel
    
b - Possua no mínimo esses métodos:
    i   -  abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
    ii  -  abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
    iii -  alterarValor( ) – altera o valor do litro do combustível.
    iv  -  alterarCombustivel( ) – altera o tipo do combustível.
    v   - alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
    OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.]
"""
    
class bomba:
    def __init__(self, tipoCombustivel = 'Gasolina', valorLitro = 5.0, quantidadeCombustivel = 100.0):
        """[init]

        Args:
            tipoCombustivel (str, optional): [Nome do tipo de combustivel]. Defaults to 'Gasolina'.
            valorLitro (float, optional): [valor por litro do combustivel]. Defaults to 5.0.
            quantidadeCombustivel (float, optional): [Quantidade total de combustivel que a bomba contém]. Defaults to 100.0.
        """        
        self.combustivel = tipoCombustivel
        self.preço = valorLitro
        self.quantidade = quantidadeCombustivel
    
    def abastecerPorValor(self):
        """[abastecer por valor, você passa o valor de combustivel que deseja abastecer, a função converte em litros, caso a quantidade que você deseja abastecer for superior a quantidade da bomba, a função retorna um erro, caso seja suficiente ela retorna o total de combustivel que você abasteceu no seu carro]
        """        
        valor = float(input(f"Quantos reais de {self.combustivel} você deseja abastecer? "))
        tot = valor / self.preço
        if tot > self.quantidade:
            print(f"Desculpe, mas a bomba não tem {self.combustivel} o suficiente")
            return(False)
        else:
            print(f"Sucesso, você abasteceu {tot} litros de {self.combustivel}")
            return(tot)
    
    def abastecerPorLitro(self):
        """[abastecer por litro, você insere quantos litros de combustivel você deseja abastecer, a função calcula o valor que irar ficar, caso a bomba não tenha combustivel o suficiente ela ira retornar False, caso tenha ele ira retornar o valor em Reais do quanto você abasteceu]
        """        
        quantidade = float(input(f"Quantos litros de {self.combustivel} você deseja abastecer? "))
        tot = quantidade * self.preço
        valor = quantidade * self.preço
        if quantidade > self.quantidade:
            print(f"Desculpe, mas a bomba não tem {self.combustivel} o suficiente")
            return(False)
        else:
            print(f"Sucesso, você abasteceu {quantidade} litros de {self.combustivel}, o preço fica em {valor} reais")
            return(valor)

    def alterarValor(self):
        """[altear Valor, você inseri o novo preço do combustivel, dessa forma ele ira alterar o valor do mesmo, retorna o preço novo]
        """        
        self.preço = float(input(f"Qual o novo preço por litro de {self.combustivel}? R$ "))
        print(f"Sucesso, o novo preço de {self.combustivel} é {self.preço} reais por litro")
        return(self.preço)

    def alterarCombustivel(self):
        """[alterar combustivel, você insere qual é o novo tipo de combustivel, então o progama ira alterar o combustivel para o nome que você inseriu, retorna o novo tipo de combustivel]
        """        
        self.combustivel = str(input("Qual é o novo tipo de combustivel? "))
        print(f"Sucesso, o novo combustivel é {self.combustivel}")
        return(self.combustivel)
    
    def alterarQuantidadeCombustivel(self):
        """[alterar Quantidade Combustivel, serve para alterar a quantidade de combustivel que existe dentro da bomba, você insere a nova quanatidade em litros e ele ira alterar a quantidade total, retorna a nova quanidade de combustivel]
        """        
        self.quantidade = float(input(f"Qual é a nova quantidade em litros de {self.combustivel}? "))
        print(f"Sucesso, a nova quantidade de {self.combustivel} é {self.quantidade} litros")
        return(self.quantidade)
    
posto = bomba()

posto.alterarQuantidadeCombustivel()