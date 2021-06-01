i = -1
while (i < 0 or i > 9999):
    i = int(input('Digite um número entre 0 e 9999: '))
num = str(i)
if len(num) == 1:
    print(f'Unidade: {num[0]}')
elif len(num) == 2:
    print(f'Unidade: {num[1]}')
    print(f'Dezena: {num[0]}')
elif len(num) == 3:
    print(f'Unidade: {num[2]}')
    print(f'Dezena: {num[1]}')
    print(f'Centena: {num[0]}')
elif len(num) == 4:
    print(f'Unidade: {num[3]}')
    print(f'Dezena: {num[2]}')
    print(f'Centena: {num[1]}')
    print(f'Milhar: {num[0]}')

