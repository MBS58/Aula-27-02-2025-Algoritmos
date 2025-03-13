#include <stdio.h>

int main()
{
    int countArrayLength = 0;
    int arrayInicial[255];
    while (1)
    {   
        printf("\nDigite um número inteiro: ");
        int res;
        scanf("%d", &res);
        arrayInicial[countArrayLength] = res;
        countArrayLength++;

        int escolha;
        printf("\nDeseja continuar [1/0]? ");
        scanf("%d", &escolha);
        if(escolha == 0){
            printf("%d\n", countArrayLength);
            break;
        }
    }

    int arrayNums[countArrayLength];
    for(int i = 0; i < countArrayLength; i++){
        arrayNums[i] = arrayInicial[i];
    }
    

    // ordena array em ordem crescente
    while (1)
    {
        int count = 0;
        for (int j = 0; j < countArrayLength; j++)
        {
            if (j < (countArrayLength - 1))
            {
                if (arrayNums[j] > arrayNums[j + 1])
                {
                    int checkpoint = arrayNums[j];
                    arrayNums[j] = arrayNums[j + 1];
                    arrayNums[j + 1] = checkpoint;
                }
                else
                {
                    count++;
                }
            }
        }
        if (count == (countArrayLength - 1))
        {
            break;
        }
    };

    for (int i = 0; i < countArrayLength; i++)
    {
        printf("%i ", arrayNums[i]);
    }
    printf("\n");
    return 0;
}