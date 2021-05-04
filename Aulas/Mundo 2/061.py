primeiro = int(input('Primeiro termo '))
razao = int(input('Razão '))
decimo = primeiro + (10) * razao
while primeiro != decimo:
    print(f'{primeiro}', end=' ')
    primeiro += razao
print('fim')
