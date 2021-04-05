lista = []
for c in range(0, 5):#repita 5 vezes
    n = int(input('Digite um valor: '))
    if c == 0:#primeiro valor
        lista.append(n)
        print('Primeiro valor adicionado')
    elif n > lista[-1]:#verifica se o ultimo valor digitado é superior ao ultimo valor da lista, usa o [-1] para saber qual é o ultimo valor da lista
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista): #enquanto a posição for inferior ao numero de intes na lista, repita
            if n <= lista[pos]:#se o numero digitado for igual ou superior a posição da lista
                lista.insert(pos, n)#coloque na lista o numero digitado antes da posição
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1

print(lista)
