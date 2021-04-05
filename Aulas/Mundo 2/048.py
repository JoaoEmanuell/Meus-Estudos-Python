soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0: #serve para mostrar os mutiplos, nesse caso os multiplos de 3
        cont = cont + 1#isso é um contador, cada vez que um numero multiplo de 3 aparece ele adiciona um valor.
        soma = soma + c#isso é um acumulador, ela pega o valor da soma e acumula com os numeros
print('A soma entre os {} valores é igual a {}'.format(cont, soma))
