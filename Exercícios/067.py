while 1:
    num = int(input('Digite um número para obter a tabuada: [n° negativo para encerrar]\n'))
    if num < 0:
        break
    i = 0
    while i < 11:
        print(f'{num} x {i} = {num * i}.')
        i += 1
    print('')
print('\nPrograma Encerrado!')
