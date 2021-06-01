palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar')
for i in palavras:
    print(f'Na palavra {i} temos ', end='')
    for j in i:
        if j.lower() in 'aeiou':
            print(f'{j.lower()} ', end='')
    print('')
