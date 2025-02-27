#include <stdio.h> //importando a biblioteca de entrada e saída 

int main() {
    printf("Digite um número: "); //imprime na tela uma mensagem de escolha de número  
    int n; //declara n
    scanf("%d", &n); //recebe o valor de n
    int p = n * n; //declara p e atribui o valor de n multiplicado por ele mesmo
    printf("%d ao quadrado é %d\n", n,p); //imprime na tela o valor de n e o valor de p
    return 0; //fecha o programa
  }