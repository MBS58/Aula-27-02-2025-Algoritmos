# imports para verificar tempo, tamanho e criar numeros aleatórios
import random
import time
import sys

#pegar o tempo inicial
start_time = time.time()
#verificar quantos números deseja realizar a média
n_media = int(input("Digite quantos números deseja fazer a média: "))
#inicializa a soma das média
soma_media = 0

#laço de repetição
for i in range(n_media):
    valor = random.uniform(1, 100) #usando valores aleatórios
    soma_media = soma_media + valor #somando os valores no soma média
    
media = soma_media / n_media #média dos valores
#pegar o tempo fianl
end_time = time.time()
print(f"Média dos valores finais para {n_media} números : {media}") #mostrando a média
print(f"Tempo de execução: {end_time - start_time:.5f} segundos") # mostrando o tempo
print(f"Uso de memória: {sys.getsizeof(valor)} bytes") # mostrando o tamanho