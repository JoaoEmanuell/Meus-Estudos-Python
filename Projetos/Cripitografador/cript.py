'''
Esse projeto se trata de um cripitografador de mensagens, nos teclados de celulares antigos, temos que teclar mais de uma vez uma tecla para que a letra desejada apareça, cada tecla possui um número, portanto o criptiografador ira fazer a conversão da string desejada para o número que corresponde a ela.

2 | a = 2; b = 22; c = 222;
3 | d = 3; e = 33; f = 333;
4 | g = 4; h = 44; i = 444;
5 | j = 5; k = 55; l = 555;
6 | m = 6; n = 66; o = 666;
7 | p = 7; q = 77; r = 777; s = 7777;
8 | t = 8; u = 88; v = 888;
9 | w = 9; x = 99; y = 999; z = 9999;
'''

texto = 'Oi, tudo bem?'
def criptiografador(texto):
    def grupo3(l, a, b, c, a1, b1, c1):
            if (l == a):
                return(a1)
            elif(l == b):
                return(b1)
            else:
                return(c1)
    def grupo4(l, a, b, c, d, a1, b1, c1, d1):
            if (l == a):
                return(a1)
            elif(l == b):
                return(b1)
            elif(l == c):
                return(c1)
            else:
                return(c1)
    txt = texto.lower()
    conver = []
    for l in txt:
    #Grupo dos 2
        if (l == 'a' or l == 'b' or l == 'c'):
            conver.append(grupo3(l, 'a', 'b', 'c', 2, 22, 222))
    #Grupo dos 3
        elif (l == 'd' or l == 'e' or l == 'f'):
            conver.append(grupo3(l, 'd', 'e', 'f', 3, 33, 333))
    #Grupo dos 4
        elif (l == 'g' or l == 'h' or l == 'i'):
            conver.append(grupo3(l, 'g', 'h', 'i', 4, 44, 444))
    #Grupo dos 5
        elif (l == 'j' or l == 'k' or l == 'l'):
            conver.append(grupo3(l, 'j', 'k', 'l', 5, 55, 555))
    #Grupo dos 6
        elif (l == 'm' or l == 'n' or l == 'o'):
            conver.append(grupo3(l, 'm', 'n', 'o', 6, 66, 666))
    #Grupo dos 7
        elif (l == 'p' or l == 'q' or l == 'r' or l == 's'):
            conver.append(grupo4(l, 'p', 'q', 'r', 's', 7, 77, 777, 7777))
    #Grupo dos 8
        elif (l == 't' or l == 'u' or l == 'v'):
            conver.append(grupo3(l, 't', 'u', 'v', 8, 88, 888))
    #Grupo dos 9
        elif (l == 'w' or l == 'x' or l == 'y' or l == 'z'):
            conver.append(grupo4(l, 'w', 'x', 'y', 'z', 9, 99, 999, 9999))
    #Espaços
        elif (l == ' '):
            conver.append('')
    #Caracteres especiais
        elif (l == ',' or l == '!' or l == '.' or l == '-' or l == '_' or l == '?'):
            if (l == ','):
                conver.append(',')
            elif (l == '!'):
                conver.append('!')
            elif (l == '.'):
                conver.append('.')
            elif (l == '-'):
                conver.append('-')
            elif (l == '_'):
                conver.append('_')
            elif (l == '?'):
                conver.append('?')
    #Erro
        else:
            print('Erro')
    return(conver)

print(criptiografador(texto))