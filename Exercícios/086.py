linha = list()
matriz = list()
for i in range(0, 3):
    for j in range(0, 3):
        linha.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
    matriz.append(linha[:])
    linha.clear()
print(30 * '=-')
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[  {matriz[c][d]}  ]', end='')
    print()
