from datetime import date
ano = date.today().year
velhas = 0
novas = 0
for c in range(1, 8):
    cont = 0
    pergunta = int(input(f'Em que ano a {c}° pessoa nasceu? ').format(cont))
    idade = ano - pergunta
    if 18 > idade:
        novas = novas + 1
    elif idade == 18:
        velhas = velhas + 1
    elif idade > 18:
        velhas = velhas + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(velhas))
print('E tambem tivemos {} pesosas menores de idade'.format(novas))
