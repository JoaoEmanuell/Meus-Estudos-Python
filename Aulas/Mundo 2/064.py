nd = 0
soma = 0
sm = 0
while soma != 999:
    soma = int(input('Digite um valor '))
    nd += 1
    sm += soma
print('A quantidade de numeros digitados foi de {}'.format(nd - 1))
if 999 > sm:
    sm = 999 - sm
    print('A soma dos numeros digitados foi de {}'.format(sm))
else:
    sm = sm - 999
    print('A soma dos numeros digitados foi de {}'.format(sm))
