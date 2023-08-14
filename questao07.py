'''
7)	Fazer um algoritmo que pergunte os valores dos catetos de um triângulo retângulo e apresente o valor da hipotenusa.
Obs: A fórmula é hipotenusa2	=	cateto12	+	cateto22  ou, se preferir, hipotenusa cateto12	+	cateto22).
'''

import math

a = int(input("Qual o valor do primeiro cateto?"))
b = int(input("Qual o valor do segundo cateto?"))

c = math.pow(a,2)
d = math.pow(b,2)
e = c + d
f = float(math.sqrt(e))

print(f"A hipotenusa desses catetos é {f}")