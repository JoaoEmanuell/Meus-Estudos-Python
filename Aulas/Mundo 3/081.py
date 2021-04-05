lista = []
fim = ' '

while True:
    lista.append(int(input('Digite um valor ')))
    while fim not in 'SsNn':
        fim = str(input('Deseja continuar? '))[0]
    if fim in 'Nn':
        break
    fim = ' '

print('='*30)
print(f'Foram digitados {len(lista)} numeros')
print('='*30)
print(f'A lista escrita de forma reversa fica: ')
lista.sort(reverse=True)
print(lista)
print('='*30)
if lista.count(5) == True:
    print('O numero cinco está \033[1:32mpresente\033[m na lista na lista')
else:
    print('O numero cinco \033[1:31mnão\033[m está na lista')
