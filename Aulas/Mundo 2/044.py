print('\033[1;37mLoja careira onde tudo é pela metade do dobro\033[m')
compras = float(input('\033[1;31mQual foi o valor das compras? \033[m'))
print('''\033[1;31mFormas de pagamento\033[m
\033[1;32m [ 1 ] Á vista dinheiro/cheque\033[m
 \033[1;33m[ 2 ] Á vista no cartão\033[m
 \033[1;34m[ 3 ] Em até 2x no cartão\033[m
 \033[1;35m[ 4 ] 3x ou mais no cartão''')
fmp = int(input('\033[1;31mQual a forma de pagamento? \033[m'))
if fmp == 1:
    fmp1 = compras - (compras / 100) * 10
    print('\033[1;32mO valor das compras foi de\033[m \033[1;31m{}\033[m \033[1;32mreais!\033[m'.format(fmp1))
elif fmp == 2:
    fmp2 = compras - (compras / 100) * 5
    print('\033[1;33mO valor das compras foi de \033[m \033[1;31m{}\033[m \033[1;33mreais!\033[m'.format(fmp2))
elif fmp == 3:
    fmp3 = compras / 2
    print('\033[1;34mO valor sera 2 parcelas de \033[1;31m{}\033[m \033[1;34mreais sem juros!\033[m'.format(fmp3))
elif fmp == 4:
    par = int(input('\033[1;31mQuantas parcelas? \033[m'))
    fmp4 = compras - (compras / 100) * 30
    fmp5 = fmp4 / par
    print('\033[1;35mO valor sera \033[1;31m{}\033[m \033[1;35mparcelas de \033[m\033[1;31m{}\033[m \033[1;35mreais com juros!\033[m'.format(par, fmp5))
else:
    print('\033[1;31mErro, {} não é uma opçaõ valida, tente novamente\033[m'.format(fmp))