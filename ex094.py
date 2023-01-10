pessoas = list()
pessoa = {'nome': '',
          'genero': '',
          'idade': ''
          }
idades = []
mulheres = []
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['genero'] = str(input('Genero: [M/F] '))
    if pessoa['genero'] not in 'MmFf':
        print('ERRO! Responda apenas M ou F.')
        pessoa['genero'] = str(input('Genero: [M/F] '))
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    idades.append(pessoa['idade'])
    if pessoa['genero'] in 'Ff':
        mulheres.append(pessoa['nome'])
    pessoa.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp not in 'SsNn':
        print('ERRO! Responda apenas S ou N')
        resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 20)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas. ')
media = sum(idades) / len(pessoas)
print(f'B) A média de idade é de {media:.0f} anos')
print(f'C) As mulheres cadastradas foram {mulheres}')
print('D) Pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] > media:
        print('    ', p)
