salario = float(input('\033[1;31mQual é o salario do funcionario? \033[m'))
if salario <= 1250.00:
    aumento = (salario/100)*15
    print('O salario com aumento passara a ser de \033[1;32m{}\033[m'.format(salario+aumento))
else:
    aumentoo = (salario/100)*10
    print('O salario com aumento passara a ser de \033[1;32m{}\033[m'.format(aumentoo+salario))