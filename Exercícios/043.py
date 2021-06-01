peso = float(input('Digite o peso: '))
altura = float(input('Digite a aultura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Acima do peso.')
elif imc < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')