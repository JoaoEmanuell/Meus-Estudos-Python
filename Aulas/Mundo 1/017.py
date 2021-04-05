from math import floor, ceil
num = float(input('\033[1;31mQual é o valor do cateto oposto? \033[m'))
numm = float(input('\033[1;32mQual é o valor do cateto adjacente? \033[m'))
hip = (num + numm)
arr = floor(hip)
arb = ceil(hip)
print('O valor do cateo oposto é \033[1;31m{}\033[m, ja o cateto adjacente é \033[1;32m{}\033[m portanto o valor da hipotenusa sera \033[1;35m{:.3}!\033[m'.format(num,numm,hip))
print('arredondado de forma absoluta sera \033[1;36m{}\033[m e de forma positiva sera \033[1;33m{}\033[m'.format(arr,arb))