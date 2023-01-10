matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
print('=-'*30)
for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-' * 30)
maior = 0
for l in matriz[1]:
    if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
        maior = matriz[1][0]
    elif matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
        maior = matriz[1][1]
    else:
        maior = matriz[1][2]
print(f'A soma dos valores pares é: {sum(pares)}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}.')
print(f'O maior valor da segunda linha é {maior} .')

#como o professor fez:

'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}] '))
print('=-'*30)
for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('=-' * 30)
print(f'A soma dos valores pares é {spar}. ')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')'''