A, B = input('Digite dois números inteiros: ').split()
A, B = int(A), int(B)
if A > B:
    print('O primeiro valor é maior')
elif B > A:
    print('O segundo valor é maior')
elif B == A:
    print('Não existe valor maior, os dois são iguais')
