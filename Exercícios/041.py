import time
ano = int(input('Digite o ano de nascimento do atleta: '))
tupla = time.localtime()
idade = tupla[0] - ano
if idade <= 9:
    print('Categoria Mirim.')
elif idade <= 14:
    print('Categoria Infantil.')
elif idade <= 19:
    print('Categoria Junior.')
elif idade <= 20:
    print('Categoria Sênior.')
else:
    print('Categoria Master.')