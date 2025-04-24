# Utilizando biblioteca do python 
from fractions import Fraction
# Pede o valor do numerador da primeira fração para o usuário 
numerador1 = int(input("Digite o numerador da primeira fração: "))
# Pede o valor do denominador da primeira fração para o usuário 
denominador1 = int(input("Digite o denominador da primeira fração: "))

# Pede o valor do numerador da segunda fração para o usuário 
numerador2 = int(input("Digite o numerador da segunda fração: "))
# Pede o valor do denominador da segunda fração para o usuário 
denominador2 = int(input("Digite o denominador da segunda fração: "))

# Cria a fração1
fracao1 = Fraction(numerador1, denominador1)
# Cria a fração2
fracao2 = Fraction(numerador2, denominador2)

# Soma as frações
somaFracao = fracao1 + fracao2
# Printo a soma no terminal Simplificada
print("Soma Fracao", somaFracao)