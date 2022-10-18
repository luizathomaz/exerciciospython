dist = float(input('Qual a distância da viagem? '))
if dist<=200:
    p1 = dist * 0.5
    print('O valor da sua viagem é R${:.2f}.'.format(p1))
else:
    p2 = dist * 0.45
    print('O valor da sua viagem é R${:.2f}.'.format(p2))
#preço = dist * 0.50 if dist <=200 else dist * 0.45
#print('O preço da viagem será de R${}.'.format(preço))
