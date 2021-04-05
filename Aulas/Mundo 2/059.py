'''v1 = 0
v2 = 0'''
op = 0
v1 = int(input('\033[1;31mDigite o primeiro valor: \033[m'))
v2 = int(input('\033[1;32mDigite o segundo valor: \033[m'))
while op != 5:
    print('''\033[1;33m[1] Soma\033[m
\033[1;34m[2] Subtração\033[m
\033[1;35m[3] Maior\033[m
\033[1;36m[4] Novos numeros\033[m
\033[1;37m[5] Sair do progama\033[m''')
    op = int(input(' '))
    if op == 1:
        print('\033[1;31m{}\033[m mais \033[1;32m{}\033[m é igual a \033[1;33m{}\033[m'.format(v1, v2, v1 + v2))
    elif op == 2:
        print('\033[1;31m{}\033[m menos \033[1;32m{}\033[m é igual a \033[1;34m{}\033[m'.format(v1, v2, v1 - v2))
    if op == 3:
        menor = v1
        maior = v1
        if (v2 < menor):
            menor = v2
        if (v2 > maior):
            maior = v2
        print('\033[1;31m{}\033[m é maior do que \033[1;32m{}\033[m '.format(maior, menor))
    elif op == 5:
        print('Fim do progama')
    if op == 4:
        v1 = int(input('\033[1;31mDigite o primeiro valor: \033[m'))
        v2 = int(input('\033[1;32mDigite o segundo valor: \033[m'))
        print('''
\033[1;33m[1] Soma\033[m
\033[1;34m[2] Subtração\033[m
\033[1;35m[3] Maior\033[m
\033[1;36m[4] Novos numeros\033[m
\033[1;37m[5] Sair do progama\033[m''')
        op = int(input(' '))
        if op == 1:
            print('\033[1;31m{}\033[m mais \033[1;32m{}\033[m é igual a \033[1;33m{}\033[m'.format(v1, v2, v1 + v2))
        elif op == 2:
            print('\033[1;31m{}\033[m menos \033[1;32m{}\033[m é igual a \033[1;34m{}\033[m'.format(v1, v2, v1 - v2))
        if op == 3:
            menor = v1
            maior = v1
            if (v2 < menor):
                menor = v2
            if (v2 > maior):
                maior = v2
            print('\033[1;31m{}\033[m é maior do que \033[1;32m{}\033[m '.format(maior, menor))
        elif op == 5:
            print('Fim do progama')
        else:
            print('{} não é uma opção valida, tente novamente'.format(op))
