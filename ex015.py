dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('E quantos Km (quilometros) foram rodados nesse período? '))
pag = (60 * dias) + (0.15 * km)
print('O pagamento a ser feito pelo aluguel do carro durante {} dias e percorrendo {}Km é de R${:.2f}'.format(dias, km, pag))
