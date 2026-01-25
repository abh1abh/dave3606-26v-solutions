#include <stdlib.h>
#include <stdio.h>


// Function now takes a pointer to int (int*) to store the result
void add(int a, int b, int* sum) {
    // Print the address of sum in add
    printf("Address of sum in add: %p\n", sum);
    *sum = a + b;
}
 
int main() {
    int sum;
    // Print the address of sum in main
    printf("Address of sum in main: %p\n", &sum);
    // Pass the address (&) of sum to the add function
    add(3, 4, &sum);
    printf("%d\n", sum);
    return 0;
}