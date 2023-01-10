somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for i in range(1, 5):
    print('-'*5, '{}° PESSOA'.format(i), '-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    gen = str(input('Genêro [M/F]: ')).strip()
    somaidade += idade
    if i == 1 and gen in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if gen in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if gen in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é {:.1f} anos'.format(mediaidade))
print('O nome do homem mais velho é {} que tem {} anos'.format(nomevelho, maioridadehomem))
print(f'No grupo existem {totmulher20} mulheres com menos de 20 anos')
