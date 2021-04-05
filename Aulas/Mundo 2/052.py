num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;31m',end=' ')
        tot += 1
    else:
        print('\033[m',end=' ')
    print('{}'.format(c),end =' ')
print('\n' #isso aqui é uma quebra de linha
      '\033[mO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('Portanto o numero \033[1;31m{}\033[m é primo'.format(num))
else:
    print('Portanto o numero \033[1;31m{}\033[m não é primo'.format(num))
