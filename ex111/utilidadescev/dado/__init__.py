def leiaDinheiro(msg):
    preço = input(msg).replace(',', '.').strip()
    while True:
        if not preço.isalpha():
            return float(preço)
        else:
            print(f'ERRO: {preço} é um preço inválido!')
            preço = input(msg).replace(',', '.').strip()
    
