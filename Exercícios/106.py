def pyhelp(fun):
    print((36 + len(fun)) * '\033[;;46m~')
    print(f"  Acessando o manual do comando '{fun}'")
    print((36 + len(fun)) * '~')
    print('\033[m\033[7m', end='')
    help(fun)


while True:
    print('\033[;;43m~' * 27)
    print('  SISTEMA DE AJUDA PyHELP')
    print('~' * 27)
    comando = str(input('\033[mFunção ou Biblioteca > '))
    if comando not in 'FIMfim':
        pyhelp(comando)
    else:
        break
print('\033[;;41m~' * 13)
print('  ATÉ LOGO!')
print('~' * 13)
