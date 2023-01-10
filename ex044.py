print('{:=^40}'.format('LOJAS LUIZA'))
valor = float(input('Digite o preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO 
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
tipo = int(input('Qual é a opção? '))
if tipo == 1:
    valor2 = valor * 0.90
    print(f'Sua compra de R${valor:.2f} vai custar R${valor2:.2f} no final.')
elif tipo == 2:
    valor3 = valor * 0.95
    print(f'Sua compra de R${valor:.2f} vai custar {valor3:.2f} no final.')
elif tipo == 3:
    print('Sua compra será de {}.'.format(valor))
elif tipo == 4:
    parc = int(input('Quantas parcelas? '))
    mensal = valor / parc
    valor4 = (mensal * 1.20) * parc
    print('Sua compra será parcelada em 10x de R${:.2f} COM JUROS'.format(mensal *1.20))
    print(f'Sua compra de R${valor:.2f} vai custar R${valor4:.2f} no final.')
else:
    tipo = 0 or tipo > 5
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente')