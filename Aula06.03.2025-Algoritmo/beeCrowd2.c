/*Exemplos de Entrada	Exemplos de Saída
3.0 4.0 5.2             TRIANGULO: 7.800
                        CIRCULO: 84.949
                        TRAPEZIO: 18.200
                        QUADRADO: 16.000
                        RETANGULO: 12.000
*/

#include <stdio.h>
 
int main() {
    double A, B, C;
    scanf("%lf %lf %lf", &A, &B, &C);

    double areaTriangulo = (A * C) /2;
    double areaCirculo = 3.14159 * (C*C);
    double areaTrapezio = ((A+B) * C) / 2;
    double areaQuadrado = B * B;
    double areaRetangulo = A * B;

    printf("TRIANGULO: %.3lf\n", areaTriangulo);
    printf("CIRCULO: %.3lf\n", areaCirculo);
    printf("TRAPEZIO: %.3lf\n", areaTrapezio);
    printf("QUADRADO: %.3lf\n", areaQuadrado);
    printf("RETANGULO: %.3lf\n", areaRetangulo);


    return 0;
}