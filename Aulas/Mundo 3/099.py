from time import sleep


def lis(* lista):
    print('-' * 30)
    print('Analisando os valores informados')
    sleep(1)
    print(f'{lista} Foram informados {len(lista)} valores ao todo')
    cont = 1
    maior = menor = 0
    for valor in lista:
        if cont == 1:
            maior = menor = valor
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
        cont += 1
    sleep(1)
    print(f'O maior valor informado foi {maior}')


lis(3, 6, 9, 20)
lis(6, 9, 3, 5, 6, 9, 8, 10, 3, 6,)
lis(9, 66, 887, 9898, 363656, 21, -366)
