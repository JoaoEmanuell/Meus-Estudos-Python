somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----------{}° Pessoa ----------'.format(p))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M': #vai perguntar se a primeira pessoa é a mais velha
        maioridadehomen = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomen: #caso o contrario ele verifica dnv e adiciona o valor a pessoa
        maioridadehomen = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('Media {}'.format(mediaidade))
print('Homen mais velho é {} com a idade de {}'.format(nomevelho, maioridadehomen))
print('{} Mulheres tem menos de 20 anos'.format(totmulher20))
