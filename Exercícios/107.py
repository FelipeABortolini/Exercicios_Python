import moeda

preco = int(input('Digite o preço: R$'))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'Aumentando 10% de {preco}, temos {moeda.aumentar(preco, 10)}')
print(f'Diminuindo 35% de {preco}, temos {moeda.diminuir(preco, 35)}')
