num = int(input('Digite um n° inteiro: '))
fat = 1
n = num
while num != 0:
    fat *= num
    num -= 1
print(f'O fatorial de {n} é {fat}.')

#Fatorial com laço for:
'''num = int(input('Digite um n° inteiro: '))
fat = 1
for i in range(num, 0, -1):
    fat *= i
print(f'O fatorial de {num} é {fat}.')'''