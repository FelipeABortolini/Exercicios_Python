def leiaint(n):
    if n.isnumeric():
        print(f'Você digitou o valor {n}.')
    else:
        print('\033[0;31mErro! Digite um número inteiro válido.')
        numero = str(input('\033[mDigite um número: '))
        leiaint(numero)


num = str(input('Digite um número: '))
leiaint(num)
