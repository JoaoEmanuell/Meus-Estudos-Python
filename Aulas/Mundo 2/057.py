s = 'p'
fim = 'S'
m = f = 0
while fim != 'N': #enquanto fim for diferente de FIM repita
    s = str(input('Qual é o seu sexo? ')).upper().strip()
    if s == 'M':
        m += 1
    elif s == 'F':
        f += 1
    else:
        print('{} Não é um sexo valido, digite novamente'.format(s))
