#include <stdlib.h>
#include <stdio.h>

// C would like you to always say `struct Person` when you talk about
// the `Person` type. Luckily, we can define a shorter name for it.
// Read this as "I want to be able to refer to the
// type `struct Person` as just `Person`".
typedef struct Person Person;

struct Person {
    char* name;
    int age;
    Person* previous;
    Person* next;
};
Person* create_person(char* name, int age) {
    Person* person = (Person*) malloc(sizeof(Person));
    person->name = name;
    person->age = age;
    person->previous = NULL;
    person->next = NULL;
    return person;
}

// This variable contains a five-element array where each element
// is a pointer to a char array.
char* names[] = {"Aasmund", "Astrid", "Kari", "Per", "Nils"};

int main() {
    // Tracks first and last person in the list
    Person* first_person = NULL;
    Person* last_person = NULL;
    for (int i = 0; i < 5; i++) {
        // Create a new person
        Person* new_person = create_person(names[i], i * 8);
        // Link the new person into the list
        new_person->previous = last_person;
        // If there is a last person, link it to the new person
        if (last_person != NULL) {
            last_person->next = new_person;
        }
        // Update first_person if this is the first person created
        if (first_person == NULL) {
            first_person = new_person;
        }
        // Update last_person to the new person
        last_person = new_person;
    }
    // Traverse the list from first to last
    Person* current_person = first_person;
    while (current_person) {
        printf(
        "%s is %d years old\n",
        current_person->name, current_person->age);
        current_person = current_person->next;
    }

    // Print the structure of the list
    printf("\nList Structure\n");
    printf("first_person points to: %p (%s)\n", first_person, first_person->name);
    printf("last_person points to: %p (%s)\n\n", last_person, last_person->name);
    current_person = first_person;
    while (current_person) {
        printf("Person: %s (address: %p)\n", current_person->name, current_person);
        printf("previous: %p", current_person->previous);
        // Check if previous is not NULL before dereferencing
        if (current_person->previous) printf(" (%s)", current_person->previous->name);
        printf("\n");
        printf("next: %p", current_person->next);
        // Check if next is not NULL before dereferencing
        if (current_person->next) printf(" (%s)", current_person->next->name);
        printf("\n\n");
        current_person = current_person->next;
    }
}