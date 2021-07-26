def descriptografador(texto):
    if texto == []:
        texto = [input('Digite o texto ')]
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
        if (texto[l] == 2 or texto[l] == 22 or texto[l] == 222):
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

texto = []

print(descriptografador(texto))