aluno = {'nome': str(input('Nome: ')), 'média': '', 'situação': ''}
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] > 7:
    aluno['situação'] = 'Aprovado(a)'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 15)
'''print(aluno['nome'])
print(aluno['média'])
print(aluno['situação'])
print(aluno)'''
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
