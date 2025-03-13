'''
Exemplos de Entrada
25
100
5.50

Exemplos de Saída
NUMBER = 25
SALARY = U$ 550.00
'''

number = int(input())
quantidadeHorasTrabalhads = int(input())
valorPorHora = float(input())

salary = quantidadeHorasTrabalhads*valorPorHora

print("NUMBER = ",number)
print(f"SALARY = U$ {salary:.2f}")
