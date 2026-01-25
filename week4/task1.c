#include <stdio.h>
#include <stdbool.h>

int main() {
    printf("Integers\n");
    printf("char:        %zu byte\n", sizeof(char));
    printf("short:       %zu bytes\n", sizeof(short));
    printf("int:         %zu bytes\n", sizeof(int));
    printf("long:        %zu bytes\n", sizeof(long));
    printf("long long:   %zu bytes\n", sizeof(long long));

    printf("\nFloating-points\n");
    printf("float:       %zu bytes\n", sizeof(float));
    printf("double:      %zu bytes\n", sizeof(double));
    printf("long double: %zu bytes\n", sizeof(long double));

    printf("\nOther types\n");
    printf("bool:        %zu bytes\n", sizeof(bool));

    return 0;

}