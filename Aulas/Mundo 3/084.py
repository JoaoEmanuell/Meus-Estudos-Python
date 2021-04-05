temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Qual é o nome da pessoa ')).capitalize())
    temp.append(int(input('Qual é o peso da pessoa ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    fim = ' '
    while fim not in 'SsNn':
        fim = str(input('Deseja continuar? ')).upper()[0]
    if fim == 'N':
        break
print(f'{len(princ)} pessoas foram cadastradas')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}, ', end='')
print(f'pesam {mai} Kg, sendo os mais pesados')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}, ', end='')
print(f'pesam {men} Kg, sendo os mais leves')
