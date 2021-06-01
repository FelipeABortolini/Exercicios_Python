km = float(input('Digite quantos km foram percorridos: '))
dias = int(input('Digite por quantos dias o carro ficou alugado: '))
preco = km*0.15 + dias*60
print(f'O preço final é R${preco:.2f}')