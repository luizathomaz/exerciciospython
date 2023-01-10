#genero = ['M', 'F']
genero = []
while genero != 'M' and genero != 'F':
    genero = str(input('Digite seu genêro: [M/F] ')).upper()
    if genero == 'M':
        print('Certo obrigada. ')
    elif genero == 'F':
        print('Certo obrigada. ')
    else:
        print('Digite um dos genêros indicados. ')
print('fim')
