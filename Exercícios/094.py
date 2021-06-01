num = int(input('Quantas pessoas serão cadastradas? '))
pessoa = dict()
lista = list()
somaIdades = 0
listaMulheres = list()
listaIdade = list()

for i in range(0, num):
    pessoa.clear()
    print(f'{f" Pessoa {i + 1} ":-^40}')
    pessoa['nome'] = str(input('Nome: ')).title().strip()
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    while pessoa['sexo'] not in 'MF':
        print('Opção inválida! Tente novamente.')
        del pessoa['sexo']
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    somaIdades += lista[i]['idade']
    if lista[i]['sexo'] == 'F':
        listaMulheres.append(lista[i]['nome'])

mediaIdades = somaIdades / num

for i in range(0, num):
    if lista[i]['idade'] > mediaIdades:
        listaIdade.append(lista[i]['nome'])
print(lista)
print(30 * '=-')
print(f'Foram cadastradas {num} pessoas.')
print(f'A média de idades é {mediaIdades}.')
print(f'Lista com todas mulheres: {listaMulheres}')
print(f'Lista com todas pessoas com idade acima da média: {listaIdade}')
