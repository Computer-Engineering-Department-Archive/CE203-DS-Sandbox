# Circular Linked List
A Circular Linked List is just a simple linked list with the next pointer of the last node of a linked list connected to the first node.

![](https://www.codesdope.com/staticroot/images/ds/circular1.png)

As you can see in the above picture that there is no start and end of a circular linked list, but we will maintain a pointer to represent the last element of the linked list as shown in the picture given below.

![](https://www.codesdope.com/staticroot/images/ds/circular2.png)

We have chosen to keep a record of the last element and not the first because inserting a new node after the last node will be efficient in this case instead of traversing over the entire list in the case of keeping the record of the first element.

## Algorithm
#### Initializing a new Circular Linked List
To initialize a circular linked list we will point the next node of head to itself.

![](https://www.codesdope.com/staticroot/images/ds/circular3.png)

This is our last node as well.

#### Inserting a new node in Circular Linked List
To insert a new node at any position, we will have to break the existing link and add the new node at that position.

##### Inserting a new node after a given node
Let's assume we want to add new node n after node a.

In the first step we point next of n to next of a.

![](https://www.codesdope.com/staticroot/images/ds/circular5.png)

After this we will point next of a to new node n.

![](https://www.codesdope.com/staticroot/images/ds/circular6.png)

##### Inserting a new node after the last node
We will simply insert the node by connecting the new node to the first node and the last node to the new node.

![](https://www.codesdope.com/staticroot/images/ds/circular7.png)

At last, we will update the last pointer of the linked list.

![](https://www.codesdope.com/staticroot/images/ds/circular8.png)

#### Deleting a Node from Circular Linked List
We will first make a temporary pointer to the last node of the linked list. After this, we will check if the node to be deleted is the last node or not. If it is the last node, then we will have to update the last pointer. In the case of the last node, it is also possible that the node is the only node of the linked list, we will handle this case differently.

![](https://www.codesdope.com/staticroot/images/ds/circular9.png)

If the linked list has only one node we simply make our last pointer null.

If the linked list has more than one node and the node to be deleted is the last node, we are pointing the next pointer of the node previous to the node to be deleted to the next of it. At last, we are updating the last pointer.

When the node to be deleted is not the last node, then we don't have to update the last pointer. We will just connect the previous node to the next node of the node which we are going to delete.