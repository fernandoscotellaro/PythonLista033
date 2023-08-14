'''
3)	Fazer um programa que pergunte dois valores reais e apresente o primeiro com acréscimo de 30% e o segundo com desconto de 25%.
'''

val1 = float(input("Qual é o primeiro valor?"))
val2 = float(input("Qual é o segundo valor?"))

conta1 = (val1 * 0.3) + val1
conta2 = val2 - (val2 * 0.25)

print(f"O resultado do primeiro valor com um acréscimo de 30% é de {conta1}, E o resultado do segyndo valor com um desconto é de {conta2}")