maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Qual o peso da {p}° pessoa? ')) #lembre de colocar a variavel igual a de baixo
    if p == 1:
        maior = peso #igual a essa aqui
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}kg'.format(maior))
print('O menor peso foi de {}kg'.format(menor))
