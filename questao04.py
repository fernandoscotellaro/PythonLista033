'''4)	Fazer um algoritmo que pergunte 4 números e apresente a média aritmética ponderada, com pesos respectivos de 1, 2, 3 e 4.
Obs: Sabe-se que o cálculo da média aritmética ponderada (mp) é feito da seguinte forma:
mp = ( (num1 x peso1) + (num2 x peso2) + (num3 x peso3) + (num4 x peso4) ) / (peso1 + peso2 + peso3 + peso4)
'''


num1 = float(input("Qual o primeiro valor?"))
num2 = float(input("Qual o segundo valor?"))
num3 = float(input("Qual o terceiro valor?"))
num4 = float(input("Qual o quarto valor?"))

peso1 = 1
peso2 = 2
peso3 = 3
peso4 = 4



mp = ((num1 * peso1) + (num2 * peso2) + (num3 * peso3) + (num4 * peso4) ) / (peso1 + peso2 + peso3 + peso4)

print(f"O valor da média dos seus números é de: {mp}")