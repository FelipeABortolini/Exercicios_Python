lista = ['masculino', 'feminino']
sexo = str(input('Digite seu sexo, [M] para masculino e [F] para feminino: ')).upper().strip()
while len(sexo) != 1 or (sexo != 'M' and sexo != 'F'):
    print('Opção inválida! Tente novamente.')
    sexo = str(input('Digite seu sexo, [M] para masculino e [F] para feminino: ')).upper().strip()
print('')
if sexo == 'M':
    i = 0
    print(f'Você pertence ao sexo {lista[i]}.')
if sexo == 'F':
    i = 1
    print(f'Você pertence ao sexo {lista[i]}.')

