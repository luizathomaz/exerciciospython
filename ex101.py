def pegaidade():
    from datetime import date
    ano = date.today().year
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = ano - nasc
    return idade


def voto():
    idade = pegaidade()
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade <18 or 65 <= idade:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


#programa principal:
print(voto())
