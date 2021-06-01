valor1 = int(input('Digte o primeiro valor: '))
valor2 = int(input('Digte o segundo valor: '))
opcao = int(input('''Escolha uma opção:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa\n'''))
while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
    print('Opção inválida! Tente novamente.')
    opcao = int(input('''Escolha uma opção:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa\n'''))
while opcao != 5:
    if opcao == 1:
        print(f'\nA soma entre {valor1} e {valor2} é {valor1 + valor2}.')
        opcao = int(input('''\nEscolha uma opção:
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos Números
        [ 5 ] Sair do Programa\n'''))
    elif opcao == 2:
        print(f'\nO produto entre {valor1} e {valor2} é {valor1 * valor2}.')
        opcao = int(input('''\nEscolha uma opção:
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos Números
        [ 5 ] Sair do Programa\n'''))
    elif opcao == 3:
        if valor1 > valor2:
            print(f'\n{valor1} é maior que {valor2}.')
            opcao = int(input('''\nEscolha uma opção:
            [ 1 ] Somar
            [ 2 ] Multiplicar
            [ 3 ] Maior
            [ 4 ] Novos Números
            [ 5 ] Sair do Programa\n'''))
        elif valor2 > valor1:
            print(f'\n{valor2} é maior que {valor1}.')
            opcao = int(input('''\nEscolha uma opção:
            [ 1 ] Somar
            [ 2 ] Multiplicar
            [ 3 ] Maior
            [ 4 ] Novos Números
            [ 5 ] Sair do Programa\n'''))
        else:
            print(f'\n{valor1} é igual ao {valor2}.')
            opcao = int(input('''\nEscolha uma opção:
            [ 1 ] Somar
            [ 2 ] Multiplicar
            [ 3 ] Maior
            [ 4 ] Novos Números
            [ 5 ] Sair do Programa\n'''))
    elif opcao == 4:
        valor1 = int(input('\nDigte um novo valor para o primeiro termo: '))
        valor2 = int(input('Digte um novo valor para o segundo termo: '))
        opcao = int(input('''\nEscolha uma opção:
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos Números
        [ 5 ] Sair do Programa\n'''))
print('\nPrograma Encerrado!')