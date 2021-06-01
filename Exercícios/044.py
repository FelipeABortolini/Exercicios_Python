preco = float(input('Digite o preço do produto: '))
condicao = 0
while condicao == 0:
    condicao = float(input('''Escolha a condição de pagamento:
    [ 1 ] À vista no dinheiro ou cheque;
    [ 2 ] À vista no cartão;
    [ 3 ] 2x no cartão;
    [ 4 ] 3x ou mais no cartão;\n'''))
    if condicao != 1 and condicao != 2 and condicao != 3 and condicao != 4:
        print('Condição inválida, tente novamente.\n')
        condicao = 0
if condicao == 1:
    print(f'O preço no pagamento à vista em dinherio/cheque possui 10% de desconto, o preço com esse desconto é R${preco - (preco*0.1):.2f}.')
elif condicao == 2:
    print(f'O preço no pagamento à vista no cartão possui 5% de desconto, o preço com esse desconto é R${preco - (preco * 0.05):.2f}.')
elif condicao == 3:
    print(f'O preço no pagamento em 2x no cartão não possui desconto nem acréscimo, permanece então R${preco:.2f}.')
else:
    print(f'O preço no pagamento em 3x ou mais no cartão possui acréscimo de 20% de juros, o novo preço ficará R${preco + (preco*0.2):.2f}.')