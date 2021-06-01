km = float(input('Digite a distânica da viagem: '))
if km <= 200:
    print('O valor da passagem é R${:.2f}'.format(km*0.5))
else:
    print('O valor da passagem é R${:.2f}'.format(km * 0.45))