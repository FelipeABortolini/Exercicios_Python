'''expressao = str(input('Digite uma expressão com parênteses: ')).strip()
abre = expressao.split('(')
fecha = expressao.split(')')
if len(abre) == len(fecha):
    print('Expressão é válida!')
else:
    print('Expressão não é válida!')'''

#Usando Listas:
expr = str(input('Digite uma expressão com parênteses: ')).strip()
pilha = []
for i in expr:
    if i == '(':
        pilha.append('(')
    if i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')
