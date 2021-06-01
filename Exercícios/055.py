cont = 0
for i in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    if cont == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
    cont += 1
print(f'O maior peso regitrado foi {maior}kg e o menor foi {menor}kg.')

#Utilizando Listas:
'''lista = list()
for i in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    lista.append(peso)
maior = max(lista)
menor = min(lista)
print(f'O maior peso regitrado foi {maior}kg e o menor foi {menor}kg.')'''


