import numpy as np
num = []
for val in range(0, 500, 3):
    if val % 2 == 1:
        num.append(val)
array = np.array(num)
#print(array)
#print(len(array))
sum_numbers = np.sum(array)
#print(sum_numbers)
print(f'A soma de todos os {len(array)} valores solicitados é {sum_numbers}')
#como o professor fez:
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
