import random
jogo = list()
todosJogos = list()
numjogos = int(input('Digite o número de jogos que deseja gerar: '))
for c in range(0, numjogos):
    for i in range(0, 6):
        jogo.append(random.randint(1, 60))
    jogo.sort()
    todosJogos.append(jogo[:])
    jogo.clear()
print(3 * '=-', f'  SORTEANDO {numjogos} JOGOS  ', 3 * '=-')
for i in range(0, len(todosJogos)):
    print(f'Jogo {i + 1}: {todosJogos[i]}')
