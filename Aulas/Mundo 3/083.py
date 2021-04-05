expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:#para cada simbolo na expressão
    if símb == '(':#se o simbolo for um parentese abrindo
        pilha.append('(')#coloque ele na lista
    elif símb == ')':#se for um parentese fechando
        if len(pilha) > 0:#e se a quantidade de intens em pilha for maior do que 0
            pilha.pop()#delete o ultimo adicionado
    else:
        pilha.append(')')#se não, adicione um parentese fechado a pilha e encerre
        break
if len(pilha) == 0:#se a quantidade de intens a pilha for igual a 0
    print('Sua expressão está valida')
else:#se não
    print('Sua expressão está invalida')
print(pilha)
