from random import shuffle
a1 = input('\033[1;31mNome do primeiro aluno \033[m')
a2 = input('\033[1;32mNome do segundo aluno \033[m')
a3 = input('\033[1;33mNome do terceiro aluno \033[m')
a4 = input('\033[1;34mNome do quarto aluno \033[m')
lista = [a1,a2,a3,a4]
shuffle(lista)
print('\033[1;35mA ordem de apresentação sera:\033[m')
print(lista)