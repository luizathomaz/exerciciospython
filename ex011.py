larg = float(input('Qual a largura da sua parede? '))
h = float(input('Qual a altura da sua parede? '))
area = larg * h
t = area / 2
print('Para essa parede, que tem área {} m², será preciso {:.1f} litros de tinta.'.format(area, t))
