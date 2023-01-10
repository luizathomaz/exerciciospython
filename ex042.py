a = float(input('Digite o primeiro comprimento: '))
b = float(input('Digite o segundo comprimento: '))
c = float(input('Digite o terceiro comprimento: '))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('Pode ser triangulo!')
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b != c or a == c != b or b == c != a:
        print('ISÓSCELES')
    elif a != b != c:
        print('ESCALENO')
else:
    print('Não pode ser triangulo!')
