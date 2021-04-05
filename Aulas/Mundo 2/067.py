while True:
    n = int(input('Quer ver a tabuada de qual numero? '))
    if n <= 0:
        break
    for c in range(1, 11):
        print(f'\033[1;31m{n}\033[m x \033[1;32m{c}\033[m = \033[1;33m{n*c}\033[m')
print('Fim do progama, obrigado por utilizar!')
