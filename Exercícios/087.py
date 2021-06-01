linha = list()
matriz = list()
somaPares = 0
soma3Coluna = 0
maior2Linha = 0

for i in range(0, 3):
    for j in range(0, 3):
        linha.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        if linha[j] % 2 == 0:
            somaPares += linha[j]
        if j == 2:
            soma3Coluna += linha[j]
        if i == 1:
            if j == 0:
                maior2Linha = linha[j]
            elif linha[j] > maior2Linha:
                maior2Linha = linha[j]
    matriz.append(linha[:])
    linha.clear()

print(30 * '=-')

for c in range(0, 3):
    for d in range(0, 3):
        print(f'[  {matriz[c][d]}  ]', end='')
    print()

print(30 * '=-')

print(f'A soma dos elemntos pares da matriz é {somaPares}.')
print(f'A soma dos elementos da terceira coluna da matriz é {soma3Coluna}.')
print(f'O maior elemento da segunda linha da matriz é {maior2Linha}.')
