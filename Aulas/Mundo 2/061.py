primeiro = int(input('Primeiro termo '))
razao = int(input('Razão '))
decimo = primeiro + (11 - 1) * razao
while primeiro != decimo:
    print('{}'.format(primeiro), end=' ')
    primeiro += razao
print('fim')
