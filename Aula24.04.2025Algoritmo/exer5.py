# Lista com as distâncias dos postos de gasolina ao ponto de partida (em km)
postos = [0, 30, 60, 100, 140, 200, 250, 300]

# Distância total a ser percorrida
distanciaTotal = int(input("Distância Total a Ser Percorrida: "))

# Capacidade do tanque do carro
capacidadeTanque = int(input("Capacidade do Tanque de Combustível (em litros): "))

# Rendimento do carro (km/litro)
rendimento = int(input("Rendimento do Carro por Litro: "))

# Capacidade do carro em km com um tanque cheio
autonomia = capacidadeTanque * rendimento

# Velocidade constante em km/h
velocidade = 80

# Tempo fixo por abastecimento (em minutos)
tempo_abastecimento = 10

# Variáveis de controle
posto_atual = 0
tempo_total = 0
abastecimentos = 0

# Percorrer os postos até o limite da distância total
for i in range(1, len(postos)):
    # Para caso o próximo posto esteja além da distância final da viagem
    if postos[i] > distanciaTotal:
        break

    distancia_proximo = postos[i] - postos[posto_atual]

    # Se a distância até o próximo posto for maior que a autonomia, precisa abastecer no posto anterior
    if distancia_proximo > autonomia:
        print(f"Parar para abastecer no posto de {postos[i-1]} km")
        abastecimentos += 1
        tempo_total += tempo_abastecimento
        posto_atual = i - 1  # Abastece no posto anterior

    # Agora que pode ir até o próximo posto, atualiza o tempo de viagem
    distancia = postos[i] - postos[posto_atual]
    tempo_viagem = (distancia / velocidade) * 60  # converte horas para minutos
    tempo_total += tempo_viagem
    posto_atual = i

# Calcula a distância restante do último posto até o destino final
distancia_restante = distanciaTotal - postos[posto_atual]

if distancia_restante > 0:
    if distancia_restante > autonomia:
        print(f"Parar para abastecer no posto de {postos[posto_atual]} km para chegar ao destino final")
        abastecimentos += 1
        tempo_total += tempo_abastecimento

    tempo_viagem = (distancia_restante / velocidade) * 60
    tempo_total += tempo_viagem

# Exibir o resumo
print(f"\nResumo da Viagem:")
print(f"Total de abastecimentos: {abastecimentos}")
print(f"Tempo total de viagem: {tempo_total:.2f} minutos")
