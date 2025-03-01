#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Inicializa a contagem de tempo
    clock_t start_time = clock();

    // Pergunta quantos números deseja calcular a média
    int n_media;
    printf("Digite quantos números deseja fazer a média: ");
    scanf("%d", &n_media);

    // Inicializa a soma das médias
    double soma_media = 0.0;
    double valor; // Variável para armazenar os números aleatórios
    double media;

    // Inicializa a semente do gerador de números aleatórios
    srand(time(NULL));

    // Laço de repetição para gerar números e calcular a soma
    for (int i = 0; i < n_media; i++) {
        valor = 1 + ((double)rand() / RAND_MAX) * 99; // Gerando número entre 1 e 100
        soma_media += valor;
        media = soma_media / (i+1);
        printf("Média dos valores parciais para %d números: %.5f\n", (i+1), media);
    }

    // Calcula a média
    media = soma_media / n_media;

    // Pega o tempo final
    clock_t end_time = clock();
    double tempo_execucao = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    // Exibe os resultados
    printf("Média dos valores finais para %d números: %.5f\n", n_media, media);
    printf("Tempo de execução: %.5f segundos\n", tempo_execucao);
    printf("Uso de memória da variável valor: %lu bytes\n", sizeof(valor));

    return 0;
}