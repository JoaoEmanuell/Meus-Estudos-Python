from datetime import date
ano = int(input('\033[1;31mQual ano você quer analisar? Coloque 0 para o ano atual \033[m'))
if ano == 0:
    ano = date.today().year # a biblioteca datetime serve para eu contabilizar dias, o comando diz: dia do ano de hj, no caso 2021
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #o sinal '' != '' quer dizer diferente, and = e, or = ou
    print('O ano \033[31m{}\033[m é bixessto'.format(ano))
else:
    print('O ano \033[31m{}\033[m não é bixessto'.format(ano))
