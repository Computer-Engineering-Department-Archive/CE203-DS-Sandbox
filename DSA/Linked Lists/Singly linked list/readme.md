# Singly Linked List
In computer science, a linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence. In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence. This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration. More complex variants add additional links, allowing more efficient insertion or removal of nodes at arbitrary positions. A drawback of linked lists is that access time is linear (and difficult to pipeline). Faster access, such as random access, is not feasible. Arrays have better cache locality compared to linked lists.

<p align="center">
  <img src="https://www.codesdope.com/staticroot/images/ds/link1.png">
</p>

As you can see in the above picture, each data is connected (or linked) to a different data and thus, forming a linear list of data, and this is a linked list. Since data in a linked list are stored in a linear fashion, a linked list is a linear data structure. There are also non-linear data structures like trees, graphs, etc.

## Algorithm
#### Node
A node can be viewed as a container or a box which contains data and other information in it. Nodes are connected (or organized) in a specific way to make data structures like linked lists, trees, etc.

![](https://www.codesdope.com/staticroot/images/ds/link3.png)

In the above picture, each node has two parts, one stores the data and another is connected to a different node. The last node is not connected to any other node and thus, its connection to the next node is null.

In a linked list, a node is connected to a different node forming a chain of nodes.

![](https://www.codesdope.com/staticroot/images/ds/link4.png)

Thus to make a linked list, we first need to make a node which should store some data into it and also a link to another node.

#### Traversing a Linked List
Traversing is visiting all the nodes of a linked list. As stated above, we always keep a record of the head of a linked list. We also know that the last node of a linked list is null.

![](https://www.codesdope.com/staticroot/images/ds/link12.png)

So, we start a loop from the head of the linked list and end it when the node is null.

![](https://www.codesdope.com/staticroot/images/ds/link13.gif)

#### Inserting Nodes in a Linked List
There can be three different positions where we can insert a new node in a linked list:
- At the beginning of the list.
- At the end of the list.
- Anywhere except the above-mentioned positions.

##### Inserting a New Node at the Beginning of a Linked List
The new node is always added before the head of the given Linked List. And newly added node becomes the new head of the Linked List.

For example lets assume we want to add node n to our list.

![](https://www.codesdope.com/staticroot/images/ds/link15.png)

We point the next of the node to the head of the linked list

![](https://www.codesdope.com/staticroot/images/ds/link16.png)

Since the head should always point to the first element of the linked list, so we change the head to point to the new node.

![](https://www.codesdope.com/staticroot/images/ds/link17.png)

##### Inserting a New Node at the End of a Linked List.
To insert a node at the end of a linked list, we just iterate to the last of the linked list and add a new node there. This is described in the picture given below.

![](https://www.codesdope.com/staticroot/images/ds/link18.gif)

##### Inserting a New Node in the Middle of a Linked List
To insert a new node in the middle of a linked list, we need to break the existing links and create new links. This will be clear from the picture given below.

![](https://www.codesdope.com/staticroot/images/ds/link20.png)

We point next of the new node (n) to next of the node a.

![](https://www.codesdope.com/staticroot/images/ds/link21.png)

After this, we point next of the a to the new node.

![](https://www.codesdope.com/staticroot/images/ds/link22.png)

This will be clear from the picture given below.

![](https://www.codesdope.com/staticroot/images/ds/link19.gif)

#### Deleting a Node from a Linked List
We delete any node of a linked list by connecting the predecessor node of the node to be deleted by the successor node of the node. For example, if we have a linked list a → b → c, then to delete the node 'b', we will connect 'a' to 'c' i.e., a → c. But this will make the node 'b' inaccessible and this type of inaccessible nodes are called garbage.

We might need to clean this garbage ourself in some languages like C by using the free function while some languages like Java does it automatically.

Let's assume we want to delete node n from our list. We will first iterate to the node previous to the node n. So, we will first start from the head of the linked list.

If the node we are going to delete is the head of the linked list, then we will just update the head pointer.

![](https://www.codesdope.com/staticroot/images/ds/link23.png)

Otherwise, we will iterate to the node previous to the node n and then link the node previous of the node to be deleted to the next of it.

![](https://www.codesdope.com/staticroot/images/ds/link24.png)