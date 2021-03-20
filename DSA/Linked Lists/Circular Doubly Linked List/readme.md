# Circular Doubly Linked List
Circular Doubly Linked List has properties of both doubly linked list and circular linked list in which two consecutive elements are linked or connected by previous and next pointer and the last node points to first node by next pointer and also the first node points to last node by previous pointer.

![](https://static.javatpoint.com/ds/images/circular-doubly-linked-list.png)

## Algorithm
A circular doubly linked list is a linear data structure, in which the elements are stored in the form of a node. Each node contains three sub-elements. A data part that stores the value of the element, the previous part that stores the pointer to the previous node, and the next part that stores the pointer to the next node as shown in the below image:

![](https://www.alphacodingskills.com/imgfiles/doubly-linked-list-node.PNG)

The first node also known as HEAD is always used as a reference to traverse the list. Last element contains link to the first element as next and the first element contains link of the last element as previous. A circular doubly linked can be visualized as a chain of nodes, where every node points to previous and next node.

![](https://www.alphacodingskills.com/imgfiles/circular-doubly-linked-list.PNG)

#### Traverse a Circular Doubly Linked List
A circular doubly linked list can be traversed from any node of the list using a temp node. Keep on moving the temp node to the next one and displaying its content. Stop the traversal, after reaching the last node.

#### Inserting a new node in Circular Doubly Linked List
we can have three cases:

- Inserting a new node at the front of the circular doubly linked list.
- Inserting a new node at the end of the circular doubly linked list.
- Inserting a new node after any node in the circular doubly linked list.

##### Insert a new node at the start
First, a new node with given element is created. It is then added at the start of the list by linking the head node and last node to the new node.

![](https://www.alphacodingskills.com/imgfiles/circular-doubly-linked-list-add-node-at-start.PNG)

##### Insert a new node after a given node
First a new node with the given element is created. It is then linked with the given node.

![](https://media.geeksforgeeks.org/wp-content/uploads/Insertion-in-between-the-list.png)

##### Insert a new node at the end
First, a new node with given element is created. It is then added at the end of the list by linking the last node and head node to the new node.

![](https://www.alphacodingskills.com/imgfiles/circular-doubly-linked-list-add-node-at-end.PNG)

#### Deletion in Circular Doubly Linked List
First we will check if the node to be deleted is the last node or not. If it is the last node, then we will have to update the last pointer. In the case of the last node, it is also possible that the node is the only node of the linked list, we will handle this case differently.

If the linked list has more than one node and the node to be deleted is the last node, we are pointing the next pointer of the node previous to the node to be deleted to the next of it. At last, we are updating the last pointer.

When the node to be deleted is not the last node, then we don't have to update the last pointer. We will just connect the previous node to the next node of the node which we are going to delete.