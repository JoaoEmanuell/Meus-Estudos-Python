def leia(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Porfavor digite um numero valido')
        if ok:
            break
    return n


n = leia('Digite um numero ')
print(f'Você digitou {n}')
