# Stack Using Array
We are going to use the element at the index 1 of the array as the bottom of the stack and the last element of the stack as the top of the stack as described in the picture given below.

![](https://www.codesdope.com/staticroot/images/ds/stack8.png)

We are going to use a pointer which is always going to point the topmost element of the stack. It will point to the element at index 0 when the stack is empty.

![](https://www.codesdope.com/staticroot/images/ds/stack9.png)

We are going to consider only the elements from 1 to S.top as part of the stack. It might be possible that there are other elements also in the array but we are not going to consider them as stack.

![](https://www.codesdope.com/staticroot/images/ds/stack10.png)

To add an item to a stack (push), we just need to increment the top pointer by 1 and add the element there.

Let’s suppose that stack size is the maximum size of the stack. So, if top+1 exceeds stack size, then the stack is **overflowed**. So, we will first check for the overflowing of the stack and then accordingly add the element to it.

![](https://www.codesdope.com/staticroot/images/ds/stack11.gif)

Similarly to remove an item from a stack (pop), we will first check if the stack is empty or not. If it is empty, then we will throw an error of **Stack Underflow**, otherwise remove the element from the stack and return it.