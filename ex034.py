salario = float(input('Digite o seu salário: R$'))
if salario > 1250:
    novo1 = salario * 1.10
    print('Ápos aumento, seu novo salario será de R${:.2f}!'.format(novo1))
else:
    novo2 = salario * 1.15
    print('Ápos aumento, seu novo salário será de R${:.2f}!'.format(novo2))
