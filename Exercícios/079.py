lista = list()
resp = 'S'
while resp == 'S':
    num = int(input('Digite um valor numérico: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar!')
    print('Deseja continuar? [S/N]')
    resp = str(input()).upper().strip()
    while resp != 'S' and resp != 'N':
        print('Opção inválida! Tente novamente.')
        print('Deseja continuar? [S/N]')
        resp = str(input()).upper().strip()
lista.sort()
print(30*'=-')
print('Os valores únicos digitados em ordem crescente são: ', end='')
for i in range(0, len(lista)):
    print(f'{lista[i]} ', end='')