from uteis import numbers
n = float(input('Digite o preço '))
print(f'A metade de {numbers.coin(n)} é {numbers.coin(numbers.half(n))}')
print(f'O dobro de {numbers.coin(n)} é {numbers.coin(numbers.double(n))}')
print(f'Aumentado 10% de {numbers.coin(n)} teremos {numbers.coin(numbers.positive_percentage(n, 10))}')
