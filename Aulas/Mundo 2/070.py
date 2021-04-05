soma = somc = cont = prec = menor = contm = 0
barato = ''
while True:
    produto = str(input('Qual é o nome do produto? '))
    prec = float(input('Qual é o preço do produto? '))
    soma += prec
    contm += 1
    fim = ' '
    while fim not in 'SN':
        fim = str(input('Você deseja encerrar o progama? [S/N] ')).strip().upper()[0]
    if contm == 1 or prec < menor:
        menor = prec
        barato = produto
    if prec >= 1000:
        somc += prec
        cont += 1
    if fim in 'Ss':
        break
print(f'O valor das compras foi de {soma}')
print(f'{cont} produtos tiveram o valor superior a R$ 1000')
print(f'{barato} foi o produto mais barato')
