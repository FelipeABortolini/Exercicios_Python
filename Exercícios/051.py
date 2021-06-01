primTermo = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite a razão da Progressão Aritmética: '))
lista = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'sétimo', 'oitavo', 'nono', 'décimo']
for i in range(0, 10):
    print(f'O {lista[i]} termo da PA é {primTermo + (razao*i)}.')