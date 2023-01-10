def escreva(mensagem):
    print('-' * (len(mensagem) + 4))
    print(f'  {mensagem}')
    print('-' * (len(mensagem) + 4))


escreva(str(input('Digite uma mensagem: ')))
