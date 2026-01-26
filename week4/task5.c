#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct Person Person;

struct Person {
    char* name;
    int age;
};

Person* new_person(char* name, int age) {
    Person* person = (Person*) malloc(sizeof(Person));
    person->name = name;
    person->age = age;
    return person;
}
bool is_adult(Person* person) {
    return person->age >= 18;
}

int main() {
    Person* per = new_person("Per", 30);
    Person* ola = new_person("Ola", 15);

    if (is_adult(per)) {
        printf("%s is an adult.\n", per->name);
    } else {
        printf("%s is not an adult.\n", per->name);
    }

    if (is_adult(ola)) {
        printf("%s is an adult.\n", ola->name);
    } else {
        printf("%s is not an adult.\n", ola->name);
    }

    free(per);
    free(ola);
    return 0;
}

