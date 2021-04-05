while True:
    while True:
        try:
            i = int(input('Digite um numero inteiro '))
        except:
            print(f'Por favor digite um numero inteiro valido')
        else:
            break
    while True:
        try:
            r = float(input('Digite um numero real '))
        except:
            print(f'Por favor digite um numero real valido')
        else:
            break
    break
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
