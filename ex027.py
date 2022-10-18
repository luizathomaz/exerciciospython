nom = str(input('Digite o seu nome: ')).strip().split()
print('Seu primeiro nome é {}'.format(nom[0]))
print(f'Seu último nome é {nom[len(nom)-1]}')
