from time import localtime

dados = dict()
dados['nome'] = str(input('Nome: ')).title().strip()
print('Ano de nascimento: ', end='')
ano = int(input())
data = localtime()
dados['idade'] = data[0] - ano
dados['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] - (data[0] - dados['contratação']) + 35

print(30 * '=-')
for i, j in dados.items():
    print(f'{i} tem valor {j}')
