idade = fem = man = 0
while True:
    per1 = int(input('Qual é a idade da pessoa? '))
    per2 = ' '
    while per2 not in 'MF':
        per2 = str(input('Qual é o sexo da pessoa? [M/F] ')).strip().upper()[0]
    if per1 >= 18:
        idade += 1
    if per2 in 'Mm':
        man += 1
    if per2 in 'Ff' and per1 < 20:
        fem += 1
    fim = ' '
    while fim not in 'SN':
        fim = str(input('Você quer encerrar o progama? [S/N] ')).strip().upper()[0]
    if fim in 'Ss':
        break
print(f'Houveram {idade} pessoa com mais de 18 anos.')
print(f'{man} homens foram cadastrados')
print(f'{fem} mulheres tem menos de 20 anos')
