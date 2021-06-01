tabela = ('São Paulo', 'Atlético Mineiro', 'Flamengo', 'Inter', 'Grêmio', 'Palmeiras', 'Santos', 'Fluminense', 'Corinthians', 'Fortaleza',
          'Ceará', 'Athletico Paranaense', 'Sport', 'Bahia', 'Vasco', 'Atlético Goianiense', 'Goiás', 'Bragantino', 'Botafogo', 'Coritiba')
print(f'Os 5 primeiros colocados são {tabela[0:5]}.')
print(f'\nOs 4 últimos colocados são {tabela[-4:]}: ')
print(f'\nOs times em ordem alfabética são {sorted(tabela)}')
print(f'\nO Grêmio está em {tabela.index("Grêmio") + 1}° colocado.')

