A, B = input('Digite duas notas: ').split()
A, B = float(A), float(B)
media = (A + B) / 2
print(f'Quem tirou as notas {A:.1f} e {B:.1f} tem como média {media:.1f}.')
if media < 5.0:
    print('REPROVADO')
elif 5.0 <= media < 7.0:
    print('RECUPERAÇÃO')
elif 7.0 <= media:
    print('APROVADO')
