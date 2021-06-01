import random
alunos = list()
alunos.append(input('Digite o nome do primeiro aluno: '))
alunos.append(input('Digite o nome do segundo aluno: '))
alunos.append(input('Digite o nome do terceiro aluno: '))
alunos.append(input('Digite o nome do quarto aluno: '))
alunoSort = random.choice(alunos)
print(f'O aluno sorteado foi {alunoSort}')
