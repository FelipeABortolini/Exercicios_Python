aproveitamento = dict()
golsPartidas = list()
totalGols = 0
aproveitamento['nome'] = str(input('Nome do Jogador: ')).title().strip()
numPartidas = int(input('Número de partidas jogadas: '))

for i in range(0, numPartidas):
    golsPartidas.append(int(input(f'N° de gols na {i + 1} partida: ')))
    totalGols += golsPartidas[i]

aproveitamento['gols'] = golsPartidas
aproveitamento['totalDeGols'] = totalGols
print(30 * '=-')
print(f'O jogador {aproveitamento["nome"]} jogou {numPartidas} partidas.')

for i in range(0, numPartidas):
    print(f'{"=>":>7} Na partida {i + 1} marcou {aproveitamento["gols"][i]}.')
print(f'Foi um total de {aproveitamento["totalDeGols"]} gols.')
