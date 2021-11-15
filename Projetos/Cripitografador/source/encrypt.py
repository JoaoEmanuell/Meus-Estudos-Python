def criptografador(texto):
    encrpty_dict = {'a' : 2, 'b' : 22, 'c' : 222, 'd' : 3, 'e' : 33, 'f' : 333, 'g' : 4, 'h' : 44, 'i' : 444, 'j' : 5, 'k' : 55, 'l' : 555, 'm' : 6, 'n' : 66, 'o' : 666, 'p' : 7, 'q' : 77, 'r' : 777, 's' : 7777, 't' : 8, 'u' : 88, 'v' : 888, 'w' : 9, 'x' : 99, 'y' : 999, 'z' : 9999}

    """[Encryptor, serves to encrypt the string that was passed to it.]

      Args:
          text ([str]): [text that should be passed to it]
      Return:
         convert ([list]): [List with converted text]
    """    
    # Text is empty?
    if texto == '':
        texto = str(input('Digite o texto: '))

    txt = texto.lower()
    conver = []
    for l in txt:
        if l in encrpty_dict:
            conver.append(int(f'{encrpty_dict[l]}'))
        elif l == ' ':
            conver.append(' ')
        else:
            conver.append(l)

    return(conver)