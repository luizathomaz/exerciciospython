def area(a, b):
    c = a * b
    print(f'Um terreno com dimensões {a}m e {b}m tem área {c:.1f}m²')


print('Digite as dimensões do terreno para calcular a área: ')
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
