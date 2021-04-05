jogador = {}
jogadores = []
gols = []
while True:
    jogador['nome'] = str(input('Nome do jogador '))
    par = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, par+1):
        gols.append(int(input(f'Quantos gols na partida {c} ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    fim = ' '
    while fim not in 'SsNn':
        fim = str(input('Deseja continuar? ')).upper().strip()
    if fim in 'Nn':
        break
print('=+' * 60)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    n = int(input('Codigo do jogador (999 para parar) '))
    if n == 999:
        break
    if n >= len(jogadores):
        print('Erro, não existe jogador com esse codigo')
    else:
        print(f'Levantamento do jogador {jogadores[n] ["nome"]}')
        for i, g in enumerate(jogadores[n] ['gols']):
            print(f' No jogo {i+1} fez {g} gols')
        print('=+' * 60)
