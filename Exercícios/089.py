aluno = list()
turma = list()
resp = ''
media = 0

while True:
    aluno.append(str(input('Nome: ')).title().strip())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    turma.append(aluno[:])
    aluno.clear()
    resp = str(input('há mais alunos? [S/N] '))
    print()
    while resp not in 'S s N n':
        print('Opção inválida! Tente novamente.')
        resp = str(input('há mais alunos? [S/N] '))
        print()
    if resp in 'Nn':
        break

print(15 * '=-')
print(f'{"N°":<4}{"NOME":<20}{"MÉDIA":>6}')
print(30 * '-')

for i in range(0, len(turma)):
    print(f'{i:<4}{turma[i][0]:<20}{(turma[i][1] + turma[i][2]) / 2:>6.1f}')

print(30 * '-')

cont = 0
resp1 = ''
while True:
    if cont == 0:
        resp1 = str(input('Deseja obter as notas individuais de um aluno? [S/N] '))
        while resp1 not in 'S s':
            print('Opção inválida! Tente novamente.')
            resp1 = str(input('Deseja obter as notas individuais de um aluno? [S/N] '))
        if resp1 in 'N n':
            break
    nome = str(input('\nDigite o nome do aluno que deseja obter as notas: ')).title().strip()
    cont += 1
    for i in range(0, len(turma)):
        if nome == turma[i][0]:
            print(f'Prova 1 de {turma[i][0]}: {turma[i][1]}\nProva 2 de {turma[i][0]}: {turma[i][2]}')
    resp1 = str(input('\nDeseja obter as notas individuais de outro aluno? [S/N] '))
    while resp1 not in 'S s N n':
        print('Opção inválida! Tente novamente.')
        resp1 = str(input('\nDeseja obter as notas individuais de outro aluno? [S/N] '))
    if resp1 in 'N n':
        break

print()
print('Programa Encerrado!')
