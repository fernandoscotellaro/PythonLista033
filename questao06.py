'''
6)	Fazer um algoritmo que pergunte dois valores a e b, efetue a troca dos valores, de forma que a variável a passe a possuir o valor da variável b, e que a variável b passe a possuir o valor da variável a, e apresente os valores trocados.
'''

a = int(input("Insira o primeiro valor:"))
b = int(input("Insira o segundo valor:"))

c = (a - a) + b
d = (b - b) + a

print(f"Os valores respectivamente de A e B trocados por si mesmos são: {c}, {d}")