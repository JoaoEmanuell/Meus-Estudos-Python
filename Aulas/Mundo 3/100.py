from random import randint
from time import sleep


valores = []


def aleatorio():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        valores.append(randint(1, 10))
    for v in valores:
        print(f'{v}', end=' ')
        sleep(0.3)


def soma():
    pares = 0
    print(f'Somando os valores pares de {valores},', end=' ')
    sleep(1)
    for v in valores:
        if v % 2 == 0:
            pares += v

    print(f'a soma de todos os valores pares é igual a {pares}')


aleatorio()
print()
soma()
