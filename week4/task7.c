#include <stdlib.h>
#include <stdio.h>

int* create_int(int value) {
    int* p = (int*) malloc(sizeof(int));
    // a)
    *p = value;
    return p;
}
int main() {
    int* a = create_int(10);
    int* b = create_int(20);
    printf("%d %d\n", *a, *b);

    // b)
    free(a);
    free(b);

    // c)
    a = NULL;
    b = NULL;

    // d)
    // After free the memory is no longer owned by the program, so dereferencing a or b
    // would lead to undefined behavior. Setting them to NULL prevents accidental access.
    
    return 0;
}