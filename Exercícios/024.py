cidade = str(input('Digite o nome da cidade: '))
lista = cidade.split(" ")
if "Santo" in lista[0]:
    print("O nome da cidade começa com 'Santo'")
else:
    print("O nome da cidade não começa com 'Santo'")
