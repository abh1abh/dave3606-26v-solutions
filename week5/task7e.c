
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Person {
    char name[50];
    int age;
} Person;

Person* create_person(char* name, int age) {
    Person* person = (Person*) malloc(sizeof(Person));
    strcpy(person->name, name);
    person->age = age;
    return person;
};

typedef struct DoublyLinkedListNode {
    struct DoublyLinkedListNode* previous;
    struct DoublyLinkedListNode* next;
    Person* person;
} DoublyLinkedListNode;

typedef struct DoublyLinkedList {
    DoublyLinkedListNode* first;
    DoublyLinkedListNode* last;
} DoublyLinkedList;

// Initialize the list
DoublyLinkedList* initList() {
    DoublyLinkedList* list = (DoublyLinkedList*)malloc(sizeof(DoublyLinkedList));
    list->first = NULL;
    list->last = NULL;
    return list;
}


// Add a person to the end of the list (person is managed by caller)
void addPerson(DoublyLinkedList* list, Person* person) {
    DoublyLinkedListNode* newNode = (DoublyLinkedListNode*)malloc(sizeof(DoublyLinkedListNode));
    newNode->person = person;
    newNode->previous = NULL;
    newNode->next = NULL;

    if (list->first == NULL) {
        // List is empty
        list->first = newNode;
        list->last = newNode;
    } else {
        // Add to the end
        newNode->previous = list->last;
        list->last->next = newNode;
        list->last = newNode;
    }
}

// Print all persons in the list 
void printList(DoublyLinkedList* list) {
    if (list->first == NULL) {
        printf("List is empty.\n");
        return;
    }

    printf("List:\n");
    DoublyLinkedListNode* current = list->first;
    while (current != NULL) {
        printf("Name: %s, Age: %d\n", current->person->name, current->person->age);
        current = current->next;
    }
}

// Deallocate nodes and list, not persons           
void deleteList(DoublyLinkedList* list) {
    DoublyLinkedListNode* current = list->first;
    while (current != NULL) {
        DoublyLinkedListNode* toDelete = current;
        current = current->next;
        free(toDelete);  // Only free the node
    }
    free(list);  // Free the list structure itself
}


int main() {
    DoublyLinkedList* list = initList();

    // Create persons - caller manages their memory
    Person* alice = create_person("Alice", 30);

    Person* bob = create_person("Bob", 25);

    Person* charlie = create_person("Charlie", 35);

    // Add persons to the list
    addPerson(list, alice);
    addPerson(list, bob);
    addPerson(list, charlie);

    // Print forward
    printList(list);
    printf("\n");

    // Delete the list 
    deleteList(list);
    printf("List deleted. Persons still exist in memory.\n\n");

    // Still access to created persons
    printf("Alice is still accessible: %s, age %d\n", alice->name, alice->age);

    // Now we need to manually free the persons since we own them
    free(alice);
    free(bob);
    free(charlie);
    printf("Persons deallocated.\n");

    return 0;
}
