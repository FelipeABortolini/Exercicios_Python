from time import sleep


def maior(*num):
    maiorvalor = 0
    cont = 0
    print(30 * '=-')
    print('Analisando valores passados...')
    for i in num:
        print(f'{i} ', end='')
        if cont == 0:
            maiorvalor = i
        elif i > maiorvalor:
            maiorvalor = i
        cont += 1
        sleep(0.25)
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maiorvalor}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
