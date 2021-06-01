salario = int(input('Digite o salário: '))
if salario > 1250:
    salario += 0.1*salario
else:
    salario += 0.15*salario
print(f'O salário será de R${salario:.2f}')