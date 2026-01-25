#include <stdlib.h>
#include <stdio.h>

typedef struct {
    int age;
    char* name;
    
} Person;

Person* create_person(char* name, int age) {
    Person* person = (Person*) malloc(sizeof(Person));
    person->name = name;
    person->age = age;
    return person;
}

int main () {
    // a)
    Person* aasmund = create_person("Aasmund", 30);

    printf("Size of Person instance: %zu bytes\n", sizeof(*aasmund));
    printf("Size of age (int): %zu bytes\n", sizeof(aasmund->age));
    printf("Size of name (char*): %zu bytes\n", sizeof(aasmund->name));
    printf("Name: %s, Age: %d\n", aasmund->name, aasmund->age);
    free(aasmund);

    // b)
    Person local_person = { .age = 40, .name = "Local" };
    Person* person_ptr = &local_person;
    Person** person_pptr = &person_ptr;

    // c)
    printf("\nPointer to Person instance:\n");
    printf("Local: %p\n", (void*) &local_person);
    printf("Person*: %p\n", (void*) person_ptr);
    printf("Person**: %p\n", (void*) person_pptr);
    printf("Address of Person*: %p\n", (void*) &person_ptr);
    printf("Address of Person**: %p\n", (void*) &person_pptr);

    // d)
    printf("\nAccessing properties via different levels:\n");
    printf("name via local: %s\n", local_person.name);
    printf("name via Person*: %s\n", person_ptr->name);
    printf("name via Person**: %s\n", (**person_pptr).name);
    printf("age via local: %d\n", local_person.age);
    printf("age via Person*: %d\n", person_ptr->age);
    printf("age via Person**: %d\n", (**person_pptr).age);

    // e)
    printf("\nAddresses within local_person (object and its fields):\n");
    printf("&local_person (object): %p\n", (void*) &local_person);
    printf("&local_person.age (first field): %p\n", (void*) &local_person.age);
    printf("&local_person.name (second field): %p\n", (void*) &local_person.name);

    free(person_ptr);
    free(person_pptr);
    return 0;
}
