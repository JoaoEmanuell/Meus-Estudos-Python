vu = float(input('\033[1;31mDigite o primeiro valor \033[m'))
vd = float(input('\033[1;32mDigite o segundo valor \033[m'))
vt = float(input('\033[1;33mDigite o terceiro valor \033[m'))
#menor valor
menor = vu
if vd < vu and vd < vt:
    menor = vd
if vt < vu and vt < vd:
    menor = vt
print('O menor valor digitado foi \033[1;34m{}\033[m'.format(menor))
#maior valor
maior = vu
if vd > vu and vd > vt:
    maior = vd
if vt > vu and vt > vd:
    maior = vt
print('O maior valor digitado foi \033[1;35m{}\033[m'.format(maior))