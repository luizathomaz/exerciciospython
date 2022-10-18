'''num = input('Informe um número: ')
print(f'Analisando o número {num}')
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print(f'Milhar: {num[0]}')'''
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisan o número {}'.format(num))
print('Unidade: {}'.format(u))
print(f'Dezena: {d}')
print(f'Centena: {c}')
print('Milhar: {}'.format(m))
