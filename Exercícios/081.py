lista = list()
resp = ''
quantidade = 0
val5 = False
while 1:
    resp = ''
    num = int(input('Digite um valor numérico: '))
    lista.append(num)
    quantidade += 1
    if num == 5:
        val5 = True
    while resp != 'S' and resp != 'N':
        print('Deseja continuar? [S/N] ', end='')
        resp = str(input()).upper().strip()
        if resp != 'S' and resp != 'N':
            print('Opção inválida! Tente novamente.')
    if resp == 'N':
        break
lista.sort(reverse=True)
print(30*'=-')
print(f'Foram digitados {quantidade} números na lista.')
print(f'A lista em ordem decrescente é {lista}')
if val5 == False:
    print('O valor 5 não está na lista.')
else:
    print('O valor 5 está na lista.')

