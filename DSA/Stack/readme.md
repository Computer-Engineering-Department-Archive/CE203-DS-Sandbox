# Stack
In our day to day life, we see stacks of plates, coins, etc. All these stacks have one thing in common that a new item is added at the top of the stack and any item is also removed from the top i.e., the most recently added item is removed first.

![](https://www.codesdope.com/staticroot/images/ds/stack1.png)

In Computer Science also, a stack is a data structure which follows the same kind of rules i.e., the most recently added item is removed first. It works on LIFO (Last In First Out) policy. It means that the item which enters at last is removed first.

![](https://www.codesdope.com/staticroot/images/ds/stack2.png)

Since a stack just has to follow the LIFO policy, we can implement it using a linked list as well as with an array. However, we will restrict the linked list or the array being used to make the stack so that any element can be added at the top or can also be removed from the top only.

A stack supports few basic operations, and we need to implement all these operations (either with a linked list or an array) to make a stack. These operations are:

**Push** → The push operation adds a new element to the stack. As stated above, any element added to the stack goes at the top, so push adds an element at the top of a stack.

![](https://www.codesdope.com/staticroot/images/ds/stack3.gif)

**Pop** → The pop operation removes and also returns the top-most (or most recent element) from the stack.

![](https://www.codesdope.com/staticroot/images/ds/stack4.gif)

**Top** → The Top operations only returns (doesn’t remove) the top-most element of a stack.

**isEmpty** → This operation checks whether a stack is empty or not i.e., if there is any element present in the stack or not.

We also handle two errors with a stack. They are stack underflow and stack overflow. When we try to pop an element from an empty stack, it is said that the stack underflowed. However, if the number of elements exceeds the stated size of a stack, the stack is said to be overflowed.

![](https://www.codesdope.com/staticroot/images/ds/stack7.png)

At many places, you might find out that a stack is referred to as an abstract data type.

## Stack - Abstract Data Type or Data Structure
In an Abstract Data Type (or ADT), there is a set of rules or description of the operations that are allowed on data. It is based on a user point of view i.e., how a user is interacting with the data. However, we can choose to implement those set of rules differently.

A stack is definitely an ADT because it works on LIFO policy which provides operations like push, pop, etc. for the users to interact with the data. A stack can be implemented in different ways and these implementations are hidden from the user. For example, as stated above, we can implement a stack using a linked list or an array. In both the implementations, a user will be able to use the operations like push, pop, etc. without knowing the data structure used to implement those operations.

However, when we choose to implement a stack in a particular way, it organizes our data for efficient management and retrieval. So, it can be seen as a data structure also.

