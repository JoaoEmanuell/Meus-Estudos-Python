v1 = float(input('\033[1;31mQual é o primeiro valor?\033[m '))
v2 = float(input('\033[1;32mQual é o segundo valor?\033[m '))
if v1 > v2:
    print('O valor \033[1;31m{}\033[m é maior que \033[1;32m{}\033[m!'.format(v1, v2))
elif v2 > v1:
    print('O valor \033[1;32m{}\033[m é maior que \033[1;31m{}\033[m!'.format(v2, v1))
else:
    print('O valor \033[1;31m{}\033[m é igual ao valor \033[1;32m{}\033[m'.format(v1, v2))
