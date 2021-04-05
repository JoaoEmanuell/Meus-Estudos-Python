perm = []
cont = 0
while True:
    nome = (str(input('Nome do aluno: ')).capitalize())
    n1 = (float(input('Primeira nota: ')))
    n2 = (float(input('Segunda nota: ')))
    media = n1 + n2 / 2
    fim = ' '
    perm.append([nome, [n1, n2], media])
    while fim not in 'SsNn':
        fim = str(input('Deseja continuar? '))[0].upper()
    if fim in 'N':
        fim = ' '
        break

print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
for c in perm:
    print(f'{cont:<4} {c[0]:<10} {c[2]:>8.1f}')
    cont += 1
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('fim')
        break
    else:
        print(f'Notas de {perm[opc][0]} são {perm[opc][1]}')


