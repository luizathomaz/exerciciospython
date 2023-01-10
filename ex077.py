palavras = ('kim', 'namjoon', 'kim', 'seokjin', 'min', 'yoongi', 'jung', 'hoseok',
            'park', 'jimin', 'kim', 'taehyung', 'jeon', 'jungkook',)
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')