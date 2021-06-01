import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'''Seno: {seno}
Cosseno: {cosseno}
Tangente: {tangente}''')