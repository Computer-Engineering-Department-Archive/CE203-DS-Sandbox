# Doubly Linked List
In a singly linked list, we can only move forward from any node. For example, if we are at node b, as shown in the picture given below, we can’t access the node previous to it.

<p align="center">
  <img src="https://www.codesdope.com/staticroot/images/ds/double1.png">
</p>

This problem can easily be fixed by using one extra link for each node which will point to the previous node.

<p align="center">
  <img src="https://www.codesdope.com/staticroot/images/ds/double2.png">
</p>

This is called doubly linked list.

## Algorithm
#### Inserting new node

Similar to singly linked lists, we can have three cases:

- Inserting a new node at the front of the doubly linked list.
- Inserting a new node at the end of the doubly linked list.
- Inserting a new node after any node in the doubly linked list.

##### Inserting a new node at the front
Lets assume we want to add new node n to our linked list.
Our first task is to point next of the new node (n) to the head of the linked list.
Then, we will point prev of the head to the new node. And that's it were done.

##### Inserting a new node at the end
Lets assume we want to add new node n to our linked list.
To insert a new node at the tail, we will first iterate to the last node.

      temp = head
      while(temp.next != null)
          temp = temp.next

Now, we will point next of temp to n and prev of n to temp. And that's it were done.

##### Inserting a new node after any node
Lets assume we want to add new node n after node a to our linked list.
Firstly, we will link the new node n and a.next. 
After this, we will link a to n.

![](https://www.codesdope.com/staticroot/images/ds/double8.png)

#### Deleting a Node
Lets assume we want to delete node a from our list.
We will first check if the node a is head or not. We can do it easily by checking if the prev pointer of the node is null or not because prev of the head is always null. If the node is not head, then we will point next pointer of the node previous to a to the next of a. If the node a is head, then we will mark the node next to a as the head of the linked list. 
At last, we will point the prev pointer of the node next to a to the node previous of a.

![](https://media.geeksforgeeks.org/wp-content/uploads/20200318150826/ezgif.com-gif-maker1.gif)