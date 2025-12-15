#include <stdio.h>

int main() {
    int intVar = 10;
    char charVar = 'A';
    double doubleVar = 2.71828;
    float floatVar = 3.14;

    printf("정수형 변수: %d\n", intVar);
    printf("문자형 변수: %c\n", charVar);
    printf("실수형 변수 (double): %.5lf\n", doubleVar);
    printf("실수형 변수 (float): %.2f\n", floatVar);

    return 0;
}