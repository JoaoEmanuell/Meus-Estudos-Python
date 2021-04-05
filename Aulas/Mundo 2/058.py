from random import randint
from time import sleep
aleatorizador = randint(1,10)
tentativas = 0
resultado = 0
print('\033[1;31mO computador pensara em um numero entre 1 e 10, tente acertar\033[m')
print('\033[1;33mSorteando . . .\033[m')
sleep(0.50)
while resultado != aleatorizador: #repita se resultado for diferente de aleatorizador
    resultado = int(input('Qual foi o valor pensado pelo computador? '))
    if resultado != aleatorizador:
        tentativas += 1
print('\033[1;35mParabens\033[m vc ganhou, o numero pensado pelo computador foi \033[1;31m{}\033[m'.format(aleatorizador))
print('Foram nessesarias \033[1;32m{}\033[m tentativas'.format(tentativas))
