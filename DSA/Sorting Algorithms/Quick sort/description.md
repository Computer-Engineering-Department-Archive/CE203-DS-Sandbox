# Quick sort
Quick sort is a highly efficient sorting algorithm and is based on partitioning of array of data into smaller arrays. A large array is partitioned into two arrays one of which holds values smaller than the specified value, say pivot, based on which the partition is made and another array holds values greater than the pivot value.

Quicksort partitions an array and then calls itself recursively twice to sort the two resulting subarrays.

## Algorithm
Quicksort is a divide and conquer algorithm. It first divides the input array into two smaller sub-arrays: the low elements and the high elements. It then recursively sorts the sub-arrays. The steps for in-place Quicksort are:

1. Pick an element, called a pivot, from the array.
2. Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position. This is called the partition operation.
3. Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.
The base case of the recursion is arrays of size zero or one, which are in order by definition, so they never need to be sorted.

The pivot selection and partitioning steps can be done in several different ways; the choice of specific implementation schemes greatly affects the algorithm's performance.

## Performance
Time taken by QuickSort in general can be written as following.

    T(n) = T(k) + T(n-k-1) + theta(n)

The first two terms are for two recursive calls, the last term is for the partition process. k is the number of elements which are smaller than pivot.
The time taken by QuickSort depends upon the input array and partition strategy. Following are three cases.

**Worst Case**: The worst case occurs when the partition process always picks greatest or smallest element as pivot. If we consider above partition strategy where last element is always picked as pivot, the worst case would occur when the array is already sorted in increasing or decreasing order. Following is recurrence for worst case.

    T(n) = T(0) + T(n-1) + theta(n)
    which is equivalent to  
    T(n) = T(n-1) + theta(n)

The solution of above recurrence is theta(n2).

**Best Case**: The best case occurs when the partition process always picks the middle element as pivot. Following is recurrence for best case.

    T(n) = 2T(n/2) + theta(n)

The solution of above recurrence is theta(nLogn). It can be solved using case 2 of Master Theorem.

**Average Case**:
To do average case analysis, we need to consider all possible permutation of array and calculate time taken by every permutation which doesn’t look easy.
We can get an idea of average case by considering the case when partition puts O(n/9) elements in one set and O(9n/10) elements in other set. Following is recurrence for this case.

    T(n) = T(n/9) + T(9n/10) + theta(n)