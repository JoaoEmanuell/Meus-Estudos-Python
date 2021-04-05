km = int(input('\033[1;31mA quantos km/h o carro estava andando? \033[m'))
mu = (km-80)*7.00
if km >80:
    print('Parado, você esta multado no valor de \033[1;32m{}\033[m reais'.format(mu))
else:
    print('\033[1;35mTudo bem pode passar\033[m')