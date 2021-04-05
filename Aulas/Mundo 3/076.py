lista = ('Lapis', 2.0,
         'Borracha', 3.0,
         'Caneta', 1.0)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:.2f}')
