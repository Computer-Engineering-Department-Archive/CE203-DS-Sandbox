#include <stdio.h>

#define SIZE 10

int stack[SIZE + 1];
int top;

int isEmpty() {
    if (top == 0) {
        return 1;
    }
    
    return 0;
}

void push(int e) {
    top++;
    if (top > SIZE) {
        printf("Stack Overflow\n");
        return;
    }

    stack[top] = e;
}

int pop() {
    if (isEmpty()) {
        printf("Stack Underflow\n");
        return -9999999;
    }
    
    top--;
    return stack[top];
}

int main() {
    pop();
    push(1);
    push(2);
    push(3);
    push(4);
    push(5);
    push(6);
    push(7);
    push(8);
    push(9);
    push(10);
    push(11);

    for(int i=1; i<=SIZE; i++) {
        printf("%d\n",stack[i]);
    }

    return 0;
}