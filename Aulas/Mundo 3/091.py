from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('Valores sorteados')
rank = []
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
print('=' * 30)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)#o itemgetter vai ser responsavel por permitr uma organização de forma mais facil, ele ira pegar os dados do dicionario, e utiliza-los de forma organizada
for i, v in enumerate(rank):
    print(f'{i+1}° o lugar: {v[0]} com {v[1]}')
