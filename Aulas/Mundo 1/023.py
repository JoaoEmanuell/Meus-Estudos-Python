from time import sleep
num = int(input('\033[1;31mDigite um numero de ate 4 digitos\033[m'))
print('Analisando o numero \033[1;32m{}\033[m'.format(num))
sleep(3.0)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[1;33mUnidade {}\033[m'.format(u))
print('\033[1;34mDezena {}\033[m'.format(d))
print('\033[1;35mCentena {}\033[m'.format(c))
print('\033[1;36mMilhar {}\033[m'.format(m))
