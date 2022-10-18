'''a = float(input('Digite o primeiro comprimento: '))
b = float(input('Digite o segundo comprimento: '))
c = float(input('Digite o terceiro comprimento: '))
if a < (b - c):
    print('Não pode ser triangulo!')
if b < (a-c):
    print('Não pode ser triângulo!')
if c < (a - b):
    print('Não pode ser triangulo!')
if a > (b - c):
    print('Pode ser triangulo! ')
if b > (a - c):
    print('Pode ser triangulo!')
if c > (a - b):
    print('Pode ser triangulo!')'''

a = float(input('Digite o primeiro comprimento: '))
b = float(input('Digite o segundo comprimento: '))
c = float(input('Digite o terceiro comprimento: '))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('Pode ser triangulo!')
else:
    print('Não pode ser triangulo!')
