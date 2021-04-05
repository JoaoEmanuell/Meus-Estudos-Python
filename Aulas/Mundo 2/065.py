maior = menor = 0
cm = 0
sm = 0
soma = 0
media = 0
cont = 0
repetidor = 'S'
while repetidor != 'N':
    soma = int(input('Digite um valor '))
    media += soma + sm
    cont += 1
    repetidor = str(input('Você deseja continuar? [S/N] ')).strip().upper()
    if cont == 1:#estrutura para saber se um numero é maior ou menor, ser contador foi igual a 1 ele excecuta
        maior = menor = soma #o primeiro numero vai ser o maior e o menor ao mesmo tempo
    else:#a parti daqui ele já executa sempre
        if soma > maior:#verifica se o num digitado agora é o maior
            maior = soma#se for ele transforma o maior no atual
        if soma < menor:#se o menor num for inferior ao digitado agora
            menor = soma#ele transforma o menor no atual
cm += media / cont
print('A media entre os valores digitados foi: {}'.format(cm))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
