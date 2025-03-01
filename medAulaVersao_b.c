#include <stdio.h> //importando a biblioteca de entrada e saída
// função principal do programa
int main() {
  printf("Digite quantos número deseja fazer a média: "); // imprime na tela uma
                                                          // mensagem de escolha
                                                          // de número
  int nMedia;                                             // declara nMedia
  scanf("%d", &nMedia); // recebe o valor de nMedia
  int myNumber[nMedia];
  float media;
  int somaMedia = 0;
  int valor = 0;
  int i = 0;

  for (i = 0; i < nMedia; i++) {
    printf("Digite o %dº número : ", i + 1);
    scanf("%d", &valor);
    myNumber[i] = valor;
    somaMedia = somaMedia + myNumber[i];
    media = somaMedia / (i+1);
    printf("Média dos valores parciais %f\n ", media);
  }
media = somaMedia / nMedia;
printf("Média dos valores %f\n", media); // imprime na tela o valor de n e o valor de p
  return 0;      // fecha o programa
}