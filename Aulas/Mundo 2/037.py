num = int(input('\033[1;31mDigite um numero inteiro: \033[m'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para \033[1;32mBINÁRIO\033[m
[ 2 ] converter para \033[1;33mOCTAL\033[m
[ 3 ] converter para \033[1;34mHEXADECIMAL\033[m''')
opcao = int(input('\033[1;31mSua opção: \033[m'))
if opcao == 1:
    print('\033[1;31m{}\033[m Convertido para \033[1;32mBinário\033[m é igual a \033[1;32m{}\033[m!'.format(num, bin(num)[2:])) #o "[2:]" serve para impedir que o progama exiba o representador dele, caso o contraio o progama ira exibir "b, o codigo"
elif opcao == 2:
    print('\033[1;31m{}\033[m Convertido para \033[1;33mOctal\033[m é igual a \033[1;33m{}\033[m!'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('\033[1;31m{}\033[m Convertido para \033[1;34mHexadecimal\033[m é igual a \033[1;34m{}\033[m!'.format(num, hex(num)[2:]))
else:
    print('\033[1;31m{} Não é uma opção valida\033[m'.format(num))