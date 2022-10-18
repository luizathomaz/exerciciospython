'''from math import hypot
num = float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(num, adj)
print('Um triângulo que tem {} de cateto oposto e {} de cateto adjacente possui {:.2f} de hipotenusa'.format(num, adj, hip))'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
