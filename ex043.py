peso = float(input('Digite o peso em kg: '))
alt = float(input('Digite a altura em cm: '))
imc = peso / (alt**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobrepeso ')
elif 30 <= imc < 40:
    print('Obesidade ')
elif imc >= 40:
    print('Obesidade Mórbida')
