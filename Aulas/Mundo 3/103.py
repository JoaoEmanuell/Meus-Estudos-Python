def gols(nome='Desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato')


j = str(input('Nome do jogador '))
g = str(input('Quantos gols o jogador fez? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    gols(gols=g)
else:
    gols(j, g)
