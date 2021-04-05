from uteis import numbers
n = float(input('Digite o preço '))
print(f'A metade de {numbers.coin(n)} é {numbers.half(n, True)}')
print(f'O dobro de {numbers.coin(n)} é {numbers.double(n, True)}')
print(f'Aumentado 10% de {numbers.coin(n)} teremos {numbers.positive_percentage(n, 10, True)}')
