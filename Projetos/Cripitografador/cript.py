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

texto = 'agora indepedente do texto eu terei ele criptografado e discriptografado'
def criptografador(texto):
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
                return(d1)
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

def descriptografador(texto):
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
            elif(l == d):
                return(d1)
    conver = ''
    for l in texto:
    #Grupo dos 2
        if (l == 2 or l == 22 or l == 222):
            conver += grupo3(l, 2, 22, 222, 'a', 'b', 'c')
    #Grupo dos 3
        elif (l == 3 or l == 33 or l == 333):
            conver += grupo3(l, 3, 33, 333, 'd', 'e', 'f')
    #Grupo dos 4
        elif (l == 4 or l == 44 or l == 444):
            conver += grupo3(l, 4, 44, 444, 'g', 'h', 'i')
    #Grupo dos 5
        elif (l == 5 or l == 55 or l == 555):
            conver += grupo3(l, 5, 55, 555, 'j', 'k', 'l')
    #Grupo dos 6
        elif (l == 6 or l == 66 or l == 666):
            conver += grupo3(l, 6, 66, 666, 'm', 'n', 'o')
    #Grupo dos 7
        elif (l == 7 or l == 77 or l == 777 or l == 7777):
                conver += grupo4(l, 7, 77, 777, 7777, 'p', 'q', 'r', 's')
    #Grupo dos 8
        elif (l == 8 or l == 88 or l == 888):
            conver += grupo3(l, 8, 88, 888, 't', 'u', 'v')
    #Grupo dos 9
        elif (l == 9 or l == 99 or l == 999 or l == 9999):
                conver += grupo4(l, 9, 99, 999, 9999, 'w', 'x', 'y', 'z')
    #Espaços
        elif (l == ''):
            conver += ' '
    #Caracteres especiais
        elif (l == ',' or l == '!' or l == '.' or l == '-' or l == '_' or l == '?'):
            if (l == ','):
                conver += ','
            elif (l == '!'):
                conver += '!'
            elif (l == '.'):
                conver += '.'
            elif (l == '-'):
                conver += '-'
            elif (l == '_'):
                conver += '_'
            elif (l == '?'):
                conver += '?'
    return conver

cript = criptografador(texto)
print(descriptografador(cript))