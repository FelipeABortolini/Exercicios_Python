frase = str(input('Digite uma frase: ')).upper()
print(f"A letra 'A' apareceu {frase.count('A')} vezes na frase.")
print(f"A primeira aparição da letra 'A' foi na letra de número {frase.index('A')+1}")
print(f"A última aparição da letra 'A' foi na letra de número {frase.rindex('A')+1}")