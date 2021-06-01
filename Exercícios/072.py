tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um núemro de 0 a 20 para obter sua escrita por extenso: '))
while n < 0 or n > 20:
    print('Número inválido! Tente novamente.')
    n = int(input('\nDigite um núemro de 0 a 20 para obter sua escrita por extenso: '))
print(tupla[n])
