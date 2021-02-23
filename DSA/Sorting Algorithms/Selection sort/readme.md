# Selection Sort    
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

## Algorithm
The algorithm divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list and a sublist of the remaining unsorted items that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

## Performance
Selection sort is not difficult to analyze compared to other sorting algorithms, since none of the loops depend on the data in the array. Selecting the minimum requires scanning {\displaystyle n}n elements (taking {\displaystyle n-1}n-1 comparisons) and then swapping it into the first position. Finding the next lowest element requires scanning the remaining {\displaystyle n-1}n-1 elements and so on. Therefore, the total number of comparisons is

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/022f41f8c29a0da175bc0d4f84c53a8046e6cb8f)

By arithmetic progression,

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/5042a309a9d1de0d8c89443c1950dd1e28a802e3)

which is of complexity O(n^2) in terms of number of comparisons. Each of these scans requires one swap for n-1 elements (the final element is already in place).