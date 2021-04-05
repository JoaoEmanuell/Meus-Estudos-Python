n = int(input('Numero '))
c = n
f = 1#vai servir pra calcular o fatorial
while c > 0:
    print('{}'.format(c), end=' ')
    print(' X ' if c > 1 else ' = ', end=' ')
    f *= c #vai pegar o valor de 1 e multiplicar por c
    c -= 1
print(f)
