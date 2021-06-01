maior = 0
menor = 0

n1 = int(input('Digite números para fazer a média entre eles:\n'))
n2 = int(input())

if n1 > n2:
    maior = n1
    menor = n2
elif n2 > n1:
    maior = n2
    menor = n1
else:
    maior = n1
    menor = n1
soma = n1 + n2
media = soma / 2

print(f'A média é {media:.2f}, o maior valor digitado é {maior} e o menor é {menor}. Deseja continuar [S/N]? ', end='')
resp = str(input()).upper()
while resp != 'S' and resp != 'N':
    print('\nOpção inválida! Tente novamente.')
    print('Deseja continuar [S/N]? ', end='')
    resp = str(input()).upper()

cont = 2

while resp == 'S':
    n = int(input('\nDigite outro número para entrar no cálculo da média:\n'))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    cont += 1
    soma += n
    media = soma / cont
    print(f'A média é {media:.2f}, o maior valor digitado é {maior} e o menor é {menor}. Deseja continuar [S/N]? ', end='')
    resp = str(input()).upper()
    while resp != 'S' and resp != 'N':
        print('\nOpção inválida! Tente novamente.')
        print('Deseja continuar [S/N]? ', end='')
        resp = str(input()).upper()
print('\nPrograma Encerrado!')