temp = {}
galera = []
soma = 0
while True:
    temp['nome'] = str(input('Nome da pessoa: ')).capitalize()
    while True:
        temp['sexo'] = str(input(f'Sexo de {temp["nome"]}: ')).strip().upper()
        if temp['sexo'] in 'MF':
            break
        else:
            print('Sexo invalido, por favor digite \033[1:31mM\033[m ou \033[1:31mF\033[m')
    temp['idade'] = int(input(f'Idade de {temp["nome"]}: '))
    soma += temp['idade']
    galera.append(temp.copy())
    fim = ' '
    while fim not in 'SN':
        fim = str(input('Deseja continuar? ')).strip().upper()
        if fim not in 'SN':
            print('Digite apenas \033[1:32mS\033[m ou \033[1:32mN\033[m')
    if fim in 'N':
        break
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
print()
print(f'A media das idade é de {soma / len(galera):5.2f} anos')
print()
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=', ')
print(' ')
print('\nAs pessoas com idade acima da media são: ')
for p in galera:
    if p['idade'] >= soma / len(galera):
        print('     ')
        for k, v in p.items():
            print(f' {k} = {v} ', end='')
