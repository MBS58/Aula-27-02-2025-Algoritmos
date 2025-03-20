#include <stdio.h>
#include <math.h>

int main(){ 

double A, B, C, delta, X1, X2;
scanf("%lf", &A);
scanf("%lf", &B);
scanf("%lf", &C);

delta = (B*B) - (4.0 * (A * C));

if (delta < 0 || A == 0)
{
   printf("Impossivel calcular\n");
} else
{
    X1 = ((-B) + (pow(delta, 0.5))) / (2 * A);
    X2 = ((-B) - (pow(delta, 0.5))) / (2 * A);

    printf("R1 = %.5lf\n", X1);
    printf("R2 = %.5lf\n", X2);
}

    return 0;
}