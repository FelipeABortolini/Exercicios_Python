num = int(input('Digite um número inteiro: '))
cont = 0
for i in range(num, 0, -1):
    if num % i == 0:
        cont += 1
if cont == 2:
    print(f'{num} é primo!')
else:
    print(f'{num} não é primo!')