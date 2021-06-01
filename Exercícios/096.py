def area(larg, comp):
    a = larg * comp
    print(30 * '=-')
    print(f'A área de um terreno de {larg} x {comp} é {a} metros quadrados.')


largura = float(input('Largura do terreno (m): '))
comprimento = float(input('Comprimento do terreno (m): '))
area(largura, comprimento)
