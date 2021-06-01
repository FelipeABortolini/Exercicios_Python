lista = list()
for i in range(0, 5):
    print('Digite um valor numérico: ', end='')
    num = int(input())
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
    print(f'Adicionado na posição {lista.index(num)} da lista.')
print(f'{lista}')

