numeros = ( int(input('Digite um número: ')),
            int(input('Digite outro número: ')),
            int(input('Digite mais um número: ')),
            int(input('Digite o último número: ')))
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na posição {numeros.index(3) + 1}. ')
else:
    print('O valor 3 não foi digitado. ')
print(f'Os valores pares digitados foram ', end='')
pares = 0
for c in numeros:
    if c % 2 == 0:
        pares += 1
        print(c, end=' ')
