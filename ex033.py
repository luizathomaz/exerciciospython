n1 = int(input('Digite o primeio número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 < n2 < n3:
    print(f'O maior número é {n3}, e o menor é {n1}.')
if n3 < n2< n1:
    print('O maior número é {} e o menor é {}.'.format(n1, n3))
if n2 < n3 < n1:
    print(f'O maior número é {n1} e o menor é {n2}')
if n2 < n1 < n3:
    print(f'O maior número é {n3} e o menor número é {n2}')
if n1 < n3 < n2:
    print(f'O maior número é {n2} e o menor número é {n1}')
if n3 < n1 < n2:
    print(f'O maior número é {n2} e o menor número é {n3}')
else:
    print('nada')
'''
# verificando o menor 
menor = n1
if n2<n1 and n2<n3:
    menor = n2 
if n3<n1 and n3<n2:
    menor = n3
# verificando o maior
maior = n1 
if n2>n1 and n2>n3: 
    maior = n2 
if n3>n1 and n3>n2: 
    maior = n3 
print('O maior é {} e o menor é {}.'.format(maior, menor))'''