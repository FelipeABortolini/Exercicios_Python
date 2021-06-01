tupla = (int(input('Primeiro valor: ')), int(input('Segundo valor: ')),
         int(input('Terceiro valor: ')), int(input('Quarto valor: ')))
print(f'\nNúmeros digitados: {tupla}')
print(f'\nO valor 9 apareceu {tupla.count(9)} vezes.')
print(f'O valor 3 foi digitado pela primeira vez na posição {tupla.index(3) + 1}')
pares = list()
for i in range(0, 4):
    if tupla[i] % 2 == 0:
        pares.append(tupla[i])
print(f'Os valores pares digitados foram {pares}')