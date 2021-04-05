extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = 21
end = ' '
while True:
    while num >= 21:
        num = int(input('Digite um numero entre 0 e 20 '))
        if num >= 21:
            print('Numero incorreto, por favor digite novamente')
    print(f'Você digitou o numero {extenso[num]}')
    while end not in 'SsNn':
        end = str(input('Você quer continuar? ')).strip().upper()[0]
    if 'N' in end:
        print('Fim do progama, adeus')
        break
    num = 21
    end = ' '
