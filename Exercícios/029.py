velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80.0:
    print('Velocidade acima da permitida! Você foi multado em R${:.2f}'.format((velocidade - 80)*7))