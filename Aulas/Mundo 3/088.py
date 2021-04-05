from random import randint
lista = []
jogo = []
print('MEGA-SENA')
print('='*30)
quant = int(input('Quantos jogos você quer que eu sortei? '))
print('='*30)
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            tot += 1
            break

    lista.sort()
    jogo.append(lista[:])
    lista.clear()
cont = 1
for c in jogo:
    print(f'Jogo {cont}° {c}')
    print('='*30)
    cont += 1
