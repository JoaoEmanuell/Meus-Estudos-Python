from time import sleep
nome = str(input('\033[1;31mDigite seu nome completo \033[m')).strip()
print('\033[1;33mAnalisando seu nome...\033[m')
sleep(3)
print('Seu nome em maísculas é \033[1;32m{}\033[m'.format(nome.upper()))
print('Seu nome me minusculas é \033[1;34m{}\033[m'.format(nome.lower()))
print('Seu nome tem \033[1;36m{}\033[m letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem \033[1;37m{}\033[m letras'.format(nome.find(' ')))