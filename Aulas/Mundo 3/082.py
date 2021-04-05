lista = []
listapar = []
listaimpar = []
fim = ' '

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)#a lista principal sempre ira receber o numero digitado
    if n % 2 == 0:#se o resto da divisão do numero por 2 for igual a 0
        listapar.append(n)#a lista par recebe o numero digitado
    else:
        listaimpar.append(n)#se não a lista impar recebe o numero digitado
    while fim not in 'SsNn':
        fim = str(input('Você deseja continuar? '))[0]
    if fim in 'Nn':
        break
    fim = ' '

print(f'A lista completa apresenta os valores {lista}\n')
print(f'Os numeros pares digitados foram {listapar}\n')
print(f'Os numeros impares digitados foram {listaimpar}\n')
