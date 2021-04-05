from datetime import date
ano = int(input('\033[1;31mQual é o ano de nascimento do atleta? \033[m'))
atual = date.today().year
idade = atual - ano
#Mirin
if 9 >= idade:
    print('O atleta competira na classificatoria \033[1;32mMirin\033[m pois tem \033[1;31m{}\033[m anos de idade!'.format(idade))
#Infantil
elif idade >= 10 and 14 >= idade:
    print('O atelta competira na classificatoria \033[1;33mInfantil\033[m pois tem \033[1;31m{}\033[m anos de idade!'.format(idade))
#Junior
elif idade >= 15 and 19 >= idade:
    print('O atleta competira na classificatoria \033[1;34mJunior\033[m pois tem \033[1;31m{}\033[m anos de idade!'.format(idade))
#Senior
elif idade >= 20 and 25 >= idade:
    print('O atlta competira na classificatoria \033[1;35mSênior\033[m pois tem \033[1;31m{}\033[m anos de idade'.format(idade))
#Master
else:
    print('O atleta competira na classficatoria \033[1;36mMaster\033[m pois tem \033[1;31m{}\033[m anos de idade'.format(idade))