game = {}
partidass = []
game['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {game["nome"]} jogou? '))
for c in range(0, partidas):
    partidass.append(int(input(f'      Quantos gols na partida {c} ')))
game['gols'] = partidass[:]
game['total'] = sum(partidass)#o comando sum serve para somar os numeros da lista indicada
print('=+' * 60)
print(game)
print('=+' * 60)
for k, v in game.items():
    print(f'O campo {k} tem o valor {v}')
print('=+' * 60)
print(f'O jogador {game["nome"]} jogou {len(game["gols"])} partidas')
for i, v in enumerate(game['gols']):
    print(f'Na partida {i} fez {v} gols')
print(f'Um total de {game["total"]} gols')
