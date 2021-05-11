    """[10 - 
    Faça um programa completo utilizando classes e métodos que:
a - Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
    i   - tipoCombustivel.
    ii  - valorLitro
    iii - quantidadeCombustivel
    
b - Possua no mínimo esses métodos:
    i   -  abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
    ii  -  abastecerPorLitro( ) – método onde é informado a quantidade em litros de    combustível e mostra o valor a ser pago pelo cliente.
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