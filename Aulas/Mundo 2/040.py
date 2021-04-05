m1 = float(input('\033[1;31mPrimeira media \033[m'))
m2 = float(input('\033[1;32mSegunda media \033[m'))
mf = (m1 + m2) / 2
if mf < 5.0:
    print('O aluno esta \033[1;31mreprovado\033[m, sua media foi de \033[1;32m{}\033[m!'.format(mf))
elif mf >= 5.0 and mf < 6.9:
    print('O aluno esta em recuperação sua media foi de \033[1;32m{}\033[m!'.format(mf))
else:
    print('O aluno está aprovado, sua media foi \033[1;35m{}\033[m!'.format(mf))
