from datetime import date #serve para importar as informações sobre a data atual, memoriza esse comando por favor cara, ele é util
atual = date.today().year #serve para pegar o ano atual
anonasci = int(input('\033[1;31mQual é o seu ano de nascimento? \033[m'))
idade = atual - anonasci #calcula a idade da pessoa
print('Quem nasceu em \033[1;31m{}\033[m terá \033[1;32m{}\033[m anos em \033[1;33m{}\033[m!'.format(anonasci, idade, atual))
if idade == 18:
    print('Você tem \033[1;31m{}\033[m anos e tera que se alistar esse ano :)'.format(idade))
elif idade < 18:
    print('Você tem \033[1;31m{}\033[m anos e tera que se alistar daqui a \033[1;32m{}\033[m anos'.format(idade, 18 - idade))
    print('O ano do seu alistamento sera em \033[1;35m{}\033[m!'.format(18 - idade + atual))
else:
    print('Você tem \033[1;31m{}\033[m anos, ja deveria ter se alistado a \033[1;35m{}\033[m anos'.format(idade, idade - 18))
    print('O ano do seu alistamento foi em \033[1;35m{}\033[m!'.format(atual - idade + 18))
