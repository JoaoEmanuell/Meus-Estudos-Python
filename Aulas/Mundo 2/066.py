n = s = c = 0
while True:
    n = int(input('Digite um numero [Digite \033[1;31m999\033[m para parar] '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Você digitou {c} valores, a soma entre eles foi de {s}')
