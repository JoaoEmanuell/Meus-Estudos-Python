from time import sleep


def linha():
    print('-' * 30)


def contador(i, f, p):
    print('-' * 30)
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    print('-' * 30)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
            sleep(0.30)
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
            sleep(0.30)


contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
linha()
print('Sua vez')
linha()
i = int(input('Inicio '))
f = int(input('Fim '))
p = int(input('Passo '))
contador(i, f, p)
