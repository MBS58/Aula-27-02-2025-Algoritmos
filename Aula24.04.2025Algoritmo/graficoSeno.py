import math

#vetores para poder armazenar os valores de x e y 
valoresX = []
valoresY = []

# range para poder realizar o gráfico com os valores do seno de 1 a 360
for i in range(0, 360):
    x = i + 1
    # adiciona o x no vetor valoresX
    valoresX.append(x)
    # pego o radiano com a biblioteca do py
    angulo = math.radians(x)
    # pego o seno com a bilbioteca do py
    y = math.sin(angulo)
    # adiciono o seno em valoresY
    valoresY.append(y)

# Parâmetros para o gráfico
centro = 40         # Posição central da linha
escala = 30         # Escala de multiplicação para o valor de Y

# Imprime o gráfico linha por linha
for i in range(0, 360):
    # Calcula o deslocamento horizontal com base no valor do seno (valoresY[i]) multiplicado pela escala
    deslocamento = int(valoresY[i] * escala)
    
    # Define a posição final onde o '*' será colocado, deslocado a partir do centro
    posicao = centro + deslocamento

    # Inicializa uma nova linha vazia com espaços
    linha = []
    for _ in range(centro * 2):  # Cria uma linha com o dobro do tamanho do centro (para ter espaço à esquerda e direita)
        linha.append(' ')

    # Marca o centro da linha com o eixo vertical '|'
    linha[centro] = '|'

    # Coloca o '*' na posição correspondente ao valor de y (seno)
    linha[posicao] = '*'

    # Imprime a linha como uma string
    print(''.join(linha))

