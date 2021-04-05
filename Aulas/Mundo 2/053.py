frase = str(input('\033[1;31mDigite uma frase \033[m')).strip().upper()
palavra = frase.split() #split serve para separa a frase em palavras
junto = ''.join(palavra) #join serve para juntar a frase, nesse caso ele junta sem espaços
inverso = ''
for letra in range(len(junto) -1, -1, -1): #letra é uma variavel para saber as letras, os numeros vão da primeira letra ate a ultima invertendo a frase
    inverso += junto[letra] #esse comando pega as letras da frase e inverte elas
if inverso == junto:
    print('{} escrita de trâs para frente é {}'.format(frase, inverso))
    print('Por tanto a sua frase é um palíndromo')
else:
    print('{} escrita de trâs para frente é {}'.format(frase, inverso))
    print('Por tanto a sua frase não é um palíndromo')
