lista = list()
pares = list()
impares = list()
resp = ''
while 1:
    resp = ''
    num = int(input('Digite um valor numérico: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if resp != 'S' and resp != 'N':
            print('Opção inválida! Tente novamente.')
    if resp == 'N':
        break
print(30*'=-')
print(f'Lista completa: {lista}')
print(f'Lista com valores pares: {pares}')
print(f'Lista com valores ímpares: {impares}')