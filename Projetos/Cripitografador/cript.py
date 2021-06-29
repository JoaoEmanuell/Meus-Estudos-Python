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

texto = 'Eae vei blz?'
def criptiografador(texto):
    def grupo3(l, a, b, c, a1, b1, c1):
            if (l == a):
                return(a1)
            elif(l == b):
                return(b1)
            else:
                return(c1)
    txt = texto.lower()
    conver = []
    for l in txt:
    #Grupo dos 2
        if (l == 'a' or l == 'b' or l == 'c'):
            if (l == 'a'):
                conver.append(2)
            elif(l == 'b'):
                conver.append(22)
            else:
                conver.append(222)
    #Grupo dos 3
        elif (l == 'd' or l == 'e' or l == 'f'):
            if (l == 'd'):
                conver.append(3)
            elif(l == 'e'):
                conver.append(33)
            else:
                conver.append(333)
    #Grupo dos 4
        elif (l == 'g' or l == 'h' or l == 'i'):
            if (l == 'g'):
                conver.append(4)
            elif(l == 'h'):
                conver.append(44)
            else:
                conver.append(444)
    #Grupo dos 5
        elif (l == 'j' or l == 'k' or l == 'l'):
            if (l == 'j'):
                conver.append(5)
            elif(l == 'k'):
                conver.append(55)
            else:
                conver.append(555)
    #Grupo dos 6
        elif (l == 'm' or l == 'n' or l == 'o'):
            if (l == 'm'):
                conver.append(6)
            elif(l == 'n'):
                conver.append(66)
            else:
                conver.append(666)
    #Grupo dos 7
        elif (l == 'p' or l == 'q' or l == 'r' or l == 's'):
            if (l == 'p'):
                conver.append(7)
            elif(l == 'q'):
                conver.append(77)
            elif(l == 'r'):
                conver.append(777)
            else:
                conver.append(7777)
    #Grupo dos 8
        elif (l == 't' or l == 'u' or l == 'v'):
            if (l == 't'):
                conver.append(8)
            elif(l == 'u'):
                conver.append(88)
            else:
                conver.append(888)
    #Grupo dos 9
        elif (l == 'w' or l == 'x' or l == 'y' or l == 'z'):
            if (l == 'w'):
                conver.append(9)
            elif(l == 'x'):
                conver.append(99)
            elif(l == 'y'):
                conver.append(999)
            else:
                conver.append(9999)
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