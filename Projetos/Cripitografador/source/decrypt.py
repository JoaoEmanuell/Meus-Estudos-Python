from re import sub
def descriptografador(texto):
    """[Function for decrypt a text generated by cript]

    Args:
        texto ([str]): [text for decrypt]

    Returns:
        [str]: [text decrypt]
    """    

    # Text is empty?
    if texto == '':
        texto = input('Digite o texto: ')

    #Conversão da str para lista
    tmp = []
    na = 0
    ntmp = 0
    for i in texto:
        if i == '[' or i == ']':
            pass
        try:
            ntmp = int(str(ntmp) + str(i)) # Concatenation
        except ValueError:
            if i == ',':
                tmp.append(ntmp) # add
                ntmp = 0 # Concatenation reset
            elif i == ' ': # Space verification
                pass
            else: # Add a special character
                tmp.append(str(i))
        if i == "'" and na != 1: # Space text verification
            tmp.append('')
            na += 1
        elif na == 1:
            na = 0

    tmp.append(ntmp) # Final add
    texto = tmp # Text = list
    def grupo3(l, a, b, c, a1, b1, c1):
            """[internal function to make writing the code easier and make it consume less]

            Args:
                l ([int or str]): [current character]
                a ([int]): [number 1 of the conversion code]
                b ([int]): [number 2 of the conversion code]
                c ([int]): [number 3 of the conversion code]
                a1 ([str]): [conversion code character 1]
                b1 ([str]): [conversion code character 2]
                c1 ([str]): [conversion code character 3]
            """        
            if (l == a):
                return(a1)
            elif(l == b):
                return(b1)
            else:
                return(c1)
    def grupo4(l, a, b, c, d, a1, b1, c1, d1):
            """[internal function to make writing the code easier and make it consume less]

            Args:
                l ([int or str]): [current character]
                a ([int]): [number 1 of the conversion code]
                b ([int]): [number 2 of the conversion code]
                c ([int]): [number 3 of the conversion code]
                d ([int]): [number 4 of the conversion code]
                a1 ([str]): [conversion code character 1]
                b1 ([str]): [conversion code character 2]
                c1 ([str]): [conversion code character 3]
                d1 ([str]): [conversion code character 4]
            """      
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
    conver = sub(' {2,}', ' ', conver).strip(' ')
    #return a str 
    return conver