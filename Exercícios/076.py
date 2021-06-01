precoProdutos = ('Geladeira', 2500,
                 'Sofá', 3000,
                 'Cama', 9500,
                 'Iphone 8', 280,
                 'Estojo', 25,
                 'Lápis', 1.75,
                 'Borracha', 2)
print('-'*42)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*42)
for i in range(0, len(precoProdutos), 2):
    print(f'{precoProdutos[i]:.<30}R$ {precoProdutos[i + 1]:>8.2f}')
print('-'*42)
