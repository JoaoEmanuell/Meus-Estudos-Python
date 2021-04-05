r1 = float(input('\033[1;31mPrimeiro segmento \033[m'))
r2 = float(input('\033[1;32mSegundo segmento \033[m'))
r3 = float(input('\033[1;33mTerceiro segmento \033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 <r1 + r2:
    print('\033[1;34mOs segmentos acima podem formar um tirangulo\033[m', end=' ') # o end serve para dizer que não tera nada no fim da linha
    if r1 == r2 == r3:
        print('\033[1;35mEquilátero!\033[m')
    elif r1 != r2 != r3 != r1: # " != " siginifica diferente
        print('\033[1;36mEscaleno!\033[m')
    else:
        print('\033[1;37mIsóceles\033[m')
else:
    print('\033[1;35mOs segmentos acima não podem formar triangulo\033[m')
