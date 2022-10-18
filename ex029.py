vel = int(input('Qual a velocidade do carro em Km/h? '))
multa = (vel - 80) * 7
if vel <=80:
    print('Pode seguir, você não foi multado!')
else:
    print('Você foi multado! Sua multa é de R${}'.format(multa))
