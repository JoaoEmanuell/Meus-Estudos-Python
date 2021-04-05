#Note que no mundo 1 e no mundo 2 existem um arquivo py com o mesmo nome, isso foi um erro na hora em que eu estava criando os arquivos, perdoem a confusão

from time import sleep
print('\033[1;31mEmprestimo casa!\033[m')
sleep(0.75)
casa = float(input('\033[1;34mQual é o valor da casa? \033[m'))
sleep(0.75)
sal = float(input('\033[1;32mQual é o valor do seu salario? \033[m'))
sleep(0.75)
ano = int(input('\033[1;33mEm quanto anos você planeja pagar a casa? \033[m'))
print('\033[1;37mCalculando . . .\033[m')
sleep(2)
prec = casa / (ano * 12)
#print('Para pagar uma casa de {:.2f} R$ em {} anos, a prestação sera de {:.2f} R$'.format(casa, ano, prec))
sall = sal * 30 / 100
if prec <= sall:
    print('\033[1;34mConseguimos aprovar o emprestimo!')
    print('\033[1;34mO valor das prestações ficara por\033[m \033[1;35m{:.2f}\033[m!'.format(prec))
#elif sall <= prec:
 #   print('Teste')
else:
    print('\033[1;31mLamentamos porem não consiguiremos financiar a sua casa :(\033[m')
