#include <stdio.h> //importando a biblioteca de entrada e saída 
//função principal do programa  
int main() {
  printf("Digite um número: "); //imprime na tela uma mensagem de escolha de número  
  int n; //declara n
  scanf("%d", &n); //recebe o valor de n
  printf("Digite um número: "); //imprime na tela uma mensagem de escolha de número  
  int m; //declara n
  scanf("%d", &m); //recebe o valor de m
  int somaMedia = 0;
  
  somaMedia = (n+m) / 2;
  printf("média dos valores %d\n", somaMedia); //imprime na tela o valor de n e o valor de p
  return 0; //fecha o programa
}