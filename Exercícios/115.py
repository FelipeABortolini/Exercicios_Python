from ex115 import menu, mostra, adiciona

while True:
    escolha = menu.menu()
    if escolha == 1:
        mostra.mostra()
    elif escolha == 2:
        adiciona.adiciona()
    elif escolha == 3:
        menu.cabecalho(f'{"SAINDO DO SISTEMA... ATÉ LOGO!":^50}')
        break
