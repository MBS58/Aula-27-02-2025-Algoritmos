n_media = int(input("Digite quantos números deseja fazer a média: "))  # Lê o valor de n para poder saber quantos número iremos realizar a média
soma_media = 0  # Inicializa a soma dos números para fazer a média
    
for i in range(n_media): # Laço de repetição
    valor = int(input(f"Digite o {i + 1}º número: "))  # Lê o valor de cada número
    soma_media += valor  # Adiciona o número à soma
    media = soma_media / (i+1)  # Calcula a média
    print(f"Média dos valores Parciais: {media}")  # Imprime o resultado

    print(f"Média dos valores Final: {media}")  # Imprime o resultado
