from datetime import date
tra = {}
tra['Nome'] = str(input('Nome ')).capitalize().strip()
tra['Idade'] = int(input('Ano de nascimento '))
tra['Ctps'] = int(input('Carteira de trabalho (0 não tem) '))
tra['Idade'] = date.today().year - tra['Idade']
if tra['Ctps'] != 0:
    tra['Ano de contratação'] = int(input('Ano de contratação '))
    tra['Salário'] = float(input('Salário '))
    tra['Aposentadoria'] = tra['Idade'] + (tra['Ano de contratação'] + 35 - date.today().year)

print('=' * 30)
for k, v in tra.items():
    print(f'{k} tem o valor de {v}')
