aluno = {}
aluno['nome'] = str(input('Qual é o nome do aluno? ')).capitalize().strip()
aluno['nota'] = float(input('Qual é a media do aluno? '))
print(f'\nO nome do aluno é {aluno["nome"]}')
print(f'A media do aluno é {aluno["nota"]}')
if aluno['nota'] <= 6.9:
    print(f'{aluno["nome"]} está em recuperação')
else:
    print(f'{aluno["nome"]} está passado por media')
