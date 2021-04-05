num = ((int(input('Digite um numero: '))), (int(input('Digite um numero: '))), (int(input('Digite um numero: '))),
(int(input('Digite um numero: '))))
print(f'Vc digitou os valores {num}')
print(f'O numero 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu pela primeira vez na {num.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
