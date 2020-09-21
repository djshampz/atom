#include <stdio.h>

int main()
{
    int ferenheit, celcius;
    printf("Enter your ferenheit: ");
    scanf("%d", &ferenheit);
    celcius = (ferenheit - 32)/1.8;
    printf("\n%d farenheit is %d in celcius\n\n", ferenheit, celcius);
    return 0;

}