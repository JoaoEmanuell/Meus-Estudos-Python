print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:#enquanto a variavel mais for diferente de 0 ele continua rodando
    total = total + mais#aqui ele vai pegar o total e somar com mais
    while cont <= total:#aqui ele vai rodar enqunato cont for igual ou inferior ao total
        print('{} '.format(termo),end='')
        termo += razao
        cont += 1#conta os termos
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Foram exibidos {} termos'.format(cont))
