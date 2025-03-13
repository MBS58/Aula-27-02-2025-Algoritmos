#include <stdio.h> //importando a biblioteca de entrada e saída 
//função principal do programa  
int main() {
  printf("Digite quantos número deseja fazer a média: "); //imprime na tela uma mensagem de escolha de número  
  int nMedia; //declara n
  scanf("%d", &nMedia); //recebe o valor de n
  int myNumber[nMedia];
  int somaMedia = 0;
  int valor = 0;
  
  for (nMedia = 0; nMedia < 10; nMedia++) {
    printf("Digite o %dº número : ", nMedia + 1);
    scanf("%d", &valor);
    myNumber[nMedia] = valor;
    somaMedia = somaMedia + myNumber[nMedia];
  }
  somaMedia = somaMedia / nMedia;
  printf("média dos valores %d\n", somaMedia); //imprime na tela o valor de n e o valor de p
  return 0; //fecha o programa
}