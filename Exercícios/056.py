'''nomeVelho = ''
somaIdade = 0
mulMenos20 = 0
maior = 0
for i in range(1, 5):
    print('---------- {}ª PESSOA ----------'.format(i))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    while len(sexo) != 1:
        print('Opção inválida, tente novamente.')
        sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if i == 1 and sexo == 'M':
        maior = idade
        nomeVelho = nome
    elif idade > maior and sexo == 'M':
        maior = idade
        nomeVelho = nome
    somaIdade += idade
    if sexo == "F" and idade < 20:
        mulMenos20 += 1
mediaIdade = somaIdade/4
print(f''''''A média de idade do grupo é {mediaIdade}.
O homem mais velho tem {maior} e se chama {nomeVelho}.
Foram registradas {mulMenos20} mulheres com menos de 20 anos.
)'''

#Resolução personalizada usando dicionários e listas:
somaIdades = 0
nomeVelho = ''
mulMenor20 = 0
maiorIdadeMasc = 0
lista = list()
numVelhos = 1
listaVelhos = list()

for i in range(1, 5):
    print('---------- {}ª PESSOA ----------'.format(i))
    pessoa = {'nome': str(input('Nome: ')).strip().capitalize(), 'idade': int(input('Idade: ')), 'sexo': str(input('Sexo [M/F]: ')).upper().strip()}
    while len(pessoa['sexo']) != 1 or (pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F'):
        print('Opção inválida, tente novamente.')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    lista.append(pessoa)

for i in range(0, 4):
    somaIdades += lista[i]['idade']
    if i == 0 and lista[i]['sexo'] == 'M':
        maiorIdadeMasc = lista[i]['idade']
        nomeVelho = lista[i]['nome']
    elif lista[i]['sexo'] == 'M' and lista[i]['idade'] > maiorIdadeMasc:
        maiorIdadeMasc = lista[i]['idade']
        nomeVelho = lista[i]['nome']
    if lista[i]['sexo'] == 'F' and lista[i]['idade'] < 20:
        mulMenor20 += 1

listaVelhos.append(nomeVelho)

for i in range(0, 4):
    if lista[i]['idade'] == maiorIdadeMasc:
        if lista[i]['nome'] != nomeVelho:
            numVelhos += 1
            listaVelhos.append(lista[i]['nome'])

mediaIdades = somaIdades/4

print(f'\nA média de idade do grupo é {mediaIdades}.')

if numVelhos == 1:
    print(f'O homem mais velho tem {maiorIdadeMasc} anos e se chama {nomeVelho}.')
elif numVelhos == 2:
    print(f'Os homens mais velhos têm {maiorIdadeMasc} anos e se chamam {listaVelhos[0]} e {listaVelhos[1]}.')
elif numVelhos == 3:
    print(f'Os homens mais velhos têm {maiorIdadeMasc} anos e se chamam {listaVelhos[0]}, {listaVelhos[1]} e {listaVelhos[2]}.')
elif numVelhos == 4:
    print(f'Os homens mais velhos têm {maiorIdadeMasc} anos e se chamam {listaVelhos[0]}, {listaVelhos[1]}, {listaVelhos[2]} e {listaVelhos[3]}.')

if mulMenor20 == 0:
    print(f'Não foram registradas mulheres com menos de 20 anos.')
elif mulMenor20 == 1:
    print(f'Foi registrada {mulMenor20} mulher com menos de 20 anos.')
elif mulMenor20 > 1:
    print(f'Foram registadas {mulMenor20} mulheres com menos de 20 anos.')