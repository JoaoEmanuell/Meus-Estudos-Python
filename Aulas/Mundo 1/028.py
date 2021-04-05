from random import randint
from time import sleep #comando sleep faz o computador dar um delay para executar o proximo comando
print('\033[1;31;40mJogo das adivinhações\033[m')
print('\033[1;32mO computador sorteara um numero entre 0 a 5 e você tera que dizer qual numero é esse!\033[m')
print('\033[1;33mSorteando . . .\033[m')
num = randint(0,5)
sleep(3.0) #no caso ele conta 3 segundos e executa
cho = int(input('\033[1;34mQual foi o numero escolhido pelo computador? \033[m'))
if num == cho:
    print('\033[1;35mParabens você acertou!\033[m')
else:
    print('\033[1;36mVocê errou, mais sorte da proxima vez\033[m')
print('\033[1;37mresultado:\033[m',num)