registros = list()
dado = list()
resp = 's'
pesoPesado = 0
pesoLeve = 0
cont = 0
nomesPesado = list()
nomesLeve = list()

while resp in 'Ss':
    dado.append(str(input('Nome: ')).title())
    dado.append(float(input('Peso: ')))
    if cont == 0:
        pesoPesado = dado[1]
        pesoLeve = dado[1]
    elif dado[1] > pesoPesado:
        pesoPesado = dado[1]
    elif dado[1] < pesoLeve:
        pesoLeve = dado[1]
    cont += 1
    registros.append(dado[:])
    dado.clear()
    resp = str(input('Deseja Continuar? [S/N] ')).strip()
    print()
    while resp not in 'NnSs':
        print('Opção inválida! Tente novamente.')
        resp = str(input('Deseja Continuar? [S/N] ')).strip()
        print()

for i in range(0, len(registros)):
    if pesoPesado == registros[i][1]:
        nomesPesado.append(registros[i][0])
    if pesoLeve == registros[i][1]:
        nomesLeve.append(registros[i][0])

print(f'Foram cadastradas {len(registros)} pessoas.')

if len(nomesPesado) > 1:
    print(f'As pessoas mais pesadas pesam {pesoPesado:.1f}Kg e se chamam', end='')
    for i in range(0, len(nomesPesado)):
        print(f' {nomesPesado[i]}', end='')
        if (i == 0 and len(nomesPesado) == 2) or (i == len(nomesPesado) - 2 and len(nomesPesado) > 2):
            print(' e', end='')
        elif i < len(nomesPesado) - 2 and len(nomesPesado) > 2:
            print(',', end='')
        elif i == len(nomesPesado) - 1:
            print('.')
else:
    print(f'A pessoa mais pesada pesa {pesoPesado:.1f}Kg e se chama {nomesPesado[0]}.')

if len(nomesLeve) > 1:
    print(f'As pessoas mais leves pesam {pesoLeve:.1f}Kg e se chamam', end='')
    for i in range(0, len(nomesLeve)):
        print(f' {nomesLeve[i]}', end='')
        if (i == 0 and len(nomesLeve) == 2) or (i == len(nomesLeve) - 2 and len(nomesLeve) > 2):
            print(' e', end='')
        elif i < len(nomesLeve) - 2 and len(nomesLeve) > 2:
            print(',', end='')
        elif i == len(nomesLeve) - 1:
            print('.')
else:
    print(f'A pessoa mais leve pesa {pesoLeve:.1f}Kg e se chama {nomesLeve[0]}.')
