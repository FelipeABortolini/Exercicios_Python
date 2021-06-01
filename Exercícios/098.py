import time


def contador(i, f, p):
    print(30 * '=-')
    cont = i
    if i < f:
        while cont <= f:
            if p == 0:
                p = 1
            if cont == i and p > 0:
                print(f'Contagem de {i} até {f} de {p} em {p}:')
            print(f'{cont} ', end='')
            if p > 0:
                cont += p
            elif p < 0:
                cont -= p
            time.sleep(0.25)
    else:
        while cont >= f:
            if p == 0:
                p = 1
            if cont == i and p > 0:
                print(f'Contagem de {i} até {f} de {p} em {p}:')
            elif cont == i and p < 0:
                print(f'Contagem de {i} até {f} de {-p} em {-p}:')
            print(f'{cont} ', end='')
            if p > 0:
                cont -= p
            elif p < 0:
                cont += p
            time.sleep(0.25)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
inicio = int(input('\nInício: '))
final = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, final, passo)
