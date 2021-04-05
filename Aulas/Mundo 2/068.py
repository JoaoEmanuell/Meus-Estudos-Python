from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':#serve para perguntar uma pergunta infinitamente ate que a resposta seja util para o progama
        tipo = str(input('Par ou Impar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, o total foi de {total}')
    print('Deu par' if total % 2 == 0 else 'Deu impar', end=' ')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print(f'Você ganhou!')
            v += 1
        else:
            print('Você perdeu')
            break
print(f'Você ganhou {v} vezes')
