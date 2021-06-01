maioridade = 0
homens = 0
mulherMenor20 = 0
i = 1
while 1:
    print(f'---------- {i}ª PESSOA ----------')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    while sexo != 'M' and sexo != 'F':
        print('Opção inválida! Tente novamente.')
        sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulherMenor20 += 1
    i += 1
    resp = str(input('''Deseja continuar [S/N]?''')).upper().strip()
    if resp == 'N':
        break
print(f'''\n{maioridade} pessoas têm mais de 18 anos.
{homens} homens foram cadastrados.
{mulherMenor20} mulheres têm menos de 20 anos.''')