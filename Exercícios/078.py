lista = list()
maior = 0
menor = 0
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor numérico para a posição {i}: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        elif lista[i] < menor:
            menor = lista[i]
print(25 * '=-')
print(f'Você digitou os valores {lista}')
print(f'O maior valor é {max(lista)} e está nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor é {min(lista)} e está nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
