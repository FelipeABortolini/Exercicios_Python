def metade(valor):
    print(f'A metade de R${valor:.2f} é R${valor / 2:.2f}')


def dobro(valor):
    print(f'O dobro de R${valor:.2f} é R${valor * 2:.2f}')


def aumentar(valor):
    print(f'Aumentando 10% de R${valor:.2f}, temos R${valor + (valor / 100) * 10:.2f}')


def diminuir(valor):
    print(f'Diminuindo 35% de R${valor:.2f}, temos R${valor - (valor / 100) * 35:.2f}')
