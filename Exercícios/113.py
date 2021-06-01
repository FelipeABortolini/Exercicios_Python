def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except(TypeError, ValueError):
            print('\033[;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except(TypeError, ValueError):
            print('\033[;31mERRO! Digite um número real válido.\033[m')
            continue
        else:
            return num


inteiro = leiaint('Digite um valor inteiro: ')
real = leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
