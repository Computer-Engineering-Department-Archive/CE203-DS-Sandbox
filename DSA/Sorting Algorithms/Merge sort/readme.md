# Merge Sort
Merge Sort is a **Divide and Conquer** algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

## Algorithm
Conceptually, a merge sort works as follows:

1.  Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
2.  Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Merge-sort-example-300px.gif/220px-Merge-sort-example-300px.gif">
</p>

## Performance
The complexity of merge sort is O(nlogn).

##### How many times are these steps executed?

For this, look at the tree below - for each level from top to bottom Level 2 calls merge method on 2 sub-arrays of length n/2 each. The complexity here is 2 * (cn/2) = cn Level 3 calls merge method on 4 sub-arrays of length n/4 each. The complexity here is 4 * (cn/4) = cn and so on ...

Now, the height of this tree is (logn + 1) for a given n. Thus the overall complexity is (logn + 1)*(cn). That is O(nlogn) for the merge sort algorithm.
<p align="center">
  <img src="https://i.stack.imgur.com/rPhxO.png">
</p>