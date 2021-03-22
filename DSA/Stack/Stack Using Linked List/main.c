#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

//Node constructor
Node *new_node(int data) {
    Node *newNode;

    newNode = malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;

    return newNode;
}

typedef struct Stack {
    struct Node *head;
    struct Node *top;
} Stack;

//Stack constructor
Stack *new_stack() {
    Stack *newStack;
    
    newStack = malloc(sizeof(Stack));
    newStack->head = NULL;
    newStack->top = NULL;

    return newStack;
}

void traversal(Stack *s) {
    Node *temp = s->head;

    while (temp != NULL)
    {
        printf("%d->", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

int is_empty(Stack *s) {
    if (s->top == NULL) 
        return 1;
    return 0;
}

void push(Stack *s, int data) {
    Node *newNode = new_node(data);

    if (is_empty(s))
    {
        s->head = newNode;
        s->top = newNode;
    }
    else
    {
        s->top->next = newNode;
        s->top = newNode;
    }
}

int pop(Stack *s) {
    if (is_empty(s))
    {
        printf("Stack Underflow!\n");
        return -9999999;
    }
    else
    {
        int data = s->top->data;
        if (s->top == s->head)
        {
            free(s->top);
            s->head = NULL;
            s->top = NULL;
        }
        else
        {
            Node *temp = s->head;

            while (temp->next != s->top)
                temp = temp->next;

            temp->next = NULL;
            free(s->top);
            s->top = temp;
        }
        return data;
    }
}

int main() {
    Stack *s = new_stack();

    push(s, 1);
    push(s, 2);
    push(s, 3);

    traversal(s);

    printf("%d\n", pop(s));

    traversal(s);

    return 0;
}