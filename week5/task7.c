#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Person {
    char name[50];
    int age;
    struct Person* previous;
    struct Person* next;
} Person;

typedef struct DoublyLinkedList {
    Person* first;
    Person* last;
} DoublyLinkedList;

// Initialize the list
void initList(DoublyLinkedList* list) {
    list->first = NULL;
    list->last = NULL;
}

// Add a person to the end of the list
void addPerson(DoublyLinkedList* list, const char* name, int age) {
    Person* newPerson = (Person*)malloc(sizeof(Person));
    strcpy(newPerson->name, name);
    newPerson->age = age;
    newPerson->previous = NULL;
    newPerson->next = NULL;

    if (list->first == NULL) {
        // List is empty
        list->first = newPerson;
        list->last = newPerson;
    } else {
        // Add to the end
        newPerson->previous = list->last;
        list->last->next = newPerson;
        list->last = newPerson;
    }
}

// Print all persons in the list 
void printList(DoublyLinkedList* list) {
    if (list->first == NULL) {
        printf("List is empty.\n");
        return;
    }

    printf("List (forward):\n");
    Person* current = list->first;
    while (current != NULL) {
        printf("Name: %s, Age: %d\n", current->name, current->age);
        current = current->next;
    }
}


int main() {
    DoublyLinkedList list;
    initList(&list);

    // Add some persons
    addPerson(&list, "Alice", 30);
    addPerson(&list, "Bob", 25);
    addPerson(&list, "Charlie", 35);

    // Print forward
    printList(&list);
    printf("\n");

   

    return 0;
}
