#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Person Person;
typedef struct DoublyLinkedList DoublyLinkedList;

struct Person {
    char name[50];
    int age;
    struct Person* previous;
    struct Person* next;
};

Person* create_person(char* name, int age) {
    Person* person = (Person*) malloc(sizeof(Person));
    strcpy(person->name, name);
    person->age = age;
    person->previous = NULL;
    person->next = NULL;
    return person;
};
 struct DoublyLinkedList {
    Person* first;
    Person* last;
}; 

// Initialize the list
DoublyLinkedList* initList() {
    DoublyLinkedList* list = (DoublyLinkedList*)malloc(sizeof(DoublyLinkedList));
    list->first = NULL;
    list->last = NULL;
    return list;
}

void initListStack(DoublyLinkedList* list) {
    list->first = NULL;
    list->last = NULL;
}

// Add a person to the end of the list
void addPerson(DoublyLinkedList* list, Person* person) {


    if (list->first == NULL) {
        // List is empty
        list->first = person;
        list->last = person;
    } else {
        // Add to the end
        person->previous = list->last;
        list->last->next = person;
        list->last = person;
    }
}

// Print all persons in the list 
void printList(DoublyLinkedList* list) {
    if (list->first == NULL) {
        printf("List is empty.\n");
        return;
    }

    printf("List:\n");
    Person* current = list->first;
    while (current != NULL) {
        printf("Name: %s, Age: %d\n", current->name, current->age);
        current = current->next;
    }
}

void deleteList(DoublyLinkedList* list) {
    Person* current = list->first;
    while (current != NULL) {
        Person* toDelete = current;
        current = current->next;
        free(toDelete);
    }
    list->first = NULL;
    list->last = NULL;
    free(list);
    printf("List deleted successfully.\n");
}


int main() {
    DoublyLinkedList* list = initList();

    Person* alice = create_person("Alice", 30);
    Person* bob = create_person("Bob", 25);
    Person* charlie = create_person("Charlie", 35);

    addPerson(list, alice);
    addPerson(list, bob);
    addPerson(list, charlie);

    // Print forward
    printList(list);
    printf("\n");

    // Deallocate the list which is in heap 
    deleteList(list);

    // Test persons after deallocation. Both are undefined behavior
    printf("alice->age: %d\n", alice->age); // Will crash 
    free(alice); 

    DoublyLinkedList stackList;
    initListStack(&stackList);

    addPerson(&stackList, alice);
    addPerson(&stackList, bob);
    addPerson(&stackList, charlie);

    // Deallocate the list which is in stack
    deleteList(&stackList); // Will crash

    return 0;
}
