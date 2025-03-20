#include <stdio.h>
#include <math.h>

int main(){ 

    double a, b, c;
    double pesoA = 0.2 , pesoB = 0.3, pesoC = 0.5;
    scanf("%lf\n", &a);
    scanf("%lf\n", &b);
    scanf("%lf", &c);

    double media = (a * pesoA) + (b * pesoB) + (c * pesoC);
    printf("MEDIA = %.1lf\n", media);
    return 0;
}