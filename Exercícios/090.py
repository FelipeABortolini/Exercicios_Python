aluno = {'nome': str(input('Digite o nome do aluno: ')).title().strip(), 'média': float(input('Digite a média do aluno: '))}
if aluno['média'] < 6:
    aluno['situação'] = 'Reprovado'
elif aluno['média'] >= 6 and aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
print(f'O nome do aluno é {aluno["nome"]}')
print(f'A média do aluno é {aluno["média"]}')
print(f'A situação do aluno é {aluno["situação"]}')
