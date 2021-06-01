def metade(valor, estado=False):
    res = valor / 2
    return res if estado is False else moeda(res)


def dobro(valor, estado=False):
    res = valor * 2
    return res if estado is False else moeda(res)


def aumentar(valor, taxa, estado=False):
    res = valor + (valor / 100 * taxa)
    return res if estado is False else moeda(res)


def diminuir(valor, taxa, estado=False):
    res = valor - (valor / 100 * taxa)
    return res if estado is False else moeda(res)

def moeda(valor, simb='R$'):
    return f'{simb}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, taxaaum=0, taxadim=0):
    print(29 * '-')
    print('       RESUMO DO VALOR')
    print(29 * '-')
    print(f'{"Preço analisado:":<19}', f'{moeda(valor)}')
    print(f'{"Dobro do preço:":<19}', f'{dobro(valor, True)}')
    print(f'{"Metade do preço:":<19}', f'{metade(valor, True)}')
    print(f'{f"{taxaaum}% de aumento:":<19}', f'{aumentar(valor, taxaaum, True)}')
    print(f'{f"{taxadim}% de redução:":<19}', f'{diminuir(valor, taxadim, True)}')
    print(29 * '-')

