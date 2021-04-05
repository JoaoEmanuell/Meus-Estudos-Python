frase = str(input('\033[1;31mDigite uma frase \033[m')).strip().upper()
print('A letra A aparece \033[1;32m{}\033[m vezes'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição \033[1;33m{}\033[m'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez na posição \033[1;34m{}\033[m'.format(frase.rfind('A')+1))
