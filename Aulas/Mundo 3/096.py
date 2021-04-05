def area(a, b):
    s = a * b
    print(f'A aréa de um terreno de {a} x {b} é de {s}m²')


def linha(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


linha('  Controle de terrenos  ')
l = float(input('Largura do terreno '))
c = float(input('Comprimento do terreno '))
area(l, c)
