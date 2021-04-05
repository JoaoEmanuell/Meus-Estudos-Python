num = int(input('\033[1;31mMe diga um número \033[m'))
resultado = num % 2
par = (0)
impar = (1)
if resultado == impar:
    print('\033[1;32mO número\033[m \033[1;31m{}\033[m \033[1;34mé impar\033[m'.format(num))
else:
    print('\033[1;33mO número\033[m \033[1;31m{}\033[m \033[1;34mé par\033[m'.format(num))