soma = 0
acumulador = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor '.format(c)))
    if num % 2 == 0: #serve para verificar se o numero é par ou impar, se for impar o resto é 1, se for par o resto é 0
        soma += num #serve para somar sempre um valor
        acumulador += 1 #cada vez que o if for acionado ele adiciona 1 valor
print('Você informou {} valores pares, a soma entre eles é igual a {}'.format(acumulador, soma))
