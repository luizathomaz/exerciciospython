totalhomem = mais18 = mulhermenos20 = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    genero = str(input('Genêro: [M/F] ')).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if 'M' in genero:
        totalhomem += 1
    if idade < 20 and 'F' in genero:
        mulhermenos20 += 1
    print('-'*20)
    continuar = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if 'N' in continuar:
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {totalhomem} homens cadastrados')
print(f'E temos {mulhermenos20} mulheres com menos de 20 anos ')
