lista = list()
pares = list()
impares = list()
for i in range(0, 7):
    num = int(input(f'Digite o {i + 1}° valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
lista.append(pares[:])
lista.append(impares[:])
print(30 * '=-')
print(f'Lista criada: {lista}')
print(f'Valores pares em ordem crescente: {pares}')
print(f'Valores ímpares em ordem crescente: {impares}')
