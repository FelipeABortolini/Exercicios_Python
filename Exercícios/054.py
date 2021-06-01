from time import localtime
data = localtime()
maior = 0
menor = 0
for i in range(0, 7):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = data[0] - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{menor} pessoas ainda não atingiram a maioridade e {maior} pessoas já atingiram a maioridade.')
