from time import sleep

def tempo(t):
    """[Função para contar o tempo, serve como o nome já diz para contar o tempo que você irar passar]

    Args:
        t ([int]): [Minutos que o contandor passara contando]
    """    
    minutos = int(t)
    segundos = 60
    while True:
        texto = '{:02d}:{:02d}'.format(minutos, segundos)
        if minutos < 0:
            break
        elif segundos == 60:
            minutos -= 1
            segundos -= 1
        elif segundos == 0:
            segundos = 60
        else:
            segundos -= 1
        print(texto, end = "\r")
        sleep(0.15)

t = tempo(1)