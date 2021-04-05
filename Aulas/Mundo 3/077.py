palavra = ('oi', 'ola', 'xau', 'chato')
for p in palavra:# para cada letra in palavra
    print(f'\nNa palavra {p.upper()} temos as vogais ',end='')
    for letra in p:#para cada letra em palavra temos
        if letra.lower() in 'aeiou':#calula quais são as vogais
            print(letra, end=' ')
