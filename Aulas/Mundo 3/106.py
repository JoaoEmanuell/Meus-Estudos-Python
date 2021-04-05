from time import sleep
c = ['\033[m',       # 0 sem cor
     '\033[0:30:41m',#red
     '\033[0:30:42m',#green
     '\033[0:30:43m',#yellow
     '\033[0:30:44m',#blue
     '\033[0:30:45m',#purple
     '\033[m']#white

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'    {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('Sistema de ajuda PyHelp', 2)
    comando = str(input('Função ou biblioteca '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
