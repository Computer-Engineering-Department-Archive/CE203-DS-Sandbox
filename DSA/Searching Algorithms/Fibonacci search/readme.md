# Fibonacci search
In computer science, the Fibonacci search technique is a method of searching a sorted array using a divide and conquer algorithm that narrows down possible locations with the aid of Fibonacci numbers.[1] Compared to binary search where the sorted array is divided into two equal-sized parts, one of which is examined further, Fibonacci search divides the array into two parts that have sizes that are consecutive Fibonacci numbers. On average, this leads to about 4% more comparisons to be executed, but it has the advantage that one only needs addition and subtraction to calculate the indices of the accessed array elements, while classical binary search needs bit-shift, division or multiplication, operations that were less common at the time Fibonacci search was first published. Fibonacci search has an average- and worst-case complexity of O(log n).

The Fibonacci sequence has the property that a number is the sum of its two predecessors. Therefore the sequence can be computed by repeated addition. The ratio of two consecutive numbers approaches the Golden ratio, 1.618... Binary search works by dividing the seek area in equal parts (1:1). Fibonacci search can divide it into parts approaching 1:1.618 while using the simpler operations.

If the elements being searched have non-uniform access memory storage (i. e., the time needed to access a storage location varies depending on the location accessed), the Fibonacci search may have the advantage over binary search in slightly reducing the average time needed to access a storage location. If the machine executing the search has a direct mapped CPU cache, binary search may lead to more cache misses because the elements that are accessed often tend to gather in only a few cache lines; this is mitigated by splitting the array in parts that do not tend to be powers of two. If the data is stored on a magnetic tape where seek time depends on the current head position, a tradeoff between longer seek time and more comparisons may lead to a search algorithm that is skewed similarly to Fibonacci search.

Fibonacci search is derived from Golden section search, an algorithm by Jack Kiefer (1953) to search for the maximum or minimum of a unimodal function in an interval.

## Algorithm
Let the length of given array be n [0...n-1] and the element to be searched be x.

Then we use the following steps to find the element with minimum steps:

    Find the smallest Fibonacci number greater than or equal to n. Let this number be fb(M) [m’th Fibonacci number]. Let the two Fibonacci numbers preceding it be fb(M-1) [(m-1)’th Fibonacci number] and fb(M-2) [(m-2)’th Fibonacci number].

    While the array has elements to be checked:
    -> Compare x with the last element of the range covered by fb(M-2)
    -> If x matches, return index value
    -> Else if x is less than the element, move the third Fibonacci variable two Fibonacci down, indicating removal of approximately two-third of the unsearched array.

    -> Else x is greater than the element, move the third Fibonacci variable one Fibonacci down. Reset offset to index. Together this results into removal of approximately front one-third of the unsearched array.

    Since there might be a single element remaining for comparison, check if fbMm1 is '1'. If Yes, compare x with that remaining element. If match, return index value.

From the above algorithm it is clear if we have to search the larger section of the array then the time taken will be more and will result into worst case and it's complexity wil be O(log n). If on the very first search, we get our element then it will be considered as the best case and complexcity will be O(1). When we consider the average case then case left and lies between the best and worst i when we have to search the element on the smaller section of the array and hence we get our average case complexity as O(log n). 

## Performance
Worst case time complexity: Θ(logn)
Average case time complexity: Θ(log n)
Best case time complexity: Θ(1)
Space complexity: Θ(1)