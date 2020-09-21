#include <stdio.h>

int main()
{
    int miles, yards;
    double kilometers;
    printf("Enter distace Miles and Yards: ");
    scanf("%d%d", &miles, &yards);
    kilometers = 1.609 * (miles + yards / 1760.0);
    printf("\nA marathon is %lf kilometers.\n\n", kilometers);

    return 0;
}