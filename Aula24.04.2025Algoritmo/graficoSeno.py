import math

valoresX = []
valoresY = []

for i in range(0, 360):
    x = i + 1
    valoresX.append(x)
    angulo = math.radians(x)
    y = math.sin(angulo)
    valoresY.append(y)

# Parâmetros para o gráfico
centro = 40         # Posição central da linha
escala = 30         # Escala de multiplicação para o valor de Y

# Imprime o gráfico
for i in range(0, 360):
    deslocamento = int(valoresY[i] * escala)
    posicao = centro + deslocamento

    linha = []
    for _ in range(centro * 2):
        linha.append(' ')
    linha[centro] = '|'         # Eixo central
    linha[posicao] = '*'        # Ponto do gráfico

    print(''.join(linha))
