frase = str(input('Digite um frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')

