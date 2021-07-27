def criptografador(texto):
    """[Encryptor, serves to encrypt the string that was passed to it.]

      Args:
          text ([str]): [text that should be passed to it]
      Return:
         convert ([list]): [List with converted text]
    """    
    if texto == '':
        texto = str(input('Digite o texto: '))
    def grupo3(l, a, b, c, a1, b1, c1):
            """[internal function to make writing the code easier and make it consume less]

             Args:
                 l ([str]): [current character]
                 a ([str]): [character 1 of the conversion code]
                 b ([str]): [character 2 of the conversion code]
                 c ([str]): [character 3 of the conversion code]
                 a1 ([int]): [conversion code number 1]
                 b1 ([int]): [conversion code number 2]
                 c1 ([int]): [conversion code number 3]
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
                 l ([str]): [current character]
                 a ([str]): [character 1 of the conversion code]
                 b ([str]): [character 2 of the conversion code]
                 c ([str]): [character 3 of the conversion code]
                 d ([str]): [character 4 of the conversion code]
                 a1 ([int]): [conversion code number 1]
                 b1 ([int]): [conversion code number 2]
                 c1 ([int]): [conversion code number 3]
                 d1 ([int]): [conversion code number 4]
             """            
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
        elif (l == '!' or l == '.' or l == '-' or l == '_' or l == '?'):
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
            #print(f'Erro, caractere "{l}" não é conhecido!')
            pass
    return(conver)