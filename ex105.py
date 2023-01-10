def notas(* num, sit=False):
    """
    Programa que le notas de alunos e devolve a quantidade, maior, menor, média e situação(opicional)
    :param num: médias 
    :param sit: situação do aluno
    :return: um dicionário "aluno" com as informações
    """
    aluno = {'total': len(num), 'maior': '', 'menor': '', 'media': ''}
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    media = sum(num) / len(num)
    aluno['media'] = f'{media:.2f}'
    if sit:
        if aluno['media'] < 5:
            aluno['situação'] = 'RUIM'
        elif 5 <= aluno['media'] < 7:
            aluno['situação'] = 'RAZOÁVEL'
        elif 7 <= aluno['media'] <= 10:
            aluno['situação'] = 'BOA'
    return aluno


#programa principal 
resp = notas(7.34, 5.2, 6.8954, 6.34)
print(resp)