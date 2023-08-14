'''
2)	Desenvolver um programa que calcule o salário líquido de um professor. Para elaborar o programa, é necessário possuir alguns dados, tais como: Valor da hora aula, número de horas trabalhadas no mês e percentual de desconto do INSS.
'''
ha = float(input("Qual o valor que você recebe por aula dada? R$:"))
na = int(input("Quantas aula foram dadas por você durante o mês?"))
pe = float(input("Qual é o valor em porcentagem descontado pelo INSS no seu salário bruto?"))

porcentagem = pe / 100
conta = (ha * na) * porcentagem
salario = (ha * na) - conta

print(f"O valor líquido de seu salário é de R$:{salario}")