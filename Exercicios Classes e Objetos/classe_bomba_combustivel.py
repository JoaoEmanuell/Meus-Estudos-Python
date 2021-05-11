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
        self.combustivel = tipoCombustivel
        self.preço = valorLitro
        self.quantidade = quantidadeCombustivel
    
    def abastecerPorValor(self):
        valor = float(input(f"Quantos reais de {self.combustivel} você deseja abastecer? "))
        tot = valor / self.preço
        if tot > self.quantidade:
            print(f"Desculpe, mas a bomba não tem {self.combustivel} o suficiente")
            return(False)
        else:
            print(f"Sucesso, você abasteceu {tot} litros de {self.combustivel}")
            return(tot)
    
    def abastecerPorLitro(self):
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
        self.preço = float(input(f"Qual o novo preço por litro de {self.combustivel}? R$ "))
        print(f"Sucesso, o novo preço de {self.combustivel} é {self.preço} reais por litro")
        return(self.preço)

    def alterarCombustivel(self):
        self.combustivel = str(input(f"Qual é o novo tipo de combustivel? "))
        print(f"Sucesso, o novo combustivel é {self.combustivel}")
        return(self.combustivel)
    
    def alterarQuantidadeCombustivel(self):
        pass   
        
posto = bomba()

posto.alterarCombustivel()