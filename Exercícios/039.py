import time
ano = int(input('Digite o ano de seu nascimento: '))
tupla = time.localtime()
idade = tupla[0] - ano
if idade < 18:
    print(f'Você ainda terá de se alistar ao serviço militar, restam {18 - idade} anos para o alistamento.')
elif idade == 18:
    print('Este ano você deve realizar seu alistamento ao serviço militar.')
else:
    print(f'Você já passou do tempo de fazer o alistamento militar, fazem {idade - 18} que você se deveria ter se alistado.')