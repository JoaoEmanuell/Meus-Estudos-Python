vi = float(input('\033[1;31mQual é a distancia da viagem? \033[m'))
if vi <= 200.0:
    print('O custo da viagem será \033[1;32m{}\033[m reais'.format(vi*0.50))
else:
    print('O custo da viagem será \033[1;34m{}\033[m reais'.format(vi*0.45))