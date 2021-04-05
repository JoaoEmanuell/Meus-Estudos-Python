def ano(n=0):
    from datetime import date#ao fazer a importação somente durante a execução da função, vc economiza memoria
    idade = date.today().year - n
    if idade >= 18 and idade <= 70:
        return (f'Com {idade} anos o voto é \033[1:31mOBRIGATORIO\033[m')
    if idade >= 16 and idade <= 17 or idade >= 65:
        return (f'Com {idade} anos o voto é \033[1:31mOPCIONAL\033[m')
    if idade <= 15:
        return (f'Com {idade} anos \033[1:31mNão\033[m vota')


i = int(input('Em que ano você nasceu? '))
print(ano(i))
