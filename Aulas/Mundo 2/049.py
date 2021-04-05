num = int(input('\033[1;31mDigite um numero \033[m'))
for c in range(1, 11):
    print('\033[1;32m{}\033[m x \033[1;33m{}\033[m = \033[1;34m{}\033[m'.format(num, c, num*c))
