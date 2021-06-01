totalGasto = 0
maisMil = 0
barato = ''
i = 1
valorBarato = 0
while 1:
    print(f'---------- {i}ª PRODUTO ----------')
    nome = str(input('Nome: ')).strip()
    preco = float(input('Preço: '))

    totalGasto += preco

    if preco > 1000:
        maisMil += 1

    if i == 1:
        valorBarato = preco
        barato = nome
    elif preco < valorBarato:
        valorBarato = preco
        barato = nome

    resp = str(input('\nDeseja continuar a compra [S/N]? ')).upper().strip()
    while resp != 'S' and resp != 'N':
        print('\nOpção inválida! Tente novamente.')
        resp = str(input('Deseja continuar a compra [S/N]? ')).upper().strip()
    if resp == 'N':
        break

    i += 1
print('---------- FIM DO PROGRAMA ----------')
print(f'''O total gasto foi de R${totalGasto:.2f}.
{maisMil} produtos custaram mais de R$1.000.00.
{barato} é o produto mais barato comprado.''')
