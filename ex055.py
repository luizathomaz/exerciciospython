maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg')
print('O menor peso lido foi  de {}kg'.format(menor))

'''maior = peso[0]
for numeros in peso:
    if numeros > maior:
        maior = numeros
print(maior)
#lista_peso = lista.append(peso)
#print(lista_peso)'''
