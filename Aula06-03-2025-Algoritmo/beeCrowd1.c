#include <stdio.h>
/*Exemplos de Entrada	Exemplos de Saída
    3                      VOLUME = 113.097

    15                     VOLUME = 14137.155

    1523                   VOLUME = 14797486501.627
*/
 
int main() {
 
    /**
     * Escreva a sua solução aqui
     * Code your solution here
     * Escriba su solución aquí
     */
    double raio;
      scanf("%lf", &raio);
     double pi = 3.14159;
      
     double volume = (4.0/3) * pi * (raio * raio * raio);
      printf("VOLUME = %.3lf\n", volume);
  
    return 0;
}