'''
1)	Elaborar um programa de computador que pergunte ao usuário o valor do Raio de um círculo e calcule a área do referido círculo, apresentando o resultado deste cálculo.
Obs: A fórmula da área é 𝒂 = 𝝅𝒓𝟐. Considere o valor de 𝝅 = 𝟑. 𝟏𝟒𝟏𝟓𝟗𝟐𝟔𝟓.
'''
import math

raio = float(input("Qual o valor do raio?"))

conta = (raio * raio) * math.pi

print(f"O valor da área do circulo é de: {conta}")