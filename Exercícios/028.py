import random
num = random.randint(0, 5)
n = int(input('Digite um valor entre 0 e 5: '))
if n == num:
    print('Parabéns, você acertou o valor!')
else:
    print(f'Você errou o valor, o valor correto é {num}.')