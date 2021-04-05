print('Sequencia de Fibonacci')
n = int(input('Quantos termos você quer mostrar: '))
t1 = 0#os dois primeiros termos sempre serão esses
t2 = 1
print('{} {}'.format(t1, t2), end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2#aqui ele vai somar o primeior + segundo termo e da o terceiro termo
    print('{}'.format(t3), end=' ')
    t1 = t2#aqui ele transforma o primeiro termo em segundo
    t2 = t3#e aqui ele transforma o segundo em terceiro, assim por diante ate que a sequencia
    cont += 1
print('Fim')
