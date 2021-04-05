from random import randint
from time import sleep
intes = ('\033[1;32mPedra\033[m', '\033[1;33mPapel\033[m', '\033[1;34mTesoura\033[m')
computador = randint(0, 2)
print('''\033[1;31mSuas opções\033[m
\033[1;32m[ 0 ] Pedra\033[m
\033[1;33m[ 1 ] Papel\033[m
\033[1;34m[ 2 ] Tesoura\033[m''')
jogador = int(input('\033[1;31mQual é a sua jogada? \033[m'))
print('\033[1;32mPEDRA\033[m')
sleep(0.50)
print('\033[1;33mPAPEL\033[m')
sleep(0.50)
print('\033[1;34mTESOURA\033[m')
sleep(0.50)
print('-=' * 20) #usar ' ' a coisa que vc quer digitar e * X depois faz o progama repertir aquela coisa das aspas
print('Computador jogou {}'.format(intes[computador])) #se a variavel lista for colocada usando [] antes do sorteador, ele passa a sortear a lista
print('Jogador jogou {}'.format(intes[jogador]))
print('-=' * 20)
if computador == 0: #pedra
    if jogador == 0:
        print('\033[1;31mEMPATE\033[m')
    elif jogador == 1:
        print('\033[1;35mVITORIA DO JOGADOR\033[m')
    elif jogador == 2:
        print('\033[1;34mVITORIA DO COMPUTADOR\033[m')
elif computador == 1: #papel
    if jogador == 1:
        print('\033[1;31mEMPATE\033[m')
    elif jogador == 2:
        print('\033[1;35mVITORIA DO JOGADOR\033[m')
    elif jogador == 0:
        print('\033[1;34mVITORIA DO COMPUTADOR\033[m')
elif computador == 2: #tesoura
    if jogador == 2:
        print('\033[1;31mEMPATE\033[m')
    elif jogador == 0:
        print('\033[1;35mVITORIA DO JOGADOR\033[m')
    elif jogador == 1:
        print('\033[1;35mVITORIA DO COMPUTADOR\033[m')
