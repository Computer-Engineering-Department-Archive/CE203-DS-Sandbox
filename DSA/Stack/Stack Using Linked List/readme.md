# Stack Using Linked List
A stack using a linked list is just a simple linked list with just restrictions that any element will be added and removed using push and pop respectively. In addition to that, we also keep top pointer to represent the top of the stack.

![](https://www.codesdope.com/staticroot/images/ds/stack12.png)

A stack will be empty if the linked list won’t have any node i.e., when the top pointer of the linked list will be null. 

Now, to push any node to the stack, we will first check if the stack is empty or not. If the stack is empty, we will make the new node head of the linked list and also point the top pointer to it.
If the stack is not empty, we will add the new node at the last of the stack. For that, we will point next of the top to the new node and the make the new node top of the stack.


![](https://www.codesdope.com/staticroot/images/ds/stack14.gif)

Similarly, to remove a node (pop), we will first check if the stack is empty or not.
In the case when the stack is not empty, we will first store the value in top node in a temporary variable because we need to return it after deleting the node.
Now if the stack has only one node (top and head are same), we will just make both top and head null.

![](https://www.codesdope.com/staticroot/images/ds/stack15.png)

If the stack has more than one node, we will move to the node previous to the top node and make the next of point it to null and also point the top to it.

![](https://www.codesdope.com/staticroot/images/ds/stack16.gif)

We first iterated to the node previous to the top node, and then we marked its next to null. After this, we pointed the top pointer to it.

At last, we will return the data stored in the temporary variable.