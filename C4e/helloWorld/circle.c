#include <stdio.h>

#define PI 3.142

int main(){
    double area = 0.00, radius = 0.00;
    printf("Enter Radius: ");
    scanf("%lf", &radius);
    area = PI * radius * radius;
    printf("radius of %lf meters; area is %lf sq.meters\n", radius, area);
    return 0;
}