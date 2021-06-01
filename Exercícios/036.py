valor = float(input('Digite o valor do empréstimo: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Digite em quantos anos deseja pagar: '))
meses = anos * 12
prestacao = valor / meses
if prestacao > salario * 0.3:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')