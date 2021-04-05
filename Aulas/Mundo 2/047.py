from time import sleep
print('\033[1;31mNumeros pares\033[m')
for c in range(2, 51, 2):
    print(c, end=' ')
    sleep(0.25)
