val = []#lista vazia
fim = ' '#fim é definido como str com um espaço
while True:
    pergunta = (int(input('Digite um valor: ')))#aqui temos uma pergunta
    if pergunta not in val:#se o valor de pergunta não estiver na lista
        val.append(pergunta)#adicione o valor de pergunta a lista
    else:#se não
        print('Numero duplicado, não ira ser adicionado')#escreva 'numero duplicado' esse numero não sera adicionado
    while fim not in 'SsNn':#enquanto fim não tiver uma resposta como 'SsNn' repita
        fim = str(input('Deseja Finalizar? '))[0].upper()#pergunta fim
    if fim in 'Ss':#se dentro de fim tiver 'Ss'
        break#encerre
    fim = ' '#fim retorna a uma str com um espaço
print(sorted(val))#escreva a lista em ordem numerica
